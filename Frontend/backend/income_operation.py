from backend.connection import connecting


def update_income(income,user_id):

        with connecting() as connection:
                with connection.cursor() as cursor:
        
                        cursor.execute("UPDATE users SET monthly_income=%s WHERE user_id=%s;",(income,user_id))
                        connection.commit()
                        return "Income updated successfully"
        

def get_income(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
                cursor.execute("SELECT monthly_income FROM users WHERE user_id=%s;",(user_id,))
                income=cursor.fetchone()[0]
                return income
    