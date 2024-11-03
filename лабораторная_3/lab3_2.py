# функция find_common_participants
def find_common_participants(group_one, group_two, split=','):
    first_group = set(participants_first_group.split(split))
    second_group = set(participants_second_group.split(split))
    intersection_set = list(first_group.intersection(second_group))
    intersection_set.sort()
    print(f'{intersection_set[0]}, {intersection_set[1]}')


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# проверка функции с разделителем, отличным от запятой
find_common_participants(participants_first_group, participants_second_group, '|')
