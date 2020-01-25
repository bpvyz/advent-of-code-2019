from collections import Counter

with open("input.txt") as f:
    s = f.read()
    lo, hi = [int(n) for n in s.split('-')]

def part1(num):
    bool = False
    for i in range(1, len(num)):
        if num[i] < num[i-1]:
            return False
        if num[i] == num[i-1]:
            bool = True
    return bool

def part2(num):
    a = Counter(num)
    if 2 in a.values():
        return True
    return False

nums = []

#
# part 1
#

for nr in range(lo, hi):
    if part1(str(nr)):
        nums.append(str(nr))
print("part 1: ",len(nums))

#
# part 2
#

cnt = 0

for nr in range(len(nums)):
    if part2(nums[nr]):
        cnt += 1
print("part 2: ",cnt)