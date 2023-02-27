# Localmente
## Ver qué hay
docker ps -a

## Borrar todo
docker system prune --all --force --volumes

<!-- ## Construir el docker
docker build -t backend:fool . -->

## Al parecer M1 la cajetea, prueba con esto
docker buildx build --platform linux/amd64 -t backend:rob .

## Re-etiqueta y vuelve a subir
docker tag backend:rob abrahammurillo7443/backend:rob
docker push abrahammurillo7443/backend:rob


## Correr el docker localmente
docker run -d -p 5000:5000 backend:rob

docker run -d backend:fool

# Google cloud (https://www.youtube.com/watch?v=_Zul8u5YypA)
## Cargar la imagen desde docker hub
docker pull abrahammurillo7443/backend:rob

## Re-etiqueta y vuelve a subir
docker tag abrahammurillo7443/backend:rob gcr.io/cp-problem-classification/backend:rob

docker push gcr.io/cp-problem-classification/backend:rob


