# import copy
#
# with open('day8_input.txt') as f:
#     data = [x.strip() for x in f.readlines()]
#
# dataDict = { key : value for key,value in enumerate(data)}
#
# setOperation = set(dataDict.keys())
# accumulator = 0
# key = 0
# try:
#     while True:
#         setOperation.remove(key) # remove operation ID from list of available op
#         current_op = dataDict[key]
#         if "nop" in current_op:
#             key += 1
#         elif "acc" in current_op:
#             accumulator += int(dataDict[key].split()[1])
#             key +=1
#         elif "jmp" in current_op:
#             key += int(dataDict[key].split()[1])
# except KeyError:
#     print(f"accumulator is equal to {accumulator}")
#
# #-------
# # Part2
# # create a generator of all possible configuration with a single change of nop or jmp
# conf_change = (i for i, x in enumerate(list(dataDict.values())) if x.split()[0] in ('nop', 'jmp'))
# for i in conf_change:
#     # create a new dictionary with amended instruction
#     op, arg = dataDict[i].split()
#     new_listofinstruction = copy.deepcopy(dataDict)
#     if op == 'jmp':
#         new_listofinstruction[i] = 'nop' + ' ' + arg
#     else:
#         new_listofinstruction[i] = 'jmp' + ' ' + arg
#     setOperation = set(new_listofinstruction.keys())
#     accumulator = 0
#     key = 0
#     solution = False
#     try:
#         while True:
#             setOperation.remove(key) # remove operation ID from list of available op
#             current_op = new_listofinstruction[key]
#             if key == len(new_listofinstruction):
#                 solution = True
#                 break
#             if "nop" in current_op:
#                 key += 1
#             elif "acc" in current_op:
#                 accumulator += int(new_listofinstruction[key].split()[1])
#                 key +=1
#             elif "jmp" in current_op:
#                 key += int(new_listofinstruction[key].split()[1])
#     except KeyError:
#         print(f"not the correct configuration")
#     if solution:
#             break
#
# print(accumulator)


with open('day8_input.txt') as f:
    ws = [line.strip().split() for line in f.readlines()]

instructions = [w[0] for w in ws]
values = [int(w[1]) for w in ws]


def run(insts, values):
    i = 0
    seen = set()
    acc = 0
    while True:
        # Part one
        if i in seen:
            return (False, acc)
        # Part two
        elif i == len(ws):
            return (True, acc)
        seen.add(i)
        inst = insts[i]
        value = values[i]
        if inst == 'acc':
            acc += value
        if inst == 'jmp':
            i += value
        else:
            i += 1


# Part one
_, acc = run(instructions, values)
print(acc)

# Part two
to_change = (i for i, x in enumerate(instructions) if x in ('nop', 'jmp'))
for i in to_change:
    new_instructions = list(instructions)
    new_instructions[i] = 'jmp' if instructions[i] == 'nop' else 'nop'
    halts, acc = run(new_instructions, values)
    if halts:
        break
print(acc)
