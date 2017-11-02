import sys

sand = []
for sand_i in xrange(6):
    sand_temp = map(int, raw_input().strip().split(' '))
    sand.append(sand_temp)

total = -63
for sand_i in xrange(1, 5):
    for sand_j in xrange(1, 5):
        part = sand[sand_][sand_j]+sand[sand_i-1][sand_j-1] +\
               sand[sand_i-1][sand_j]+sand[sand_i-1][sand_j+1] +\
               sand[sand_i+1][sand_j-1]+sand[sand_i+1][sand_j] +\
               sand[sand_i+1][sand_j+1]
        if part > total:
            total = part

print total
