import re 
str1='from: the beginning: character'
y=re.findall('^f.+?:',str1) # *? non greedy
print(y)