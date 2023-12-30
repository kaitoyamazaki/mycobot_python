#!/usr/bin/env python3

import time
import os
import serial

from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
from pymycobot.genre import Angle
import csv
import numpy as np
import pandas as pd

port: str
mc: MyCobot
sp: int 

def setup():
    print("")
    global port, mc
    plist = list(serial.tools.list_ports.comports())
    idx = 1
    for port in plist:
        print("{} : {}".format(idx, port))
        idx += 1

    _in = input("\nPlease input 1 - {} to choice:".format(idx - 1))
    port = str(plist[int(_in) - 1]).split(" - ")[0].strip()
    print(port)
    print("")

    baud = 1000000
    _baud = input("Please input baud(default:1000000):")
    try:
        baud = int(_baud)
    except Exception:
        pass
    print(baud)
    print("")

    DEBUG = False
    f = input("Wether DEBUG mode[Y/n](default:n):")
    if f in ["y", "Y", "yes", "Yes"]:
        DEBUG = True
    # mc = MyCobot(port, debug=True)
    mc = MyCobot(port, baud, debug=DEBUG)
    mc.send_angles([0.0, -80.0, -20.0, 10.0, 0.0, -45], 100)
    time.sleep(1)

class ApiTest():

    def __init__(self, mycobot):
        self.mc = mycobot
        self.filepath = "../data/deg_control_data2.csv"
        self.df = pd.read_csv(self.filepath, header=None)
        self.data = self.df.values

    def play(self):
        print(f"connected mycobot!")

        data = self.data
        for i in range(len(data)):
            now_data = data[i]
            self.mc.send_angles([-45.0, now_data[0], now_data[1], now_data[2], 0.0, -45], 100)
            time.sleep(0.1)

        self.mc.send_angles([0.0, 0.0, 0.0, 0.0, 0.0, -45], 100)

if __name__ == "__main__":
    setup()
    manipulator = ApiTest(mc)
    manipulator.play() 
