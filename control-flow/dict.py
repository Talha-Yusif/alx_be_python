import random
book=dict([('title','kill'),('author','prince'),('genre','dirge')])
print(book)
retrieve=book['genre']
print(retrieve)
import random
num=set()
for _ in range(5):
    num.add(random.randint(1,10))
print(num)