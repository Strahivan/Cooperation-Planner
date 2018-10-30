class Builder(object):
    """ SQL QUERY Builder."""

    __select = None
    __from = None
    __where = None
    __and = None

    def __init__(self, select):
        self.__and = []
        self.__select = 'SELECT {}'.format(select)

    def from_table(self, table):
        self.__from = ' FROM {}'.format(table)
        return self

    def where(self, key, value):
        value = check_square_brackets(value)
        if value[1].isdigit():
            self.__where = ' WHERE {} {} {}'.format(key, value[0], value[1])
        else:
            self.__where = ' WHERE {} {} "%{}%"'.format(key, value[0], value[1])
        return self

    def and_where(self, key, value):
        value = check_square_brackets(value)
        if value[1].isdigit():
            self.__and.append(' AND {} {} {}'.format(key, value[0], value[1]))
        else:
            self.__and.append(' AND {} {} "%{}%"'.format(key, value[0], value[1]))
        return self

    def build(self):
        return self.__select + self.__from + (self.__where or '') + ''.join(self.__and)


def check_square_brackets(value):
    if value.find('>=') == 0:
        value = value.split('>=')
        return '>=', value[1]
    if value.find('<=') == 0:
        value = value.split('<=')
        return '<=', value[1]
    if value.find('>') == 0:
        value = value.split('>')
        return '>', value[1]
    if value.find('<') == 0:
        value = value.split('<')
        return '<', value[1]
    if value.isdigit():
        return '=', value
    return 'like', value
