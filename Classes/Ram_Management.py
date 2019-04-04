from Classes.bcolors import bcolors


class Memory_management:
    def __init__(self):
        self.memory_partitions = []
        self.processes = []
        self.taken = []

    def input_memory(self):
        running = True
        print("Input Memory Partitions : ")
        while (running):
            x = input()
            if x == "":
                break
            else:
                try:
                    self.memory_partitions.append(int(x))
                except:
                    print("Could not add, only input integers")

    def input_process(self):
        running = True
        print("\nInput Processes : ")
        while (running):
            x = input()
            if x == "":
                break
            else:
                try:
                    self.processes.append(int(x))
                except:
                    print("Could not add, only input integers")

    def display_bar(self, dis_bar, color):
        fl = 0
        bar = dis_bar[:]
        for i in bar:
            if i > 99:
                fl = 1
            elif i > 999:
                fl = 2
        if fl == 1:
            bar[:] = [x / 20 for x in bar]
        if fl == 2:
            bar[:] = [x / 200 for x in bar]

        print()
        for i in bar:
            print(color + "|", end="")
            for j in range(int(i)):
                print("▓", end="")
        print("| " + bcolors.ENDC, end="")

    def First_fit(self, type):
        taken = []
        internal_fragmentation = 0
        external_fragmentation = 0

        for i in self.memory_partitions:
            taken.append(-1)
        print("Initialising first fit of type : ", type)
        for i in self.processes:
            fl = 0
            for j in self.memory_partitions:
                if i <= j and taken[self.memory_partitions.index(j)] == -1:
                    # print("i = ",i)
                    # print("j = ",j)
                    taken[self.memory_partitions.index(j)] = self.processes.index(i)
                    # print(taken.index(self.processes.index(i)), " >> ",self.processes.index(i))
                    internal_fragmentation = internal_fragmentation + (j - i)
                    fl = 1
                    break
                    print()
            if fl == 0:
                external_fragmentation = external_fragmentation + i
        print("Internal Fragmentation : ", internal_fragmentation)
        print("External Fragmentation : ", external_fragmentation)
        for i in taken:
            if i != -1:
                print("Block number ", taken.index(i) + 1, " has been given to Process number ", i + 1)

    def Best_fit(self, type):
        taken = []
        internal_fragmentation = 0
        external_fragmentation = 0
        min_count = None
        index_mem_partition = -1
        index_process = -1
        for i in self.memory_partitions:
            taken.append(-1)
        print("Initialising best fit of type : ", type)
        for i in self.processes:
            fl = 0
            min_count = None
            for j in self.memory_partitions:
                if i <= j and taken[self.memory_partitions.index(j)] == -1:
                    # print("i = ",i)
                    # print("j = ",j)
                    # taken[self.memory_partitions.index(j)] = self.processes.index(i)
                    # print(taken.index(self.processes.index(i)), " >> ",self.processes.index(i))
                    # internal_fragmentation=internal_fragmentation+(j-i)
                    if min_count == None:
                        index_mem_partition = self.memory_partitions.index(j)
                        index_process = self.processes.index(i)
                        min_count = j - i
                    elif (j - i) < min_count:
                        index_mem_partition = self.memory_partitions.index(j)
                        index_process = self.processes.index(i)
                        min_count = j - i
                    fl = 1


            if fl == 0:
                external_fragmentation = external_fragmentation + i
            else:
                taken[index_mem_partition] = index_process
                internal_fragmentation = internal_fragmentation + (min_count)
        print("Internal Fragmentation : ", internal_fragmentation)
        print("External Fragmentation : ", external_fragmentation)
        for i in taken:
            if i != -1:
                print("Block number ", taken.index(i) + 1, " has been given to Process number ", i + 1)

    def Worst_fit(self, type):
        taken = []
        internal_fragmentation = 0
        external_fragmentation = 0
        max_count = None
        index_mem_partition = -1
        index_process = -1
        for i in self.memory_partitions:
            taken.append(-1)
        print("Initialising Worst fit of type : ", type)
        for i in self.processes:
            fl = 0
            max_count = None
            for j in self.memory_partitions:
                if i <= j and taken[self.memory_partitions.index(j)] == -1:
                    # print("i = ",i)
                    # print("j = ",j)
                    # taken[self.memory_partitions.index(j)] = self.processes.index(i)
                    # print(taken.index(self.processes.index(i)), " >> ",self.processes.index(i))
                    # internal_fragmentation=internal_fragmentation+(j-i)
                    if max_count == None:
                        index_mem_partition = self.memory_partitions.index(j)
                        index_process = self.processes.index(i)
                        max_count = j - i
                    elif (j - i) > max_count:
                        index_mem_partition = self.memory_partitions.index(j)
                        index_process = self.processes.index(i)
                        max_count = j - i
                    fl = 1


            if fl == 0:
                external_fragmentation = external_fragmentation + i
            else:
                taken[index_mem_partition] = index_process
                internal_fragmentation = internal_fragmentation + (max_count)
        print("Internal Fragmentation : ", internal_fragmentation)
        print("External Fragmentation : ", external_fragmentation)
        for i in taken:
            if i != -1:
                print("Block number ", taken.index(i) + 1, " has been given to Process number ", i + 1)


    def Main(self):
        print("Initiating Memory Management")
        self.input_memory()
        self.input_process()
        print()
        print("Memory Partitions : ", end="")
        for i in self.memory_partitions:
            print(i, end="  ")
        self.display_bar(self.memory_partitions, bcolors.OKBLUE)
        print("\nProcesses : ", end="")
        for i in self.processes:
            print(i, end="  ")
        # self.display_bar(self.processes, bcolors.WARNING)

        print("Initiating Taken bar")
        self.taken = self.memory_partitions[:]
        print()
        self.First_fit("Fixed")
        print()
        self.Best_fit("Fixed")
        print()
        self.Worst_fit("Fixed")
