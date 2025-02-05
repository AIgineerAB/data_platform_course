# Postgres sink 

TODO: VIDEO

<a href="" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/FOLDER_NAME/.png?raw=true" alt="DESCRIPTION" width="600">
</a>

In this lecture we'll build a pipeline that ends up persisting data into postgresql. In more detail we'll ingest data from an API, publish events from producer into a Kafka topic, then read these events in a consumer and sink into a postgres database. We start building our multiapp container with the following containers: 

- postgres
- broker
- schema-registry
- control-center

TODO: pipeline picture