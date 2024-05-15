FROM python:latest
WORKDIR /home/app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY . /home/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "gunicorn", "Carpetaprojecto.carpetaprojecto.wsgi", "-b", "0.0.0.0:8000"]

#CMD [ "python3", "/home/david/aprendizaje/python/BD/myenv/carpetaprojecto/manage.py", "runserver", "0.0.0.0:8000" ]
