
import copy

#----------------------------------------
# Part 1

def search(myDict, search1):
    keys=[]
    for key, value in myDict.items():
        if search1 in value:
            keys.append(key)
    return keys


luggage_rule={}
with open("day7_input.txt") as f:
    for line in f:
        line_list = line.split(' bags contain ')
        listofbags = []
        if 'no other' not in line_list[1]:
            for bag in line_list[1].split(','):
                bag_type = bag.lstrip(' ').split(' ')[1:-1]
                listofbags = listofbags + [' '.join(bag_type)]
        luggage_rule[line_list[0]]=listofbags
luggage_rule

container_bag = set(search(luggage_rule, 'shiny gold'))
all_container_bag =  copy.deepcopy(container_bag)
print(container_bag)
container_number = len(container_bag)

# Find all the container bag containing container bags
while len(container_bag)!=0:
    container_of_containers = set()
    for bag in container_bag:
        container_of_containers |= {*search(luggage_rule, bag)}
    # Make sure to not account the bag which have already been identified as
    # container bag
#    [container_of_containers.discard(x) for x in all_container_bag]
    container_of_containers -= all_container_bag
    all_container_bag |= container_of_containers
    print(container_of_containers)
    container_number += len(container_of_containers)
    container_bag = container_of_containers

print(container_number)

#-----------------------------------
# Part2

luggage_rule={}
with open("day7_input.txt") as f:
    for line in f:
        line_list = line.split(' bags contain ')
        listofbags = []
        if 'no other' not in line_list[1]:
            for bag in line_list[1].split(','):
                bag_type = bag.lstrip(' ').split(' ')[1:-1]
                number_of_bag = int(bag.lstrip(' ').split(' ')[0])
                listofbags = listofbags + [(number_of_bag,' '.join(bag_type))]
        luggage_rule[line_list[0]]=listofbags
luggage_rule

number_of_bag = 0;
def num_bag(color):
    return 1 + sum(count * num_bag(bag) for count, bag in luggage_rule[color])

num_bag('shiny gold') - 1 
