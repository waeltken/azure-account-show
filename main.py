import sys, signal, time, json

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
        sub_list = subscription_client.subscriptions.list()
        first_sub = next(sub_list, "No subscriptions for this account")
        print("halloooo?")
        print(first_sub)
    except ClientAuthenticationError as e:
        print(e.exc_msg)


def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    main()
