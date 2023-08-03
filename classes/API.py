import requests
from abc import ABC, abstractmethod
import os

URL_HH = 'https://api.hh.ru/vacancies'
URL_SJ = 'https://api.superjob.ru/2.0/vacancies/'
SUPERJOB_API = "v3.r.137693077.1be4c5ca3276df7e216e968fdb6766cbafb1cb18.9a6d59398c153f8b23762af4f39ed7fe3fbebee8"


class VacancyAPI(ABC):

    """ абстрактный класс для работы с API"""
    @abstractmethod
    def get_vacancies(self, name):
        pass


class HHAPI(VacancyAPI):
    """ Класс для работы с HH.ru. Наследуется от абстрактного"""
    def get_vacancies(self, name):
        """ запрос к сайту HH по параметрам. Выводит до 100 страниц."""
        params = {
            'text': f'NAME:{name}',
            'page': 0,
            'per_page': 100,
            'only_with_salary': True
        }

        response = requests.get(URL_HH, params)
        data = response.json()['items']
        page_count = 1
        if len(data) == 100:
            while True:
                params["page"] = page_count
                response = requests.get(URL_HH, params)
                new_data = response.json()['items']
                data += new_data
                if len(new_data) == 100:
                    page_count += 1
                else:
                    break
        return data

class SJAPI(VacancyAPI):
    """ запрос к сайту SJ по параметрам.Передается ключ для работы с API- headers.  Выводит до 100 страниц."""
    def get_vacancies(self, name):
        headers = {'X-Api-App-Id': SUPERJOB_API}
        params = {
            'keywords': name,
            'page': 0,
            'count': 100,
            'no_agreement': 1
        }

        response = requests.get(URL_SJ, headers=headers, params=params)
        data = response.json()['objects']
        page_count = 1
        if len(data) == 100:
            while True:
                params["page"] = page_count
                response = requests.get(URL_SJ, headers=headers, params=params)
                new_data = response.json()['objects']
                data += new_data
                if len(new_data) == 100:
                    page_count += 1
                else:
                    break
        return data
