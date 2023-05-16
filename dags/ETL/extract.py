import requests
import sys, os
sys.path.append(os.path.dirname(sys.path[0]))

from variables import HEADERS

def extract_data(url):
  headers = HEADERS
  response = requests.get(
    url=url, 
    headers=headers)
  
  return response