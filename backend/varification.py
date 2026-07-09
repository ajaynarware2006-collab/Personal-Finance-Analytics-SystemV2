from backend.connection import connecting

def login(name,password):
    with connecting() as connection:
                with connection.cursor() as cursor:
                        cursor.execute("SELECT user_id,name,password FROM users WHERE name=%s AND password=%s",(name,password))
                        user=cursor.fetchone()
                        return user
                
def signup(name,income,password,budget):
        with connecting() as connection:
                with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO users(name,monthly_income,password,budget) VALUES (%s,%s,%s,%s) RETURNING user_id;",(name,income,password,budget))
                        user_id=cursor.fetchone()
                        return user_id
        