class Vacancy:
    def __init__(self, vacancy_id, name, city, url, salary_from, salary_to,
                 currency, published_at, requirement, responsibility):
        self.vacancy_id = vacancy_id
        self.name = name
        self.city = city
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.published_at = published_at
        self.requirement = requirement
        self.responsibility = responsibility

    def __repr__(self):
        return f'Vacancy(vacancy_id={self.vacancy_id},' \
               f'name={self.name} ' \
               f'city={self.city},' \
               f'url={self.url}, ' \
               f'salary={self.salary_from}-{self.salary_to},' \
               f'currency={self.currency},' \
               f'published_at={self.published_at} ' \
               f'requirement={self.requirement},' \
               f'responsibility={self.responsibility})'

    def __str__(self):
        salary = ""
        if self.salary_from and self.salary_to:
            salary = f"зарплата: от {self.salary_from} до {self.salary_to}"
        elif self.salary_from is None:
            salary = f"зарплата: до {self.salary_to}"
        elif self.salary_to is None:
            salary = f"зарплата: от {self.salary_from}"
        return f"vacancy_id: {self.vacancy_id}\n, " \
               f"профессия: {self.name}\n, " \
               f"город: {self.city}\n, " \
               f"ссылка: {self.url}\n, " \
               f"зарплата: {salary}\n, " \
               f"дата публикации: {self.published_at}\n, " \
               f"требования: {self.requirement}\n, " \
               f"обязанности: {self.responsibility}\n"

    def __gt__(self, other):
        return self.salary_from > other.salary_from