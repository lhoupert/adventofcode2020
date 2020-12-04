
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
