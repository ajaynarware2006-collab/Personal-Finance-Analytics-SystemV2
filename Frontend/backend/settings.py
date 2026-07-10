from backend.connection import connecting


def get_user_expenses(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT expense_id,category_name,amount,expense_date FROM user_view WHERE user_id=%s",(user_id,))

            user_expenses=cursor.fetchall()

            return user_expenses


def add_expense(category_id,user_id,amount,description,pay_method):

    with connecting() as connection:
        with connection.cursor() as cursor:

            cursor.execute("INSERT INTO expenses (user_id,category_id,amount,description,payment_method) VALUES(%s,%s,%s,%s,%s)",(user_id,category_id,amount,description,pay_method))
            connection.commit()
            return "Expense Successfully Added"


def delete_expense(user_id,expense_id):

    with connecting() as connection:
        with connection.cursor() as cursor:

            cursor.execute("DELETE FROM expenses WHERE expense_id=%s AND user_id=%s",(expense_id,user_id))

            connection.commit()

            return "Expense Successfully Deleted."


def update_expense(user_id,new_amount,new_category_id,expense_id):

    with connecting() as connection:
        with connection.cursor() as cursor:


            cursor.execute("UPDATE expenses SET amount=%s,category_id=%s WHERE expense_id=%s AND user_id=%s",(new_amount,new_category_id,expense_id,user_id))

            connection.commit()
            
            return "Expense Successfully Update."


