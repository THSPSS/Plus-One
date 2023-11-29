

# Solution 1
# split input by " "
a,b = input().split()
#add two String using int conversion
print(int(a) + int(b))


# Solution 2
#using map to convert input split string to int
a,b = map(input().split())
print(a+b)