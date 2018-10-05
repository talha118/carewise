import os
import requests
from carewise.settings import TABLEAU_IP

proxyDict = {
              "http"  : os.environ.get('FIXIE_URL', ''),
              "https" : os.environ.get('FIXIE_URL', '')
            }

def trusted_authentication_tableau(requested_view, tableau_username):
    response = requests.post(TABLEAU_IP, data = {'username': tableau_username}, proxies = proxyDict)
    ticket = ""
    final_url = ""

    if response.status_code == 200:
        if str(response.text) != "-1":
            ticket = str(response.text)
            return (TABLEAU_IP + "/" + ticket +"/views/"+ requested_view)
    return None