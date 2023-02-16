import requests

location = 'Eiffel Tower, Paris'  # example location
opencage_api_key = '510f29bf21b44ba6a7e39b4f0275f902'  # replace with your API key

opencage_url = 'https://api.opencagedata.com/geocode/v1/json'
params = {
    'q': location,
    'key': opencage_api_key
}
response = requests.get(opencage_url, params=params)
location_data = response.json()['results'][0]['geometry']

latitude=location_data['lat']
longitude=location_data['lng']
params = {
    'q': f'hospitals near {latitude}, {longitude}',
    'key': opencage_api_key,
    'radius': 5000,  # search within 5km radius
    'no_annotations': 1  # exclude additional metadata
}
response = requests.get(opencage_url, params=params)
results = response.json()['results']
print(results)
for result in results:
    print(result['formatted'])

