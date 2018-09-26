import mysql.connector
from flask import g


def connect():
    from main import app
    conn = mysql.connector.connect(user=app.config["MYSQL_DATABASE_USER"],
                                   password=app.config["MYSQL_DATABASE_PASSWORD"],
                                   host=app.config["MYSQL_DATABASE_HOST"],
                                   database=app.config["MYSQL_DATABASE_DB"])
    return conn


def disconnect_db():
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = connect()
        db.row_factory = make_dicts
    return db


def fetch_all(cur):
    rv = []
    row = cur.fetchone()
    while row is not None:
        rv.append(make_dicts(cur,row))
        row = cur.fetchone()
    if len(rv) == 0:
        return None
    else:
        return rv


def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.cursor()
    cur.execute(query, args)
    rv = fetch_all(cur)
    cur.close()
    db.commit()
    return (rv[0] if rv else None) if one else rv
