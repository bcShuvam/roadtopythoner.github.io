l1 = ["Bhindi","Aloo","Chopsticks","Mo:Mo","Chowmein"]

i = 1
for item in l1:
    if i%2 != 0:
        print(f"Jarvis please buy {item}")
    i+=1
print("")
for index,item in enumerate(l1):
    if index%2 == 0:
        print(f"Jarvis please buy {item}")