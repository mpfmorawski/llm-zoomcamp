Before all, prepare your environment (check [README.md](../README.md)) and run Elastic Search in Docker container:

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

### Q1. Getting the embeddings model

Check [homework.ipynb](./homework.ipynb)

### Q2. Creating the embeddings

Check [homework.ipynb](./homework.ipynb)

### Q3. Search

Check [homework.ipynb](./homework.ipynb)

### Q4. Hit-rate for our search engine

Check [homework.ipynb](./homework.ipynb)

### Q5. Indexing with Elasticsearch

Check [homework.ipynb](./homework.ipynb)

### Q6. Hit-rate for Elasticsearch

Check [homework.ipynb](./homework.ipynb)