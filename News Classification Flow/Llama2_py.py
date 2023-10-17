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


    


from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(headline, short_description: str) -> str:
 

  data =  {
    "input_data": {
      "columns": [
        "input_string"
      ],
      "index": [0],
      "data": [{
        "input_string": "headline:\n" + headline + "\nshort_description:\n" + short_description + "\n"
      }]
    },
    "params": {}
  }


  print(data)

  body = str.encode(json.dumps(data))

  ##### IMPORTANT: Replace this with the URL for your endpoint #####
  url = 'https://endpoint.westeurope.inference.ml.azure.com/score'

   ##### IMPORTANT: Replace this with the primary/secondary key or AMLToken for the endpoint #####
  # Replace this with the primary/secondary key or AMLToken for the endpoint
  api_key = '111111111111111111111111111111111'
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")

  # The azureml-model-deployment header will force the request to go to a specific deployment.
  # Remove this header to have the request observe the endpoint traffic rules
  ### IMPORTANT: Replace 'llmops-ft-llama2-news-1' with the name of your model deployment ###
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'llmops-ft-llama2-news-1' }

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)
      print(response)
      result = json.loads(response.read().decode("utf8", 'ignore'))[0]["0"]
      print(result)
      return result
  except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))

      # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      # print(error.info())
      print(error.read().decode("utf8", 'ignore'))
      return error.read().decode("utf8", 'ignore')

