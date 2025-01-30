class ConnectionMatrix:
    def __init__(self):
        self.Matrix = []
        self.Points = {}

    def AddPoint(self, point: tuple[int, int, int]):
        stringified = stringified = f"({point[0]},{point[1]},{point[2]})"
        if (self.points[stringified] is True):
            return
        else:
            self.Points[stringified] = True
            # To Do: I need to find a way to maintain a 2d matrix of points
