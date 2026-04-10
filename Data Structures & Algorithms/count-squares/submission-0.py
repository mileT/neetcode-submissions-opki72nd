class CountSquares:

    def __init__(self):
        self.point_count = defaultdict(int)
        self.x_by_y = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.point_count[(x, y)] += 1
        self.x_by_y[y].add(x)
        
    def count(self, point: List[int]) -> int:
        px, py = point
        result = 0

        for x2 in self.x_by_y[py]:
            if x2 == px:
                continue

            d = x2 - px
            result += (self.point_count[(x2, py)]
                        * self.point_count[(px, py + d)]
                        * self.point_count[(x2, py + d)])

            result += (self.point_count[(x2, py)]
                        * self.point_count[(px, py - d)]
                        * self.point_count[(x2, py - d)])

        return result
                
