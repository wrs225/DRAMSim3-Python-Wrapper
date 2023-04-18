
from DRAMsimWrapper.memory_system import * 
import ctypes
import numpy as np


def callback_read(i):
    pass

def callback_write(i):
    pass

memsys = MemorySystem(u'./MemoryConfigs/DDR3_1Gb_x8_1333.ini',u'./runs',callback_read,callback_write)

base_addr = 0

stride = 64

curr_addr = base_addr

cycles = 0


while curr_addr != 6400:
    memsys.ClockTick()
    cycles = cycles + 1
    if(memsys.WillAcceptTransaction(curr_addr, True)):
        memsys.AddTransaction(curr_addr, True)
        curr_addr = curr_addr + stride

print(cycles)
cycles = 0
curr_addr = base_addr
while curr_addr != 6400:
    memsys.ClockTick()
    cycles = cycles + 1
    if(memsys.WillAcceptTransaction(curr_addr, False)):
        memsys.AddTransaction(curr_addr, False)
        curr_addr = curr_addr + stride
print(cycles)

memsys.PrintStats()   
