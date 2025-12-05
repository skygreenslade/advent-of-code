
import os



class Lock:
    def __init__(self, starting_value):
        self.value = starting_value
        self.zeros = 0


    def left(self, to_rotate):
        # Rotate left
        new_value = self.value - to_rotate

        # Handle negative rollover
        while new_value < 0:
            new_value += 100

        # Add zero if hit
        if new_value == 0:
            self.zeros += 1

        #update value
        self.value = new_value


        
    def right(self, to_rotate):
        # Rotate right and handle rollover
        new_value = (self.value + to_rotate) % 100

        # Add zero if hit
        if new_value == 0:
            self.zeros += 1

        self.value = new_value

def main():
    lock = Lock(50)
    
    in_file = open("day_1_input.txt", "r")
    for line in in_file:
        rotation = int(line[1:])
        if line[0] == 'R':
            lock.right(rotation)
        elif line[0] == 'L':
            lock.left(rotation)
        else:
            print(line)
            raise Exception("Invalid argument") 
        
    print(f"Zeros: {lock.zeros}")
    




if __name__ == "__main__":
    main()



