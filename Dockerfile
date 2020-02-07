FROM python:3.7
ADD . /app
RUN set -x &&\
    pip install pipenv &&\
    cd /app &&\
    pipenv install
WORKDIR /app
EXPOSE 8000
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "demo"]
    
