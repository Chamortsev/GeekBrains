import os
try:
    with open('config.yaml') as f:
        lines = f.read().splitlines()
        for line in lines:
          key,value = line.split(':')
          if key.endswith('dir'):
              if key == 'home_dir':
                  home_dir = value
                  if not os.path.exists(value):
                      os.mkdir(home_dir)
              else:
                  if not os.path.exists(home_dir + '/' + value):
                      os.makedirs(home_dir + '/' + value)
          else:
              if key.endswith('settings'):
                value=str(value).split(',')
                for i in value:
                    with open(home_dir+'/settings/'+ i, 'w') as f:
                        f.write(' ')
              if key.endswith('mainapp'):
                  value = str(value).split(',')
                  for i in value:
                      with open(home_dir + '/mainapp/' + i, 'w') as f:
                          f.write(' ')
              if key.endswith('authapp'):
                  value = str(value).split(',')
                  for i in value:
                      with open(home_dir + '/authapp/' + i, 'w') as f:
                          f.write(' ')
              if key.endswith('mainapp_tm'):
                  value = str(value).split(',')
                  for i in value:
                      with open(home_dir + '/mainapp/templates/mainapp/' + i, 'w') as f:
                          f.write(' ')
              if key.endswith('authapp_tm'):
                  value = str(value).split(',')
                  for i in value:
                      with open(home_dir + '/authapp/templates/mainapp/' + i, 'w') as f:
                          f.write(' ')
except FileNotFoundError:
     print("Файл не найден")
