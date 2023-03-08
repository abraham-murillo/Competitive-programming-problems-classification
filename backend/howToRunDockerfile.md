# Localmente
## Ver qué hay
docker ps -a

## Borrar todo
docker system prune --all --force --volumes

<!-- ## Construir el docker
docker build -t backend:fool . -->

## Al parecer M1 la cajetea, prueba con esto
docker buildx build --platform linux/amd64 -t backend:abraham .

## Re-etiqueta y vuelve a subir
docker tag backend:abraham abrahammurillo7443/backend:abraham
docker push abrahammurillo7443/backend:abraham


## Correr el docker localmente
docker run -d -p 5000:5000 backend:abraham

docker run -d backend:abraham

# Google cloud (https://www.youtube.com/watch?v=_Zul8u5YypA)
## Cargar la imagen desde docker hub
docker pull abrahammurillo7443/backend:abraham

## Re-etiqueta y vuelve a subir
docker tag abrahammurillo7443/backend:abraham gcr.io/cp-problem-classification/backend:abraham

docker push gcr.io/cp-problem-classification/backend:abraham


