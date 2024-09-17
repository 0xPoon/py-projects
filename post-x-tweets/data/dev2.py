import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e']
}

df = pd.DataFrame(data)

print(df)

# Introduce some 'None' values in the DataFrame
df.loc[1, 'A'] = None
df.loc[3, 'B'] = None

# Fill down cells based on the previous row's value
df_filled = df.ffill

print("Original DataFrame:")
print(df)

print("\nDataFrame with down-filled values:")
print(df_filled)