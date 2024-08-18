from typing import Dict, List

import numpy as np
from elasticsearch import Elasticsearch, exceptions


QUERY = "When is the next cohort?"


@data_loader
def search(*args, **kwargs) -> List[Dict]:
    
    connection_string = kwargs.get('connection_string', 'http://localhost:9200')
    index_name = kwargs.get('index_name', 'documents')
    top_k = kwargs.get('top_k', 5)

    query = QUERY

    search_query = {
        "size": top_k,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question"],
                        "type": "best_fields"
                    }
                }
            }
        }
    }

    es_client = Elasticsearch(connection_string)
    
    response = es_client.search(index=index_name, body=search_query)

    try:
        response = es_client.search(index=index_name, body=search_query)

        for hit in response['hits']['hits']:
            print(f"score: {hit['_score']}")
            print(f"document_id: {hit['_source']['document_id']}")
            print(f"question: {hit['_source']['question']}")
            print(f"text: {hit['_source']['text']}")
            print("---")

        return [hit for hit in response['hits']['hits']]

    except exceptions.BadRequestError as e:
        print(f"BadRequestError: {e.info}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []