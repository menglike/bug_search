FROM m.daocloud.io/library/python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 7777
CMD [ "python", "main.py" ]