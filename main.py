import requests
from APIs import ZooAnimalsAPI
from APIs import ImageSearchAPI

def main():
  info = ZooAnimalsAPI.ZooAnimal()
  info.get()
  data = info.__str__()
  imagesearch = ImageSearchAPI.ImageSearch(data['name'])
  imagesearch.get()
  images = imagesearch.__str__()
  print('Your random animal is: ' + data['name'] + ', A.K.A, ' + data['latin_name'])
  print('\nThey live in ' + data['habitat'] + ' in ' + data['geo_range'])
  print('\nThe ' + data['name'] + ' are a type of ' + data['animal_type'] + ' that eat ' + data['diet'] + ' and can live up to ' + data['lifespan'] + ' years.')
  print('\nHere are some images of them:\n=============================')
  for image in range(5):
    print(images[image]) if images[image] != images[(image - 1)] else None
  
main()