

docker build . -t challenge-neuralworks-endpoint
docker run --name challenge-neuralworks-endpoint -p 8080:8080 --net=bridge -d challenge-neuralworks-endpoint