
#Скачивает образ официальный с сайта 
FROM python:3.9


#Настройка рабойчей директории
WORKDIR /my_first_site_root


#Установка переменных окружения
ENV PYTHONDONTWRUTEBYBITECODE 1
ENV PYTHONUNBUFFERED 1


#Установка зависимостей
RUN pip install --upgrade pip
COPY requirements.txt  .
RUN pip install -r requirements.txt


#Копируем проект
COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


