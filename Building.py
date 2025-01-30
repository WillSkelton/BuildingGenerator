class Building:
    def __init__(self):
        self.counter = 0
        self.PointLookup = {}
        self.ConnectionMatrix = []

    def addPoint(self, point: tuple[int, int, int]):
        stringified = f"({point[0]},{point[1]},{point[2]})"
        self.PointLookup[stringified] = self.counter
        self.counter = self.counter + 1

    def printMatrix(self):
        print(self.PointLookup)
