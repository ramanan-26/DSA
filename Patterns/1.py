# Shri: Ranganyaki

def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ") 
        print()

def left_aligned_pyramid(n):
    for i in range(n):
        for j in range(n - i + 1):
            if i + j <= n - 1:
                print("*", end='')
            else:
                print(end=" ")
        print()

def binary_right_angle_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            if (i + j) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

def hollow_square_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end='')
            else:
                print(" ", end='')
        print()


# Run them
square_pattern(4)
left_aligned_pyramid(5)
binary_right_angle_triangle(5)
hollow_square_pattern(4)
