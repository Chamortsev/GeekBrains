u = sum(1 for m in open('users.csv', 'r'))
h = sum(1 for s in open('hobby.csv', 'r'))
if u < h:
    exit(code=1)
else:
    with open("users.csv") as f_users, open("hobby.csv") as f_hobby:
        for line in f_users:
            user = line.strip()
            hobby = f_hobby.readline().rstrip()
            if hobby == '':
                hobby = None
            with open('users_hobby.txt', 'a', encoding='utf-8') as f:
                f.write(str(user) + ': ' + str(hobby) + '\n')
