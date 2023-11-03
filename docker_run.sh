# Build the docker file 
docker build -t digits:v1 -f ./Dockerfile .
# Mount our volume to models directory (where train data is stored)
docker run -v ./models:/digits/models digits:v1