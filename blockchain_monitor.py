from __future__ import division
#from websocket import create_connection
import json
from pprint import pprint

from websocket_lib import * # My websocket connection file
from transaction import *

tx_limit = 0
min_tx_display_value = 1
tx_limit =  int(raw_input("Enter number of transactions to watch: "))
min_tx_display_value =  int(raw_input("Enter minimum transaction size to show details for (BTC): "))

count = 0

# Set up Websocket connection
connection_url = "wss://ws.blockchain.info/inv"
ws = create_connection("wss://ws.blockchain.info/inv")

# Send Websocket message
#send_text = '{"op":"blocks_sub"}' # Subscribe to blocks
send_text = '{"op":"unconfirmed_sub"}' # Subscribe to unconfirmed transactions
send_message(ws, send_text)

# Create instance of transaction class for storing/processing transactions
tx = transaction()

# Loop for the number of transactions selected
while (count < tx_limit):
    print("\nWaiting for data... (" + str(count + 1) + " of " + str(tx_limit) + ")")
    result = ws.recv()

    # Convert JSON string to Python dictionary via .loads
    data = json.loads(result)
    
    # Parse the Python dictionary of Tx data and extract relevant parts
    tx.parse_tx_data(data)

    if tx.satoshi_to_BTC(tx.get_output_value()) >= min_tx_display_value:
        tx.print_tx_data()
    else:
        print("Output value =   " + str("{:16.8f}".format(tx.satoshi_to_BTC(tx.tx_output_value))) + " BTC")
        tx.get_avg_output()
        tx.get_total_output()

    count = count + 1
    
# Close Websocket
ws.close()

print("\n")
tx.get_min_output()
tx.get_max_output()
tx.get_avg_output()
tx.get_total_output()




#########################
# Misc stuff used along the way

#send_text = '{"op":"ping_block"}' # Returns the latest block
#send_text = '{"op":"ping_tx"}' # Returns the latest tx

#raise SystemExit
    #print(data.items())
    #print(data.keys())
    #print(data.values())

    #print(tx.tx_hash)

    #print(type(data))
    #relayed_by = data["relayed_by"]
    #if relayed_by == "127.0.0.1":
    #    relayed_by = "127.0.0.1 (Blockchain.info)"

    #print("\n" + str(len(data)) + "\n")
    #print(data["out"])
    #output_value = tx.satoshi_to_BTC(data["out"][0]["value"]) #+ data["out"][1]["value"]

    #if output_value >= min_tx_display_value:
        #print("\nRelayed by: " + relayed_by)
    #    print("Output Value: " + str(output_value) + " BTC \n")
    #    print("Running output: " + str(running_output_tally)) + " BTC"
    #    print("Average output: " + str(running_output_tally/(count+1))) + " BTC \n"
    #else:
        #print("Running output: " + str(running_output_tally)) + " BTC"
        #print("Average output: " + str(running_output_tally/(count+1))) + " BTC \n"


    #tx.iter_tx_data(data)
