# Jerry Abril and Roderick Zak
# 2017

from copy import copy

def main(start_word, end_word):
 f = open('words.txt')
 d = {}
 q = [start_word]
 letters = 'abcdefghijklmnopqrstuvwxyz' 
    
 for line in f:
  if len(line) == len(start_word)+1:
   line = line.strip ()
   for i in start_word:
    d[line] = start_word
                
 while len(q): 
  path = q[0]
  q.pop(0)
        
  if end_word == path: 
   print d[path] + "! Best path found!"
  for x in letters:
   for y in range(len(start_word)):  
    if path[y] != x:              
     temp = list(path)           
     temp[y] = x              
     alternative = str(''.join(temp))    
    if alternative in d and d[alternative] == start_word:
     q.append(alternative)
     d[alternative] = d[path] + '\n -> ' + alternative

if __name__=='__main__':
    main('snakes', 'brains')