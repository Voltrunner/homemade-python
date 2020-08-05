# Этот скрипт предназначен для массовой упаковки FB2 файлов
# внутри вложенных директорий. Скрипт обходит директории
# рекурсивно, находит несжатые FB2 файлы, сжимает их zip
# архиватором и переименовывает из zip снова в FB2 файлы.
# Уже сжатые файлы скрипт пропускает.
import os
import zipfile
# посчитаем обработанные файлы в этих переменных
fb2finded = 0
fb2compressed = 0
initialdir = input('Введите имя и полный путь к каталогу\n')
if os.path.exists(initialdir) is False:
    print('Такой путь к каталогу не найден')
# запускаем полный обход файлов во всех вложенных каталогах
for root, dirs, files in os.walk(initialdir):
    for file in files:
        # файл с полным путем, для удобства подстановки
        filepath = os.path.join(root, file)
        # если расширение fb2
        if file[-4:] == ('.fb2' or '.FB2'):
            fb2finded += 1
            # если это не уже пожатый в zip fb2
            if zipfile.is_zipfile(filepath) is False:
                # вот теперь жмем
                with zipfile.ZipFile(filepath + '.zip', 'w', zipfile.ZIP_DEFLATED) as newzip:
                    newzip.write(filepath, file)
                print(file)
                fb2compressed += 1
                # удаляем старый fb2
                os.remove(filepath)
                # переименовываем архив обратно в fb2
                os.rename(filepath + '.zip', filepath)
        else:
            continue
print('Всего файлов найдено:', fb2finded)
print('Всего сжато:', fb2compressed)
