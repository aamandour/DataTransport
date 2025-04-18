from google.cloud import pubsub_v1
import json
import time

# Your project ID and topic
project_id = "verdant-upgrade-456819-i2"
topic_id = "my-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Load JSON data
# with open("bcsample.json", "r") as f:
#    records = json.load(f)

# Load JSON data from the Glitch group (200 vehicles)
with open("bcsample_glitch_200.json", "r") as f:
    records = json.load(f)



# Publish each record
# for record in records:
#    data = json.dumps(record).encode("utf-8")
#    future = publisher.publish(topic_path, data)
#    print(f"Published message ID: {future.result()}")
#    time.sleep(0.05)  # small delay to avoid overloading

count = 0
for record in records:
    data = json.dumps(record).encode("utf-8")
    future = publisher.publish(topic_path, data)
    count += 1

print(f"\n✅ Published total: {count} messages")
