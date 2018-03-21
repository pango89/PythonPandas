import pandas as pd
from Classes import RouteSchema
import json

df = pd.read_excel("sample1.xls", sheet_name='Sheet1')
#print(df)
data = df.to_json(orient ='records',date_format='iso')
input_data = json.loads(data)
#print(data)
schema = RouteSchema(many=True)
obj = schema.load(input_data)





if __name__ == '__main__':
    print("All Done")