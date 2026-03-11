import pandas as pd

data=[["Alice",28,70000],
      ["Bob",34,80000],
      ["Charlie",25,50000],
      ["Diana",42,110000],
      ["Ethan",30,75000]]

df = pd.DataFrame(data,columns="Name Age Salary".split())
print(df)
print()

df['Tax'] = df["Salary"]*0.2
print(df)
print()

above_30 = df[df['Age']>=30]
print(above_30)
print()

under_30 = df[df["Age"]<30]
print(under_30)
print(under_30["Salary"].mean())
print()

print(df.sort_values("Salary"))