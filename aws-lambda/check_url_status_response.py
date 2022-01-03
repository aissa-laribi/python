#A Lambda function that returns the GET HTTP response status codes using the Requests Python library https://docs.python-requests.org/en/latest/
import requests

def lambda_handler(event, context):
    r = requests.get(event['url1'],)
    if r.status_code == 200:
        return "The status code of the URL "+str(event['url1'])+"is 200 which means the URL is working"
    else:
        return("The status code of the URL "+str(event['url1'])+"is ,which means something is wrong with this URL")
    

    return { 
        lambda_handler(event, 'url1'),
        }
