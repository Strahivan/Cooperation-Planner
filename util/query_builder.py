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
        if value.isdigit():
            self.__where = ' WHERE {} = {}'.format(key, value)
        else:
            self.__where = ' WHERE {} LIKE "%{}%"'.format(key, value)
        return self

    def and_where(self, key, value):
        if value.isdigit():
            self.__and.append(' AND {} = {}'.format(key, value))
        else:
            self.__and.append(' AND {} LIKE "%{}%"'.format(key, value))
        return self

    def build(self):
        return self.__select + self.__from + (self.__where or '') + ''.join(self.__and)
