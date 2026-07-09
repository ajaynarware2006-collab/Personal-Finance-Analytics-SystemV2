from backend.connection import connecting



def view_categories():
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT category_name FROM category ORDER BY category_id;")
            data=cursor.fetchall()

            return [category[0] for category in data]
