from itertools import product, tee
def pairwise(iterable):
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Cuboid:

    __slots__ = '__x1', '__y1', '__z1', '__x2', '__y2', '__z2'

    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.__setstate__((min(x1, x2), min(y1, y2), min(z1, z2), max(x1, x2), max(y1, y2), max(z1, z2)))

    def __repr__(self):
        return '{}({})'.format(type(self).__name__, ', '.join(map(repr, self)))

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __hash__(self):
        return hash(self.data)

    def __len__(self):
        return 6

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __and__(self, other):
        x1, y1, z1, x2, y2, z2 = max(self.x1, other.x1), max(self.y1, other.y1), max(self.z1, other.z1), \
                                 min(self.x2, other.x2), min(self.y2, other.y2), min(self.z2, other.z2)
        if x1 < x2 and y1 < y2 and z1 < z2:
            return type(self)(x1, y1, z1, x2, y2, z2)

    def __sub__(self, other):
        intersection = self & other
        if intersection is None:
            yield self
        else:
            x, y, z = {self.x1, self.x2}, {self.y1, self.y2}, {self.z1, self.z2}
            if self.x1 < other.x1 < self.x2:
                x.add(other.x1)
            if self.y1 < other.y1 < self.y2:
                y.add(other.y1)
            if self.z1 < other.z1 < self.z2:
                z.add(other.z1)
            if self.x1 < other.x2 < self.x2:
                x.add(other.x2)
            if self.y1 < other.y2 < self.y2:
                y.add(other.y2)
            if self.z1 < other.z2 < self.z2:
                z.add(other.z2)
            for (x1, x2), (y1, y2), (z1, z2) in product(pairwise(sorted(x)),
                                                        pairwise(sorted(y)),
                                                        pairwise(sorted(z))):
                instance = type(self)(x1, y1, z1, x2, y2, z2)
                if instance != intersection:
                    yield instance

    def __getstate__(self):
        return self.x1, self.y1, self.z1, self.x2, self.y2, self.z2

    def __setstate__(self, state):
        self.__x1, self.__y1, self.__z1, self.__x2, self.__y2, self.__z2 = state

    @property
    def x1(self):
        return self.__x1

    @property
    def y1(self):
        return self.__y1

    @property
    def z1(self):
        return self.__z1

    @property
    def x2(self):
        return self.__x2

    @property
    def y2(self):
        return self.__y2

    @property
    def z2(self):
        return self.__z2

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    @property
    def depth(self):
        return self.z2 - self.z1

    @property
    def volume(self):
        return self.width * self.height * self.depth

    intersection = __and__

    difference = __sub__

    data = property(__getstate__)

if __name__ == '__main__':
    A = Cuboid(0, 0, 0, 2, 2, 2)
    print(A, A.volume)
    B = Cuboid(1, 1, 1, 3, 3, 3)
    print(B, B.volume)
    print('A - B', list(A-B), sum(r.volume for r in A - B))
    print('B - A', list(B-A), sum(r.volume for r in B - A))