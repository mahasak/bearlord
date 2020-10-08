# BearLord Discord Bot

## How to build discord docker bot
```
$ docker build  --build-arg DISCORD_ARG=<discord-token> -t <image-name> .   
```

## How to run discord bot docker
```
$  docker run --tty=true --interactive=true --detach=true <image-name>:latest  
```