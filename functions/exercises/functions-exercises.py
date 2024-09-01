# Part 1 A -- Make a Line
def make_line(size):
    for num in range(size):
        return ("#"*size)
print(make_line(5))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size):
    square=""
    for num in range(size):
        square += "\n" + make_line(size)
    return square
print(make_square(4))

# Part 1 C -- Make a Rectangle
def make_rectangle(width,height):
    rectangle=""
    for num in range(height):
        rectangle += "\n"+make_line(width)
    return rectangle
print(make_rectangle(4,6))

# Part 2 A -- Make a Stairs
def make_downward_stairs(height):
    stair=""
    for num in range(height):
        stair += "\n"+make_line(num+1)
    return stair
print(make_downward_stairs(5))

# Part 2 B -- Make Space-Line 
def make_space_line(numSpaces, numChars):
    line=""
    line = "\n" + (" "*numSpaces) + make_line(numChars) + (" "*numSpaces)
    return line
print(make_space_line(3,5))

# Part 2 C -- Make Isosceles Triangle
def make_isosceles_triangle(height):
    isoTriangle=""
    for i in range(height):
        isoTriangle += make_space_line(height-i-1,2*i+1)
    return isoTriangle
print(make_isosceles_triangle(5))

# Part 3 -- Make a Diamond
def make_diamond(height):
    diamond=""
    for i in range(height):
        diamond += make_space_line(height-i-1,2*i+1)
    for index in range(height-1,-1,-1):
        diamond += make_space_line(height-index-1,2*index+1)
    return diamond
print(make_diamond(5))
