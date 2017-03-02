# Boogle
# Jerry Abril & Roderick Zak - 2017

from copy import copy

dictionary = {}
prefix = {}
possible = {}
poss_positions = {}
letters=''
word=''
visited = []

def generate_words():
    global dictionary
    f=open ("attempt.txt")
    for line in f:
        line = line.strip()
        dictionary[line]=line
    return dictionary    
    
def generate_grid():
    grid = [['u', 'n', 't', 'h'],
            ['g', 'a', 'e', 's'],
            ['s', 'r', 't', 'r'],
            ['h', 'm', 'i', 'a']]
                 
    letters='theungasmri'
    return grid     
    
def generate_prefix():
    for line in generate_words():
        line = line.strip()
        pre = line [:2]
        if pre in prefix:
            prefix[pre].append(line)
        else:
            prefix[pre]=[line]
    return prefix
    
    
def loc(matrix, c, r):
    return matrix [c][r]

   
def valid_moves(matrix, c, r):
    valid_move_set=[]
    if( r == 0):
        if( c == 0):
            valid_move_set.append ([c+1, r])
            valid_move_set.append ([c+1, r+1])
            valid_move_set.append ([c, r+1])
        elif(c == 3):
            valid_move_set.append([c-1, r+1])
            valid_move_set.append([c-1, r])
            valid_move_set.append([c, r+1])
        else:
            valid_move_set.append([c+1,r])
            valid_move_set.append([c+1, r+1])
            valid_move_set.append([c-1,r])
            valid_move_set.append([c-1, r+1])
            valid_move_set.append([c, r+1])
    elif ( r == 3):
        if ( c == 0):
            valid_move_set.append ([c, r-1])
            valid_move_set.append ([c+1, r-1])
            valid_move_set.append ([c+1, r])
        elif (c == 3):
            valid_move_set.append ([c-1, r-1])
            valid_move_set.append ([c, r-1])
            valid_move_set.append ([c-1, r])
        else:
            valid_move_set.append([c+1,r])
            valid_move_set.append([c+1,r-1 ])
            valid_move_set.append([c-1,r])
            valid_move_set.append([c-1, r-1])
            valid_move_set.append([c, r-1])
    else:
        if(c == 0):
            valid_move_set.append([c+1,r])
            valid_move_set.append([c+1,r+1]) 
            valid_move_set.append([c+1,r-1])
            valid_move_set.append([c,r-1])
            valid_move_set.append([c,r+1])
        elif(c == 3):
            valid_move_set.append([c, r-1])
            valid_move_set.append([c-1, r-1])
            valid_move_set.append([c, r+1])
            valid_move_set.append([c-1, r+1])
            valid_move_set.append([c-1, r])
        else: 
            valid_move_set.append ([c,r+1])
            valid_move_set.append ([c,r-1])
            valid_move_set.append ([c-1,r+1])
            valid_move_set.append ([c-1,r-1])
            valid_move_set.append ([c-1,r])
            valid_move_set.append ([c+1,r-1])
            valid_move_set.append ([c+1,r])
            valid_move_set.append ([c+1,r+1])
    return valid_move_set
    

# recursive search method for a given cell value
# adds the given cell to a global list of visited cells
# generates all possible moves from that cell
# if there is a possible move which is not visited,
# call the search method on the cell corresponding to that move
# if there are no possible unvisited moves, 
# return the visited list as the word which has been constructed
def search(cell):
    global visited
    global found_words
    global word
    grid = generate_grid()
    visited.append(cell)
    valid_move_set = valid_moves(grid, cell[0], cell[1])
    print "valid moves for %d, %d are" % (cell[0], cell[1])
    print valid_move_set
    word += loc(grid,cell[0],cell[1])
    # print word
    # print valid_move_set
    # print visited
    loopval = len(valid_move_set)
    # if word is in dictionary, add word to found_words
    for i in range(len(valid_move_set)):
        more_moves = 0
        print "cell is "
        print cell
        if(valid_move_set[i] not in visited):
            print cell
            print "word is %s, valid move set is" % word
            print valid_move_set
            print valid_move_set[i]
            print "not in"
            print visited
            print "i ="
            print i
            print "calling search"
            more_moves = 1
            search(valid_move_set[i])
    if(more_moves == 0):
        print "moves exhausted, word is %s" % word
        print valid_move_set[i]
        print visited
        return word
        
    

def main():
    #queue.append(poss_positions[0,1])
    print search ([0,0])
    #print valid_moves(generate_grid(),3,1)
    
          

if __name__=='__main__':
    main()