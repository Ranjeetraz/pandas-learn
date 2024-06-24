import pandas as pd
"""This is Series data structure"""
# a=[1,2,3,4,5,6,7,8,9]
# var = pd.Series(a)
# print(var)
# var = pd.Series()
# print(var)
"""pd.Series parameter (inder=[2,3,4,5], dtype="float, name="python)"""
# var = pd.Series(a,index=['a','b','c','d','e','f','g','h','i'])
# print(var)
# print(type(var))

"""this is dataframe"""
# s=pd.Series(12)
# print(s)

# a = [1,2,3,4,5,6,7]
# var = pd.DataFrame(a)
# print(var)

# a = {"a": [3,4,5,6,7], "b": [3,6,8,9,1], "c": [4,7,5,3,2]}
# var = pd.DataFrame(a)
# print(var)
"""insert data in csv file(paramiter possion(index, column_name, column_values )"""
# a = {"a": [3,4,5,6,7], "b": [3,6,8,9,1], "c": [4,7,5,3,2]}
# var = pd.DataFrame(a)
# ab = [34,56,78,90,34]
# var.insert(1,"col_name",ab)
# print(var)
# =======================================================
"""create a csv file from pandas"""

# dic = {"age": [12,34,56,12], "name": ["ranjeet", "suraj", "niraj", "manish"], "rollno": [12,45,76,34]}
# print(dic)  
# a = pd.DataFrame(dic)

"""create csv file with index"""

# dic = {"age": [12,34,56,12], "name": ["ranjeet", "suraj", "niraj", "manish"], "rollno": [12,45,76,34]}
# a = pd.DataFrame(dic)
# a.to_csv("r.txt")
# a.to_csv("with_index.csv")
"""without indexsing"""
# dic = {"age": [12,34,56,12], "name": ["ranjeet", "suraj", "niraj", "manish"], "rollno": [12,45,76,34]}
# a = pd.DataFrame(dic)
# a.to_csv("without_index.csv",index=False)
"""change header"""
# dic = {"age": [12,34,56,12], "name": ["ranjeet", "suraj", "niraj", "manish"], "rollno": [12,45,76,34]}
# a = pd.DataFrame(dic)
# a.to_csv("change_header.csv",index=False, header=["col1","col2","col3"])

# ===============================
"""how to read csv file"""
# print("read csv file ........")
# read_csv = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv")
# print(read_csv)

"""get limit rows using [nrows] method"""
# print("getting row .................")
# get_row = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv", nrows=3)
# print(get_row)

"""getting column using [usecols] method """
# print("getting column .......................")
# get_column = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv", usecols=["name", "age"])
# print(get_column)

"""getting column using column index"""
# get_column = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv", usecols=[1,2])
# print(get_column)

"""change the data type values of specific column"""
# get_column = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv", dtype={"rollno": float})
# print(get_column)

"""Skip the special row"""
# print("skip the row.......................")
# skip_row = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv", skiprows=[1,4])
# print(skip_row)


"""show limit rows using(head(like uper), tail(like niche))"""
# skip_row = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv", skiprows=[1,4])
# print(skip_row.head(2))
# print(skip_row.tail(2))
# print(skip_row.describe())

"""csv getting all columns"""
# get_all_column = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv")
# columns = get_all_column.columns
# print(columns)

""" geting specific rows useing [salasing_rows[starting_index:ending_index] method]"""
# salasing_rows= pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv")
# sapecific = salasing_rows[1:3]
# print(sapecific)
"""sort desending"""
# sort_desing = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv")
# sapecific = sort_desing.sort_index(axis=0, ascending=False)
# print(sapecific)
"""change specifyc value using loc method [index, column]"""
# change_value = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\with_index.csv")
# s = change_value.loc[0, "name"] = "Ranjkumari"
# print(s)
# change_value.to_csv("change_value.csv", index=False)

"""geting specific value useing column and index"""
# data1 = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\without_index.csv", index_col=False)
# change_value = data1["name"][0]
# print(change_value)

"""geting all index useing [index] method"""
# data1 = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\with_index.csv", index_col=False)
# a=data1.index
# print(a)

"""romave particular rows using [dropna] method where colun in non and set default value using [fillna] method"""
# drop_rows = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\with_index.csv")
# d = drop_rows.dropna()
# print(d)

"""replace valuses useing [to_replace=values] method"""
# replace_data = pd.read_csv("C:\\Users\\LENOVO\Desktop\\Ranjeet\\django project\\pandas\\with_index.csv")
# d = replace_data.replace(to_replace=56, value=100)
# d = replace_data.replace(to_replace=[100,12,34], value=[100,23,45])
# print(d)

"""merge data frames useing [merge] method"""
# a = {"id": [1,2,3,4,5], "col1": [3,6,8,9,1], "col2": [4,7,5,3,2]}
# b = {"id": [1,2,3,4,5], "col3": [3,6,8,9,1], "col4": [4,7,5,3,2]}
# var1 = pd.DataFrame(a)
# var2 = pd.DataFrame(b)
# merge_data = pd.merge(var1, var2, on="id")
# merge_data = pd.merge(var2, var1, on="id")
# print(merge_data)

"""join data frames useing [join] method"""
# a = {"id": [1,2,3,4,5], "col1": [3,6,8,9,1], "col2": [4,7,5,3,2]}
# b = {"col3": [3,6,8,9,1], "col4": [4,7,5,3,2]}
# var1 = pd.DataFrame(a)
# var2 = pd.DataFrame(b)
# merge_data = var1.join(var2)
# print(merge_data)
