import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
  "question": "How can I request a refill for my prescription at Lamna Healthcare?",
  "chat_history": []
}


body = str.encode(json.dumps(data))

url = 'https://rag-6669-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCIsImtpZCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2IyMGEwMzgxLTFjY2ItNDA1NC04YWQ0LTk3ZmI1NWRlYmZjYS8iLCJpYXQiOjE3MjkyMzgyODEsIm5iZiI6MTcyOTIzODI4MSwiZXhwIjoxNzI5MjQzNTQwLCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFlBQUFBSVpLNjFjRW5xbFlPZW82VktocjRvWFNDL3Q2cFhpS1Rsdk9qQkFyMXFtZFdYWnEzT2kvQnZqVmQ1bVc0Nzc0YU5hRHY1RFBlVlpMc1RiMlhRVSsrT3NHWnplQkFuYm5Xc0hmYnhtRGpGR2M9IiwiYW1yIjpbInB3ZCIsInJzYSIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiNWQwMWUyMTctMGRjYS00NDU1LWIyZGQtOTU5NWFjNjE4NzA0IiwiZmFtaWx5X25hbWUiOiJBZG1pbmlzdHJhdG9yIiwiZ2l2ZW5fbmFtZSI6IlN5c3RlbSIsImdyb3VwcyI6WyIyMDc1OGM4ZS1mZTkwLTQ4MDAtYWVhYy0wYmEyOGI3OWIyODEiXSwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiOTQuMTA1LjEwNS4xMzQiLCJuYW1lIjoiU3lzdGVtIEFkbWluaXN0cmF0b3IiLCJvaWQiOiJmMjEyNjRjMi00NDhlLTQ5NGItOGM1NS1iYTVmNjY2MjgwZTIiLCJwdWlkIjoiMTAwMzIwMDM5ODVBQzNGRSIsInJoIjoiMC5BYmNBZ1FNS3Nzc2NWRUNLMUpmN1ZkNl95bDl2cGhqZjJ4ZE1uZGNXTkhFcW5MNzhBS1UuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiN0hRaEVwYk5zWkU4d0lMSFoyakprVE9BNjZJRkpUczk4TDB4NnBMckRfWSIsInRpZCI6ImIyMGEwMzgxLTFjY2ItNDA1NC04YWQ0LTk3ZmI1NWRlYmZjYSIsInVuaXF1ZV9uYW1lIjoiYWRtaW5ATW5nRW52TUNBUDI4Njc1Mi5vbm1pY3Jvc29mdC5jb20iLCJ1cG4iOiJhZG1pbkBNbmdFbnZNQ0FQMjg2NzUyLm9ubWljcm9zb2Z0LmNvbSIsInV0aSI6Ikp4WFlfTDFfM0U2cUZwVjlibThaQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfaWRyZWwiOiIxIDE0In0.TOQld-FfF3i85poqG40r0uehhcTwC-O-R-9NJm7ZGW8Mry7DdXP5_wqmJA1nXJwm4Lh4LvfGja6X_oU4woh7GQwk2MC0Cnh4j3BAnaJql0LqZtZWuOgNBlYh0KEwp0TsNqPgdmL6Aoc852Y073z_N4NSApj9IGog1XIwH6OzoSI5mquQEUhe69Ue8lwgQSlit0981YVtKt0iTcLYjdDRt8ZGIE0SGsa9wmc5lxAMJUlA2YrnpXj0UohDA85ybyztwJw4cLOA2sVkoNbjqEXYOaGf3SDagK9HsJIA49ya-Yq0bohHDc6y50Ze75UM6ODjnC7ycDAt0N9ckPlLVXDkGg'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))