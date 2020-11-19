import requests
import pandas as pd


r = requests.get("http://127.0.0.1:5000/es?response=503")
list_of_dicts = r.json()

# print(len(list_of_dicts))

sum_list = []
for i in range(len(list_of_dicts)):
    sum_list.append(list_of_dicts[i])

df_output = pd.DataFrame.from_dict(sum_list)
df_output.to_excel(r'C:\Users\user\Desktop\test.xlsx', index=0)
