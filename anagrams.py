# Anagrams
# Jerry Abril & Roderick Zak - 2017

f = open ("words.txt")

d = {}

comma = "," 

for line in f:
    line = line.strip () # Get rid of whitespace
    key = tuple(sorted(line)) # Turn word into a sorted tuple
    
    if key in d:
        anag = d.get(key) + ", " + line
        d[key] = anag
    else:
        d[key] = line
    
for key in d:
    if (comma in d[key]):
 
        print " [" + d[key] + "]"