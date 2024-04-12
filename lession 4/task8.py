class Judge:
    def __init__(self, name, experience_years, specialization):
        self.name = name  # Имя судьи
        self.experience_years = experience_years  # Опыт работы судьи в годах
        self.specialization = specialization  # Специализация судьи
        self.cases_assigned = []  # Список дел, назначенных на рассмотрение
        self.self_count_cases_assigned = "doh**a" # Самостоятельно подсчитанное судьёй колличество дел

    def assign_case(self, case):
        """Назначить дело судье"""
        self.cases_assigned.append(case)

    def review_case(self, case):
        """Рассмотреть дело"""
        # В этом методе может быть логика рассмотрения дела, например, проведение слушаний и вынесение решения
        pass

    def retire(self):
        """Уход на пенсию"""
        # Метод, который будет вызываться при уходе судьи на пенсию
        pass

    def __str__(self):
        """Возвращает строковое представление судьи"""
        return f"Судья {self.name}, {self.experience_years} лет опыта, специализация: {self.specialization}"

    def self_count_cases_assigned(self):
        """Если спросить у судьи сколько дел в работе"""
        return self.self_count_cases_assigned
