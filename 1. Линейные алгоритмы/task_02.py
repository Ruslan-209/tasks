# С клавиатуры вводится номер (позиция) буквы в английском алфавите. Вывести на экран запрашиваемый символ

position = int(input('Введите номер позиции: '))

first_symbol = ord('A')
position_number = first_symbol + position - 1
symbol = chr(position_number)

print(f'Это буква {symbol}')