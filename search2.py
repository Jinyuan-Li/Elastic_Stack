import pandas as pd
from collections import Counter
from elasticsearch import Elasticsearch

index = 'kibana_sample_data_logs'
es = Elasticsearch(hosts="http://192.168.43.89:9200/", http_auth=('A/C','PWD'))
query_json = {}

# size = 5
size = es.search(index=index, body=query_json)['hits']['total']['value']
query = es.search(index=index, body=query_json, size=size)
result = query['hits']['hits']

sum_list = []
for i in range(size):
    sum_list.append(result[i]['_source'])

df = pd.DataFrame.from_dict(sum_list)
df[['date', 'time']] = df.timestamp.str.split("T", expand=True)

date = sorted(set(df['date']))
for i in date:
    locals()["counter_%s" % i] = Counter()

for j in range(df.shape[0]):
    locals()["counter_%s" % df.iloc[j, 20]][df.iloc[j, 2]] += 1

fw1 = open(r'/Users/lijinyuan/Desktop/output1.txt', 'w')
for i in date:
    print('%s:%s' % (i, locals()["counter_%s" % i].most_common(10)))
    fw1.write('%s:%s\n' % (i, locals()["counter_%s" % i].most_common(10)))

response = sorted(set(df['response']))
for k in response:
    locals()["counter_%s" % k] = Counter()

for j in range(df.shape[0]):
    locals()["counter_%s" % df.iloc[j, 15]][df.iloc[j, 2]] += 1

fw2 = open(r'/Users/lijinyuan/Desktop/output2.txt', 'w')
for k in response:
    if k > 400:
        print('%s:%s' % (k, locals()["counter_%s" % k].most_common(10)))
        fw2.write('%s:%s\n' % (k, locals()["counter_%s" % k].most_common(10)))
