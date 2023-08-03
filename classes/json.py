import json

from abc import ABC, abstractmethod


class TreatVacancy(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    def get_vacancies_by_salary(self, salary):
        pass

    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(TreatVacancy):
    def add_vacancy(self, vacancy, vacancy2):
        new_list = []
        counter = 0
        for item in vacancy:
            new_list.append(item.__dict__)
            counter += 1
        for item in vacancy2:
            new_list.append(item.__dict__)
            counter += 1
        with open("data_json/vacancy.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(new_list, indent=4, ensure_ascii=False))
        print(f"\nнайдено {counter} вакансий.\n")

    def save_json(self, list_vacancy):
        new_list = []
        for item in list_vacancy:
            new_list.append(item.__dict__)
        with open("data_json/vacancy.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(new_list, indent=4, ensure_ascii=False))
            print("все вакансии по запросу сохранены в файл")



class JSONLoader(TreatVacancy):
    def add_vacancy(self, vacancy):
        pass

    def get_vacancies_by_salary(self, salary):
        with open("data_json/vacancy.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        new_list = []
        for item in data:
            if item["salary_from"] is None:
                continue
            if item["currency"] == "RUR" or item["currency"] == "rub":
                if salary <= item["salary_from"]:
                    new_list.append(item)
        return new_list
