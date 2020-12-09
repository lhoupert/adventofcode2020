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
