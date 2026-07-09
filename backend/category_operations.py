from backend.connection import connecting



def view_categories():
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT category_name,category_id FROM category ORDER BY category_id;")
            data=cursor.fetchall()

            return [(category[0] , category[1]) for category in data]