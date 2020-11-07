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
    print()  # UNCOMMENT HERE


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
        prompt="Please provide your GitHub Personal Access Token (with repo scope): "
    )
    OC_SERVER_URL = getpass(prompt="Please provide your OpenShift Server URL: ")
    OC_API_TOKEN = getpass(prompt="Please provide your OpenShift API Token: ")


def encrypt(public_key, secret_value):
    """
    Encrypt a Unicode string using the public key.
    """

    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
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
            "Content-Type": "application/json",
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
    headers = {"Authorization": "token " + GH_ACCESS_TOKEN,
    }
    URL = f"https://api.github.com/repos/{GH_REPO_OWNER}/{GH_REPO_NAME}/actions/secrets"
    response = requests.get(URL, headers=headers)
    secrets = json.loads(response.text)
    print()
    print("-" * 5, "The current repo consists of following secrets: ", "-" * 5)
    print(json.dumps(secrets, indent=4, sort_keys=True))

def show_GHA_logs():
    GH_ACCESS_TOKEN = 'f12bdc5a3a704df0b37176185c42724a1a40900a'
    GH_REPO_OWNER = 'BU-CLOUD-F20'
    GH_REPO_NAME = 'Building_CI_CD_for_API'
    """
        Show Github action logs
    """


    headers = {"Authorization": "token " + GH_ACCESS_TOKEN}
    params = {    'owner': 'BU-CLOUD-F20',
    'repo': 'Building_CI_CD_for_API',
    'run_id': 1324371347  }
# check suite id 
    check_suites_URL = f"https://api.github.com/repos/{GH_REPO_OWNER}/{GH_REPO_NAME}/commits/master/check-suites"
    response = requests.get(check_suites_URL)
    secrets = json.loads(response.text)
    print(check_suites_URL)
    print("-" * 5, "The 'check_suites' id is : ", "-" * 5)
    check_suites_ID = secrets['check_suites'][0]['id']
    print(check_suites_ID)

# check_runs id
    check_runs_URL = f"https://api.github.com/repos/{GH_REPO_OWNER}/{GH_REPO_NAME}/check-suites/{check_suites_ID}/check-runs"
    response = requests.get(check_runs_URL)
    secrets = json.loads(response.text)
    print(check_runs_URL)
    print("-" * 5, "The 'check_runs' id is : ", "-" * 5)
    check_runs_id = secrets['check_runs'][0]['id']
    print(check_runs_id)

# list of jobs of workflow runs
    check_jobs_URL = f"https://api.github.com/repos/{GH_REPO_OWNER}/{GH_REPO_NAME}/actions/runs/{check_runs_id}/jobs"
    response = requests.get(check_jobs_URL, headers=headers, params=params)
    secrets = json.loads(response.text)
    print(check_jobs_URL)
    print("-" * 5, "The List of jobs are : ", "-" * 5)
    print(json.dumps(secrets, indent=4, sort_keys=True))
    # check_runs_id = secrets['check_runs'][0]['id']
    # print(check_runs_id)

    # URL = f"https://api.github.com/repos/{GH_REPO_OWNER}/{GH_REPO_NAME}/actions/secrets"
    # response = requests.get(URL, headers=headers)
    # secrets = json.loads(response.text)
    # print()
    # print("-" * 5, "The current repo consists of following secrets: ", "-" * 5)
    # print(secrets)

def main():
    greeting()
    prompt_creds()
    configure_secrets()
    secrets = generate_encrypted_secrets()
    create_update_secrets(secrets)
    show_secrets()
    # show_GHA_logs()


main()
