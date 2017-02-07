### Project: Build and Search an Elasticsearch Index 

### Highlights:

 - Build an Elasticsearch engine.
 - Search an Elasticsearch index with appropriate queries.
 - The Elasticsearch Engine was built with **Elasticsearch** and **Python APIs** on **AWS EC2**.

### Data: [Kaggle News Aggregator Dataset](https://www.kaggle.com/uciml/news-aggregator-dataset)

### Build the index:

 - Make sure **Elasticsearch is running** before building an index
 - Command: python3 build_index.py sample_data.csv
 - Example: ```python3 build_index.py ./data/uci-news-aggregator.csv.zip```

### Search the index:

 - Make sure **Elasticsearch is running** before searching an index
 - Command: python3 search_index.py
 - Example: ```python3 search_index.py```

### Reference:
 - [Elasticsearch](https://www.kaggle.com/uciml/news-aggregator-dataset)
 - [Python Elasticsearch APIs](http://elasticsearch-py.readthedocs.io/en/master/)
