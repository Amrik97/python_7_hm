class Road:
    _length = 20
    _width = 5000
    weigh = 25
    num_m = 0.05

    def __init__(self, length, width, weigh, num_m):
        self._length = length
        self._width = width
        self.weigh = weigh
        self.num_m = num_m