import pandas as pd

def check_valid_password(df):
    # Define limit_low and limit_high
    limit = df['policy_number'].str.split("-", n = 1, expand = True).apply(pd.to_numeric)
    df['limit_low'] = limit[0]
    df['limit_high'] = limit[1]
    # Identify the row with valid passwords
    index = []
    for counter, row in enumerate(df.password):
        # Extract the policy letter and remove the extra ':' at the end of the line
        policy_letter = df.policy_letter[counter].replace(':','')
        # Calculate the number of occurence
        num_occurence = df.password[counter].count(policy_letter)
        # Test if the number of occurence follow the policy limits:
        if num_occurence >= df.limit_low[counter] and num_occurence <= df.limit_high[counter]:
            index.append(counter)
    return df.loc[index,:]


filecols = ["policy_number","policy_letter","password"]
df=pd.read_csv('day2_input.txt', sep=" ",
            names=filecols)

dfok=check_valid_password(df)
print(dfok)

# 2nd version of the problem:
# Each policy actually describes two positions in the password, where 1 means
# the first character, 2 means the second character, and so on.
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
# Exactly one of these positions must contain the given letter. Other occurrences
# of the letter are irrelevant for the purposes of policy enforcement.

def check_valid_password_2ndversion(df):
    # Define limit_low and limit_high
    limit = df['policy_number'].str.split("-", n = 1, expand = True).apply(pd.to_numeric)
    df['first_position'] = limit[0]
    df['second_position'] = limit[1]
    # Identify the row with valid passwords
    index = []
    for counter, row in enumerate(df.password):
        # Extract the policy letter and remove the extra ':' at the end of the line
        policy_letter = df.policy_letter[counter].replace(':','')
        # Extract position information
        pos1 = df.first_position[counter];
        pos2 = df.second_position[counter];
        # Check if the specific character is in 1st or second position but not in both
        cond1 = df.password[counter][pos1-1] == policy_letter
        cond2 = df.password[counter][pos2-1] == policy_letter
        bol = (cond1 or cond2) and not (cond1 and cond2)
        # Test if the number of occurence follow the policy limits:
        if bol:
            index.append(counter)
    return df.loc[index,:]


filecols = ["policy_number","policy_letter","password"]
df=pd.read_csv('day2_input.txt', sep=" ",
            names=filecols)

dfok=check_valid_password_2ndversion(df)
print(dfok)
