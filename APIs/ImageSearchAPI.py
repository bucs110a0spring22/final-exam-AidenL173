import json
import requests

class ImageSearch:
  def __init__(self, topic=None):
    '''
    saves the API address as an instance variable
    topic: str, the images you want to search
    '''
    self.api_url = f'https://imsea.herokuapp.com/api/1?q={topic}'

  def get(self):
    '''
    pulls data from the API address and saves it in an instance variable, in this case, image links
    '''
    response = requests.get(self.api_url)
    self.images = response.json()

  def __str__(self):
    '''
    str magic method that returns the results of the data pulled.
    return: list, returns a list of image links
    '''
    return self.images['results']