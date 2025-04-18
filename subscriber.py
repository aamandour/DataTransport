from google.cloud import pubsub_v1
import json
import time

project_id = "verdant-upgrade-456819-i2"
subscription_id = "my-sub"  # change this if your subscription has a different name

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

count = 0  # Track number of messages received

def callback(message):
    global count
    count += 1
    message.ack()
    
    # Only print every 10,000 messages
    if count % 10000 == 0:
        print(f"✅ Received {count} messages so far...")

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"⏳ Listening on {subscription_path}... (Press Ctrl+C to stop)")

try:
    time.sleep(60)  # Listen for 60 seconds
    streaming_pull_future.cancel()
except KeyboardInterrupt:
    streaming_pull_future.cancel()

print(f"\n✅ Total messages received: {count}")

