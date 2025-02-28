import threading
import time

def longSquare(num, results):
    time.sleep(2)
    print(num**2)
    results[num] = num ** 2
    return num**2


# for n in range(10):
#     longSquare(n)

# print([longSquare(n) for n in range(10)])

# t1 = threading.Thread(target=longSquare, args=(1,))
# t2 = threading.Thread(target=longSquare, args=(2,))
# t3 = threading.Thread(target=longSquare, args=(3,))

# t1.start()
# t2.start()
# t3.start()


# t1.join()
# t2.join()
# t3.join()

results = {}
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(10)]

for t in threads:
    t.start()


# for t in threads:
#     t.join()

[t.join() for t in threads]

# print([longSquare(n, results) for n in range(10)])

# print([longSquare(n, results) for n in range(10)])

print(results)
