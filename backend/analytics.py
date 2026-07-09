from backend.connection import connecting



def highest_expense(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT category_name,MAX(amount) FROM user_view WHERE user_id=%s GROUP BY category_name;",(user_id,))

            all_expenses=cursor.fetchall()
            if all_expenses == None:
                return None
            cursor.execute("SELECT MAX(amount) FROM user_view WHERE user_id=%s;",(user_id,))
            max_expense=cursor.fetchone()
            if not max_expense:
                return None
            else:
                max_expense=max_expense[0]


            for expense in all_expenses:
                if max_expense==expense[1]:
                    return max_expense

def lowest_expense(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT category_name,MIN(amount) FROM user_view WHERE user_id=%s GROUP BY category_name;",(user_id,))

            all_expenses=cursor.fetchall()
            if all_expenses == None:
                return None

            cursor.execute("SELECT MIN(amount) FROM user_view WHERE user_id=%s;",(user_id,))
            min_expense=cursor.fetchone()
            if not min_expense:
                return None
            else:
                min_expense=min_expense[0]


            for expense in all_expenses:
                if min_expense==expense[1]:
                    return min_expense

def monthly_expense(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT TO_CHAR(DATE_TRUNC('month',expense_date)::TIMESTAMP,'Month') AS month, SUM(amount) AS total_expense FROM user_view WHERE user_id=%s GROUP BY month ORDER BY month DESC;",(user_id,))

            data=cursor.fetchall()
            if not data:
                return None
            
            return data

def yearly_expense(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT TO_CHAR(DATE_TRUNC('year',expense_date)::TIMESTAMP,'YYYY') AS year, SUM(amount) AS total_expense FROM user_view WHERE user_id=%s GROUP BY year ORDER BY year DESC;",(user_id,))

            data=cursor.fetchall()
            if not data:
                return None
            
            return data

def category_summary(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT category_name,SUM(amount) FROM user_view WHERE user_id=%s GROUP BY category_name;",(user_id,))

            data=cursor.fetchall()
            if not data:
                return None

            return data

def average_daily_expense(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT TO_CHAR(DATE_TRUNC('month',expense_date)::TIMESTAMP,'Month') AS month, ROUND(AVG(amount)) AS avg_expense FROM user_view WHERE user_id=%s GROUP BY month ORDER BY month DESC;",(user_id,))
            data=cursor.fetchall()
            if not data:
                return None
            
            return data

def monthly_savings(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT (users.monthly_income::INTEGER-SUM(user_view.amount)::INTEGER) AS saving ,TO_CHAR(DATE_TRUNC('month',user_view.expense_date)::TIMESTAMP,'Month YYYY') AS months FROM users JOIN user_view ON users.user_id=user_view.user_id  WHERE users.user_id=%s GROUP BY  users.user_id,users.monthly_income,DATE_TRUNC('month',user_view.expense_date) order by DATE_TRUNC('month',user_view.expense_date);",(user_id,))

            data=cursor.fetchall()
            if not data:
                return None
            
            return data

def current_month_expense(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATE_TRUNC('month',expense_date) AS month, SUM(amount) AS total_expense FROM user_view  WHERE user_id=%s GROUP BY month ORDER BY month DESC;",(user_id,))

            data=cursor.fetchone()
            if not data:
                return None
            
            return data[1]

def top_category(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT category_name,SUM(amount) FROM user_view WHERE user_id=%s group by category_name order by SUM(amount) DESC;",(user_id,))

            top_cat=cursor.fetchone()
            if top_cat==None:
                return None
            
            return top_cat[0]  
    
def total_savings(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT SUM(saving) FROM (SELECT (users.monthly_income::INTEGER-SUM(user_view.amount)::INTEGER) AS SAVING ,TO_CHAR(DATE_TRUNC('month',user_view.expense_date)::TIMESTAMP,'Month YYYY') FROM users JOIN user_view ON users.user_id=user_view.user_id  WHERE users.user_id=%s GROUP BY  users.user_id,users.monthly_income,DATE_TRUNC('month',user_view.expense_date) order by DATE_TRUNC('month',user_view.expense_date));",(user_id,))

            total=cursor.fetchone()
            if total==None:
                return None
            else:
                return total[0]

def budget_remaining(user_id):
    with connecting() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT SUM(amount) FROM user_view WHERE user_id=%s AND DATE_TRUNC('MONTH',expense_date)=DATE_TRUNC('MONTH',current_date) group by DATE_TRUNC('MONTH',expense_date);",(user_id,))

            total_expesnse=cursor.fetchone()
            if not total_expesnse:
                return None
            else:
                total_expesnse=total_expesnse[0]

            cursor.execute("SELECT budget FROM users WHERE user_id=%s;",(user_id,))
            budget=cursor.fetchone()[0]

            return budget - total_expesnse
