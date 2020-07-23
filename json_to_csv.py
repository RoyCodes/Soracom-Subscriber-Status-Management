import json, time, csv

#get current time
current_time = int(time.time()) * 1000

#create list to store dormant IMSIs
imsi_list = []

with open('subscribers_list.json') as json_file:
    json_data = json.loads(json_file.read())
    for key in json_data:

        #if active and offline:
        if key['status'] == 'active' and key['sessionStatus']['online'] == False:
            #check if no data sessions for 30 days:
            print(key['imsi'])
            days_since_last_session = int((current_time - key['sessionStatus']['lastUpdatedAt']) / (1000*60*60*24))
            print(days_since_last_session)
            if days_since_last_session >= 30:
                imsi_list.append(key['imsi'])

try:
    with open('dormant_imsi_list.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        #writer.writeheader()
        print(imsi_list)
        writer.writerow(imsi_list)
except IOError:
    print("I/O error") 
csv_file.close()