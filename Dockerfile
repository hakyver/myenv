FROM python:3.7.3-stretch
WORKDIR /home/app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY . /home/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "gunicorn", "home.app.Carpetaprojecto.carpetaprojecto.wsgi.py", "-b", "0.0.0.0:$PORT"]

#CMD [ "python3", "/home/david/aprendizaje/python/BD/myenv/carpetaprojecto/manage.py", "runserver", "0.0.0.0:8000" ]
