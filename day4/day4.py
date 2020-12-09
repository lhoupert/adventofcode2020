
# import day4_input.txt as a list of dictionary
d = {}
dictlist = [];
with open("day4_input.txt") as f:
    for line in f:
        if len(line.strip()) != 0:
             pairs = line.split()
             dline ={ pair.split(':')[0] : pair.split(':')[1] for pair in pairs}
             d={**d, **dline}
        else:
             dictlist.append(d)
             d = {}

len(dictlist)

# Reference keys:
refkeys = ('byr','iyr','eyr','hgt','hcl','ecl','pid')
optkey  = ('cid')

# Function to check if a key is present or no in a dictionary
def checkKey(dict, keylist):
    d={}
    for key in keylist:
        if key in dict:
            d = {**d, key:1}
        else:
            d = {**d, key:0}
    return d

# test checkKey
testd = {'byr':2000,'iyr':'2015','eyr':2028,'ecl':'brn','hcl':'#123abz'}
dd = checkKey(testd,refkeys)
sum(dd.values())

valid_passport = 0;
for d in dictlist:
    is_refkey = checkKey(d,refkeys)
    # consider valid if all 7 mandatory fields are present
    if sum(is_refkey.values()) == 7:
        valid_passport += 1

#==============================
## Part 2

# Create validation schema
from schema import Schema, And, Use, Regex, Optional, SchemaError

hcl_expr = "^#{1}[0-9a-f]{6}$" # https://regex101.com/r/g51QAR/1
hgt_expr = "^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$"
pid_expr = "^[0-9]{9}$"
ecl_list = ('amb','blu','brn','gry','grn','hzl','oth')

schema = Schema({'byr':  And(Use(int), lambda n: 1920 <= n <= 2002),
                  'iyr':  And(Use(int), lambda n: 2010 <= n <= 2020),
                  'eyr':  And(Use(int), lambda n: 2020 <= n <= 2030),
                  'hgt': And(str, Regex(hgt_expr)),
                  'hcl': And(str, Regex(hcl_expr)),
                  'ecl': And(str, lambda s: s in ecl_list),
                  'pid': And(str, Regex(pid_expr)),
                   Optional('cid'): And(str, len),
                   Optional('name'): And(str, len)
                   })

# Try on test dict
try:
    validated = schema.validate(testd)
    print("data validated")
except SchemaError as error:
    print(error)


# Run it on the data
valid_values = 0;
for d in dictlist:
    is_refkey = checkKey(d,refkeys)
    # consider valid if all 7 mandatory fields are present
    if sum(is_refkey.values()) == 7:
        try:
            validated = schema.validate(d)
            valid_values += 1
            sortd = { k : d[k] for k in refkeys}
            print(sortd)
            print("\n")
        except SchemaError as error:
            # print(error)
            # print("\n")
            pass

valid_values

# # Alternative solution (from reddit)
# # https://www.reddit.com/r/adventofcode/comments/k6e8sw/2020_day_04_solutions/gel2t0n/?context=3
#
# from helpers.utils import get_puzzle_input
# from jsonschema import validate, exceptions
#
# schema = {
#     "required": ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"],
#     "properties": {
#         "byr": {"type": "integer", "minimum": 1920, "maximum": 2002},
#         "iyr": {"type": "integer", "minimum": 2010, "maximum": 2020},
#         "eyr": {"type": "integer", "minimum": 2020, "maximum": 2030},
#         "hgt": {
#             "type": "string",
#             "pattern": "^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$",
#         },
#         "hcl": {"type": "string", "pattern": "^#[0-9a-f]{6}$"},
#         "ecl": {"type": "string", "pattern": "^(blu|amb|brn|gry|grn|hzl|oth)$"},
#         "pid": {"type": "string", "pattern": "^([0-9]{9})$"},
#     },
# }
#
# test_input = get_puzzle_input(4)
# part_1_valid_count = 0
# part_2_valid_count = 0
# passport_strings = test_input.split("\n\n")
# int_keys = {"byr", "iyr", "eyr"}
# for passport in passport_strings:
#     fields = {
#         k: (int(v) if k in int_keys else v)
#         for k, v in (e.split(":") for e in passport.split())
#     }
#     part_1_valid_count += set(schema["required"]).issubset(set(fields.keys()))
#     try:
#         validate(instance=fields, schema=schema)
#     except exceptions.ValidationError as err:
#         continue
#     part_2_valid_count += 1
# print(f"Valid passports part 1: {part_1_valid_count}")
# print(f"Valid passports part 2: {part_2_valid_count}")
