FROM python:latest

WORKDIR /usr/app/src

COPY print_version.py ./

RUN pip install gitpython

CMD [ "python", "./print_version.py"]