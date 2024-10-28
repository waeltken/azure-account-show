import sys, signal, time
from pprint import pprint

from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient
from azure.core.exceptions import ClientAuthenticationError


def main():
    while True:
        show_subscription()
        time.sleep(10)


def show_subscription():
    try:
        credential = DefaultAzureCredential()
        subscription_client = SubscriptionClient(credential)
        subscription_list = subscription_client.subscriptions.list()
        subscription_list = [vars(subscription) for subscription in subscription_list]
        subscription_count = len(subscription_list)
        if subscription_count > 0:
            print(f"Found {subscription_count} subscriptions:")
            pprint(subscription_list)
        if subscription_count == 0:
            print("This account does not have access to any subscriptions.")
    except ClientAuthenticationError as e:
        print(e.exc_msg)


def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    main()
