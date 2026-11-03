# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

import requests
import json

url = "https://jsonplaceholder.typicode.com/users/1"

# Make a GET request
response = requests.get(url)

# Save the response in a JSON file
with open("user.json", "w") as file:
    file.write(response.text)

# Display the raw JSON response
print(response.text)

# Display the JSON in a more readable format
data = response.json()
print(json.dumps(data, indent=4))