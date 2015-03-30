from __future__ import division
from decimal import *

class transaction():

    # Set CLASS_DEBUG_ON = 1 to print additional debug info when running
    CLASS_DEBUG_ON = 0
    SATOSHI_PER_BTC = 100000000

    def __init__(self):
        #self.tx_value = value
        self.total_input_value = 0
        self.total_output_value = 0
        self.max_output_value = 0
        self.min_output_value = -1
        self.average_output_value = 0
        self.average_count = 1


    def satoshi_to_BTC(self, satoshi_value):
        #print("satoshi_to_BTC")
        return satoshi_value / self.SATOSHI_PER_BTC


    def set_min_max_value(self, value):
        # Checks to see if input value is greater than current max or less than current minimum and stores the new value if relevant

        if self.CLASS_DEBUG_ON == 1:
            print("transaction.set_value running...")
        
        # Check if new max value
        if value > self.max_output_value:
            self.max_output_value = value
            #print("new max: " + str(value))

        # Check if new min value
        if self.min_output_value == -1:
            self.min_output_value = value
        elif value < self.min_output_value:
            self.min_output_value = value


    def get_output_total(self, output_data):
        print(output_data)


    def get_min_output(self):
        print("Minimum Output = " + str("{:16.8f}".format(self.satoshi_to_BTC(self.min_output_value))) + " BTC")


    def get_max_output(self):
        print("Maximum Output = " + str("{:16.8f}".format(self.satoshi_to_BTC(self.max_output_value))) + " BTC")


    def get_avg_output(self):
        print("Average Output = " + str("{:16.8f}".format(self.satoshi_to_BTC(self.average_output_value))) + " BTC")


    def get_total_output(self):
        print("Total Output =   " + str("{:16.8f}".format(self.satoshi_to_BTC(self.total_output_value))) + " BTC")


    def parse_tx_data(self, tx_data):

        # All relevant data is in "x"
        data = tx_data["x"]
        
        self.tx_lock_time = data["lock_time"]
        self.tx_ver = data["ver"]
        self.tx_index = data["tx_index"]
        self.tx_relayed_by = data["relayed_by"]
        self.tx_vin_size = data["vin_sz"]
        self.tx_vout_size = data["vout_sz"]
        self.tx_time = data["time"]
        self.tx_hash = data["hash"]
        self.tx_size = data["size"]

        self.parse_tx_data_inputs(data["inputs"], data["vin_sz"])
        self.parse_tx_data_outputs(data["out"], data["vout_sz"])

        self.set_min_max_value(self.tx_output_value)
        self.calc_tx_fee()
        self.calc_average_value(self.tx_output_value, self.average_count)


    def parse_tx_data_inputs(self, tx_data, list_size):
        tx_list = tx_data
        input_value = 0

        for i in range(0, list_size):
            #print("\n" + str(i+1) + ". " + str(tx_list[i]['prev_out']['value']) + "\n")
            input_value = input_value + tx_list[i]['prev_out']['value']
            
        #print("Input value = " + str(input_value))
        self.total_input_value = self.total_input_value + input_value
        self.tx_input_value = input_value
        
        #print("\n" + str(tx_list[1]) + "\n")
        #print("Input data: " + str(tx_data))
        

    def parse_tx_data_outputs(self, tx_data, list_size):
        tx_list = tx_data
        output_value = 0
        
        for i in range(0, list_size):
            #print("\n" + str(i+1) + ". " + str(tx_list[i]['prev_out']['value']) + "\n")
            output_value = output_value + tx_list[i]['value']
            
        #print("Output value =   " + str("{:16.8f}".format(self.satoshi_to_BTC(output_value))) + " BTC")
        self.total_output_value = self.total_output_value + output_value
        self.tx_output_value = output_value


    def get_output_value(self):
        return self.tx_output_value

    def calc_tx_fee(self):
        self.tx_fee = self.tx_input_value - self.tx_output_value
        return self.tx_fee


    def calc_average_value(self, value, count):
        x = self.average_output_value * (count - 1)
        x = x + value
        x = x / count
        self.average_output_value = x
        self.average_count = self.average_count + 1
        #print("Average value =  " + (str("{:16.8f}".format(self.satoshi_to_BTC(x)))) + " BTC")
        

    def print_tx_data(self):

        print("Lock time:   " + str(self.tx_lock_time))
        print("Version:     " + str(self.tx_ver))
        print("Tx Index:    " + str(self.tx_index))
        print("Relayed by:  " + str(self.tx_relayed_by))
        print("V_in size:   " + str(self.tx_vin_size))
        print("V_out size:  " + str(self.tx_vout_size))
        print("Tx time:     " + str(self.tx_time))
        print("Hash:        " + str(self.tx_hash))
        print("Tx size:     " + str(self.tx_size))

        print("Tx fee: " + str("{:16.8f}".format(self.satoshi_to_BTC(self.tx_fee))) + " BTC")










    def get_tx_data(self, requested_data):
        
            print(getattr(self, requested_data))
            return getattr(self, requested_data)
        

    def iter_tx_data(self, tx_data):
        for key, value in tx_data["x"].iteritems():
            print key, 'corresponds to', tx_data["x"][key]
            

