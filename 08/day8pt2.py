import numpy as np



class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.network_num = 0
        self.connections = []

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}) Network: {self.network_num}"
    

    def connect(self, new_box):

        # If a new network, assign network num
        if new_box.network_num == 0 and self.network_num == 0:
            self.network_num = get_unique_network_num()
            new_box.network_num = self.network_num

        # if new box has no network, but this box does, add to existing
        elif new_box.network_num == 0 and self.network_num > 0:
            new_box.network_num = self.network_num

        # if new box is in a network but this box is not, add to existing
        elif new_box.network_num > 0 and self.network_num == 0:
            self.network_num = new_box.network_num

        # Convert network to lower numbered network if both in networks
        elif new_box.network_num < self.network_num:
            self.convert_network(new_box.network_num)
        elif new_box.network_num > self.network_num:
            new_box.convert_network(self.network_num)
        else:
            return False
        
        # If now connected, add to connections list
        new_box.connections.append(self)
        self.connections.append(new_box)

        return True

    # recursively converts all boxes on a network to the new network. Too slow?
    def convert_network(self, new_network):
        if new_network != self.network_num:
            self.network_num = new_network
            for connection in self.connections:
                connection.convert_network(new_network)
                connection.network_num = new_network

            

next_network_num = 0
def get_unique_network_num():
    global next_network_num
    next_network_num += 1
    return next_network_num


def calculate_distance(box1, box2):
    return ((box1.x - box2.x)**2 + (box1.y - box2.y)**2 + (box1.z - box2.z)**2)**(1/2)




def main():
    in_file = open("08/input.txt", "r")

    boxes = []

    # Arrange data into array of box objects
    for line in in_file:
        x, y, z = line.split(',')
        boxes.append(Box(int(x), int(y), int(z)))

    # Calculate distances between all boxes
    distances = []
    completed = 0
    for box1 in boxes:
        distance_row = []
        for _ in range(completed):
            distance_row.append(0)
        for box2 in boxes[completed:]:
            distance_row.append(calculate_distance(box1, box2))
        distances.append(distance_row)
        completed += 1

    # Convert to nunpy array for functions
    numpy_distances = np.array(distances)

    # Connect all but the last 2 boxes
    keep_going = True
    while keep_going:
        # find minimum non-zero distance
        minx, miny = find_min_distance(numpy_distances)
        box1 = boxes[minx]
        box2 = boxes[miny]
        box1.connect(box2)
        numpy_distances[minx][miny] = 0

        # Determine number of boxes in each network
        global next_network_num
        networks = [0] * max((next_network_num + 1), 3)

        # Count how many boxes are in each network. Slow idea, but whatever
        for box in boxes:
            networks[box.network_num] += 1
        if ((networks[0] == 1) and (len([x for x in networks[1:] if x != 0]) == 1)) \
            or ((networks[0] == 0) and (len([x for x in networks[1:] if x != 0]) == 2)):
            keep_going = False



    lastx, lasty = find_min_distance(numpy_distances)
    box1 = boxes[lastx]
    box2 = boxes[lasty]

    while box1.network_num == box2.network_num:
        lastx, lasty = find_min_distance(numpy_distances)
        box1 = boxes[lastx]
        box2 = boxes[lasty]
        numpy_distances[lastx][lasty] = 0

    print(box1, box2)
    print(f"Distance = {box1.x * box2.x}")


def find_min_distance(distances):
    min_val = np.min(distances[np.nonzero(distances)])
    where = np.where(distances == min_val)
    minx = where[0][0]
    miny = where[1][0]
    return minx, miny

if __name__ == "__main__":
    main()