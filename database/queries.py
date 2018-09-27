import dbconnect as db


def get_url():
    query = "SELECT * FROM url"
    return db.query_db(query)