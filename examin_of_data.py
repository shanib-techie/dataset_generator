import pandas as pd

df = pd.read_excel("C:\\Users\\Admin\\OneDrive\\Desktop\\dataset_generator_python\\dataset.xlsx")

print(df["TYRE_COMPANY"].value_counts())