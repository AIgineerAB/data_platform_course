# Kafka setup

<!-- <a href="https://youtu.be/3R9w1hbh1PY" target="_blank">
<img src="https://github.com/kokchun/assets/blob/main/data_platform/docker_compose.png?raw=true" alt="docker compose code" width="600">
</a> -->

## Docker compose

We will setup kafka with docker compose. So start with pasting in the code from `docker-compose.yml` in this repo into your own docker-compose.yml. Then then build the image and spin up the container in detached mode.

```
docker compose up -d
```

The docker-compose.yml file comes from [quix documentation for running kafka locally](https://quix.io/docs/quix-streams/tutorials/index.html#running-kafka-locally).

Remove the parts with rest-proxy and remove version from the docker-compose.yml file, as we won't need them when working with quixstreams. 


## Check services 

Go into the container broker interactively with 

```bash
docker exec -it broker /bin/bash
```

Inside the container lets run kafka commands to check out existing topics 

```bash
kafka-topics --list --bootstrap-server localhost:9092
```

You'll see many internal topics, but also the topics that you will create later on. It's important to understand some kafka commands inside of the broker container so that you can inspect what's happening when developing your application. Also it's good for debugging purposes later on. 


You can also describe topics with 

```bash
kafka-topics --describe --topic <topic_name> --bootstrap-server localhost:9092
```

To see existing consumer groups:

```bash
kafka-consumer-groups --list --bootstrap-server localhost:9092
```

## Other videos 📹



## Read more 👓

