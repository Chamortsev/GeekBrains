import sys

print(len(sys.argv))
if len(sys.argv) >= 3:
    user_file = sys.argv[1]
    hobby_file = sys.argv[2]
    dict_file = sys.argv[3]

else:
    user_file = 'users.csv'
    hobby_file = 'hobby.csv'
    dict_file = 'users_hobby.txt'

u = sum(1 for l in open(user_file, 'r'))
h = sum(1 for l in open(hobby_file, 'r'))
if u < h:
    exit(code=1)
else:
    with open(user_file) as f_users, open(hobby_file) as f_hobby:
        for line in f_users:
            user = line.strip()
            hobby = f_hobby.readline().strip()
            if hobby=='':
                hobby=None
            with open (dict_file, 'a', encoding='utf-8') as f:
                    f.write(str(user)+ ': '+ str(hobby)+'\n')