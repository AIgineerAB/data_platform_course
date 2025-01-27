# Kafka producer and consumer

**part 1 - theory about producer and consumer**

<a href="https://youtu.be/u5hU0KTvNnc" target="_blank">
<img src="https://github.com/kokchun/assets/blob/main/data_platform/producer_consumer_theory.png?raw=true" alt="kafka producer consumer" width="600">
</a>

**part 2 - coding producer and consumer**

<a href="https://youtu.be/cPO_NjMBecc" target="_blank">
<img src="https://github.com/kokchun/assets/blob/main/data_platform/producer_consumer.png?raw=true" alt="kafka producer consumer" width="600">
</a>


## Consume data from topic in broker 

To consume the data in the broker, start with opening up the container interactively with 

```bash
docker exec -it broker /bin/bash
```

Then run 

```bash
kafka-console-consumer --bootstrap-server localhost:9092 --topic <topic_name> --from-beginning 
```

To read messages with keys and timestamp

```bash
kafka-console-consumer --bootstrap-server localhost:9092 --topic jokes --from-beginning --property print.key=true --property print.timestamp=true
```

You can also go into the control center `localhost:9021` to check the topics and its events can be consumed from there.



## Other videos 📹

## Read more 👓

- [kafka fundamentals - conduktor kafkacademy](https://learn.conduktor.io/kafka/kafka-fundamentals/)
- [kafka topics - conduktor kafkacademy](https://learn.conduktor.io/kafka/kafka-topics/)
- [kafka producers - conduktor kafkacademy](https://learn.conduktor.io/kafka/kafka-producers/)
- [kafka consumers - conduktor kafkacademy](https://learn.conduktor.io/kafka/kafka-consumers/)
- [Sources - quix docs](https://quix.io/docs/quix-streams/connectors/sources/index.html#standalone-sources)