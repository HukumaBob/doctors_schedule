### Заполняем БД первичными данными из директории data ###
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
### Для тренировки можем внести фейковых юзеров-докторов-рентгенологов ###
```
python manage.py generate_fake_users
python manage.py generate_fake_schedules
```


