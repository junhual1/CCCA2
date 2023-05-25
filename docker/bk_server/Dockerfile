FROM python:3.8-slim-buster

# COPY mastodon /app/
COPY . /app/

WORKDIR /app


RUN pip install flask
RUN pip install couchdb
RUN pip install Flask-Cors
RUN pip install pybase64
RUN pip install pandas
RUN pip install numpy
RUN pip install matplotlib


RUN chmod +x ./entry_point.sh
ENTRYPOINT [ "/app/entry_point.sh" ]
CMD [ "echo", "Default argument from CMD instruction" ]



# CMD ["python",  "app.py", "127.0.0.1", "5000"]