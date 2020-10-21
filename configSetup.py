import requests
import json

from base64 import b64encode
from nacl import encoding, public


def greeting():
    """
    Greets the user.
    """

    welcome_message = f"Hello! Thanks for using your CI/CD pipeline action.\n"
    instruction = f"Please provide information to the prompt for setup."

    print("-" * 60)
    print(welcome_message + instruction)
    print("-" * 60)


def prompt_creds():
    """
    Prompts the user to enter required credentials.
    """
    global GH_REPO_OWNER
    global GH_REPO_NAME
    global GH_ACCESS_TOKEN
    global OC_SERVER_URL
    global OC_API_TOKEN

    GH_REPO_OWNER = input("Enter GitHub repo owner: ")
    GH_REPO_NAME = input("Enter GitHub repo name: ")
    GH_ACCESS_TOKEN = input(
        "Please provide your GitHub Personal Access Token (with repo scope): "
    )
    OC_SERVER_URL = input("Please provide your OpenShift Server URL: ")
    OC_API_TOKEN = input("Please provide your OpenShift API Token: ")


def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))

    return b64encode(encrypted).decode("utf-8")


def main():
    greeting()
    prompt_creds()


main()
