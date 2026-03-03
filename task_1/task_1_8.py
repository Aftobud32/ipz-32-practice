import pandas as pd

df = pd.read_csv('students_1_8.csv')

df['Avg'] = df[['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5']].mean(axis=1)
print(df)

print("\nСередній бал групи з предметів:")
print(df[['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5']].mean())