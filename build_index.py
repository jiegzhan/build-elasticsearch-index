import sys
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch import helpers

host = [{'host': 'localhost', 'port': 9200}]
index_name, index_type = 'news_index', 'news_type'
es = Elasticsearch(host)

def load_dataframe_into_index(df, **kwargs):
	for column in df.columns:
		df[column] = df[column].astype('str')

	df = df.apply(lambda x: x.str.strip(), axis=1)
	data = df.to_dict(orient='records')

	actions = []
	offset = kwargs['chunk_count'] * kwargs['chunksize']
	for i in range(len(data)):
		# creating actions for a bulk load operation
		action = {
			'_index': index_name,
			'_type': index_type,
			'_id': offset + i,
			'_source': data[i]
		}
		actions.append(action)

	# Bulk load the index
	if len(actions) > 0:
		helpers.bulk(es, actions)

def build_index():
	filename = sys.argv[1]

	print(es.info())
	chunk_count, chunksize = 0, 1000
	reader = pd.read_csv(filename, chunksize=chunksize, compression='zip')

	for chunk in reader:
		chunk_count += 1
		print("Chunk {0}".format(chunk_count))

		kwargs = {"chunk_count": chunk_count, "chunksize": chunksize}
		load_dataframe_into_index(chunk, **kwargs)

if __name__ == '__main__':
	build_index()
