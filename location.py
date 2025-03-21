import requests

response = requests.get('https://ipinfo.io')
data = response.json()

# Get the location data
coordinates = data['loc'].split(',')
latitude = coordinates[0]
longitude = coordinates[1]

print(f"Latitude: {latitude}, Longitude: {longitude}")