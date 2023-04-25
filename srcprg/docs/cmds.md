# criar images

docker build -t lucht .

# verificar a imagem criada latest
╰─$ docker images | grep lucht     
lucht                 latest             bf16d388cd95   3 minutes ago   383MB



docker run --rm -it -p 8000:8000 -e SECRET_KEY=secret -e ALLOWED_HOSTS=localhost, lucht python manage.py migrate 


## comando padrão 
docker run --rm -it -p 8000:8000 --env-file=.env -d lucht --name lucht 

docker run --rm -it -p 8000:8000 --env-file=.env -d --name lucht lucht python manage.py migrate