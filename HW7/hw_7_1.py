import os

dir_name = 'my_project'
dirs = ('settings', 'mainapp', 'adminapp', 'authapp')

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

for i in dirs:
    if not os.path.exists(dir_name + '/' + i):
        os.mkdir(dir_name + '/' + i)
