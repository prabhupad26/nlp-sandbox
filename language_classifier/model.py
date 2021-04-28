class Node(object):
    def __repr__(self):
        return "{} at {}".format(
            type(self).__name__, hex(id(self)))


print(Node())
