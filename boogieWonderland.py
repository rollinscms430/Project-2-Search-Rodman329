# Boogle
# Jerry Abril & Roderick Zak - 2017

from copy import copy

possible = {}
poss_positions = {}
neighbor = {}


f=open ("words.txt")
    
grid = [['u', 'n', 't', 'h'],
        ['g', 'a', 'e', 's'],
        ['s', 'r', 't', 'r'],
        ['h', 'm', 'i', 'a']]
             
letters='theungasmri'
d={}
blank = ''
for line in f:
    if line [0] in letters:
        if line [1] in letters or line [1] == blank:
            if line [2] in letters or line [2] == blank:
                line = line.strip()
                d[line] = line
    
for column in range (len(grid)):
    for row in range (len(grid)):
        position = tuple([row, column])
        poss_positions [position] = grid [row][column]    

print poss_positions

#print poss_positions [0,2]


def neighbors():
    for position in grid:
        moves =  [ [(row-1,column-1),(row-1,column),(row-1,column+1)],
				   [(row,column-1), (row,column+1)],
				   [(row+1,column-1),(row+1,column) ,(row+1,column+1)] ]