import requests
import json

from base64 import b64encode
from nacl import encoding, public
from getpass import getpass

GH_REPO_OWNER = ""
GH_REPO_NAME = ""
GH_ACCESS_TOKEN = ""
GH_PUBLIC_KEY_ID = ""
GH_PUBLIC_KEY = ""
OC_SERVER_URL = ""
OC_API_TOKEN = ""
ENCRYPTED_OC_SERVER_URL = ""
ENCRYPTED_OC_API_TOKEN = ""


def greeting():
    """
        Greets the user.
    """

    welcome_message = f"Hello! Thanks for using your CI/CD pipeline action.\n"
    instruction = f"Please provide information to the prompt for setup."

    print("-" * 60)
    print(welcome_message + instruction)
    print("-" * 60)
    print() # UNCOMMENT HERE


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
    GH_ACCESS_TOKEN = getpass(
        prompt="Please provide your GitHub Personal Access Token (with repo scope): ")
    OC_SERVER_URL = getpass(prompt="Please provide your OpenShift Server URL: ")
    OC_API_TOKEN = getpass(prompt="Please provide your OpenShift API Token: ")


def encrypt(public_key, secret_value):
    """
        Encrypt a Unicode string using the public key.
    """

    public_key = public.PublicKey(public_key.encode("utf-8"),
                                  encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))

    return b64encode(encrypted).decode("utf-8")


def configure_secrets():
    global GH_PUBLIC_KEY
    global GH_PUBLIC_KEY_ID

    headers = {"Authorization": "token " + GH_ACCESS_TOKEN}
    URL = f"https://api.github.com/repos/{GH_REPO_OWNER}/{GH_REPO_NAME}/actions/secrets/public-key"

    response = requests.get(URL, headers=headers)
    public_key = json.loads(response.text)
    GH_PUBLIC_KEY_ID = public_key["key_id"]
    GH_PUBLIC_KEY = public_key["key"]


def generate_encrypted_secrets():
    """
        Generate the encrypted secrets
    """
    global ENCRYPTED_OC_SERVER_URL
    global ENCRYPTED_OC_API_TOKEN

    secrets = {}
    ENCRYPTED_OC_SERVER_URL = encrypt(GH_PUBLIC_KEY, OC_SERVER_URL)
    ENCRYPTED_OC_API_TOKEN = encrypt(GH_PUBLIC_KEY, OC_API_TOKEN)
    secrets["OC_SERVER_URL"] = ENCRYPTED_OC_SERVER_URL
    secrets["OC_API_TOKEN"] = ENCRYPTED_OC_API_TOKEN

    return secrets


def create_update_secrets(secrets):
    """
    Create/Update secrets to current GitHub repo

    Args:
        secrets (dict): [dict contains all secret configuratoins]
    """

    for key, value in secrets.items():
        headers = {
            "Authorization": "token " + GH_ACCESS_TOKEN,
            "Content-Type": "application/json"
        }
        URL = f"https://api.github.com/repos/{GH_REPO_OWNER}/{GH_REPO_NAME}/actions/secrets/{key}"
        secret = {
            "key_id": GH_PUBLIC_KEY_ID,
            "encrypted_value": value,
        }

        response = requests.put(URL, data=json.dumps(secret), headers=headers)
        if response.status_code == 201 or response.status_code == 204:
            print()
            print("=" * 10, "Created/Updated secret.", "=" * 10)


def show_secrets():
    """
        Show secrets in current repo
    """
    headers = {"Authorization": "token " + GH_ACCESS_TOKEN}
    URL = f"https://api.github.com/repos/{GH_REPO_OWNER}/{GH_REPO_NAME}/actions/secrets"
    response = requests.get(URL, headers=headers)
    secrets = json.loads(response.text)
    print()
    print("-" * 5, "The current repo consists of following secrets: ", "-" * 5)
    print(secrets)


def main():
    greeting()
    prompt_creds()
    configure_secrets()
    secrets = generate_encrypted_secrets()
    create_update_secrets(secrets)
    show_secrets()


main()
