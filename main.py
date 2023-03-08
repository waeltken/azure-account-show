import sys, signal, time

from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient


def main():
    while True:
        show_subscription()
        time.sleep(10)


def show_subscription():
    credential = DefaultAzureCredential()
    subscription_client = SubscriptionClient(credential)
    sub_list = subscription_client.subscriptions.list()
    first_sub = next(sub_list)
    print(first_sub.subscription_id)


def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    main()
