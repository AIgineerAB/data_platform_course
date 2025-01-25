from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="text-splitter-v1",
    auto_offset_reset="earliest",
)

# as we have serialized json before, we will now deserialize it
jokes_topic = app.topic(name="jokes", value_deserializer="json")

# streaming dataframe
sdf = app.dataframe(topic=jokes_topic)

# update method to perform a side effect, in this case printing
sdf = sdf.update(lambda message: print(f"Input: {message}"))

# transformation: split incoming sentence into words
# expanding the list into several rows in the sdf
sdf = sdf.apply(
    lambda message: [{"word": word} for word in message["joke_text"].split()],
    expand=True,
)

# create new column with word lengths
sdf["length"] = sdf["word"].apply(lambda word: len(word))
sdf = sdf.update(lambda row: print(f"Output: {row}"))


if __name__ == "__main__":
    app.run()
