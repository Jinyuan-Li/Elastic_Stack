import flask
from flask import jsonify, request
from elasticsearch import Elasticsearch


# 範例
# http://127.0.0.1:5000/cities?city_name=台北
# http://127.0.0.1:5000/gapminder?country=Taiwan
# http://127.0.0.1:5000/es?response=200


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False


index = 'kibana_sample_data_logs'
es = Elasticsearch(hosts="http://192.168.0.61:9200/", http_auth=('jinyuan', 'Pn123456'))
query_json = {}
size = 10
# size = es.search(index=index, body=query_json)['hits']['total']['value']
query = es.search(index=index, body=query_json, size=size)
result = query['hits']['hits']
es_list = []
for i in range(size):
    es_list.append(result[i]['_source'])


@app.route('/', methods=['GET'])
def home():
    return "<h1>api2!</h1>"


@app.route('/es/all', methods=['GET'])
def es_all():
    return jsonify(es_list)


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
