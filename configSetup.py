from base64 import b64encode
from nacl import encoding, public

def greeting():
    welcome_message = f"Hello! Thanks for using your CI/CD pipeline action.\n"
    instruction = f"Please provide information to the prompt for setup."
    print("-" * 60)
    print(welcome_message + instruction)
    print("-" * 60)
    
def prompt_creds():
    GH_ACCESS_TOKEN = input("Please provide your GitHub Access Token: ")
    OC_SERVER_URL = input("Please provide your OpenShift server URL: ")
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
    
    