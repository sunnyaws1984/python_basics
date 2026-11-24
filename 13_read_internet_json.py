# pip install requests

import requests
import json

# Internet API URL
url = "https://jsonplaceholder.typicode.com/users"

# Send request to internet
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:

    # Convert response into Python data
    data = response.json()

    # Print data in JSON format
    print(json.dumps(data, indent=4))

else:
    print("Error:", response.status_code)
