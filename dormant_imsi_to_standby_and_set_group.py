import requests, json, time, csv, os

#remove previous output.log if exists
if os.path.exists("output.log"):
    os.remove("output.log")

#set up your Soracom API key and token
x_soracom_key = "API KEY HERE"
x_soracom_token = "API TOKEN HERE"

#enter the group id
group_id = "GROUP ID HERE"

#set up headers for soracom api calls
headers = {
  'X-Soracom-API-Key': x_soracom_key,
  'X-Soracom-Token': x_soracom_token,
  'Content-type': 'application/json'
}

output_file = open('output.log', mode='w')
csv_file = open('dormant_imsi_list.csv', mode='r')
csv_data = csv.reader(csv_file, delimiter=',')
output_data = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for csv_list in csv_data:
    for item in csv_list:
        imsi = item
        print(imsi)

        standby_url = f"https://g.api.soracom.io/v1/subscribers/{imsi}/set_to_standby"

        standby_response = requests.request("POST", standby_url, headers=headers, data = {})

        print("set to standby status: ", standby_response.status_code, standby_response.text.encode('utf8'))

        set_group_url = f"https://g.api.soracom.io/v1/subscribers/{imsi}/set_group"
        set_group_payload = {"groupId":group_id}

        set_group_response = requests.request("POST", set_group_url, headers=headers, data = json.dumps(set_group_payload))

        print("set group status: ", set_group_response.status_code, set_group_response.text.encode('utf8'))

        output_row_w_group = [imsi, standby_response.status_code, set_group_response.status_code]
        output_data.writerow(output_row_w_group)

csv_file.close()
output_file.close()