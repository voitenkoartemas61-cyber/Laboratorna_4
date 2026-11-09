from stats_lib import is_sorted, mean, index_of_max, above_mean

def main():
    print("--- Програма для роботи зі статистикою чисел ---")
    raw_input = input("Введіть числа через пробіл (наприклад: 4 1 8 2): ")
    
    parts = raw_input.split()
    numbers = []
    for part in parts:
        numbers.append(float(part))
        
    if len(numbers) == 0:
        print("Ви не ввели жодного числа.")
        return

    print(f"\nВаш список: {numbers}")
    
    if is_sorted(numbers):
        print("1. Список впорядкований за неспаданням.")
    else:
        print("1. Список НЕ впорядкований за неспаданням.")
        
    avg = mean(numbers)
    print(f"2. Середнє арифметичне: {avg}")
    
    max_idx = index_of_max(numbers)
    if max_idx is None:
        print("3. Список порожній, максимуму немає.")
    else:
        print(f"3. Індекс найбільшого елемента: {max_idx} (значення: {numbers[max_idx]})")
    
    higher = above_mean(numbers)
    print(f"4. Елементи, що більші за середнє: {higher}")

if __name__ == "__main__":
    main()
