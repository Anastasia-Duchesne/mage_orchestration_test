from mage_ai.services.dbt.dbt import DbtCloudClient
from mage_ai.data_preparation.decorators import custom

@custom
def transform_custom(*args, **kwargs):
    client = DbtCloudClient(dict(account_id=<account_id>, api_token=<api_token>))

    # Set poll_status=True to wait for job completion.
    # Set poll_status=False to not wait for job completion.
    client.trigger_job_run(<job_id>, poll_status=True)
