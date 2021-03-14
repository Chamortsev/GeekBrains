import shutil

root = 'my_project'
authapp = 'authapp/templates'
value = 'templates'
mainapp = 'mainapp/templates'


def cop_tree(dir_name):
    try:
        shutil.copytree(root + '/' + dir_name, root + '/' + value + '/' + dir_name)
        print('Каталог успешно создан', root + '/' + value + '/' + dir_name)
    except FileExistsError:
        print('Каталог уже существует', root + '/' + value + '/' + dir_name)


cop_tree(authapp)
cop_tree(mainapp)
