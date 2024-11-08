# функция find_common_participants
def find_common_participants(group_one, group_two, split=','):
    first_group = set(group_one.split(split))
    second_group = set(group_two.split(split))
    intersection_set = list(first_group.intersection(second_group))
    intersection_set.sort()
    return intersection_set


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# проверка функции с разделителем, отличным от запятой
intersection_set = find_common_participants(participants_first_group, participants_second_group, '|')
print(f'{intersection_set}')
