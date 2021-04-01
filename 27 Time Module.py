# import time
#
# initial = time.time()
# i = 0
# # 1605347442.597012
# # 1605347442.597012
# while i < 500:
#     print("While Loop")
#     # time.sleep(1)
#     i+=1
# print("While loop ran in",time.time() - initial ,"Seconds")
#
# initial2 = time.time()
# for i in range(500):
#     print("For Loop")
# print("For loop ran in",time.time() - initial2,"Seconds")
#
# local_time = time.asctime(time.localtime(time.time()))
#
# print("While loop ran in",time.time() - initial ,"Seconds")
# print("For loop ran in",time.time() - initial2,"Seconds")
#
# print(local_time)


import time

initial = time.time()
k = 0

while(k<500):
    print("This is Varun bhai")
    k +=1
print("\nWhile loop ran in ", time.time() - initial, "Seconds\n")

initial2 = time.time()

for i in range(500):
    print("This is Varun bhai")

print("\nWhile loop ran in ", time.time() - initial, "Seconds")
print("For loop ran in", time.time() - initial2, "Seconds")