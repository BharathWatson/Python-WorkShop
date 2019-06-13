file=open('demofile.txt','a')
str1='''\nappending this text to the
current text data in the document 
using files in python programming lang.'''
file.write(str1)
file.close()
print('appended data to the file')