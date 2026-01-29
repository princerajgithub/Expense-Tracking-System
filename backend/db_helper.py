import logging

import mysql.connector
from contextlib import contextmanager
from logging_setup import logger_setup

logger = logger_setup('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    print("Closing cursor")
    cursor.close()
    connection.close()


def fetch_all_records():
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date_called for {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses
        # for expense in expenses:
        #     print(expense)


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense_called for {expense_date, amount, category, notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date_called for {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary_called for start : {start_date} and end : {end_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute('''SELECT category,sum(amount) as total FROM expenses
        where expense_date between %s and %s
        group by category;''',(start_date, end_date))
        data = cursor.fetchall()
        return data


def fetch_monthly_expense():
    logger.info(f"fetch_monthly_expense called")
    with get_db_cursor() as cursor:
        cursor.execute('''select month(expense_date) as expense_month,
        monthname(expense_date) as month_name,sum(amount) as Total from expenses
                            group by expense_month, month_name
                            order by expense_month''')
        data = cursor.fetchall()
        return data


if __name__ == "__main__":
    # fetch_all_records()
    # expenses = fetch_expenses_for_date("2024-09-30")
    # print(expenses)
    # insert_expense("2024-08-25", 40, "Food", "Eat tasty samosa chat")

    # summary = fetch_expense_summary("2024-08-01","2024-08-05")
    # for record in summary:
    #     print(record)

    # delete_expenses_for_date("2024-08-25")
    # fetch_expenses_for_date("2024-08-20")

    monthly_expense = fetch_monthly_expense()
    for expense in monthly_expense:
        print(expense)
    # print(monthly_expense)