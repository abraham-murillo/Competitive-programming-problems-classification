# Localmente
## Ver qué hay
docker ps -a

## Borrar todo
docker system prune --all --force --volumes

<!-- ## Construir el docker
docker build -t backend:fool . -->

## Al parecer M1 la cajetea, prueba con esto
docker buildx build --platform linux/amd64 -t backend:abraham2 .

## Re-etiqueta y vuelve a subir
docker tag backend:abraham2 abrahammurillo7443/backend:abraham2
docker push abrahammurillo7443/backend:abraham2


## Correr el docker localmente
docker run -d -p 5000:5000 backend:abraham2

docker run -d backend:abraham2

# Google cloud (https://www.youtube.com/watch?v=_Zul8u5YypA)
## Cargar la imagen desde docker hub
docker pull abrahammurillo7443/backend:abraham2

## Re-etiqueta y vuelve a subir
docker tag abrahammurillo7443/backend:abraham2 gcr.io/cp-problem-classification/backend:abraham2

docker push gcr.io/cp-problem-classification/backend:abraham2


