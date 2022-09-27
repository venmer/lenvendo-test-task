# Тестовое задание - Lenvendo QA
Детали окружения:
- OS: Ubuntu 22.04.1 LTS
- Python 3.10.4
- Google Chrome Version 105.0.5195.102 (Official Build) (64-bit)
- allure-cli [2.19.0](https://github.com/allure-framework/allure2/releases/tag/2.19.0)

## UI тесты
Запуск тестов производился на Google Chrome Version 105.0.5195.102 (Official Build) (64-bit)

### Запуск тестов:
- Склонируйте репозиторий https://github.com/venmer/lenvendo-test-task.git
- Перейдите в директорию ```ui_tests```
- Создайте новое виртуальное окружение
```commandline
python -m venv venv
```
- Активируйте виртулальное окружение:
```commandline
source venv/bin/activate
```
- Установите необходимые библиотеки (файл ```requirements.txt```)
```commandline
pip install -r requirements.txt
```
- Подготовьте следующие параметры для запуска тестов:

| Параметр | Описание                         | Пример              |
|----------|----------------------------------|---------------------|
| BASE_URL | Основной URL адрес               | http://qa.digift.ru |
| USERNAME | Имя пользователя для авторизации | -                   |
| PASSWORD | Пароль пользователя              | -                   |

Параметры могут быть заданы как в переменных окружения, так и в строке запуска тестов:
```commandline
python -m pytest --alluredir report --base-url ${BASE_URL} --username ${USERNAME} --password ${PASSWORD} tests
```

## API тесты
### Запуск тестов:
- Склонируйте репозиторий https://github.com/venmer/lenvendo-test-task.git
- Перейдите в директорию ```api_tests```
- Создайте новое виртуальное окружение
```commandline
python -m venv venv
```
- Активируйте виртулальное окружение:
```commandline
source venv/bin/activate
```
- Установите необходимые библиотеки (файл ```requirements.txt```)
```commandline
pip install -r requirements.txt
```
- Подготовьте следующие параметры для запуска тестов:

| Параметр | Описание                         | Пример              |
|----------|----------------------------------|---------------------|
| BASE_URL | Основной URL адрес               | https://www.lenvendo.ru |

Параметры могут быть заданы как в переменных окружения, так и в строке запуска тестов:
```commandline
python -m pytest --alluredir report --base-url ${BASE_URL} tests
```
## Отчеты по запускам тестов
- Отчет по тестированию создается в директории ```report```
- Для просмотра отчета воспользуйтесь утилитой allure-cli:
```commandline
allure serve report
```