import operator
from datetime import datetime

from classes.vacancy import Vacancy


def instance_vacancy_hh(data):
    """ создает список вакансий HH.ru из экземпляров класса"""
    vacancy_list = []
    for item in data:
        vacancy = Vacancy(item["id"],
                          item["name"],
                          item["area"]["name"],
                          item["alternate_url"],
                          item["salary"]["from"],
                          item["salary"]["to"],
                          item["salary"]["currency"],
                          item["published_at"],
                          item["snippet"]["requirement"],
                          item["snippet"]["responsibility"])
        vacancy_list.append(vacancy)
    return vacancy_list


def instance_vacancy_sj(data):
    """ создает список вакансий SJ из экземпляров класса"""
    vacancy_list = []
    for item in data:
        vacancy = Vacancy(item["id"],
                          item["profession"],
                          item["town"]["title"],
                          item["link"],
                          item["payment_from"],
                          item["payment_to"],
                          item["currency"],
                          item["date_published"],
                          item["candidat"],
                          item["vacancyRichText"])
        vacancy_list.append(vacancy)
    return vacancy_list


def filter_vacancies(list_vacancies, filter_words):
    """ фильтрует по ключевым словам, введенным пользователем"""
    new_list = []
    for item in list_vacancies:
        for word in filter_words:
            if word.lower() in item["name"].lower():
                new_list.append(item)
                break
            elif item["requirement"] and item["responsibility"]:
                if word.lower() in item["requirement"].lower() or word.lower() in item["responsibility"].lower():
                    new_list.append(item)
                    break
    print(f"\nколичество вакансий после обработки фильтров: {len(new_list)}\n")
    return new_list


def sorted_data(list_vacancies):
    """ сортировка по дате """
    for item in list_vacancies:
        if 'superjob.ru' in item['url']:
            item['published_at'] = datetime.fromtimestamp(item['published_at'])
            item['published_at'] = item['published_at'].strftime('%d-%m-%Y %H:%M:%S')
            item['published_at'] = datetime.strptime(item['published_at'], '%d-%m-%Y %H:%M:%S')
        else:
            item['published_at'] = datetime.fromisoformat(item['published_at'])
            item['published_at'] = item['published_at'].strftime('%d-%m-%Y %H:%M:%S')
            item['published_at'] = datetime.strptime(item['published_at'], '%d-%m-%Y %H:%M:%S')
    sorted_list = sorted(list_vacancies, key=operator.itemgetter('published_at'), reverse=True)
    for item in sorted_list:
        item['published_at'] = item['published_at'].strftime('%d-%m-%Y %H:%M:%S')
    return sorted_list


def instance_vacancy_sorted(data):
    """ создание отсортированного списка"""
    new_list = []
    for item in data:
        vacancy = Vacancy(item["vacancy_id"],
                          item["name"],
                          item["city"],
                          item["url"],
                          item["salary_from"],
                          item["salary_to"],
                          item["currency"],
                          item["published_at"],
                          item["requirement"],
                          item["responsibility"])
        new_list.append(vacancy)
    return (new_list)


def top_n_vacancies(list_vacancies, n):
    """ выведение топа вакансий по значению, введенному пользователем"""
    counter = 1
    for item in list_vacancies:
        print(item)
        counter += 1
        if counter > n:
            break
