from stats_lib import is_sorted, mean, squares, index_of_max, above_mean

if __name__ == "__main__":
    # Перевірки для is_sorted
    assert is_sorted([1, 2, 3, 5]) == True
    assert is_sorted([1, 5, 3, 2]) == False
    assert is_sorted([]) == True
    assert is_sorted([7, 7, 7]) == True

    # Перевірки для mean
    assert mean([]) is None
    assert abs(mean([1, 2, 3, 4]) - 2.5) < 0.0001
    assert abs(mean([5, 5, 5]) - 5.0) < 0.0001

    # Перевірки для squares
    assert squares([1, 2, 3]) == [1, 4, 9]
    assert squares([]) == []
    assert squares([-2, 0]) == [4, 0]

    # Перевірки для index_of_max
    assert index_of_max([1, 5, 3, 5]) == 1
    assert index_of_max([]) is None
    assert index_of_max([-10, -5, -20]) == 1

    # Перевірки для above_mean
    assert above_mean([1, 2, 3, 4]) == [3, 4]
    assert above_mean([]) == []
    assert above_mean([5, 5, 5]) == []

    print("Усі перевірки пройдено успішно!")
