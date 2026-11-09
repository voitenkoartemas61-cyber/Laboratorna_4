def is_sorted(lst):
    """Повертає True, якщо список впорядкований за неспаданням, інакше False."""
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def mean(lst):
    """Повертає середнє арифметичне елементів списку або None, якщо список порожній."""
    if len(lst) == 0:
        return None
    
    total = 0
    for num in lst:
        total += num
    return total / len(lst)


def squares(lst):
    """Повертає новий список, що містить квадрати елементів переданого списку."""
    result = []
    for num in lst:
        result.append(num * num)
    return result


def index_of_max(lst):
    """Повертає індекс максимального елемента або None, якщо список порожній."""
    if len(lst) == 0:
        return None
    
    max_idx = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[max_idx]:
            max_idx = i
    return max_idx


def above_mean(lst):
    """Повертає новий список елементів, які більші за середнє значення (викликає mean)."""
    avg = mean(lst)
    if avg is None:
        return []
        
    result = []
    for num in lst:
        if num > avg:
            result.append(num)
    return result
