
from wooten_deja_finalproject import ExpenseInput
from wooten_deja_finalproject import BudgetSetting
from wooten_deja_finalproject import ReportGeneration


def test_expense():
	ei = ExpenseInput()
	ei.add_expense("2024-05-01", 100, "Chipotle", "restaurants")

	loaded_expenses = ei.expenses
	assert {
            'date': "2024-05-01",
            'amount': 100,
            'store': "Chipotle",
            'category': "restaurants"
        } in loaded_expenses

def test_budget():
	bu = BudgetSetting()

	bu.set_budget("travel", 100)
	bu.set_budget("restaurants", 1000)

	budget = bu.budgets

	assert budget['travel'] == 100
	assert budget['restaurants'] == 1000 

def test_report():
	ei = ExpenseInput()
	ei.add_expense("2024-05-01", 100, "Chipotle", "restaurants")
	ei.add_expense("2024-05-01", 2000, "Starbucks", "travel")

	bu = BudgetSetting()
	re = ReportGeneration(ei, bu)

	assert re.generate_report() == 2000+100

