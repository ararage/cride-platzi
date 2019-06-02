# Comparte Ride

Group-bounded, invite-only, carpooling platform

## Optional Requeriments

https://httpie.org/

## Docker Compose commands

Export the local.yml file and save the referenche with a constant, basic commands
for listing images, up docker-compose, build and down

```
$ export COMPOSE_FILE=local.yml
$ docker-compose -f local.yml ps
$ docker-compose -f local.yml up
$ docker-compose -f local.yml build
$ docker-compose -f local.yml down
```

If the local COMPOSE_FILE constant exists in the terminal session you can run like this way:

```
$ docker-compose up
$ docker-compose down
$ docker-compose ps
```

Show volumes:

```
$ docker volume ls
```

If you want to run some manage Django commands you should run in another docker-compose session your command:

```
$ docker-compose run --rm django python manage.py createsuperuser
$ docker-compose run --rm django python manage.py makemigrations
$ docker-compose run --rm django python manage.py migrate
```

If you want to delete a Volume you have to down your compose configuration with docker-compose down, after that this should works:

```
$ docker volume rm <volumen>
```

Or maybe delete an image :

```
$ docker rm -f <image_name>
```

Django Extensions - Shell Plus usage

```
$ docker-compose run --rm django python manage.py shell_plus
```

Individual images

```
$ docker-compose run --rm --service-ports django
```

## REST Services

POST Signup User

```
$ http POST localhost:8000/users/signup/ email="email@gmail.com" first_name="Jon" last_name="Rodriguez" password="secret" password_confirmation="secret" phone_number="+5577889900" username="newuser"  -b
```

POST Login User

```
$ http POST localhost:8000/users/login/ email="email@gmail.com" password="secret" -b
```

POST Verify Token

```
$ http localhost:8000/users/verify/ token="token.token.token"
```

GET Circles

```
$ http GET localhost:8000/circles/
```

POST Circles

```
http POST localhost:8000/circles/create/ name=Manzana slug_name=manzana
```

# Preload with shell plus

```
circles = [
    ["Facultad de Ciencias, UNAM","unam-fciencias",1,1,0],
    ["Tec de Monterrey, Campos Santa Fé","itesm-csf",1,1,0],
    ["Inventive","inventive",0,1,30],
    ["Platzi Bogotá","platzi-bog",0,1,120],
    ["Platzi México","platzi-mex",0,1,30],
    ["Google México","google-mx",0,1,250],
    ["Curso de Fotografía, UVA","curso-foto-uva",1,0,25],
    ["Equipo de futbol, chapinero","fut-chapinero",1,0,40],
    ["Grupo 3340, Prácticas de campo","grupo-3340-campo",1,0,50],
    ["Generación 2018 Escuela de enfermería","enfermeria-2018",1,0,0],
    ["Facultad de Ingeniería, UNAM","unam-fi",1,1,0],
    ["Facultad de Medicina, UNAM","unam-fm",1,1,0],
    ["Platzi Developer Circle - Bogotá","platzi-dev",1,0,0],
    ["Platzi Developer Circle - CDMX","platzi-dev-mx",1,0,0],
    ["IBM Santa Fé","ibm-santafe",0,1,0],
    ["P&G - Santa Fé","p-n-g",1,0,1000],
    ["Amigos de Centraal","comunidad-centraal",1,0,0],
    ["Central Academy","centraal-academy",1,1,0],
    ["Estado de México - CDMX","edomex",1,0,0],
    ["Satelite - Santa Fé entre semana","sat-sfe-week",1,0,0],
    ["Sable Digital","sable",0,0,30],
]
for cirlce in circles:
    name = cirlce[0]
    slug_name = cirlce[1]
    is_public = cirlce[2]
    verified = cirlce[3]
    members_limit = cirlce[4]
    print(f'Processed { name } { slug_name } { is_public } { verified } { members_limit }')
    Circle.objects.create(
        name=name,
        slug_name=slug_name,
        is_public=is_public,
        verified=verified,
        members_limit=members_limit,
    )
```

# Common issue for macos users

Sometimes the docker client for macos fails and this might be caused by an issue in Docker Desktop which is storing if it is using the keychain in ~/.docker/config.json with the incorrect key: "credSstore" : "osxkeychain" instead of credsStore.
