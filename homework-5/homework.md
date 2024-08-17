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

5. Go to "<> Edit" and copy & paste code from [homework-5/ingest-llm-faq-version-1.py](homework-5/ingest-llm-faq-version-1.py)

6. Run block.

7. Click "Load output results" to see them.

### Q3. Chunking

1. Go to: Data preparation / Transform / Chunking

2. Add block as "Custom code".

3. Go to "<> Edit" and copy & paste code from [homework-5/chunking-llm-faq.py](homework-5/chunking-llm-faq.py)

4. Run block.

5. Check the output.

### Tokenization and embeddings

1. Go to: Data preparation / Transform / Tokenization

2. Add block as "Custom code" and leave it like that.

3. Go to: Data preparation / Transform / Embed

4. Add block as "Custom code" and leave it like that.

### Q4. Export

1. Go to: Data preparation / Export / Vector database

2. Add block as "Elasticsearch".

3. Edit code

4. Go to "<> Edit" and copy & paste code from [homework-5/vector-database-llm-faq.py](homework-5/vector-database-llm-faq.py).

5. Replace `YOUR_PIPELINE_NAME` with your pipeline name e.g. `transcendent_nexus` (replace the space with underscore `_`)

6. Run block.

7. Check the output.