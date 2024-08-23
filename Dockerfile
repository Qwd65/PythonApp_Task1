FROM python:3.11-slim

WORKDIR /app

COPY app.py .

ENTRYPOINT ["python", "app.py"]
#Запуск приложения с параметрами из контейнера: docker run -it --rm my-python-app --path /qwe/ew --name qwe

