import requests

API_KEY = 'AIzaSyCu6r6rD1KfYybcNbwQL_f4pq96cq-mrvk'  # Replace this with your actual API key

def get_address_from_coords(lat, lng):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('results')
        if results:
            return results[0].get('formatted_address')
        else:
            return "No address found for the given coordinates."
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    lat = input("Enter latitude: ")
    lng = input("Enter longitude: ")
    address = get_address_from_coords(lat, lng)
    print(f"The address for coordinates ({lat}, {lng}) is: {address}")
