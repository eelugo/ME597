# MTConnet adapter sample for ME597 Lab5

# Code will only sample from ADXL354, port 7878

import random
import sys
import time
import datetime
from data_item import Event, Sample # load data_item package
from mtconnect_adapter import Adapter # load mtconnect_adapter package


class MTConnectAdapter(object):

    def __init__(self, host, port):
        # MTConnect adapter connection info
        self.host = host
        self.port = port
        self.adapter = Adapter((host, port))

        # For samples
        self.a1 = Sample('a1') # x
        self.adapter.add_data_item(self.a1) 
        self.a2 = Sample('a2') # y
        self.adapter.add_data_item(self.a2)
        self.a3 = Sample('a3') # z
        self.adapter.add_data_item(self.a3)


        # For events
        self.event = Event('event') # self.event takes 'event' data item name.
        self.adapter.add_data_item(self.event) # adding self.event as a data item
        ## Add more events below

        # MTConnnect adapter availability
        self.avail = Event('avail')
        self.adapter.add_data_item(self.avail)

        # Start MTConnect
        self.adapter.start()
        self.adapter.begin_gather()
        self.avail.set_value("AVAILABLE")
        self.adapter.complete_gather()
        self.adapter_stream()

    def adapter_stream(self):
        while True:
            try:
                # Do something here.
                a1 = random.uniform(-1,1) # this example is to take a random float between -1 and 1.
                a2 = random.uniform(-2, 2) #y
                a3 = 9.81 + random.uniform(-0.5, 0.5) #z

                self.adapter.begin_gather()
                self.a1.set_value(str(a1)) # set value of a1 data item, format: str(float)
                self.a2.set_value(str(a2))
                self.a3.set_value(str(a3))
                self.adapter.complete_gather()

                print("{} RANDOM VALUE a1={} mm/s^2".format(datetime.datetime.now(), a1)) # printing out datetime now and a1
                print("{} RANDOM VALUE a2={} mm/s^2".format(datetime.datetime.now(), a2)) # printing out datetime now and a2
                print("{} RANDOM VALUE a3={} mm/s^2".format(datetime.datetime.now(), a3)) # printing out datetime now and a3

                print(datetime.datetime.now(), "MTConnect data items gathering completed...\n") # printing out MTConnect data collection is done.

                time.sleep(1) # wait for 1 seconds

            except KeyboardInterrupt:
                print("Stopping MTConnect...")
                self.adapter.stop() # Stop adapter thread
                sys.exit() # Terminate Python

## ====================== MAIN ======================
if __name__ == "__main__":
    print("Starting up!")
    MTConnectAdapter('127.0.0.1', 7878) # Args: host ip, port number
