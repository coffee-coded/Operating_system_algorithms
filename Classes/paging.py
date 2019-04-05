import time

from Classes.bcolors import bcolors


class Paging:
    def __init__(self):
        x = 0
        self.page_hit = 0
        self.page_fault = 0

    def Main(self):
        print("Paging Algorithms running")
        # print(bcolors.WARNING + "Under Construction" + bcolors.ENDC)
        # time.sleep(2)
        # exit(0)
        self.input_method()
        print("=================FIFO Method=================")
        self.FIFO_Method()
        print("==================LRU Method=================")
        self.LRU_method()
        print("==================Optimal Method=================")
        self.Optimal_method()

    def FIFO_Method(self):
        self.page_hit = 0
        self.page_fault = 0
        print("  Char   |", end="")
        k = 0
        for i in self.frame_list:
            print("  {0}  ".format(k + 1), end="")
            k = k + 1
        print()
        k = 0
        for i in self.input_character_set:
            print("    %c    |" % (i), end="")
            if self.frame_list.__contains__(i):
                self.page_hit = self.page_hit + 1
                fl = 1
            else:
                self.frame_list[k] = i
                self.page_fault = self.page_fault + 1
                k = k + 1
                k = k % int(self.frames)
                fl = 2
            for j in self.frame_list:
                if j != "-1":
                    if fl == 1 and j == i:
                        print(bcolors.OKBLUE + "  {0}  ".format(j), end="" + bcolors.ENDC)
                    elif fl == 2 and j == i:
                        print(bcolors.WARNING + "  {0}  ".format(j), end="" + bcolors.ENDC)
                    else:
                        print("  {0}  ".format(j), end="")

                else:
                    print(bcolors.FAIL + "  X  ".format(j), end="" + bcolors.ENDC)
            print()
        print(bcolors.WARNING +    "Page Fault : ", str(self.page_fault) + bcolors.ENDC)
        print(bcolors.OKBLUE + "Page  Hit  : ", str(self.page_hit) + bcolors.ENDC)

    def LRU_method(self):
        self.frame_list=[]
        for i in range(int(self.frames)):
            self.frame_list.append("-1")
        self.page_hit = 0
        self.page_fault = 0
        extracted_list = []
        print("  Char   |", end="")
        k = 0
        for i in self.frame_list:
            print("  {0}  ".format(k + 1), end="")
            k = k + 1
        print()
        k = 0
        index = 0
        for i in self.input_character_set:

            print("    %c    |" % (i), end="")
            if self.frame_list.__contains__(i):
                self.page_hit = self.page_hit + 1
                fl = 1
            else:
                if self.frame_list.__contains__("-1")==False:
                    # self.frame_list[k] = i
                    self.page_fault = self.page_fault + 1
                    # k = k + 1
                    # k = k % int(self.frames)
                    reversed_list = extracted_list[:]
                    reversed_list= reversed_list[::-1]
                    count=0
                    curr_frame = self.frame_list[:]
                    for z in reversed_list:
                        if curr_frame.__contains__(z):
                            curr_frame.remove(z)
                            if len(curr_frame)==1:
                                break
                    self.frame_list[self.frame_list.index(curr_frame[0])]=i
                else:
                    self.frame_list[k] = i
                    self.page_fault = self.page_fault + 1
                    k = k + 1
                    k = k % int(self.frames)


                fl = 2
            for j in self.frame_list:
                if j != "-1":
                    if fl == 1 and j == i:
                        print(bcolors.OKBLUE + "  {0}  ".format(j), end="" + bcolors.ENDC)
                    elif fl == 2 and j == i:
                        print(bcolors.WARNING + "  {0}  ".format(j), end="" + bcolors.ENDC)
                    else:
                        print("  {0}  ".format(j), end="")

                else:
                    print(bcolors.FAIL + "  X  ".format(j), end="" + bcolors.ENDC)
            extracted_list.append(i)
            index = index+1
            print()
        print(bcolors.WARNING + "Page Fault : ", str(self.page_fault) + bcolors.ENDC)
        print(bcolors.OKBLUE + "Page  Hit  : ", str(self.page_hit) + bcolors.ENDC)

    def Optimal_method(self):
        self.frame_list = []
        for i in range(int(self.frames)):
            self.frame_list.append("-1")
        self.page_hit = 0
        self.page_fault = 0
        extracted_list = self.input_character_set[:]
        print("  Char   |", end="")
        k = 0
        for i in self.frame_list:
            print("  {0}  ".format(k + 1), end="")
            k = k + 1
        print()
        k = 0
        index = 0
        for i in self.input_character_set:
            extracted_list.remove(i)
            print("    %c    |" % (i), end="")
            if self.frame_list.__contains__(i):
                self.page_hit = self.page_hit + 1
                fl = 1
            else:
                if self.frame_list.__contains__("-1") == False:
                    # self.frame_list[k] = i
                    self.page_fault = self.page_fault + 1
                    # k = k + 1
                    # k = k % int(self.frames)
                    reversed_list = extracted_list[:]
                    count = 0
                    curr_frame = self.frame_list[:]
                    for z in reversed_list:
                        if curr_frame.__contains__(z):
                            curr_frame.remove(z)
                            if len(curr_frame) == 1:
                                break
                    self.frame_list[self.frame_list.index(curr_frame[0])] = i
                else:
                    self.frame_list[k] = i
                    self.page_fault = self.page_fault + 1
                    k = k + 1
                    k = k % int(self.frames)

                fl = 2
            for j in self.frame_list:
                if j != "-1":
                    if fl == 1 and j == i:
                        print(bcolors.OKBLUE + "  {0}  ".format(j), end="" + bcolors.ENDC)
                    elif fl == 2 and j == i:
                        print(bcolors.WARNING + "  {0}  ".format(j), end="" + bcolors.ENDC)
                    else:
                        print("  {0}  ".format(j), end="")

                else:
                    print(bcolors.FAIL + "  X  ".format(j), end="" + bcolors.ENDC)
            extracted_list.append(i)
            index = index + 1
            print()
        print(bcolors.WARNING + "Page Fault : ", str(self.page_fault) + bcolors.ENDC)
        print(bcolors.OKBLUE + "Page  Hit  : ", str(self.page_hit) + bcolors.ENDC)

    def input_method(self):
        self.input_string = input("Please provide input string : ")
        self.input_character_set = [i for i in self.input_string]
        self.frames = input("Frames present : ")
        self.frame_list = []
        for i in range(int(self.frames)):
            self.frame_list.append("-1")
        # print(frame_list)
        print()
