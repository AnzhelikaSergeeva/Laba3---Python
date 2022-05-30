import KMP
import BM
import time

n = input("Enter the string: ")
m = input("Enter something to find: ")

register_sensitive = input("Register sensitive: yes/no ")

algorithm = input('Choose the algorithm: KMP/BM ')

if register_sensitive == 'no':
    n = n.lower()
    m = m.lower()

start = time.time()

if algorithm == 'KMP':
    print(KMP.solution(n, m))
elif algorithm == 'BM':
    print(BM.solution(n, m))
else:
    print('No such algorithm')

finish = time.time() - start
print('%8.8f'%finish)

