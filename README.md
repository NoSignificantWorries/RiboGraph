
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
docker run -d \
           --rm \
           --name rna-tools \
           --user "$(id -u):$(id -g)" \
           --mount type=bind,source="$(pwd)/data/input",target=/tools/input \
           --mount type=bind,source="$(pwd)/data/output",target=/tools/output \
           rna-tools:latest \
           tail -f /dev/null

```

```bash
docker exec -it rna-tools <command>
```

