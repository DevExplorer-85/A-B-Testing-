import pandas as pd

df = pd.read_csv("BangaloreZomatoData.csv")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)
print("\nInfo:")
print(df.info())