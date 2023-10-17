from promptflow import tool
import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.


@tool
def my_python_tool(short_description: str, headline: str) -> str:
  

  data = {"inputs": {"input_signature1": [short_description], "input_signature2":[headline] }}

  body = str.encode(json.dumps(data))

  ##### IMPORTANT: Replace this with the URL for your endpoint #####
  url = 'https://endpoint.westeurope.inference.ml.azure.com/score'

  # Replace this with the primary/secondary key or AMLToken for the endpoint
  api_key = '111111111111111111111111111111111'
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")

  ### IMPORTANT: Replace 'fine-tuned-bert-news-classific-1' with the name of your model deployment ###
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'fine-tuned-bert-news-classific-1' }

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)

      result = json.loads(response.read().decode("utf8", 'ignore'))[0]["0"]
      print(result)
  except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))

      print(error.info())
      print(error.read().decode("utf8", 'ignore'))
      result = error.read().decode("utf8", 'ignore')

  return result
