def generate_court_header(case_data):
    # Данные истца (вашей компании)
    plaintiff_name = "Чичиков Павел Иванович"
    plaintiff_inn = "123456789012"
    plaintiff_ogrn = "987654321012345"
    plaintiff_address = "ул. Примерная, д. 123, кв. 45"

    # Получаем данные по ответчику из переданного словаря
    defendant_name = case_data.get("defendant_name", "")
    defendant_inn = case_data.get("defendant_inn", "")
    defendant_ogrn = case_data.get("defendant_ogrn", "")
    defendant_address = case_data.get("defendant_address", "")

    # Номер дела
    case_number = case_data.get("case_number", "")

    # Шаблон для генерации текста
    court_header = f"""
В арбитражный суд города Москвы
Адрес: 115225, г. Москва, ул. Б. Тульская, 17

Истец: {plaintiff_name}
ИНН {plaintiff_inn} ОГРНИП {plaintiff_ogrn}
Адрес: {plaintiff_address}

Ответчик: {defendant_name}
ИНН {defendant_inn} ОГРН {defendant_ogrn}
Адрес: {defendant_address}
Номер дела {case_number}
    """

    return court_header


# Пример использования функции с данными по ответчику в виде словаря
case_data = {
    "defendant_name": "ООО “Некрономикон Лтд.”",
    "defendant_inn": "987654321098",
    "defendant_ogrn": "012345678901234",
    "defendant_address": "123534, г. Чертаново,  ул. Тёмная, д. 666, офис 13",
    "case_number": "A40-24022022/2023"
}

result = generate_court_header(case_data)
print(result)


def generate_court_headers(case_data_list):
    for case_data in case_data_list:
        # Вызываем первую функцию для генерации шапки
        court_header = generate_court_header(case_data)

        # Выводим результат в консоль
        print(court_header)
        print("=" * 50)  # Добавим разделитель для наглядности


# Пример использования второй функции с списком словарей
case_data_list = [
    {
        "defendant_name": "ООО “Кооператив Озеро”",
        "defendant_inn": "1231231231",
        "defendant_ogrn": "123124129312941",
        "defendant_address": "123534, г. Москва, ул. Красивых молдавских партизан, 69",
        "case_number": "A40-123456/2023"
    },
    {
        "defendant_name": "ООО “Некрономикон Лтд.”",
        "defendant_inn": "987654321098",
        "defendant_ogrn": "012345678901234",
        "defendant_address": "123534, г. Чертаново,  ул. Тёмная, д. 666, офис 13",
        "case_number": "A40-24022022/2023"
    }
]

generate_court_headers(case_data_list)
