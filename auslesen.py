import argparse
import signal
import sys
import logging
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
# https://github.com/Domifry/

from rpi_rf import RFDevice

rfdevice = None

# pylint: disable=unused-argument
def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=17,
                    help="GPIO pin (Default: 17)")
args = parser.parse_args()

signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()
while True:
    print(rfdevice.rx_code)
    time.sleep(0.01)
rfdevice.cleanup()
