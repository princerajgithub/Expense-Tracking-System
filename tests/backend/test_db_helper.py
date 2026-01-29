from backend import db_helper

def test_fetch_expense_for_date_aug_15():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == 'Shopping'
    assert expenses[0]['notes'] == 'Bought potatoes'

def test_fetch_expense_for_date_invalid():
    summary = db_helper.fetch_expenses_for_date("9999-08-15")

    assert len(summary) == 0

def test_fetch_expense_summary_invalid_range():
    expenses = db_helper.fetch_expense_summary("9999-08-01","2999-08-05")
    assert len(expenses) == 0