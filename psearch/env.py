from json import load

def get_token():
    with open("./openai-auth.json") as auth_file:
        return load(auth_file)["token"]

token = get_token()

