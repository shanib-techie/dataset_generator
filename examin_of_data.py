import pandas as pd
import numpy as np
df = pd.read_excel("C:\\Users\\Admin\\OneDrive\\Desktop\\dataset_generator_python\\dataset.xlsx")

print(df["TYRE_COMPANY"].value_counts())
print(df.columns)
df["PRICE"] = df["PRICE"].round(-3)
df["MILEGE"] =df["MILEGE"].round(-1)
print(df["MILEGE"])
print(df["SEATER"].replace({5:4,6:7}))


# masks1 = df["MANUFACTURE"].between(2016,2022)
# df.loc[masks1,"PRICE"] = np.random.randint(500000,1000000)
# marks2 = df["MANUFACTURE"].between(2023,2026)
# df.loc[marks2,"PRICE"] = np.random.randint(1100000,3200000)

# df["PRICE"] = df["PRICE"].round(-3)
# print(df["PRICE"])

# 9761751583
df.loc[df["ACCIDENT HISTORY"] == "YES" , "MILEGE"] -=20
df.loc[df["ACCIDENT HISTORY"] == "YES" , "PRICE"] -=100000


df.loc[df["ACCIDENT HISTORY"] == "NO" , "MILEGE"] += 50
df.loc[df["ACCIDENT HISTORY"] == "NO" , "PRICE"] += 20000


df.to_csv("CARS.csv",index=False)
# if df["ACCIDENT HISTORY"] == "YES":
#     df["MILEGE"]-20
#     df["PRICE"]-100000
# else:
#     df["MILEGE"]+50
#     df["PRICE"]+20000


print(df)    


# print(df.groupby("PRE_OWNERS")["PRICE"].mean())