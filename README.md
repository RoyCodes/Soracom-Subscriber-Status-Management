# Soracom-Subscriber-Status-Management
This sample shows one way to manage your SIMs in bulk by using the Soracom CLI and APIs. This is just for reference and any pull requests or feedback is welcome.

# Step 1
Use the [Soracom CLI](https://github.com/soracom/soracom-cli) to fetch all of your subscribers and then pipe the output to a local JSON file.

Here is the CLI command for this:

`soracom subscribers list --fetch-all | tee subscribers_list.json`

# Step 2
Run the Python script `json_to_csv.py` to parse the `subscribers_list.json` that we generated in Step 1. This script will loop through each subscriber and write the IMSI to a CSV file if it is currently ACTIVE, but has not been online for 30+ days. Now we should have a local CSV file that lists every dormant IMSI that is still ACTIVE.

# Step 3
Spot check the CSV file to make sure that there are no issues.

# Step 4
Add your API key and a fresh token to the Python script `dormant_imsi_to_standby.py` and then run it. This script will loop through each IMSI in `dormant_imsi_list.csv` and set it to STANDBY status. Please note that fees may apply when using STANDBY, so please check our [Pricing & Fee Schedule](https://developers.soracom.io/en/docs/reference/fees/#soracom-air-for-cellular) for reference.