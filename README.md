# Comparte Ride

Group-bounded, invite-only, carpooling platform

#Docker Compose commands

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
```

Show volumes:

```
$ docker volume ls
```

If you want to run some manage Django commands you should run in another docker-compose session your command:

```
$ docker-compose run --rm django python manage.py createsuperuser
$ docker-compose run --rm django python manage.py  makemigrations
$ docker-compose run --rm django python manage.py  migrate
```

If you want to delete a Volume you have to down your compose configuration with docker-compose down, after that this should works:

```
$ docker volume rm <volumen>
```

Django Extensions - Shell Plus usage

```
$ docker-compose run --rm django python manage.py shell_plus
```

## Common issue for macos users

Sometimes the docker client for macos fails and this might be caused by an issue in Docker Desktop which is storing if it is using the keychain in ~/.docker/config.json with the incorrect key: "credSstore" : "osxkeychain" instead of credsStore.
