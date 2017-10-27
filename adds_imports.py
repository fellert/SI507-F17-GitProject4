from sampel_oauth1_code.py import *

client_key = "" # what Twitter calls Consumer Key
client_secret = "" # What Twitter calls Consumer Secret

if not client_secret or not client_key:
    print("You need to fill in client_key and client_secret. See comments in the code around line 8-14")
    exit()



def get_tokens():
    oauth = requests_oauthlib.OAuth1Session(client_key, client_secret=client_secret)
    request_token_url = 'https://www.tumblr.com/oauth/request_token'
    fetch_response = oauth.fetch_request_token(request_token_url)
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')
    base_authorization_url = 'https://www.tumblr.com/oauth/authorize'
    authorization_url = oauth.authorization_url(base_authorization_url)
    webbrowser.open(authorization_url) # opens a window in your web browser
    verifier = raw_input('Please input the verifier>>> ')
    oauth = requests_oauthlib.OAuth1Session(client_key,
                              client_secret=client_secret,
                              resource_owner_key=resource_owner_key,
                              resource_owner_secret=resource_owner_secret,
                              verifier=verifier)
    access_token_url = 'https://www.tumblr.com/oauth/authorize'
    oauth_tokens = oauth.fetch_access_token(access_token_url)
    resource_owner_key = oauth_tokens.get('oauth_token')
    resource_owner_secret = oauth_tokens.get('oauth_token_secret')
    return (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier)

try:
    f = open("creds.txt", 'r')
    (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier) = json.loads(f.read())
    f.close()
except:
    tokens = get_tokens()
    f = open("creds.txt", 'w')
    f.write(json.dumps(tokens))
    f.close()
    (client_key, client_secret, resource_owner_key, resource_owner_secret, verifier) = tokens

oauth = requests_oauthlib.OAuth1Session(client_key,
                        client_secret=client_secret,
                        resource_owner_key=resource_owner_key,
                        resource_owner_secret=resource_owner_secret)

r = oauth.get("https://api.tumblr.com/v2/blog/University_of_michigan')

print(type(r.json()))
res = r.json()
print(list(res.keys()))
