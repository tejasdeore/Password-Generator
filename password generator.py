import random
#importing random module to genrate pseudo random variable

lower = "abcdefghijklmnopqrstuvwxyz"
#alphabets in lower case

upper = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
#alphabets in upper case

numbers = "0123456789"

symbols = "<>?{}[]_-*()^$@"

all = lower+upper+numbers+symbols

#all- concatenation of four variables
length = 15

#lenth of the password is set to 15 
password =" ".join(random.sample(all,length))
#join - inbuilt func perform joining 
#sample - is inbuilt func of random module returns randomly selected values according to specified numbers(length)
print("RANDOM PASSWORD: \n",password)