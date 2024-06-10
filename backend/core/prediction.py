import pandas as pd
from datetime import timedelta
from django.db.models import F
import matplotlib.pyplot as plt
from prophet import Prophet
from prophet.plot import add_changepoints_to_plot
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

from django.conf import settings
from production_calendar.models import ExaminationSchedule, MedicalExamination

def prepare_data(start_date):
    # Get the data
    data = ExaminationSchedule.objects.filter(
        day__date__lt=start_date
        ).annotate(
            month=F('day__date__month'),
            year=F('day__date__year'),
            examination_code=F('examination__code')  # Get the code of the examination
            ).values(
                'month', 'year', 'examination_code', 'actual_count'
                )

    # Prepare the data
    X = [
        [item['month'], item['year'], item['examination_code']] for item in data if item['actual_count'] is not None
        ]
    y = [
        item['actual_count'] for item in data if item['actual_count'] is not None
        ]

    return X, y

def linear_regression(start_date, days_count):
    X, y = prepare_data(start_date)

    # One-hot encode the 'examination_code'
    encoder = OneHotEncoder() 
    X_encoded = encoder.fit_transform(X).toarray()

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Get all unique examinations
    examinations = MedicalExamination.objects.all()

    # Use the model to predict the future examinations for each examination
    for examination in examinations:
        for i in range(days_count):
            future_date = start_date + timedelta(days=i)
            future_examinations = model.predict(encoder.transform([[future_date.month, future_date.year, examination.code]]).toarray())

            # Update the database with the predicted values
            updated_rows = ExaminationSchedule.objects.filter(day__date=future_date, examination=examination).update(predicted_count=future_examinations)
            if updated_rows > 0:
                print(f"Updated predicted_count for {examination.code} on {future_date}")
            else:
                print(f"Failed to update predicted_count for {examination.code} on {future_date}")

def arima(start_date, days_count):
    # Get all unique examinations
    examinations = MedicalExamination.objects.all()

    # Use the model to predict the future examinations for each examination
    for examination in examinations:
        # Prepare the data for this examination
        data = ExaminationSchedule.objects.filter(
            day__date__lt=start_date,
            examination=examination  # Filter by examination
            ).annotate(
                month=F('day__date__month'),
                year=F('day__date__year'),
                examination_code=F('examination__code')  # Get the code of the examination
                ).values(
                    'month', 'year', 'examination_code', 'actual_count'
                    )

        X = [
            [item['month'], item['year'], item['examination_code']] for item in data if item['actual_count'] is not None
            ]
        y = [
            item['actual_count'] for item in data if item['actual_count'] is not None
            ]

        # Assuming 'y' is a time series data
        model = ARIMA(y, order=(5,1,0))  # Adjust the order parameters as per your data
        model_fit = model.fit()

        for i in range(days_count):
            future_date = start_date + timedelta(days=i)
            future_examinations = model_fit.forecast(steps=1)  # Adjust the steps as per your requirement

            # Update the database with the predicted values
            updated_rows = ExaminationSchedule.objects.filter(day__date=future_date, examination=examination).update(predicted_count=future_examinations)
            if updated_rows > 0:
                print(f"Updated predicted_count for {examination.code} on {future_date}")
            else:
                print(f"Failed to update predicted_count for {examination.code} on {future_date}")

def sarima(start_date, days_count):
    # Get all unique examinations
    examinations = MedicalExamination.objects.all()

    # Use the model to predict the future examinations for each examination
    for examination in examinations:
        # Prepare the data for this examination
        data = ExaminationSchedule.objects.filter(
            day__date__lt=start_date,
            examination=examination  # Filter by examination
            ).annotate(
                month=F('day__date__month'),
                year=F('day__date__year'),
                examination_code=F('examination__code')  # Get the code of the examination
                ).values(
                    'month', 'year', 'examination_code', 'actual_count'
                    )

        X = [
            [item['month'], item['year'], item['examination_code']] for item in data if item['actual_count'] is not None
            ]
        y = [
            item['actual_count'] for item in data if item['actual_count'] is not None
            ]

        # Assuming 'y' is a time series data
        model = SARIMAX(y, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))  # Adjust the order parameters as per your data
        model_fit = model.fit()

        for i in range(days_count):
            future_date = start_date + timedelta(days=i)
            future_examinations = model_fit.forecast(steps=1)  # Adjust the steps as per your requirement

            # Update the database with the predicted values
            updated_rows = ExaminationSchedule.objects.filter(day__date=future_date, examination=examination).update(predicted_count=future_examinations)
            if updated_rows > 0:
                print(f"Updated predicted_count for {examination.code} on {future_date}")
            else:
                print(f"Failed to update predicted_count for {examination.code} on {future_date}")


def prepare_data_prophet(start_date):
    # Извлечение данных из БД
    data = ExaminationSchedule.objects.filter(
        day__date__lt=start_date
    ).annotate(
        date=F('day__date'),  # Используйте ваше собственное имя столбца
        examination_code=F('examination__code')
    ).values(
        'date', 'examination_code', 'actual_count'
    )

    # Подготовка данных
    df = pd.DataFrame(data)
    df = df[df['actual_count'].notna()]

    # Переименование столбцов для Prophet
    df.rename(columns={'date': 'ds', 'actual_count': 'y'}, inplace=True)

    return df

def prophet(start_date, days_count):
    # Получение всех уникальных обследований
    examinations = MedicalExamination.objects.all()

    # Использование модели для прогнозирования будущих обследований для каждого обследования
    for examination in examinations:
        # Подготовка данных для этого обследования
        df = prepare_data_prophet(start_date)

        # Фильтрация данных для этого обследования
        df_examination = df[df['examination_code'] == examination.code]

        # Установка нижнего и верхнего пределов прогноза
        df_examination['floor'] = 0
        df_examination['cap'] = 200  # Замените 100 на ваше максимальное значение

        # Создание и обучение модели
        model = Prophet(growth='logistic')
        model.add_country_holidays(country_name='RU')
        model.add_seasonality(name='montly', period=30.5, fourier_order=5, prior_scale=0.02, mode='multiplicative')
        model.fit(df_examination)

        # Создание dataframe для будущих прогнозов
        future = model.make_future_dataframe(periods=days_count)  # Используйте days_count для прогнозирования на несколько дней вперед
        future['floor'] = 0
        future['cap'] = 200  # Замените 100 на ваше максимальное значение

        # Использование модели для прогнозирования будущих обследований
        forecast = model.predict(future)
        future_examinations = forecast['yhat'].values[-days_count:]  # Получение последних прогнозируемых значений

        # Обновление базы данных с прогнозируемыми значениями
        for i in range(days_count):
            future_date = start_date + timedelta(days=i)
            updated_rows = ExaminationSchedule.objects.filter(day__date=future_date, examination=examination).update(predicted_count=future_examinations[i])
            if updated_rows > 0:
                print(f"Updated predicted_count for {examination.examination_type} on {future_date}")
            else:
                print(f"Failed to update predicted_count for {examination.examination_type} on {future_date}")

        # Визуализация изменений в тренде
        fig = model.plot(forecast)
        a = add_changepoints_to_plot(fig.gca(), model, forecast)
        plt.title(f'Prophet: {examination.examination_type}')
        plt.tight_layout()
        plt.savefig(f'{settings.MEDIA_ROOT}/plots/{examination.code}.png')

           
