import json
import requests

class ImageSearch:
  def __init__(self, topic=None):
    self.api_url = f'https://imsea.herokuapp.com/api/1?q={topic}'

  def get(self):
    response = requests.get(self.api_url)
    self.images = response.json()

  def __str__(self):
    return self.images['results']