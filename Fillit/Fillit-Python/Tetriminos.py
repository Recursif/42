

class Tetriminos(object):
    """Object tetriminos.

    Parameters
    ----------
    t_str : string
        String representing the tetriminos.

    authorized_char : 2-uplet
        Character authorized.

    size : 2-uplet
        Size of the tetriminos.

    Attribute
    ----------
    pattern : 2d-array
        2d-array representing the tetriminos.

    """

    def __init__(self, t_str, authorized_char=('0','#') , size=(4, 4)):
        self.t_str = t_str
        self.authorized_char = authorized_char
        self.size = size
        self.pattern = []
        if (self.is_valid_tetriminos()):
            self.convert_to_pattern()

    def convert_to_pattern(self):
        """Convert the t_str in a 2d-array."""
        for j in range(0, self.size[1] - 1):
            for i in range(0, self.size[0] - 1)
                pattern[j].append(t_str[i + j * (self.size[0] + 1)])

    def is_cube_have_a_neighbors(self, x, y):
        """Check if the cube at position (x , y) have a neighbors."""
        X = [x - 1, x + 1, x, x]
        Y = [y, y, y - 1, y + 1]
        for i, j in zip(X, Y):
            if (0 =< i and 0 =< j and i < self.size[0] and j < self.size[1]):
                if (self.t_str[i + self.size[0] * j] == authorized_char[1]):
                    return (1)
        return (0)

    def is_valid_tetriminos(self):
        """Check if the t_str represent a valid tetriminos."""
        row = 0
        col = 0
        for i in range(len(t_str)):
            if (i == authorized_char[0]):
                col += 1
            elif (i == authorized_char[1]):
                if (not(is_cube_have_a_neighbors(i, row))):
                    print("Invalid tetriminos!!")
                    return (0)
                col += 1
            elif (i == '\n'):
                if (!(col == size[0])):
                    print("Wrong number of column!")
                    return (0)
                row += 1
                col = 0
            else :
                print("Unauthorized character!")
                return (0)
        if ((col, row) == size)
            return (1)
        else :
            print("Bad size!")
            return (0)
