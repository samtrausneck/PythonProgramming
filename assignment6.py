# COT 4930 Python
# name: Sam Trausneck
# id: strausneck2013
# lab: 06


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class List:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        print("insert( '" + data.strip() + "')" + "\n")
        new_node = Node(data.strip())
        inserted = False

        if self.head is None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            if data < self.head.get_data():
                new_node.set_next(self.head)
                self.head = new_node
            else:
                cur = self.head
                while cur.get_next() is not None:
                    if (
                                new_node.get_data() < cur.get_next().get_data()):  # current node is less than next nodes data  => CHAINING
                        print("test")
                        after = cur.get_next()
                        cur.set_next(new_node)  # sets next = new_node
                        new_node.set_next(after)  # sets new nodes next to after "see pic"
                        break
                    cur = cur.get_next()
                if cur.get_next() is None:
                    cur.set_next(new_node)

    def print_list(self):
        print("print( )")
        cur = self.head
        while cur:
            print(str(id(cur)) + "  " + cur.get_data() + " " + str(id(cur.get_next())))
            cur = cur.get_next()
            if cur is None:
                print()

    def remove(self, data):
        print("remove( '" + data.strip() + "')" + "\n")
        # find the data in self
        cur = self.head
        # take of the case where data is in the head
        if self.head.get_data() == data:
            self.head = cur.get_next
        else:
            while cur.get_next() is not None:
                if cur.get_next().get_data() == data:
                    cur.set_next = cur.get_next().get_next()
                cur = cur.get_next()


def main():
    i_file = open("llist.txt", "r")
    myList = List()
    for line in i_file:
        line.lstrip(" ")
        command = line[0:1]
        if command == 'i':
            myList.insert(line[2:])
        elif command == 'p':
            myList.print_list()
        elif command == 'r':
            myList.remove(line[2:])
    i_file.close()


main()
