def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total = 0
        count = 0

        for line in lines:
            try:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
            except ValueError:
                continue

        if count == 0:
            return (0, 0)

        average = total / count
        if average.is_integer():
            average = int(average)
        return (total, average)

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
