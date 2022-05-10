# Foodgram
## Приложение «Продуктовый помощник»
[![Foodgram](https://github.com/Oorzhakau/foodgram-project-react/workflows/Foodgram-workflow/badge.svg?branch=master&event=push)](https://github.com/Oorzhakau/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

Cайт, на котором пользователи могут публиковать рецепты,
добавлять чужие рецепты в избранное и подписываться на публикации других авторов.
Сервис **«Список покупок»** позволит пользователям создавать список продуктов, которые
нужно купить для приготовления выбранных блюд.

## Описание проекта

### Главная страница
Содержимое главной страницы — список первых шести рецептов,
отсортированных по дате публикации (от новых к старым).
Остальные рецепты доступны на следующих страницах: внизу страницы есть пагинация.
### Страница рецепта
На странице — полное описание рецепта. Для авторизованных пользователей — 
возможность добавить рецепт в избранное и в список покупок, возможность
подписаться на автора рецепта.
### Страница пользователя
На странице — имя пользователя, все рецепты, опубликованные пользователем
и возможность подписаться на пользователя.

## Техническое описание проекта

К проекту по адресу http://localhost/api/docs/ подключена документация **API**.
В ней описаны возможные запросы к API и структура ожидаемых ответов.
Для каждого запроса указаны уровни прав доступа: пользовательские роли, которым разрешён запрос.

## Технологии:
* Python 3.7
* Django 2
* Docker
* Nginx
* Github Action

## Описание Workflow

Workflow состоит из четырёх шагов:
1. Проверка кода на соответствие PEP8;
2. Сборка и публикация образа на DockerHub;
3. Автоматический деплой на удаленный сервер;
4. Отправка telegram-ботом уведомления в чат.

## Установка:
1. Клонируйте репозиторий на локальную машину.
   ```https://github.com/Oorzhakau/foodgram-project-react.git```
2. Установите виртуальное окружение в папке проекта.
```
cd foodgram-project-react
python -m venv venv
```
3. Активируйте виртуальное окружение.
   ```source venv\Scripts\activate```
4. Установите зависимости.
```
python -m pip install --upgrade pip
pip install -r backend\requirements.txt
```
## Запуск проекта в контейнерах
1. Перейдите в директорию `infra/`, заполните файл .venv_example и после этого переименуйте его в .env
2. Выполните команду:
   ```docker-compose up -d --build```
3. Для остановки контейнеров из директории `infra/` выполните команду:
   ```docker-compose down -v```

## Deploy проекта на удаленный сервер
Предварительно для автоматического деплоя необходимо подготовить сервер:
1. Установить docker: ```sudo apt install docker.io```
2. Установите docker-compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
1. Скопируйте файлы docker-compose.yaml и nginx.conf из `infra` проекта на сервер в
home/<ваш_username>/docker-compose.yaml и home/<ваш_username>/nginx/default.conf соответственно.
```
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
```
4. В Secrets GitHub Actions форкнутого репозитория добавить переменные окружения:
   * SSH_KEY - ssh private key для доступа к удаленному серверу
   * HOST - public id хоста
   * USER - имя user-а на удаленном сервере
   * PASSPHRASE - пароль подтверждения подключения по ssh-key
   * DOCKER_USERNAME - username на DockerHub
   * DOCKER_PASSWORD - пароль на DockerHub
   * POSTGRES_USER - имя пользователя для базы данных
   * POSTGRES_PASSWORD - пароль для подключения к базе
   * DB_ENGINE - настойка подключения django-проекта к postgresql
   * DB_NAME - имя базы данных
   * DB_HOST - название сервиса (контейнера)
   * DB_PORT - порт для подключения к БД
   * DJANGO_SU_ADMIN - имя суперюзера в django-проекте
   * DJANGO_SU_EMAIL - почта суперюзера в django-проекте
   * DJANGO_SU_PASSWORD - пароль суперюзера в django-проекте
   * TELEGRAM_TOKEN - token telegram-бота
   * TELEGRAM_TO - id пользователя, которому будут приходить оповещения
об успешном деплои

## Ссылка на проект
Проект развернут по адресу http://51.250.29.63/

## Автор:
[Александр Ооржак](https://github.com/Oorzhakau)
