import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset 
file_path = 'customers-100.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path).head(50)

# Fill missing values in Phone 2 with 'Not Provided'
data['Phone 2'] = data['Phone 2'].fillna('Not Provided')

# Convert Subscription Date to datetime and extract month/year
data['Subscription Date'] = pd.to_datetime(data['Subscription Date'], errors='coerce')
data['Subscription Month'] = data['Subscription Date'].dt.month
data['Subscription Year'] = data['Subscription Date'].dt.year

# Count customers by country
data['Country'].value_counts().plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Number of Customers by Country')
plt.xlabel('Country')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('country_distribution.png')
plt.show()

# Plot subscription trends
data.groupby(['Subscription Year', 'Subscription Month']).size().plot(kind='line', marker='o', color='green', figsize=(10, 6))
plt.title('Monthly Subscription Trends')
plt.xlabel('Time (Year, Month)')
plt.ylabel('Number of Subscriptions')
plt.xticks(rotation=45, ha='right')
plt.grid()
plt.tight_layout()
plt.savefig('subscription_trends.png')
plt.show()

# Fetch customer details by Customer ID
def fetch_customer_details(customer_id):
    customer = data[data['Customer Id'] == customer_id]
    return customer if not customer.empty else "Customer ID not found."

# Example Usage
print(fetch_customer_details(101))  # Replace 101 with an actual Customer ID

print("Visualizations saved as 'country_distribution.png' and 'subscription_trends.png'")


