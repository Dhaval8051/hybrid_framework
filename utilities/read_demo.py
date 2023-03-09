# To understand - how to read csv, excel and json file
import pandas

df=pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv",delimiter=";")
print(df)