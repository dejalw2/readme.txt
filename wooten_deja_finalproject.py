'''Expense input: users will be able to input their expenses, the date, the amount, store (name of store or vendor) and category (groceries, entertainment, travel).
  - format for the date (yyyy-mm-dd). 
Budget setting: users will set monthly budgets for different expense categories. 
  - set_budget(category,amount). 
  - category (str) the name of the expense category. 
    - utilities, insurance, transportation, restaurants, subscriptions, clothing, travel, shoes etc.
  - amount (float) the monthly budget amount a specific category. 
Report: reports will be generated explaining expenses and total spending. 
  - generate_report(). '''
import matplotlib.pyplot as plt
from prettytable import PrettyTable


category = ["travel", "monthly subscriptions", "apparel", "bills", "restaurants", "transportation"]


table = PrettyTable()

table.add_column("Possible Categories", category)


print(table)

class ExpenseInput:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, store, category):
        self.expenses.append({
            'date': date,
            'amount': amount,
            'store': store,
            'category': category
        })

class BudgetSetting:
    def __init__(self):
        self.budgets = {}

    def set_budget(self, category, amount):
        self.budgets[category] = amount

class ReportGeneration:
    def __init__(self, expense_input, budget_setting):
        self.expense_input = expense_input
        self.budget_setting = budget_setting

    def generate_report(self):
        total_spent = sum(expense['amount'] for expense in self.expense_input.expenses)
        print("Total spent: ${:.2f}".format(total_spent))

        for category, budget in self.budget_setting.budgets.items():
            total_spent_category = sum(expense['amount'] for expense in self.expense_input.expenses if expense['category'] == category)
            print("Category: {}, Budget: ${:.2f}, Spent: ${:.2f}".format(category, budget, total_spent_category))

def input_expense():
    date = input("Enter date (yyyy-mm-dd): ")
    amount = float(input("Enter amount spent: "))
    store = input("Enter store name: ")
    category = input("Enter expense category: ")
    return date, amount, store, category

def input_budget():
    category = input("Enter expense category: ")
    amount = float(input("Enter monthly budget for this category: "))
    return category, amount


expense_input = ExpenseInput()
budget_setting = BudgetSetting()
report_generation = ReportGeneration(expense_input, budget_setting)


while True:
    add_expense = input("Do you want to add an expense? (yes/no): ")
    if add_expense.lower() != 'yes':
        break
    date, amount, store, category = input_expense()
    expense_input.add_expense(date, amount, store, category)

while True:
    add_budget = input("Do you want to set a budget? (yes/no): ")
    if add_budget.lower() != 'yes':
        break
    category, amount = input_budget()
    budget_setting.set_budget(category, amount)


report_generation.generate_report()
'''
Integrating expense input, budget setting, and report generation functionalities.
Expense input class: class implementing methods for inputting expenses (add_expenses()). 
Budget setting class: class for setting and managing monthly budgets. 
Report generation class: class will contain methods for generating reports that summarize expenses and spending habits.'''
#pbc = ("travel","monthly subscriptions","apparel","bills","restaurants" )
#print (pbc)
class ExpenseInput:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, store, category):
        self.expenses.append({
            'date': date,
            'amount': amount,
            'store': store,
            'category': category
        })

    def get_expenses_by_category(self):
        expenses_by_category = {}
        for expense in self.expenses:
            category = expense['category']
            if category in expenses_by_category:
                expenses_by_category[category] += expense['amount']
            else:
                expenses_by_category[category] = expense['amount']
        return expenses_by_category

class BudgetSetting:
    def __init__(self):
        self.budgets = {}

    def set_budget(self, category, amount):
        self.budgets[category] = amount

class ReportGeneration:
    def __init__(self, expense_input, budget_setting):
        self.expense_input = expense_input
        self.budget_setting = budget_setting

    def generate_report(self):
        total_spent = sum(expense['amount'] for expense in self.expense_input.expenses)
        print("Total spent: ${:.2f}".format(total_spent))

        for category, budget in self.budget_setting.budgets.items():
            total_spent_category = sum(expense['amount'] for expense in self.expense_input.expenses if expense['category'] == category)
            print("Category: {}, Budget: ${:.2f}, Spent: ${:.2f}".format(category, budget, total_spent_category))
        
        expenses_by_category = self.expense_input.get_expenses_by_category()
        categories = list(expenses_by_category.keys())
        amounts = list(expenses_by_category.values())

        plt.bar(categories, amounts, color='pink')
        plt.xlabel('Category')
        plt.ylabel('Amount Spent')
        plt.title('Expenses by Category')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()


expense_input = ExpenseInput()
budget_setting = BudgetSetting()
report_generation = ReportGeneration(expense_input, budget_setting)




'''Three Functions: expense input, budget setting, and report generation. 

Expense Input Function: input expenses (date, amount, store, category)

Budget Setting Function: set monthly budgets for each category (potential categories: groceries, entertainment, travel, etc.) 

Report Generation Function: reports will be generated summing up expenses, total spending etc'''
