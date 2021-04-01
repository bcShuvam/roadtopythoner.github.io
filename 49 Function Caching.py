import time
from functools import lru_cache

# @lru_cache(maxsize=3)
# def some_work(n):
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("Now running some work")
#     some_work(3)
#     print("Done... Calling again")
#     some_work(3)
#     some_work(2)
#     some_work(1)
#     some_work(4)
#     print("Calling again")

##############################################3
user = int(input("Enter number of cache : "))
@lru_cache(maxsize=user)
def delayer(n):
    time.sleep(n)
    return n

for i in range(user+5):
    print(f"This is cache {i}")
    delayer(2)
    i += 1

