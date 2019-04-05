from Classes.bcolors import bcolors


class Memory_management:
    def __init__(self):
        self.memory_partitions = []
        self.processes = []
        self.taken = []
        self.internal_frag = []

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
        self.internal_frag = []
        for i in self.memory_partitions:
            self.internal_frag.append("X")
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
                    self.internal_frag[self.memory_partitions.index(j)] = j - i
                    fl = 1
                    break
                    print()
            if fl == 0:
                external_fragmentation = external_fragmentation + i
        print("Internal Fragmentation : ", internal_fragmentation)
        print("External Fragmentation : ", external_fragmentation)
        self.display_box(taken)

    def Best_fit(self, type):
        taken = []
        internal_fragmentation = 0
        external_fragmentation = 0
        self.internal_frag = []
        for i in self.memory_partitions:
            self.internal_frag.append("X")
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
                self.internal_frag[index_mem_partition] = min_count

        print("Internal Fragmentation : ", internal_fragmentation)
        print("External Fragmentation : ", external_fragmentation)
        self.display_box(taken)

    def Worst_fit(self, type):
        taken = []
        internal_fragmentation = 0
        external_fragmentation = 0
        self.internal_frag = []
        for i in self.memory_partitions:
            self.internal_frag.append("X")

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
                self.internal_frag[index_mem_partition] = max_count
        print("Internal Fragmentation : ", internal_fragmentation)
        print("External Fragmentation : ", external_fragmentation)
        self.display_box(taken)

    def First_fit_var(self, type):
        taken = []
        self.internal_frag = []
        memory_partitions = self.memory_partitions[:]
        for i in self.memory_partitions:
            self.internal_frag.append("X")
        internal_fragmentation = 0
        external_fragmentation = 0

        k = 0
        for i in self.memory_partitions:
            taken.append([])
        print("Initialising first fit of type : ", type)
        for i in self.processes:
            fl = 0
            for j in memory_partitions:
                if i <= j:
                    # print("i = ",i)
                    # print("j = ",j)
                    taken[memory_partitions.index(j)].append(self.processes.index(i))
                    memory_partitions[memory_partitions.index(j)] = memory_partitions.index(j) - i
                    # print(taken.index(self.processes.index(i)), " >> ",self.processes.index(i))
                    self.internal_frag[self.memory_partitions.index(j)] = j - i
                    fl = 1
                    break
                    print()
            if fl == 0:
                external_fragmentation = external_fragmentation + i

        for i in self.internal_frag:
            if i != "X":
                internal_fragmentation = internal_fragmentation + i
        print("Internal Fragmentation : ", internal_fragmentation)
        print("External Fragmentation : ", external_fragmentation)
        print("Taken : ", taken)
        self.display_box_var(taken)

    def Best_fit_var(self, type):
        taken = []
        internal_fragmentation = 0
        external_fragmentation = 0
        self.internal_frag = []
        for i in self.memory_partitions:
            self.internal_frag.append("X")
        k = 0
        for i in self.memory_partitions:
            taken.append([])
        memory_partitions = self.memory_partitions[:]

        min_count = None
        index_mem_partition = -1
        index_process = -1
        print("Initialising Worst fit of type : ", type)
        for i in self.processes:
            fl = 0
            min_count = None
            for j in memory_partitions:
                if i <= j:
                    # print("i = ",i)
                    # print("j = ",j)
                    # taken[self.memory_partitions.index(j)] = self.processes.index(i)
                    # print(taken.index(self.processes.index(i)), " >> ",self.processes.index(i))
                    # internal_fragmentation=internal_fragmentation+(j-i)
                    if min_count == None:
                        index_mem_partition = memory_partitions.index(j)
                        index_process = self.processes.index(i)
                        min_count = j - i
                    elif (j - i) < min_count:
                        index_mem_partition = memory_partitions.index(j)
                        index_process = self.processes.index(i)
                        min_count = j - i
                    fl = 1

            if fl == 0:
                external_fragmentation = external_fragmentation + i
            else:
                taken[index_mem_partition].append(index_process)
                # print("Previous : ", memory_partitions[index_mem_partition], " at ", index_mem_partition)
                memory_partitions[index_mem_partition] = memory_partitions[index_mem_partition] - (
                        memory_partitions[index_mem_partition] - min_count)
                # print("Updated : ",memory_partitions[index_mem_partition] ," at ",index_mem_partition)
                # internal_fragmentation = internal_fragmentation + (max_count)
                self.internal_frag[index_mem_partition] = min_count
        for i in self.internal_frag:
            if i != "X":
                internal_fragmentation = internal_fragmentation + i
        print("Internal Fragmentation : ", internal_fragmentation)
        print("External Fragmentation : ", external_fragmentation)
        print("Taken : ", taken)
        self.display_box_var(taken)

    def Worst_fit_var(self, type):
        taken = []
        internal_fragmentation = 0
        external_fragmentation = 0
        self.internal_frag = []
        for i in self.memory_partitions:
            self.internal_frag.append("X")
        k = 0
        for i in self.memory_partitions:
            taken.append([])
        memory_partitions = self.memory_partitions[:]

        max_count = None
        index_mem_partition = -1
        index_process = -1
        print("Initialising Worst fit of type : ", type)
        for i in self.processes:
            fl = 0
            max_count = None
            for j in memory_partitions:
                if i <= j:
                    # print("i = ",i)
                    # print("j = ",j)
                    # taken[self.memory_partitions.index(j)] = self.processes.index(i)
                    # print(taken.index(self.processes.index(i)), " >> ",self.processes.index(i))
                    # internal_fragmentation=internal_fragmentation+(j-i)
                    if max_count == None:
                        index_mem_partition = memory_partitions.index(j)
                        index_process = self.processes.index(i)
                        max_count = j - i
                    elif (j - i) > max_count:
                        index_mem_partition = memory_partitions.index(j)
                        index_process = self.processes.index(i)
                        max_count = j - i
                    fl = 1

            if fl == 0:
                external_fragmentation = external_fragmentation + i
            else:
                taken[index_mem_partition].append(index_process)
                # print("Previous : ", memory_partitions[index_mem_partition], " at ", index_mem_partition)
                memory_partitions[index_mem_partition] = memory_partitions[index_mem_partition] - (
                            memory_partitions[index_mem_partition] - max_count)
                # print("Updated : ",memory_partitions[index_mem_partition] ," at ",index_mem_partition)
                # internal_fragmentation = internal_fragmentation + (max_count)
                self.internal_frag[index_mem_partition] = max_count
        for i in self.internal_frag:
            if i != "X":
                internal_fragmentation = internal_fragmentation + i
        print("Internal Fragmentation : ", internal_fragmentation)
        print("External Fragmentation : ", external_fragmentation)
        print("Taken : ", taken)
        self.display_box_var(taken)

    def display_box(self, taken):
        print("""+""", end="")
        for i in taken:
            print("""-------+""", end="")
        print("\n|", end="")
        k = 0
        for i in taken:
            print(bcolors.OKBLUE + "   %3d |" % (self.memory_partitions[k]), end="" + bcolors.ENDC)
            k = k + 1

        print("\n|", end="")
        for i in taken:
            if i != -1:
                # print("Block number ", taken.index(i) + 1, " has been given to Process number ", i + 1)
                print(bcolors.WARNING + """   {0}   |""".format(i + 1), end="" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + """   X   |""", end="" + bcolors.ENDC)
        print("\n|", end="")
        k = 0
        for i in taken:
            try:
                print(bcolors.FAIL + "   %3d |" % (self.internal_frag[k]), end="" + bcolors.ENDC)
                k = k + 1
            except:
                print(bcolors.FAIL + "   X   |", end="" + bcolors.ENDC)
                k = k + 1

        print("""\n+""", end="")
        for i in taken:
            print("""-------+""", end="")
    def display_box_var(self, taken):

        print("""+""", end="")
        for i in taken:
            print("""---------------+""", end="")
        print("\n|", end="")
        k = 0
        for i in taken:
            print(bcolors.OKBLUE + "    %6d     |" % (self.memory_partitions[k]), end="" + bcolors.ENDC)
            k = k + 1

        print("\n|", end="")
        for i in taken:
            if len(i)!=0:
                # print("Block number ", taken.index(i) + 1, " has been given to Process number ", i + 1)
                i[:]=[x+1 for x in i]

                print(bcolors.WARNING + """      {0}""".format(i), end="" + bcolors.ENDC)
                for i in range(9-len(str(i))):
                    print(" ",end="")
                print("|",end="")

            else:
                print(bcolors.FAIL + """       X       |""", end="" + bcolors.ENDC)
        print("\n|", end="")
        k = 0
        for i in taken:
            try:
                print(bcolors.FAIL + "    %6d     |" % (self.internal_frag[k]), end="" + bcolors.ENDC)
                k = k + 1
            except:
                print(bcolors.FAIL + "       X       |", end="" + bcolors.ENDC)
                k = k + 1

        print("""\n+""", end="")
        for i in taken:
            print("""---------------+""", end="")


    def Main(self):
        # print("Initiating Memory Management")
        print("""
        

 /$$      /$$                                                             /$$      /$$                                                                                       /$$            /$$$$$$  /$$                    
| $$$    /$$$                                                            | $$$    /$$$                                                                                      | $$           /$$__  $$| $$                    
| $$$$  /$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$  /$$   /$$      | $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$  /$$$$$$        | $$  \ $$| $$  /$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ /$$__  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$| $$  | $$      | $$ $$/$$ $$ |____  $$| $$__  $$ |____  $$ /$$__  $$ /$$__  $$| $$_  $$_  $$ /$$__  $$| $$__  $$|_  $$_/        | $$$$$$$$| $$ /$$__  $$ /$$__  $$
| $$  $$$| $$| $$$$$$$$| $$ \ $$ \ $$| $$  \ $$| $$  \__/| $$  | $$      | $$  $$$| $$  /$$$$$$$| $$  \ $$  /$$$$$$$| $$  \ $$| $$$$$$$$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$  | $$          | $$__  $$| $$| $$  \ $$| $$  \ $$
| $$\  $ | $$| $$_____/| $$ | $$ | $$| $$  | $$| $$      | $$  | $$      | $$\  $ | $$ /$$__  $$| $$  | $$ /$$__  $$| $$  | $$| $$_____/| $$ | $$ | $$| $$_____/| $$  | $$  | $$ /$$      | $$  | $$| $$| $$  | $$| $$  | $$
| $$ \/  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$/| $$      |  $$$$$$$      | $$ \/  | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$  |  $$$$/      | $$  | $$| $$|  $$$$$$$|  $$$$$$/
|__/     |__/ \_______/|__/ |__/ |__/ \______/ |__/       \____  $$      |__/     |__/ \_______/|__/  |__/ \_______/ \____  $$ \_______/|__/ |__/ |__/ \_______/|__/  |__/   \___/        |__/  |__/|__/ \____  $$ \______/ 
                                                          /$$  | $$                                                  /$$  \ $$                                                                           /$$  \ $$          
                                                         |  $$$$$$/                                                 |  $$$$$$/                                                                          |  $$$$$$/          
                                                          \______/                                                   \______/                                                                            \______/           

""")
        self.input_memory()
        self.input_process()
        print()
        print("Memory Partitions : ", end="")
        for i in self.memory_partitions:
            print(i, end="  ")
        # self.display_bar(self.memory_partitions, bcolors.OKBLUE)
        print("\nProcesses : ", end="")
        for i in self.processes:
            print(i, end="  ")
        # self.display_bar(self.processes, bcolors.WARNING)

        # print("Initiating Taken bar")
        self.taken = self.memory_partitions[:]
        print()
        print()
        self.First_fit("Fixed")
        print()
        print()
        self.Best_fit("Fixed")
        print()
        print()
        self.Worst_fit("Fixed")
        print()
        print()
        self.First_fit_var("Variable")
        print()
        print()
        self.Best_fit_var("Variable")
        print()
        print()
        self.Worst_fit_var("Variable")
