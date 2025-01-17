from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Solver:
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m

        self.DIR_X = [1, -1, 0, 0]
        self.DIR_Y = [0, 0, 1, -1]
        
        self.memoization = [[None for j in range(m)] for i in range(n)]
        self.arr = [[None for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                self.arr[i][j] = arr[i][j]

    # There is a huge room for memoization here if a number can reach k many
    # 9's, then that can be momized and reused in future iterations

    # Current thought is how to record the number of 9's that can be reached
    # and without passing a truth table as a parameter as that's quite
    # inefficient... Maybe define it as a class variable?
    
    # New thought: Use a set and use set.add() to add elements. It does not
    # allow for duplicates. Just need to define a Point class and an __eq__
    # method so that elements can be compared by the set

    # Memoization was overcountaing something... need to investigate why.
    # Difference was between 557 and 640.

    def correct_indices(self, i, j):
        return i >= 0 and i < self.n and j >= 0 and j < self.m

    def solve(self, i, j, curr, reached_nines):
        if self.arr[i][j] != curr:
            return reached_nines

        if curr == 9:
            reached_nines.add(Point(i, j))
            return reached_nines

        # if self.memoization[i][j] != None:
        #     return self.memoization[i][j]

        for d in range(4):
            new_i = i + self.DIR_X[d]
            new_j = j + self.DIR_Y[d]

            if self.correct_indices(new_i, new_j):
                k = set()
                s = self.solve(new_i, new_j, curr + 1, reached_nines)

                k = k.union(s)
                # if(self.memoization[i][j] == None):
                #     self.memoization[i][j] = s
                # else:
                #     self.memoization[i][j] = self.memoization[i][j].union(s)

        return k


    def init_solve(self):
        ans = 0

        for i in range(self.n):
            for j in range(self.m):
                if self.arr[i][j] == 0:
                    s = self.solve(i, j, 0, set())
                    print(i, j, s)
                    ans += len(s)

        return ans      

def main():
    f = open("./input.txt", "r")

    ans = 0

    topo_map = []
    n = None
    m = None

    for line in f:
        l = list(map(lambda x: int(x), line.strip()))
        topo_map.append(l)

        if m == None:
            m = len(l)

    if n == None:
        n = len(topo_map)

    print(n, m)
    s = Solver(n, m, topo_map)
    ans = s.init_solve()

    print(ans)

if __name__ == "__main__":
    main()