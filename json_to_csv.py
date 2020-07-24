import json, time, csv

#get current time
current_time = int(time.time()) * 1000

#create list to store ACTIVE IMSIs with null data sessions
null_session_list = []

#create list to store dormant IMSIs
imsi_list = []

with open('subscribers_list.json') as json_file:
    json_data = json.loads(json_file.read())
    for key in json_data:

        #if active but null sessionStatus 
        if key['status'] == 'active' and key['sessionStatus'] == None:
            print("imsi: ", key['imsi'], " null session status")
            null_session_list.append(key['imsi'])

        #if active and offline:
        elif key['status'] == 'active' and key['sessionStatus']['online'] == False:
            #check if no data sessions for 30 days:
            days_since_last_session = int((current_time - key['sessionStatus']['lastUpdatedAt']) / (1000*60*60*24))
            if days_since_last_session >= 30:
                imsi_list.append(key['imsi'])
                print("imsi: ", key['imsi'], "days since last session: ", days_since_last_session)

try:
    with open('dormant_imsi_list.csv', 'w') as csv_file, open('null_session_status.csv', 'w') as null_session_log:
        #null session writer
        null_session_writer = csv.writer(null_session_log, quoting=csv.QUOTE_ALL)
        null_session_writer.writerow(null_session_list)

        #dormant imsi csv writer
        dormant_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        dormant_writer.writerow(imsi_list)

        
except IOError:
    print("I/O error") 
csv_file.close()