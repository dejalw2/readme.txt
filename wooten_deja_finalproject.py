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
from datetime import datetime


class ExpenseInput: 
    """
    A class designed to store the information of a all the expenses inputed

    - add_expense(date, amount, store, category). Adds an expense with these details
    - get_expenses_by_category(). Returns the cost of all the expenses as a dictionary

    """
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, store, category): #method of adding expenses 
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
    """
    A class designed to store the information of all the budgets a user wants

    - set_budget(category, amount). How much to set each budget to 

    """
    def __init__(self,expense_input=0,budget_setting=0):
        self.budgets = {}
        self.expense_input = expense_input
        self.budget_setting = budget_setting

    def set_budget(self, category, amount):
        self.budgets[category] = amount
    


class ReportGeneration:
    """
    This class will create the outputed metrics

    - generate_report(). Will print how much each category and total expenses
    - plot_expense_trends(). Visualizes this data

    """
    def __init__(self, expense_input, budget_setting):
        self.expense_input = expense_input
        self.budget_setting = budget_setting

    def generate_report(self): #generate reports that includes data
        total_spent = sum(expense['amount'] for expense in self.expense_input.expenses)
        print("Total spent: ${:.2f}".format(total_spent)) #calculates total spent

        for category, budget in self.budget_setting.budgets.items(): #prints category wise spending
            total_spent_category = sum(expense['amount'] for expense in self.expense_input.expenses if expense['category'] == category)
            print("Category: {}, Budget: ${:.2f}, Spent: ${:.2f}".format(category, budget, total_spent_category))

        return total_spent

    def plot_expense_trends(self):
        dates = [expense['date'] for expense in self.expense_input.expenses]
        amounts = [expense['amount']for expense in self.expense_input.expenses]
        dates = [datetime.strptime(date.strip(),'%Y-%m-%d') for date in dates]

        for category, budget in self.budget_setting.budgets.items():
            total_spent_category = sum(expense['amount'] for expense in self.expense_input.expenses if expense['category'] == category)
            print("Category: {}, Budget: ${:.2f}, Spent: ${:.2f}".format(category, budget, total_spent_category))
        #visualize expenses by category
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


if __name__ == "__main__":
    #Now in the main class

    #lets setup a function to input all the expenses
    def input_expense():
        date = input("Enter date (yyyy-mm-dd): ")
        amount = float(input("Enter amount spent: "))
        store = input("Enter store name: ")
        category = input("Enter expense category: ")
        return date, amount, store, category

    #lets do the same for budget
    def input_budget():
        category = input("Enter expense category: ")
        amount = float(input("Enter monthly budget for this category: "))
        return category, amount

    #now initialize the potential categories
    category = ["travel", "monthly subscriptions", "apparel", "bills", "restaurants", "transportation"] #defining possible category 

    #print them nicely
    table = PrettyTable()
    table.add_column("Possible Categories", category) #creating table for categories 
    print("Add extensive amount of data regrading spending habits and budget setting for the best results.")
    print(table)

    #setup all the needed objects
    expense_input = ExpenseInput()
    budget_setting = BudgetSetting()
    report_generation = ReportGeneration(expense_input, budget_setting)

    #now actually prompt the user using the methods we just definied
    while True:
        add_expense = input("Do you want to add an expense? (yes/no): ")
        if add_expense.lower() != 'yes':
            break
        date, amount, store, category = input_expense()
        expense_input.add_expense(date, amount, store, category)

    #do the same with budgets
    while True:
        add_budget = input("Do you want to set a budget? (yes/no): ")
        if add_budget.lower() != 'yes':
            break
        category, amount = input_budget()
        budget_setting.set_budget(category, amount)


    #finally generate all the reports
    report_generation.generate_report()
    report_generation.generate_report()
    report_generation.plot_expense_trends()


    ##IGNORE AFTER HERE:
    """
    #reminder_system = ReminderSystem(expense_input)


    class ReminderSystem: 
        def __init__ (self,expense_input):
            self.expense_input = expense_input 
        def check_due_dates(self):#check due dates of bills and send reminders
            pass
    reminder_system.check_due_dates()
    """