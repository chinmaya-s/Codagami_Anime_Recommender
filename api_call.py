import requests 

client_id = "0ea0724791b07d5c5f375a9bbb17b716"
client_secret = "30775230130dead3ed11d9298f5fd1dbb3d2759d7e4cc57663a60077e11d17dc"

# BASE_URL = 'https://myanimelist.net/v1/oauth2/token'
auth_url = 'https://myanimelist.net/v1/oauth2/token'

grant_type = "authorization_code"

code = ''
code_verifier = ''

data = {
    "grant_type": grant_type,
    "client_id": client_id,
    "client_secret": client_secret,
    "code": code,
    "code_verifier": code_verifier,
}
auth_response = requests.post(auth_url, data=data)

# Read token from auth response
auth_response_json = auth_response.json()
auth_token = auth_response_json["access_token"]

auth_token_header_value = "Bearer %s" % auth_token

auth_token_header = {"Authorization": auth_token_header_value}

print(auth_token)
