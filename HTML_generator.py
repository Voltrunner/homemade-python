# Этот скрипт формирует HTML страницу со
# ссылками на файлы, находящимися внутри
# выбранной директории.
# Сама страница после формирования кладется
# в эту же директорию. В файле будут
# использованы относительные пути
import os
initialdir = input('Введите имя и полный путь к каталогу\n')
if os.path.exists(initialdir) is False:
    print('Такой путь к каталогу не найден')
# Инициируем список для хранения найденных файлов
filelist = []
# запускаем полный обход файлов во всех вложенных каталогах
for root, dirs, files in os.walk(initialdir):
    for file in files:
        filelist.append(file)
# строки начальной разметки страницы
header = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html">
  <title>Content of directory</title>
 </head>
 <body>\n'''
titul = '<h1>' + initialdir + '</h1>\n'
footer = ''' </body>
</html>'''
with open(os.path.join(initialdir, 'content.html'), 'w') as content:
    content.write(header)
    content.write(titul)
    for file in filelist:
        content.write('<p><a href="' + file + '">' + file + '</a></p>\n')
    content.write(footer)
