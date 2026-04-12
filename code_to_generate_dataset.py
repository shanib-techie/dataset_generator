import random
import pandas as pd

print("===== DATASET GENERATOR =====")

# Step 1: Columns
num_cols = int(input("Kitne columns chahiye? "))

columns = []
col_types = {}
col_values = {}

for i in range(num_cols):
    col_name = input(f"Column {i+1} ka naam: ")
    columns.append(col_name)

    dtype = input(f"{col_name} ka type (string/int): ").lower()
    col_types[col_name] = dtype

    if dtype == "string":
        n = int(input(f"{col_name} ke liye kitne values dene hai? "))
        values = []
        for j in range(n):
            val = input(f"Value {j+1}: ")
            values.append(val)
        col_values[col_name] = values

    elif dtype == "int":
        low = int(input(f"{col_name} ke liye minimum value: "))
        high = int(input(f"{col_name} ke liye maximum value: "))
        col_values[col_name] = (low, high)

    else:
        print("Invalid type, default string le rahe hain")
        col_types[col_name] = "string"
        col_values[col_name] = ["default"]

# Step 2: Rows
num_rows = int(input("Kitni rows chahiye? (100-300-800 etc): "))

# Step 3: Data generation
data = []

for i in range(num_rows):
    row = {}
    for col in columns:
        if col_types[col] == "string":
            row[col] = random.choice(col_values[col])
        else:
            low, high = col_values[col]
            row[col] = random.randint(low, high)
    data.append(row)

# Step 4: DataFrame
df = pd.DataFrame(data)

# Step 5: Format selection
format_choice = input("Output format (excel/json): ").lower()

if format_choice == "excel":
    file_name = "dataset.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Excel file saved as {file_name}")

elif format_choice == "json":
    file_name = "dataset.json"
    df.to_json(file_name, orient="records", indent=4)
    print(f"JSON file saved as {file_name}")

else:
    print("Invalid format, default Excel bana diya")
    df.to_excel("dataset.xlsx", index=False)

print("===== DONE =====")