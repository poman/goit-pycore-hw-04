def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        cats_info = []

        for line in lines:
            try:
                cat_id, name, age = line.strip().split(',')
                cat_info = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_info)
            except ValueError:
                continue

        return cats_info

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
