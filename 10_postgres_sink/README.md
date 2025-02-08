# Postgres sink 

<a href="https://youtu.be/4uJSbC9AVxk" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_platform/postgres_sink.png?raw=true" alt="DESCRIPTION" width="600">
</a>

In this lecture we'll build a pipeline that ends up persisting data into postgresql. In more detail we'll ingest data from an API, publish events from producer into a Kafka topic, then read these events in a consumer and sink into a postgres database. We start building our multiapp container with the following containers: 

- postgres
- broker
- schema-registry
- control-center


> [!IMPORTANT]
> add kafka_data and state to your .gitignore as we bind mount this folder into kafka broker, in order to persist data in the topics.



TODO: pipeline picture