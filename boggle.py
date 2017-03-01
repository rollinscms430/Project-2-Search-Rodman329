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
    

def search(cell):
    global visited
    global word
    global found_words
    grid = generate_grid()
    visited.append(cell)
    valid_move_set = valid_moves(grid, cell[0], cell[1])
    word += loc(grid,cell[0],cell[1])
    print word
    print valid_move_set
    print visited
    loopval = len(valid_move_set)
    print loopval
    # if word is in dictionary, add word to found_words
    for i in range(loopval):
        print "vms V"
        print valid_move_set
        print "vms[i] V"
        print valid_move_set[i]
        if(valid_move_set[i] not in visited):
            print valid_move_set[i]
            search(valid_move_set[i])
        else:
            return word
        
    

def main():
    #queue.append(poss_positions[0,1])
    print search ([0,0])
    #print valid_moves(generate_grid(),3,1)
    
          

if __name__=='__main__':
    main()