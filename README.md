# Example of Django application using Elasticsearch 

## Elasticsearch

Elasticsearch is a distributed search and analytics engine designed for fast and scalable data retrieval. It's built on top of Apache Lucene, an open-source search library, and is commonly used to index, search, and analyze large volumes of data quickly. Data in Elasticsearch is stored as documents, which are essentially JSON objects consisting of key-value pairs (fields).
Documents are organized into indices (analogous to tables in a relational database). An index contains many documents with similar characteristics, such as log data or product listings. Elasticsearch indices are divided into shards, which are smaller units of the index distributed across the cluster. Each shard can be thought of as a self-contained, independent index that can be stored on any node in an Elasticsearch cluster.

The core of Elasticsearch's indexing mechanism is the inverted index. This structure allows Elasticsearch to perform full-text searches quickly. The inverted index maps each unique word or term (a token) in a document to the documents that contain that term.
Instead of searching every document directly, Elasticsearch looks up the terms in the inverted index to find matching documents, which makes searches highly efficient.


When a document is added to an index, the following happens:

- Tokenization: The text fields of the document are broken down into individual terms or tokens (like splitting sentences into words). This process is called analyzing and is controlled by an analyzer.
- Inverted Index Creation: Each token is then indexed in the inverted index, where it points to the documents containing the token.
- Storage: The original document is also stored so that it can be retrieved later if necessary (depending on the index settings).

When a search query is executed, Elasticsearch goes through the following steps:

- Query Parsing: The query is parsed and terms are extracted.
- Search Across Shards: The search is performed on all the relevant shards (primary and replica) in parallel.
- Relevance Scoring: Elasticsearch calculates a relevance score based on how well documents match the query. The most relevant documents are then returned.
- Aggregation (Optional): Elasticsearch can also perform aggregations, allowing for operations like counting, averaging, or summing values across documents.

In order to start Elasticsearch follow [instructions from the official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html).

## Setup of the example

In order for Django application to be able to communicate with Elasticsearch, install *elasticsearch-dsl* package with following command:
```
pip install elasticsearch-dsl
```
**Note**: First step is to install Elasticsearch. After that, you should install proper version of *elasticsearch-dsl* package that corresponds to the selected version of the Elasticsearch platform. You can check the documentation of the package for the compatibility details.

Adding testing data to database can be achieved by running command:
```
python manage.py popuni_bazu
```

Adding testing data to Elasticsearch can be achieved by running command:
```
python manage.py popuni_podatke_za_pretragu
```

## How to connect Django application with Elasticsearch?

Add following line of code into Django application settings:
```
connections.create_connection('default', hosts=['localhost'], timeout=60)
```

An example of a Document structure can be seen in *index.py* file. File *pretraga_view.py* demonstrates performing different queries and handling the results.


**Note**: This code was tested with Elasticsearch 7.6.2 and elasticsearch-dsl 7.4.1.
