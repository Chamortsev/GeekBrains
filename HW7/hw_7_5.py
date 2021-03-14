import os
from collections import defaultdict
from os.path import relpath

root_dir = 'C:/Users/chamorcev/PycharmProjects/GeekBrains/HW7'
my_files = defaultdict(list)
for root, dirs, files in os.walk(root_dir):
   for file in files:
       ext = file.rsplit('.', maxsplit=1)[-1].lower()
       rel_path = relpath(os.path.join(root, file), root_dir)
       my_files[ext].append(rel_path)

for ext, files in sorted(my_files.items(),
                        key=lambda x: len(x[1]), reverse=True):
   print(f'{ext}: {len(files)}')




#
# import os
# from os.path import getsize, join
#
# root_dir = 'C:/Users/chamorcev/PycharmProjects/GeekBrains/HW7'
#
#
# for root, dirs, files in os.walk(root_dir):
#     print(os.path.splitext(files) for name in files)
#
#
# s_10 = 0
# s_100 = 0
# s_1000 = 0
# s_10000 = 0
# s_100000 = 0
# s_1000000 = 0
# result={}
#
# for root, dirs, files in os.walk(root_dir):
#     total_size = sum(getsize(join(root, name)) for name in files)
#     if total_size<10:
#         s_10 =s_10+len(files)
#     if 10 <total_size< 100:
#         s_100=s_100+len(files)
#     if 100<total_size<1000:
#         s_1000=s_1000+len(files)
#     if 1000<total_size<10000:
#         s_10000=s_10000+len(files)
#     if 100000<total_size<100000:
#         s_100000=s_100000+len(files)
#
# result[10] = s_10
# result[100] = s_100
# result[1000] = s_1000
# result[10000] = s_10000
# result[100000] = s_100000
#
# print(result)
