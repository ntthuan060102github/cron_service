import requests
from celery import shared_task

@shared_task
def abstract_request_api_task(**kwargs):
    try:
        print("CALLING API...")
        return "CALLING API..."
        # response = requests.request(
        #     verify=False,
        #     **kwargs
        # )
        # return response.json()

    except Exception as e:
        print(e)
        raise e
