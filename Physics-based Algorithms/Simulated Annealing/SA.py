"""
Python Codes for Simulated Annealing and Its Applications
"""
__version__ = "1.0.0"
__author__ = "domain"
__all__ = ['SAtsp']
class SA:
    def __init__(self, t0: float, cool: float, inIter: int, maxIter: int):
        """Basic Attributes"""
        self.t0 = t0  # Initial Temp
        self.cool = cool  # Cooling Facor
        self.inIter = inIter  # InIter Times
        self.maxIter = maxIter  # Max Iter Times
        """Optimal Solution"""
        self.code = []    # Code Sequence
        self.val = 0   # Optimal Fitness
        self.code_len = 0  # Code Length
        self.count = 0    # Total Iteration times
        self.runtime = 0  # Running Time

    def generate(self):
        """Generate Initial Code Sequence"""
        print(self.code)

    def change(self, method: str, w: tuple):
        """Generate Neibourhood"""
        print(self.code)
    
    def fitness(self, val_list):
        """Compute Fitness Value"""
        print(self.val)
    
    def solve(self, val_list: list, method: str, w: tuple):
        """Solve Problems"""
        from math import exp
        from random import uniform
        self.generate()
        self.fitness(val_list)
        old_code = self.code.copy()
        old_val = self.val
        while self.count < self.maxIter:
            i = 0
            while i <= self.inIter:
                self.change(method, w)
                self.fitness(val_list)
                p = exp((old_val - self.val)/self.t0)
                if self.val >= old_val and uniform(0, 1) >= p:
                    self.code = old_code.copy()
                    self.val = old_val
                else:
                    old_code = self.code.copy()
                    old_val = self.val
                self.count += 1
                if self.count >= self.maxIter:
                    break
            self.t0 *= self.cool


class SAtsp(SA):
    def __init__(self, t0=5000, cool=0.98, inIter=100, maxIter=20000):
        """
        t0: Initial Temperature
        cool: Cooling Factor(0~1)
        inIter: Inner Iteration Times
        maxIter: Max Iteration Times
        """
        super().__init__(t0, cool, inIter, maxIter)
        self.loc = None   # Location List
        self.name = None  # City Name

    def generate(self):
        """Create Initial Sequence"""
        from random import shuffle
        seq = [i for i in range(self.code_len)]
        shuffle(seq)
        self.code = seq.copy()
    
    def exchange_site(self):
        """Exchange Two Codes"""
        from random import randint
        while True:
            a = randint(0, self.code_len - 1)
            b = randint(0, self.code_len - 1)
            if a != b:
                self.code[a], self.code[b] = self.code[b], self.code[a]
                break

    def reverse_site(self):
        """Reverse Codes Between Two Specific Codes"""
        from random import randint
        while True:
            a = randint(0, self.code_len - 1)
            b = randint(0, self.code_len - 1)
            if a < b and a != 0:
                self.code[a:b+1] = self.code[b:a-1:-1]
                break
            elif a > b and b != 0:
                self.code[b:a+1] = self.code[a:b-1:-1]
                break
            elif a == 0:
                self.code[:b+1] = self.code[b::-1]
                break
            elif b == 0:
                self.code[:a+1] = self.code[a::-1]
                break

    def insert_site(self):
        """Insert the First Code After the Second Code"""
        from random import randint
        while True:
            a = randint(0, self.code_len - 1)
            b = randint(0, self.code_len - 1)
            if a < b:
                temp = self.code[a]
                self.code[a:b] = self.code[a+1:b+1]
                self.code[b] = temp
                break
            elif a > b:
                temp = self.code[b]
                self.code[b:a] = self.code[b+1:a+1]
                self.code[a] = temp
                break

    def change(self, method: str, w: tuple):
        """
        Choose a Method to Generate A New Solution
        method: Method to generate solution
        w: The weight of the first two methods(If you choose roulette)
        """
        from random import uniform
        import sys
        if method == "exchange":
            self.exchange_site()
        elif method == "reverse":
            self.reverse_site()
        elif method == "insert":
            self.insert_site()
        elif method == "roulette":
            if sum(w) >= 1 or w[0] < 0 or w[1] < 0:
                print("Please input right weigt values!")
                sys.exit(1)
            p = uniform(0, 1)
            if p < w[0]:
                self.exchange_site()
            elif p < w[0] + w[1]:
                self.reverse_site()
            else:
                self.insert_site()
    
    def fitness(self, loc: list):
        """Compute the Total Distance"""
        self.val = 0
        temp = self.code.copy()
        temp.append(temp[0])
        for i in range(1, self.code_len + 1):
            self.val += ((loc[temp[i]][0]-loc[temp[i-1]][0])**2+(loc[temp[i]][1]-loc[temp[i-1]][1])**2)**0.5

    def report(self):
        """Output the result"""
        print("---------------------------")
        print("          Results          ")
        print("---------------------------")

        print("The optimal path is: ")
        route = self.code.copy()
        route.append(route[0])
        print("  ", self.name[route[0]], end="")
        for i in route[1:]:
            print(" ->", self.name[i], end="")
        
        print("\nDistance: %.2f"%self.val)
        print("Iteration Count: %d"%self.count)
        print("Running Time: %.2f s"%self.runtime)

        print("---------------------------")

    def visual(self):
        """
        Visualize the result in map
        name_list: City name(same order as loc_list)
        loc_list: list consists of (x,y) tuples
        """
        import matplotlib.pyplot as plt
        # scatter
        x1 = []
        y1 = []
        for i in self.loc:
            x1.append(i[0])
            y1.append(i[1])
        plt.scatter(x1, y1)
        # Tag
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus']=False
        for i in range(len(self.name)):
            plt.text(x1[i], y1[i], self.name[i], fontsize = 12, color = "#E58CAF")
        # line
        route = self.code.copy()
        route.append(route[0])
        x2 = []
        y2 = []
        for i in route:
            x2.append(self.loc[i][0])
            y2.append(self.loc[i][1])
        plt.plot(x2, y2)
        # Other set
        plt.title("TSP Map")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.grid(alpha=0.5, linestyle="-.")
        plt.show()

    def solveTSP(self, loc_list: list, name_list: list, method: str, w: tuple=(0.4, 0.4)):
        """
        Main method to solve TSP.
        loc_list: list consists of (x,y) tuples
        name_list: City names(same order as loc_list)
        method: "exchange","reverse","insert","roulette"
        w: The weight of the first two methods(If you choose roulette)
        """
        # Update Attribues
        self.code_len = len(loc_list)
        self.loc = loc_list
        self.name = name_list
        # Start
        from time import time
        start_time = time()
        SA.solve(self=self, val_list=self.loc, method=method, w=w)
        stop_time = time()
        self.runtime = stop_time - start_time
