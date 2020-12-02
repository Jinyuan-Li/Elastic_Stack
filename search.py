import pandas as pd
from elasticsearch import Elasticsearch

index = 'kibana_sample_data_ecommerce'
es = Elasticsearch(hosts="http://192.168.43.89:9200/", http_auth=('A/C','PWD'))
query_json = {
    # "_source": [ "ip", "machine" ]
}

# size = 5
size = es.search(index=index, body=query_json)['hits']['total']['value']
query = es.search(index=index, body=query_json, size=size)
result = query['hits']['hits']

sum_list = []
for i in range(size):
    sum_list.append(result[i]['_source'])

df_output = pd.DataFrame.from_dict(sum_list)
df_output.to_excel(r'/Users/lijinyuan/Desktop/test.xlsx', index=0)
