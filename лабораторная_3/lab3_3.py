# функция count_letters
def count_letters(string):
    symb_dict = dict()
    for symbol in string.casefold():
        if symbol in symb_dict:
            symb_dict[symbol] += 1
        else:
            symb_dict[symbol] = 1
    not_letters = [' ', ',', '!', '—', ':', '.', '…', ';', '\n']
    for i in not_letters:
        del symb_dict[i]
    return symb_dict


# функция calculate_frequency
def calculate_frequency(symb_dict):
    summed_letters = sum(symb_dict.values())
    freq = dict()
    for letter, value in symb_dict.items():
        freq[letter] = round(value / summed_letters, 2)
    return freq


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
letters_count = count_letters(main_str)
letters_freq = calculate_frequency(letters_count)

for letter, value in letters_freq.items():
    print(f'{letter}: {value}')
