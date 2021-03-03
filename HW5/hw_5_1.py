a=20

def nums_generator(max_num):
   for num in range(1, max_num + 1, 2):
       yield num

nums_gen = nums_generator(a)
try:
    for i in range(a):
        print(next(nums_gen))
except StopIteration:
    print('end')