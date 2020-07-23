import requests, json, time, csv

#set up your Soracom API key and token
x_soracom_key = "API KEY HERE"
x_soracom_token = "API TOKEN HERE"

headers = {
  'X-Soracom-API-Key': x_soracom_key,
  'X-Soracom-Token': x_soracom_token
}

payload = {}

csv_file = open('dormant_imsi_list.csv')
csv_data = csv.reader(csv_file, delimiter=',')
for csv_list in csv_data:
    for item in csv_list:
        imsi = item
        print(imsi)

        url = f"https://g.api.soracom.io/v1/subscribers/{imsi}/set_to_standby"

        payload = {}
        headers = {
        'X-Soracom-API-Key': x_soracom_key,
        'X-Soracom-Token': x_soracom_token
        }

        response = requests.request("POST", url, headers=headers, data = payload)

        print(response.status_code, response.text.encode('utf8'))