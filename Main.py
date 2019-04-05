import time

from Classes.Ram_Management import Memory_management
from Classes.bcolors import bcolors
from Classes.CPU_Scheduling_algo import CPUSchedulers
from Classes.paging import Paging
if __name__ == "__main__":
    print("""
                1. CPU Scheduling Algorithms
                2. Memory Management Algorithms
                3. Paging""")
    try:
        x = int(input())
    except:
        print(bcolors.FAIL + "YOU ENTERED A WRONG INPUT! EXITING NOW")
        time.sleep(2)
        exit(0)
    if x == 2:
        mem = Memory_management()
        mem.Main()
    elif x == 1:
        cpu = CPUSchedulers()
        cpu.Main()
    elif x==3:
        page = Paging()
        page.Main()

