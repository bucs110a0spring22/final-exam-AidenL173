import json
import requests
  
class ZooAnimal:
  def __init__(self):
    self.api_url = 'https://zoo-animal-api.herokuapp.com/animals/rand'
  
  def get(self):
    response = requests.get(self.api_url)
    self.info = response.json()
    
  def __str__(self):
    return self.info