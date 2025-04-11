# 📊 Smart Budget Helper

A simple  personal finance tracker that helps you record your Income and Expenses, view summaries by Category, and generate insightful Charts📈


## 🚀 Features

- Add transactions (income/expense) with category and date
- View all transactions in a tabulated format
- View total income, expense, and balance
- View totals by category (separating income and expense)
- Delete transactions
- Visualize category-wise expenses using Bar chart and Pie chart


## 🛠 Technologies Used

- Python 🐍
- CSV for data storage
- tabulate for tabular view
- matplotlib for charts


## 📁 File Structure

```
smart-budget-helper/
│
├── data/
│   └── expense.csv        # Stores all transaction data
│
├── main.py                # Main script to run the project
└── README.md              # Project description
```




## 💻 How to Run

1. Make sure you have Python installed
2. Install required modules:
   * matplotlib
   * tabulate
3. Run the Program

## ‼️IMPORTENT
if you're running the project using IDLE or directly from a terminal, you might notice that the data folder is created in a different location than expected.
This happens because, in VS Code, the script is typically run from the project root (where data/ already exists). But in IDLE or other environments, the script may be run from the location of main.py, causing Python to create a new data folder next to main.py instead.
