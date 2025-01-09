import pandas as pd
import matplotlib.pyplot as plt
data = {
    'State': [
        'Andaman and Nicobar', 'Arunachal Pradesh', 'Assam', 'Meghalaya',
        'Nagaland', 'Manipur', 'West Bengal', 'Orissa',
        'Bihar (Plains)', 'Uttar Pradesh (Plains)'
    ],
    'Region': [
        'Andaman and Nicobar Islands', 'Arunachal Pradesh',
        'Assam and Meghalaya', 'Assam and Meghalaya',
        'Nagaland, Manipur, Mizoram, Tripura', 'Nagaland, Manipur, Mizoram, Tripura',
        'Sub-Himalayan West Bengal and Sikkim', 'Orissa',
        'Bihar Plains', 'Plain of West Uttar Pradesh'
    ],
    'Rainfall (mm)': [2967, 2782, 2818, 2818, 1881, 1881, 2739, 1489, 1186, 896]
}
df = pd.DataFrame(data)

print("Average Rainfall:", df['Rainfall (mm)'].mean())
print("State with Maximum Rainfall:", df.loc[df['Rainfall (mm)'].idxmax()]['State'])

plt.figure(figsize=(10, 6))
plt.bar(df['State'], df['Rainfall (mm)'], color='skyblue')
plt.title('Rainfall Comparison Across 10 States', fontsize=14)
plt.xlabel('State', fontsize=12)
plt.ylabel('Rainfall (mm)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()







