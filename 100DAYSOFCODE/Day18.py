from matplotlib import pyplot as plt
# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Winter (January) data
temperature = [7, 5, 6, 8, 4, 3, 5]  # Average temperature (°C)
humidity = [80, 85, 82, 78, 90, 92, 88]  # Humidity percentage
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(days, temperature, marker='o', label="Temperature (°C)", color='b')
plt.plot(days, humidity, marker='s', label="Humidity (%)", color='g')
plt.title("Temperature vs Humidity: January Winter Trends", fontsize=14)
plt.xlabel("Days", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
