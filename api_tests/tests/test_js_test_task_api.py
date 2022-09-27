import allure
import requests
from hamcrest import assert_that, equal_to, has_key, is_not, empty, contains_string

from model.lenvendo import JsTestTask


@allure.feature("JsTestTask")
@allure.story("Фильтрация и сортировка по параметру")
def test_js_test_task_api_parameters(lenvendo_api):

    parameters = {"search": "Alcatel", "sort-field": "name"}
    with allure.step("Отправить запрос 'GET https://www.lenvendo.ru/api/js-test-task/?search=Alcatel&sort_field=name'"):
        resp = lenvendo_api.get_js_test_task(parameters)
        assert_that(resp.status_code, equal_to(requests.status_codes.codes.OK))

    with allure.step("Проверить, что ответ содержит элементы"):
        resp_json = resp.json()
        assert_that(resp_json, has_key("products"), "Ответ не содержит 'products'")
        assert_that(resp_json['products'], is_not(empty()), "'products' не содержит записей")

    js_test_task_objects = [JsTestTask.from_dict(product) for product in resp_json['products']]

    with allure.step(f"Проверить, что все элементы содержат {parameters['search']} в name"):
        for js_test_task_object in js_test_task_objects:
            assert_that(js_test_task_object.name, contains_string(parameters['search']),
                        f"{js_test_task_object.name} не содержит строку {parameters['search']}")

    with allure.step(f"Проверить, что все элементы отсортированы по {parameters['sort-field']} в алфавитном порядке"):
        assert_that(js_test_task_objects, equal_to(sorted(js_test_task_objects, key=lambda jt: jt.name)),
                    f"Элементы в ответе не отсортированы по полю {parameters['sort-field']}")