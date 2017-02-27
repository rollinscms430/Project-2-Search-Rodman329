# Boogle
# Jerry Abril & Roderick Zak - 2017

from copy import copy

possible = {}
poss_positions = {}
nextMove = {}


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



def neighbors():
    nextMove = {position: [] for position in poss_position}
    for position in poss_position:
        moves =  [ [(row-1,column-1),(row-1,column),(row-1,column+1)],
				   [(row,column-1), (row,column+1)],
				   [(row+1,column-1),(row+1,column) ,(row+1,column+1)] ]
    for out in moves: 
	   if 0<= pos[1] < 4 and 0 <= pos [0] < 4:
	        result[moves].append(out)
    return nextMove


#if word in f:
 #   print word