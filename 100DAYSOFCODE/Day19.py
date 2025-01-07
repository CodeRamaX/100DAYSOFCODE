import matplotlib.pyplot as plt

# Data: Daily time distribution (in hours)
activities = ['Sleep', 'Work', 'Exercise', 'Leisure', 'Other']
time_spent = [7, 8, 1, 5, 3]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
# Creating the pie chart
plt.figure(figsize=(8, 8))
plt.pie(time_spent, labels=activities, colors=colors, autopct='%1.1f%%', startangle=90)
# Adding title
plt.title("Daily Time Distribution", fontsize=16)
# Displaying the chart
plt.show()



