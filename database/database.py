import os

from flask import request
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from tld import get_fld

from model.csvdata import Csv
from util.query_builder import Builder

# ------- DATABASE.PY -------

"""
This module handles all queries and actions with the database.
It uses the query_builder.py-file in order to build the queries and is mainly called by the main.py-file

:copyright: (c)2018 by Michele Santoro, Steve Iva
:license: Apache 2.0, see LICENSE
"""

"""
Initializes the database in the first step.
Calls the engine for the database and specifies the local database structure.
"""

dir_path = os.path.join(os.environ['HOME'], 'CooperationPlanner')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
file_path = os.path.join(dir_path, 'database.db')
print file_path

metadata = MetaData()
engine = create_engine('sqlite:///' + file_path)
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

"""
This method is a filter function and pulls the filter arguments from the request (user input) in the first step.
Then builds an SQL query with the filter arguments.
Nothing is executed at this point, only the SQL queries are built.
"""


def get_sql_query():
    csv_filter = Csv(None,
                     str(request.args['reach']),
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


"""
Builds a SQL query that checks if a selected URL is already in the database (exception if it's a 404 status code).
If it's a 404, it should return a builder.build() that in turn returns a SQL query to execute.
If it is not a 404, it returns nothing.
"""


def select_query_for(selectedUrl, statuscode):
    if statuscode != 404:
        builder = Builder('*')
        builder.from_table('url')
        builder.where('url', get_fld(selectedUrl, fix_protocol=True))
        return builder.build()
    return None


"""Method for deleting all entries from the url-table (database)"""


def get_sql_delete_query():
    return 'DELETE from url;'
