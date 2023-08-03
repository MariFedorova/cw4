from classes.json import JSONSaver, JSONLoader
from classes.API import HHAPI, SJAPI
from src.utils import instance_vacancy_hh, instance_vacancy_sj, filter_vacancies, \
    sorted_data, instance_vacancy_sorted, \
    top_n_vacancies

hh_api = HHAPI()
superjob_api = SJAPI()
json_saver = JSONSaver()
json_loader = JSONLoader()


def user_interaction():
    # получаем список вакансий по запросу пользователя от API и создаем экземпляры класса
    search_query = input("Введите название профессии: ")
    hh_vacancy = hh_api.get_vacancies(search_query)
    list_instance_vacancy_hh = instance_vacancy_hh(hh_vacancy)
    sj_vacancy = superjob_api.get_vacancies(search_query)
    list_instance_vacancy_sj = instance_vacancy_sj(sj_vacancy)
    if len(list_instance_vacancy_hh) == 0 and len(list_instance_vacancy_sj) == 0:
        print("Введенная профессия не найдена")
        return
    # сохраняем список вакансий в файл json
    json_saver.add_vacancy(list_instance_vacancy_hh, list_instance_vacancy_sj)
    # фильтр вакансий по зарплате
    search_salary = int(input("Введите желаемую минимальную зарплату: "))
    salary_sorted = json_loader.get_vacancies_by_salary(search_salary)
    if len(salary_sorted) == 0:
        print("Нет вакансий, соответствующих заданным критериям")
        return
    # фильтруем список вакансий по ключевым словам пользователя
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(salary_sorted, filter_words)
    if len(filtered_vacancies) == 0:
        print("Нет таких вакансий")
        return
    # сортируем список вакансий по дате
    sort_data = sorted_data(filtered_vacancies)

    # создаем экземпляры классов после фильтров и сортировки
    list_instance_vacancy_sorted = instance_vacancy_sorted(sort_data)

    # вывод топ n вакансий
    top_n = int(input("Введите количество вакансий в топ n "))
    top_n_vacancies(list_instance_vacancy_sorted, top_n)

    # сохраняем список вакансий в json файл
    while True:
        save_json = input("Сохранить в json файл? [y/n] ")
        if save_json.lower() == "y":
            json_saver.save_json(list_instance_vacancy_sorted)
            break
        elif save_json.lower() == "n":
            print("Программа завершена")
            break
        else:
            print("Неверный ввод")


if __name__ == '__main__':
    user_interaction()
