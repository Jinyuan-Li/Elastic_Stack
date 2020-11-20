import flask
import numpy as np
import pandas as pd
from flask_cors import CORS
from collections import Counter
from flask import jsonify, request
from elasticsearch import Elasticsearch
from datetime import timedelta, datetime


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False


# 讀取Elasticsearch資料，輸出為jsonify()可讀取格式
index = 'kibana_sample_data_logs'
es = Elasticsearch(hosts="http://192.168.0.61:9200/", http_auth=('jinyuan', 'Pn123456'))
query_json = {}

size = 1000
# size = es.search(index=index, body=query_json)['hits']['total']['value']
query = es.search(index=index, body=query_json, size=size)
result = query['hits']['hits']
es_list = []
for i in range(size):
    es_list.append(result[i]['_source'])


# 因讀取資料可能非每日皆有404/503資料，故產出開始至結束日期每天日期之list
df = pd.DataFrame.from_dict(es_list)
df[['date', 'time']] = df.timestamp.str.split("T", expand=True)
df.to_excel(r'C:\Users\user\Desktop\test.xlsx', index=0)

date_old = sorted(set(df['date']))
interval = (datetime.strptime(date_old[-1], "%Y-%m-%d") - datetime.strptime(date_old[0], "%Y-%m-%d")).days
date_new = pd.DataFrame([str((datetime.strptime(date_old[0], "%Y-%m-%d") + timedelta(i)).date()) for i in range(interval + 1)])

# print('%s~~%s' % (date_old[0], date_old[-1]))
# print('%s~~%s' % (date_new[0], date_new[-1]))


# 每天日期之list分為404/503
date_404, date_503 = date_new.copy(), date_new.copy()
date_404[1],date_503[1] = 404, 503


# 計算404/503在每天的數量，並合併為單一DataFrame
counter_404, counter_503 = Counter(), Counter()
for j in range(df.shape[0]):
    if df.iloc[j, 14] != 200:
        locals()["counter_%s" % df.iloc[j, 14]][df.iloc[j, 20]] += 1

count_404 = pd.DataFrame(counter_404.most_common())
count_503 = pd.DataFrame(counter_503.most_common())
df_404 = pd.merge(date_404, count_404, how='left', on=0)
df_503 = pd.merge(date_503, count_503, how='left', on=0)
df_sum = pd.concat([df_404, df_503], ignore_index=True)
df_sum.columns = ['date', 'response', 'count']
df_sum['count'] = df_sum['count'].fillna(0)


date_response_list = []
for i in range(df_sum.shape[0]):
    ser = df_sum.loc[i, :]
    row_dict = {}
    for idx, val in zip(ser.index, ser.values):
        if type(val) is str:
            row_dict[idx] = val
        elif type(val) is np.int64:
            row_dict[idx] = int(val)
        elif type(val) is np.float64:
            row_dict[idx] = float(val)
    date_response_list.append(row_dict)


@app.route('/', methods=['GET'])
def home():
    return "<h1>api2!</h1>"


@app.route('/es/all', methods=['GET'])
def es_all():
    return jsonify(es_list)


@app.route('/es/date_response', methods=['GET'])
def date_response_all():
    return jsonify(date_response_list)


@app.route('/es', methods=['GET'])
def response():
    if 'response' in request.args:
        response = int(request.args['response'])
    else:
        return "Error: No response provided. Please specify a response."
    results2 = []
    for elem in es_list:
        if elem['response'] == response:
            results2.append(elem)
    return jsonify(results2)


app.run()
