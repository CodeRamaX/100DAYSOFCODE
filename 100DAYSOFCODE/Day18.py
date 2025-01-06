from matplotlib import pyplot as plt
# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Data
temperature = [30, 32, 31, 33, 35, 36, 34]
humidity = [70, 65, 75, 60, 80, 78, 74]
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(days, temperature, marker='o', label="Temperature (°C)", color='r')
plt.plot(days, humidity, marker='s', label="Humidity (%)", color='b')
plt.title("Temperature vs Humidity Over a Week", fontsize=14)
plt.xlabel("Days", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
