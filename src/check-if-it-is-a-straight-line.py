from collections import namedtuple

P = namedtuple('P', 'x y')

class Solution:
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    if len(set(x[0] for x in coordinates)) == 1: return True

    points = list(map(lambda x: P(*x), coordinates))

    a, b = points[:2]

    def get_validator(m, b):
      return lambda point: point.y == (m * point.x) + b

    validator = get_validator(
      *(lambda m: (m, b.y - (m * b.x)))((b.y - a.y) / (b.x - a.x) if b.x -
                                        a.x != 0 else 0)
    )

    return all(validator(point) for point in points)
