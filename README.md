
## Tools container usage

### Building container

```bash
# legacy
docker build -f ./Dockerfile.tools -t rna-tools:latest .
# buildx
docker buildx build --load -f ./Dockerfile.tools -t rna-tools:latest .
```

### Run bash in container

```bash
docker run --rm -it --name rna-tools rna-tools:latest /bin/bash
```

### Run container in background

```bash
docker run -d --name rna-tools -v $(pwd)/data/input:/tools/input -v $(pwd)/data/output:/tools/output rna-tools:latest tail -f /dev/null
```

```bash
docker exec -it rna-tools <command>
```

