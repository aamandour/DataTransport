from google.cloud import pubsub_v1

project_id = "verdant-upgrade-456819-i2"
topic_id = "my-topic"
subscription_id = "my-sub"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

print(f"🔁 Flushing messages in {subscription_path}... (wait 10s)")
import time
time.sleep(10)

streaming_pull_future.cancel()
