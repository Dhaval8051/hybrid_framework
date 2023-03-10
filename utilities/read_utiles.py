import pandas

df=pandas.read.excel(io="../test_date/orange_test_data.xlsx", sheet_name= "test_Add_valid_employee")

print(df)
print(df.values.tolist())