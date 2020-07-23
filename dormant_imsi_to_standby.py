import requests, json, time, csv, os

#remove previous output.log if exists.
if os.path.exists("output.log"):
    os.remove("output.log")

#set up your Soracom API key and token
x_soracom_key = "API KEY HERE"
x_soracom_token = "API TOKEN HERE"

headers = {
  'X-Soracom-API-Key': x_soracom_key,
  'X-Soracom-Token': x_soracom_token
}

payload = {}

output_file = open('output.log', mode='w')
csv_file = open('dormant_imsi_list.csv', mode='r')
csv_data = csv.reader(csv_file, delimiter=',')
output_data = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

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
        output_row = [imsi, response.status_code]
        output_data.writerow(output_row)

csv_file.close()
output_file.cose()