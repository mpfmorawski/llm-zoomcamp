### Q1. Running Mage

Before all, prepare your environment by running Mage.

If you use GitHub Codespaces, please remember to run 4-core machine type.
To do that go to "New with options..." and change "Machine type" to "4-core - 16GB RAM - 32GB".

1. Clone the same repo we used in the module and run mage:

    ```
    git clone https://github.com/mage-ai/rag-project
    ```

2. Add the following libraries to the requirements document (rag-project/llm/requirements.txt):

    ```
    python-docx
    elasticsearch
    ```

3. Make sure you use the latest version of mage:

    ```
    docker pull mageai/mageai:llm
    ```

4. Start it:

    ```
    cd rag-project/
    ./scripts/start.sh
    ```

5. Now mage is running on http://localhost:6789/. Open it in a web browser.


6. You can check mage version in the top right corner (next to current time).

    ```
    v0.9.72
    ```

### Q2. Reading the documents

1. Stay in web browser (http://localhost:6789/).

2. Create a new pipeline (Retrieval Augmented Generation).

3. Go to: Data preparation / Load / Ingest.

4. Add block as "Custom code".

5. Go to "<> Edit" and copy & paste code from [homework-5/ingest-llm-faq.py](ingest-llm-faq.py)

6. Run block.

7. Check the output

    ```
    llm-faq-version-1
    ```

8. Click "Load output results" to see more details.

### Q3. Chunking

1. Go to: Data preparation / Transform / Chunking

2. Add block as "Custom code".

3. Go to "<> Edit" and copy & paste code from [homework-5/chunking-llm-faq.py](chunking-llm-faq.py)

4. Run block.

5. Check the output.

    ```
    86
    ```

### Tokenization and embeddings

1. Go to: Data preparation / Transform / Tokenization

2. Add block as "Custom code" and leave it like that.

3. Go to: Data preparation / Transform / Embed

4. Add block as "Custom code" and leave it like that.

### Q4. Export

1. Go to: Data preparation / Export / Vector database

2. Add block as "Elasticsearch".

3. Set value of "Connection string" to

    ```
    http://elasticsearch:9200
    ```

4. Go to "<> Edit" and copy & paste code from [homework-5/vector-database-llm-faq.py](vector-database-llm-faq.py).

5. Replace `YOUR_PIPELINE_NAME` with your pipeline name e.g. `transcendent_nexus` (replace the space with underscore `_`)

6. Run block.

7. Check the output.

    ```
    index name: documents_20240818_2425
    [...]
    Indexing 86 documents to Elasticsearch index documents_20240818_2425
    [...]
    Indexing document 2b15bf75
    Indexing document b65737cb
    Indexing document 2b15bf75

    {'text': 'Prior to using Ollama models in llm-zoomcamp tasks, you need to have ollama installed on your pc and the relevant LLM model downloaded with ollama from https://www.ollama.com\nTo download ollama for Ubuntu:\n``` curl -fsSL https://ollama.com/install.sh | sh ```\nTo download ollama for Mac and Windows, follow the guide on this link:\nhttps://ollama.com/download/\nOllama a number of open-source LLMs like:\nLlama3\nPhi3\nMistral and Mixtral\nGemma\nQwen\nYou can explore more models on https://ollama.com/library/\nTo download a model in Ollama, simply open command prompt and type:\n``` ollama run model_name ```\ne.g.\n``` ollama run phi3 ```\nIt will automatically download the model and you can use it same way as above for later time.\nTo use Ollama models for inference and llm-zoomcamp tasks, use the following function:\nimport ollama\ndef llm(prompt):\nresponse = ollama.chat(\nmodel="llama3",\nmessages=[{"role": "user", "content": prompt}]\n)\nreturn response[\'message\'][\'content\']\nFor example, we can use it in the following way:\nprompt = "When does the llm-zoomcamp course start?"\nanswer = llm(prompt)\nprint(answer)', 'section': 'Module 1: Introduction', 'question': 'OpenSource: How can I use Ollama open-source models locally on my pc without using any API?', 'course': 'llm-faq-version-1', 'document_id': '2b15bf75'}
    ```

### Q5. Testing the retrieval

1. Go to: Inference / Retrieval / Iterative retrieval

2. Add block as "Elasticsearch".

3. Set value of "Connection string" to

    ```
    http://elasticsearch:9200
    ```

4. Set value of "Index name" basing on the output from the previous task. For example:

    ```
    documents_20240818_2425
    ```





