import sys
import pandas as pd
from pprint import pprint
from elasticsearch import Elasticsearch

host = [{'host': 'localhost', 'port': 9200}]
index_name, index_type = 'news_index', 'news_type'
es = Elasticsearch(host)

def match_all():
	"""Match all the documents in the index"""
	query = {'query': {'match_all': {}}}
	return query

def search_index(query):
	requests = []
	header = {'index': index_name, 'doc_type': index_type}
	requests.extend([header, query])

	result = es.msearch(body=requests)['responses'][0]
	pprint(result)

if __name__ == '__main__':
	search_index(match_all())
