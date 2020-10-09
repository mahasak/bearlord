# BearLord Discord Bot

## How to build discord docker bot
```
$ docker build  --build-arg DISCORD_ARG=<discord-token> --build-arg AIRTABLE_KEY_ARG=<airtable-key> --build-arg AIRTABLE_BASE_ARG=<airtable-base> -t <image-name> .   
```

## How to run discord bot docker
```
$  docker run --tty=true --interactive=true --detach=true <image-name>:latest  
```