import  random
lower = "abcdefghijklmnopqrstuvwxyz"
upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbol = "[~`!@#$%^&*()_+=-{\|;:'/?.><,}]"
all = lower + upper + number + symbol 
length = 20
password = "". join(random.sample(all, length))
print("The Password You Generated is: ", password)
