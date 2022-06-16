# Local testing

```shell
docker build -t gcr.io/holy-diver-297719/cloud-run-demo . && \
docker push gcr.io/holy-diver-297719/cloud-run-demo && \
docker run --rm -p 8082:8080 gcr.io/holy-diver-297719/cloud-run-demo
```
