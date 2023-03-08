from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient


def main():
    credential = DefaultAzureCredential()
    subscription_client = SubscriptionClient(credential)
    sub_list = subscription_client.subscriptions.list()
    first_sub = next(sub_list)
    print(first_sub.subscription_id)


if __name__ == "__main__":
    main()
