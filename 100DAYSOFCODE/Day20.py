import pandas as pd
from matplotlib import pyplot as plt
data = {
    'Category': ['Groceries', 'Rent', 'Utilities', 'Entertainment', 'Travel', 'Miscellaneous'],
    'Amount': [4500, 12000, 3000, 2000, 4000, 1500]
}
df = pd.DataFrame(data)

total_expenses = df['Amount'].sum()

print("Category-wise Expenses:\n", df)

df['Percentage'] = (df['Amount'] / total_expenses) * 100

print(f"\nTotal Expenses: ₹{total_expenses}")

df.plot(kind='bar', x='Category', y='Amount', title='Monthly Expenses Breakdown', legend=False)
plt.show()









