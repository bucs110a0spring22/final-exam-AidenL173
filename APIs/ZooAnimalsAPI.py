import json
import requests
  
class ZooAnimal:
  def __init__(self):
    '''
    saves the API address as an instance variable
    '''
    self.api_url = 'https://zoo-animal-api.herokuapp.com/animals/rand'
  
  def get(self):
    '''
    pulls data from the API address and saves it in an instance variable, in this case, animal data
    '''
    response = requests.get(self.api_url)
    self.info = response.json()
    
  def __str__(self):
    '''
    str magic method that returns the data pulled.
    return: dict, returns a dictionary of animal information
    '''
    return self.info