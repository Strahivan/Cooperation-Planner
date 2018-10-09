from flask import request
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

from model.csvdata import Csv
from util.query_builder import Builder

# TODO: adjust DB-Structure for new DB-Fields of Amazon
metadata = MetaData()
engine = create_engine('sqlite:///database/database.db')
if not engine.dialect.has_table(engine, 'url'):
    metadata = MetaData(engine)
    url = Table('url', metadata,
                Column('id', Integer, primary_key=True, autoincrement=1),
                Column('url', String(4000), nullable=True),
                Column('statuscode', Integer, nullable=True),
                Column('tld', String(128), nullable=True),
                Column('reach', Integer, nullable=True),
                Column('globalrank', Integer, nullable=True))
    url.create(engine)


# TODO: adjust get-method for new DB-Fields of Amazon
def get_sql_query():
    csv_filter = Csv(str(request.args['reach']),
                     str(request.args['url']),
                     str(request.args['tld']),
                     str(request.args['statuscode']),
                     str(request.args['globalrank']))

    builder = Builder('*')
    builder.from_table('url')

    count = 0
    for key, value in csv_filter.__dict__.iteritems():
        if value is not None and value is not '':
            if count == 0:
                builder.where(key, value)
            else:
                builder.and_where(key, value)
            count += 1

    return builder.build()
