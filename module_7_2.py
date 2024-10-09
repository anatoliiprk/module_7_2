print('------\nЗадача "Записать и запомнить"\n------')

def custom_write(file_name, string: list):
    file = open(file_name, 'a+', encoding='utf-8')
    string_positions = {}
    for i in range(len(string)):
        position = file.tell()
        file.write(f'{string[i]}\n')
        string_positions[i, position] = string[i]
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

print('------')