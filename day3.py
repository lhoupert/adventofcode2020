import pandas as pd

# import day3_input.txt
df=pd.read_csv('day3_input.txt',header=None,names=['geology'])

# create a function that go will move the pointer accross the dataframe
# and change the character at the location of the pointer by a O if it is an open space
# or by a X if there is a tree

x_displacement = 3; # positive mean going right on the dataframe
y_displacement = 1; # positive mean going down in the dataframe

# print(df[:16])
# for i in range(0,9):
def tree_checker(df_original,x_displacement,y_displacement):
    df = df_original.copy()
    x_pos = 0; # initial position in the row of the dataframe (1st character)
    y_pos = 0; # initial position in the dataframe (1st row)
    while y_pos + y_displacement < df.size:
        # if new x position is outside the row start again from beginning
        if x_pos + x_displacement < len(df.geology[0]):
            x_pos_new = x_pos + x_displacement
        else:
            x_pos_new = x_pos + x_displacement - len(df.geology[0])

        y_pos_new = y_pos + y_displacement
        new_pos_geology = df.geology[y_pos_new][x_pos_new]
        geology_id = " "
        if new_pos_geology =='#':
            geology_id = "X"
        elif new_pos_geology =='.':
            geology_id = "O"
        else:
            print("problem: 'geology' is not defined. Should be '#' or '.'")
        new_geology_row = df.geology[y_pos_new][:x_pos_new] + geology_id + df.geology[y_pos_new][x_pos_new+1:]
        df.geology[y_pos_new] = new_geology_row
        x_pos = x_pos_new
        y_pos = y_pos_new

    tree_number = df.geology.str.count('X').sum()
    print("Number of trees for right {dx}, down {dy}: {tree} trees ".format(
            dx=x_displacement,
            dy=y_displacement,
            tree=tree_number)
)
    return tree_number

tree1=tree_checker(df,x_displacement,y_displacement)


#
# def check_valid_password(df):
#     # Define limit_low and limit_high
#     limit = df['policy_number'].str.split("-", n = 1, expand = True).apply(pd.to_numeric)
#     df['limit_low'] = limit[0]
#     df['limit_high'] = limit[1]
#     # Identify the row with valid passwords
#     index = []
#     for counter, row in enumerate(df.password):
#         # Extract the policy letter and remove the extra ':' at the end of the line
#         policy_letter = df.policy_letter[counter].replace(':','')
#         # Calculate the number of occurence
#         num_occurence = df.password[counter].count(policy_letter)
#         # Test if the number of occurence follow the policy limits:
#         if num_occurence >= df.limit_low[counter] and num_occurence <= df.limit_high[counter]:
#             index.append(counter)
#     return df.loc[index,:]
#
#
# filecols = ["policy_number","policy_letter","password"]
# df=pd.read_csv('day2_input.txt', sep=" ",
#             names=filecols)
#
# dfok=check_valid_password(df)
# print(dfok)
#
# # 2nd version of the problem:
# # Each policy actually describes two positions in the password, where 1 means
# # the first character, 2 means the second character, and so on.
# # (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
# # Exactly one of these positions must contain the given letter. Other occurrences
# # of the letter are irrelevant for the purposes of policy enforcement.
#
# def check_valid_password_2ndversion(df):
#     # Define limit_low and limit_high
#     limit = df['policy_number'].str.split("-", n = 1, expand = True).apply(pd.to_numeric)
#     df['first_position'] = limit[0]
#     df['second_position'] = limit[1]
#     # Identify the row with valid passwords
#     index = []
#     for counter, row in enumerate(df.password):
#         # Extract the policy letter and remove the extra ':' at the end of the line
#         policy_letter = df.policy_letter[counter].replace(':','')
#         # Extract position information
#         pos1 = df.first_position[counter];
#         pos2 = df.second_position[counter];
#         # Check if the specific character is in 1st or second position but not in both
#         cond1 = df.password[counter][pos1-1] == policy_letter
#         cond2 = df.password[counter][pos2-1] == policy_letter
#         bol = (cond1 or cond2) and not (cond1 and cond2)
#         # Test if the number of occurence follow the policy limits:
#         if bol:
#             index.append(counter)
#     return df.loc[index,:]
#
#
# filecols = ["policy_number","policy_letter","password"]
# df=pd.read_csv('day2_input.txt', sep=" ",
#             names=filecols)
#
# dfok=check_valid_password_2ndversion(df)
# print(dfok)
