class CountSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.pointsXByY = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pointsCount[(x, y)] += 1
        self.pointsXByY[y].add(x)

    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0

        for x2 in self.pointsXByY[y]:
            if x2 == x:
                continue

            d = x - x2
            result += self.pointsCount[(x2, y)] * self.pointsCount[(x2, y + d)] * self.pointsCount[(x, y + d)]
            result += self.pointsCount[(x2, y)] * self.pointsCount[(x2, y - d)] * self.pointsCount[(x, y - d)]

        return result

