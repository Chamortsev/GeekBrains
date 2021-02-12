a = int(input())

def convert_sec(n):
    if (n % 60 < 10):
        return '0'+str(n % 60)+' сек'
    else:
        return str(n % 60)+' сек'

def convert_min(n):
    if (n // 60 % 60 < 10):
        return '0'+str(n // 60 % 60)+' мин ' + convert_sec(a)
    else:
        return str(n // 60 % 60) + ' мин ' + convert_sec(a)

def convert_hour(n):
    if (n // 3600 % 24 < 10):
        return '0'+str(n // 3600 % 24)+' час ' + convert_min(a)
    else:
        return str(n // 3600 % 24) + ' час ' + convert_min(a)

def convert_day(n):
    if (n >= 86400):
        return str(n // 86400)+' Дн '+ convert_hour(a)
    elif (3600 <= n < 86400):
        return  convert_hour(a)
    elif (60 <= n < 3600):
        return convert_min(a)
    else:
        return convert_sec(a)


print(convert_day(a))
