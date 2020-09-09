import requests, json, time, csv, os

#remove previous output.log if exists.
if os.path.exists("output.log"):
    os.remove("output.log")

# Your Soracom API key ID and secret
auth_key_id = 'keyId-xxxxxxxxxx'
auth_key = 'secret-yyyyyyyyyy'

# Authenticate and get API key and token
auth_headers = { "Content-Type": "application/json", "Accept": "application/json" }
body = { "authKeyId": auth_key_id, "authKey": auth_key }
auth_response = requests.post('https://g.api.soracom.io/v1/auth', data=json.dumps(body), headers=auth_headers)
if auth_response.status_code != 200: # An error occurred, print the error and exit
    print(auth_response.text)
    quit()
# Set up headers for subsequent Soracom API calls
headers = {
    "X-Soracom-API-Key": auth_response.json().get('apiKey'),
    "X-Soracom-Token": auth_response.json().get('token'),
    "Content-Type": "application/json"
}

output_file = open('output.log', mode='w')
csv_file = open('dormant_imsi_list.csv', mode='r')
csv_data = csv.reader(csv_file, delimiter=',')
output_data = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for csv_list in csv_data:
    for item in csv_list:
        imsi = item
        print(imsi)

        url = f"https://g.api.soracom.io/v1/subscribers/{imsi}/set_to_standby"

        response = requests.request("POST", url, headers=headers, data = {})

        print(response.status_code, response.text.encode('utf8'))
        output_row = [imsi, response.status_code]
        output_data.writerow(output_row)

# Close files after writing
csv_file.close()
output_file.close()