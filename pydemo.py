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
print(list(file))
