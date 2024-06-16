# hackathon Backend

## Описание проекта

X-ray schedule - это веб-приложение, разработанное на Django DRF и React JS которое позволяет радиологам создавать расписания в условиях больших (и не очень) диагностических центров

## Установка и запуск проекта

### Требования

- Python 3.11 или выше
- pip (Python Package Installer)

### Шаги для установки

1. **Клонирование репозитория**

   Сначала клонируйте репозиторий на ваш локальный компьютер с помощью git.

   ```bash
   git clone https://github.com/hukumabob/doctors_schedule.git
   ```

2. **Создание виртуального окружения**

   Перейдите в каталог проекта и создайте виртуальное окружение Python с помощью команды:

   ```bash
   cd backend
   python -m venv venv
   ```

3. **Активация виртуального окружения**

   Активируйте виртуальное окружение с помощью следующей команды:

   - На Windows:

     ```bash
     . \venv\Scripts\activate
     ```

   - На Unix или MacOS:

     ```bash
     source venv/bin/activate
     ```

4. **Установка зависимостей**

   Установите все необходимые зависимости, указанные в файле `requirements.txt`, с помощью pip:

   ```bash
   pip install -r requirements.txt
   ```

5. **Инициализация базы данных**

   Примените все миграции Django для инициализации базы данных:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   и соберите статические файлы
   
   ```
   python manage.py collectstatic
   ```

   Создайте суперюзера:

   ```bash
   python manage.py createsuperuser
   ```

6. ** Заполняем БД первичными данными из директории data **
```
python manage.py generate_work_calendar
python manage.py generate_initial_modality
python manage.py generate_examinations_frequency
```
Вводим одно из предсказаний:
```
python manage.py generate_examinations_prognosis prophet
python manage.py generate_examinations_prognosis linear
python manage.py generate_examinations_prognosis arima
python manage.py generate_examinations_prognosis sarima
```
*** Для тренировки можем внести фейковых юзеров-докторов-рентгенологов ***
```
python manage.py generate_fake_users
python manage.py generate_fake_schedules
```