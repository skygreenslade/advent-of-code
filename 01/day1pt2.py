
import os



class Lock:
    def __init__(self, starting_value):
        self.value = starting_value
        self.zeros = 0

        
    def rotate(self, to_rotate):
        # Rotate
        new_value = self.value + to_rotate

        # Full rotations
        passes = abs(new_value//100)
        self.zeros += passes

        # Mod new value to range 0-99
        new_value = new_value%100

        # Remove a zero if the dial was at 0 and went negative (double counted)
        if (self.value == 0) and to_rotate < 0:
            self.zeros -= 1

        # Add a zero if the dial was turned negatively to land on 0 (not counted otherwise)
        if (to_rotate < 0) and (new_value == 0):
            self.zeros+=1

         # Update value           
        self.value = new_value

def main():
    lock = Lock(50)
    
    in_file = open("day_1_input.txt", "r")
    for line in in_file:
        rotation = int(line[1:])
        if line[0] == 'R':
            lock.rotate(rotation)
        elif line[0] == 'L':
            lock.rotate(-rotation)
        else:
            print(line)
            raise Exception("Invalid argument") 
        
    print(f"Zeros: {lock.zeros}")
    




if __name__ == "__main__":
    main()



