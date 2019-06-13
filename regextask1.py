# check emails,phone numbers in the file
import re
file=open('regexdemo.txt','w')
str1='''the following are the gmails - 
bharathwatson@gmail.com
sameerjani1999hfbg_87@yahoo.com
doncheadle@hotmail.com
123345@gmail.com
bharath@rvrjc.ac.in
abc@bc
bharath@india
the following are the phone numbers - 
adam - 8464778899
even - 8657456857
english - 5775567578
'''
file.write(str1)
file.close()
file=open('regexdemo.txt','r')
#list1=[i for i in list(str(file) if re.findall('^[a-z0-9]\S.*@\S.*[.]com|[.]in$',i)]
list2=list(set([re.findall('\d\d\d\d\d\d\d\d\d\d',i) for i in file]))
#print(list1)
print(list2)
file.close()
