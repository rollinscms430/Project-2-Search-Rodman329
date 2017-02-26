#Jerry Abril and Roderick Zak
#word_ladders
#2017

def wordLadders (start_word, end_word):
 f = open ("words.txt")
 path = []
 d = {}
 queue = [start_word]
 letters = 'abcdefghijklmnopqrstuvwxyz'
    
 for line in f:
  word = line [:-1]
  if len(word) == len (start_word):
   d[word] = word

 queue = [start_word]
 path.append(start_word)
 
 while len(queue):
  variable = queue [0]
  queue.pop (0)
  
 if variable == end_word:
  return path
 for x in range (len(start_word)):
  for y in letters:
   if variable[x] != y:
    nu = list (variable)
    nu[x] = y
    blah = str(''.join(nu))
    if blah[:len(variable)] in d:
     queue.append(blah)
     path.append(blah)
     print blah

print wordLadders('snakes', 'brains')