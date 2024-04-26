import os
import json
import requests
import google.oauth2.id_token
import google.auth.transport.requests


data_to_publish = {
    "data": {
        "message": {
            "data": "Executing cloud function from Mage"
        }
    },
    "type": "google.cloud.pubsub.topic.v1.messagePublished",
    "specversion": "1.0",
    "source": "//pubsub.googleapis.com/",
    "id": "mage"
}

@custom
def call_google_function(**kwargs):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/root/.ssh/google_credentials.json'
    request = google.auth.transport.requests.Request()
    api_post_url = kwargs['orchestration_testing_post_url']
    TOKEN = google.oauth2.id_token.fetch_id_token(request, api_post_url)

    r = requests.post(
        api_post_url, 
        headers={'Authorization': f"Bearer {TOKEN}", "Content-Type": "application/json"},
        data=json.dumps(data_to_publish)
    )

    print(r.status_code)
    print(r.reason)