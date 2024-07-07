### Q1. Running Ollama with Docker

Run ollama with Docker:

```bash
docker run -it \
    --rm \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```

In another terminal enter the container:

```bash
docker exec -it ollama bash
```

To check the ollama version, execute in the container:

```bash
ollama -v
```

### Q2. Downloading an LLM

Enter the container again:

```bash
docker exec -it ollama bash
```

Pull the model:

```bash
ollama pull gemma:2b
```

Go to directory with Gemma metadata (manifest file):

```bash
cd /root/.ollama/models/manifests.ollama.ai/library/
```

Show metadata:
```bash
cat gemma/2b
```

### Q3. Running the LLM

Check [homework.ipynb](./homework.ipynb)

### Q4. Donwloading the weights

Run docker container mapped to a local directory:

```bash
cd homework-2
mkdir ollama_files

docker run -it \
    --rm \
    -v ./ollama_files:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```

Pull the model in another terminal:

```bash
docker exec -it ollama ollama pull gemma:2b 
```

Check the size of `ollama_files/models` directory:

```bash
du -h homework-2/ollama_files/models
```

### Q5. Adding the weights

Solution: [Dockerfile](./Dockerfile)

If you want to run this container, you can (after checking that you are in `homework-2` directory)...

Build the image:

```bash
docker build .
```

Find image id:

```bash
docker images
```

Run docker container (remember to replace <IMAGE_ID> with proper value):

```bash
docker run -it \
    --rm \
    -v ./ollama_files:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    <IMAGE_ID>
```

OR

Build the image with tag:

```bash
docker build -t ollama-gemma2b .
```

And run it with tag:

```bash
docker run -it --rm -p 11434:11434 ollama-gemma2b
```

### Q6. Serving it

Check [homework.ipynb](./homework.ipynb)