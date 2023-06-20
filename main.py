file1 = 'checker.py'
file2 = 'xlsx.py'

# Запускаем первый файл
with open(file1) as f:
    code = compile(f.read(), file1, 'exec')
    exec(code)

# Запускаем второй файл
with open(file2) as f:
    code = compile(f.read(), file2, 'exec')
    exec(code)