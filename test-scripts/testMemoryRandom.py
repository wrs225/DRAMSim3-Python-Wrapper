import memory_system
import ctypes
import numpy as np
import random


def callback_read(i):
    pass

def callback_write(i):
    pass

memsys = memory_system.MemorySystem(u'./DDR3_1Gb_x8_1333.ini',u'./',callback_read,callback_write)

numtrans = 0

cycles = 0
addr = random.randint(0,1000000000)
while numtrans != 1000:
    memsys.ClockTick()
    cycles = cycles + 1
    if(memsys.WillAcceptTransaction(addr, True)):
        memsys.AddTransaction(addr, True)
        addr = random.randint(0,1000000000)
        numtrans = numtrans + 1

print(cycles)