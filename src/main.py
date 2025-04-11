import csv
from datetime import datetime
import os
from tabulate import tabulate
import matplotlib.pyplot as plt 

def add_transaction():
    t_type=input("enter transacton type(expense or income)").lower().strip()
    amount=float(input("enter amount:"))
    category=input("enter category").strip()
    date=input("enter date(YYYY-MM-DD) or leave blank for today:").strip()
    if not date:
        date=datetime.today().strftime('%Y-%m-%d')
    file_exist=os.path.isfile("data/expense.csv")

    with open("data/expense.csv",'a',newline='') as f:
         writer=csv.writer(f)
         if not file_exist:
             writer.writerow(['type', 'amount', 'category', 'date'])
         writer.writerow([t_type, amount, category, date])
         print("✅ Transaction recorded!!!")

def view_transaction():
    file_path="data/expense.csv" 
    
    if not os.path.isfile(file_path):
        print("No Transaction found")
        return

    with open("data/expense.csv",'r') as f:
        reader=csv.reader(f)
        rows=list(reader)

    if len(rows)<=1:
        print("no data available")
        return
    header=rows[0]
    data=rows[1:]
    print(tabulate(data, headers=header, tablefmt="grid"))


def view_totals():
    file_path="data/expense.csv" 
    if not os.path.isfile(file_path):
        print("No Transaction found")
        return

    with open("data/expense.csv",'r') as f:
        reader=csv.reader(f)
        rows=list(reader)

    if len(rows)<=1:
        print("no data available")
        return
    
    total_income=0
    total_expense=0
    for i in rows[1:]:
        t_type=i[0].strip().lower()
        try:
            amount=float(i[1])
        except ValueError:
            continue
        if t_type=="expense":
            total_expense+=amount
        elif t_type=="income":
            total_income+=amount
    balance=total_income-total_expense

    print("\nSummary💵")
    print(f"Total income  : {total_income:.2f}")
    print(f"Total expense : {total_expense:.2f}")
    print(f"Balance : {balance:.2f} {'✅'if balance >= 0 else '❌' }")

def view_totals_by_categories():

    file_path="data/expense.csv" 
    if not os.path.isfile(file_path):
        print("No Transaction found")
        return

    with open("data/expense.csv",'r') as f:
        reader=csv.reader(f)
        rows=list(reader)

    if len(rows)<=1:
        print("no data available")
        return

    total_income={}
    total_expense={}
   
    for i in rows[1:]:
        t_type=i[0].strip().lower()
        try:
            amount=float(i[1])
        except ValueError:
            continue
        category=i[2].strip().capitalize()

        if t_type=="expense":
            if category in total_expense:
              total_expense[category]+=amount
            else:
              total_expense[category]=amount
        elif t_type=="income":
            if category in total_income:
              total_income[category]+=amount
            else:
              total_income[category]=amount
    
    print("\n📂 Totals by categories (Income Vs Expense)")
    if total_income:
        print("\n🟢 Income")
        for i,j in total_income.items():
            print(f"{i:<10} ₹{j:.2f}")
    if total_expense:
        print("\n🔴 Expense")
        for i,j in total_expense.items():
            print(f"{i:<10} ₹{j:.2f}")

def delete_transactions():
    file_path="data/expense.csv" 
    if not os.path.isfile(file_path):
        print("No Transaction found")
        return

    with open("data/expense.csv",'r') as f:
        reader=csv.reader(f)
        rows=list(reader)

    if len(rows)<=1:
        print("no data available")
        return
    header=rows[0]
    data=rows[1:]
    
    print("\nTransactions📈")
    for i,j in enumerate(data,start=1):
        print(f"{i}.{', '.join(j)}")

    try:
        ch=int(input("\nEnter the specific number of transaction to delete"))
        if 1 <= ch <= len(data):
            delete=data.pop(ch-1)
            print(f"Deleted ✅: {', '.join(delete)}")
        else:
            print("invalid choice")
            return
    except ValueError:
        print("invalid choice enter a valid number")
        return
    
    
    with open("data/expense.csv",'w',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
           
def show_charts():
    file_path="data/expense.csv" 
    if not os.path.isfile(file_path):
        print("No Transaction found")
        return

    with open("data/expense.csv",'r') as f:
        reader=csv.reader(f)
        rows=list(reader)

    if len(rows)<=1:
        print("no data available")
        return
    data=rows[1:]
    total_income=0
    total_expense=0
    category_expense={}
   
    for i in data:
        t_type=i[0].strip().lower()
        try:
            amount=float(i[1])
        except ValueError:
            continue
        category=i[2].strip().capitalize()

            
        if t_type=="income":
            total_income+=amount
        elif t_type=="expense":
            total_expense+=amount
            if category in category_expense:
              category_expense[category]+=amount
            else:
              category_expense[category]=amount
    #Pie chart
    plt.figure(figsize=(6, 6)) 
    plt.pie([total_income,total_expense],labels=["Income","Expense"], autopct='1%.1f%%',colors=["#8fd9a8", "#ff7f7f"])
    plt.title('Income Vs Expense')
    plt.show()
    #Bar chart
    if category_expense:
        plt.figure(figsize=(8,6))
        categories=list(category_expense.keys())
        amounts=list(category_expense.values())
        plt.bar(categories,amounts,color='red')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Category-Expense-Chart')
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()
def export_summary_report():

    file_path="data/expense.csv" 
    if not os.path.isfile(file_path):
        print("No Transaction found")
        return

    with open("data/expense.csv",'r') as f:
        reader=csv.reader(f)
        rows=list(reader)

    if len(rows)<=1:
        print("no data available")
        return
    
    header=rows[0]
    data=rows[1:]
    
    total_income=0
    total_expense=0
    for i in data:
        t_type=i[0].strip().lower()
        try:
            amount=float(i[1])
        except ValueError:
            continue
        if t_type=="expense":
            total_expense+=amount
        elif t_type=="income":
            total_income+=amount
    balance=total_income-total_expense
    today=datetime.today().strftime('%Y-%m-%d')
    report=f""" BUDGET SUMMARY REPORT- {today}
-------------------------------------- 
Total Income  : ₹{total_income:.2f}
Total Expense : ₹{total_expense:.2f}
Balance       : ₹{balance:.2f} {'✅'if balance >= 0 else '❌' } 

Transactions:
--------------------------------------
"""
    for i in data:
        report += f"{i[0]:<10} | ₹{i[1]:<10} | {i[2]:<10} | {i[3]}\n"
    filename=f"Report{today}.txt"
    with open(filename,'w',encoding='utf-8') as f:
        f.write(report)
    print(f"✅ Report exported to {filename}")    

while True:
    print("\n💰SMART BUDGET HELPER💰")
    print("1️⃣  Add transaction")
    print("2️⃣  View transactions")
    print("3️⃣  View totals")
    print("4️⃣  View totals by category")
    print("5️⃣  Delete Transactions")
    print("6️⃣  Show Charts")
    print("7️⃣  Export Summary")
    print("8️⃣  Exit")
    ch=input("▶️  Enter yourchoice").strip()
    if ch == '1':
       add_transaction()
    elif ch =='2':
        view_transaction()
    elif ch =='3':
        view_totals()
    elif ch == '4':
        view_totals_by_categories()
    elif ch == '5':
        delete_transactions()
    elif ch == '6':
        show_charts()
    elif ch == '7':
        export_summary_report()
    elif ch == '8':
       print("exiting...Thank You")
       break
    else:
        print("Invalid choice")
