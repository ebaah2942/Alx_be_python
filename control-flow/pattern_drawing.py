pattern_size = int(input("Enter the size of the pattern: "))
row = 0

while row < pattern_size:
    for _ in range(pattern_size):
        print("*", end="")
    print()
    row += 1
    
