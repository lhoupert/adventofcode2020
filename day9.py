with open('day9_input.txt') as f:
     data = f.read().strip().split('\n')

values = [int(d) for d in data]
preamble_length = 25

# create a generator that yields list of defined length
def preamble_list(numlist, n):
    istart = 0
    while istart+n+1 < len(numlist):
        yield (numlist[(istart):(istart+n)],numlist[istart+n])
        istart += 1


for list,num_to_check in preamble_list(values,preamble_length):
    # Print all possible 2-element sum
    list_all_sums = [x+y for x in list for y in list if x!=y]
    if num_to_check not in list_all_sums:
#        print(list)
        invalid_num = num_to_check
        break

print(f"The invalid number is {invalid_num}\n")

# Part 2 - find a contiguous set of at least two numbers in your list
# which sum to the invalid number from step 1
def continuous_set(list, n):
    istart = 0
    while istart+n+1 < len(list):
        yield list[(istart):(istart+n)]
        istart += 1

# loop on different contiguous set length
for n in range(2,len(values)-2):
    for x in continuous_set(values,n):
        if sum(x)==invalid_num:
            print(f"Contiguous set of {n} elements:\n{x}\n")
            print(f"The encryption weakness is {min(x) + max(x)}")
            break
