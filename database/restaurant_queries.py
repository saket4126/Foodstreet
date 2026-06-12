from database.db import db, cursor

def add_restaurant_request(data):

    sql = """
    INSERT INTO restaurant_requests
    (restaurant_name, owner_name, email,
    phone, address, cuisine, description)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(sql, data)
    db.commit()