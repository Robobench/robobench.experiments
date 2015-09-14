__author__ = 'flier'

import sys
import time
sys.path.append('/opt/strands-morse-simulator/lib/python3/dist-packages/')
sys.path.append('/opt/strands-morse-simulator/lib/python3/dist-packages/pymorse/')
sys.path.append('/opt/strands-morse-simulator/lib/python3/dist-packages/morse/')
import pymorse

with pymorse.Morse() as sim:
    sim.rpc('simulation', 'set_camarafp_position', [25, -35, 25])

while True:
    time.sleep(10)
