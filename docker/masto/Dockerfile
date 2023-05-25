FROM python:3.8-slim-buster

# COPY mastodon /app/
COPY Mastodon.py-1.8.0.dist-info /app/
COPY mastodon_base.py /app/
COPY entry_point.sh /app

WORKDIR /app

RUN pip install python-dateutil
RUN pip install couchdb
RUN pip install mastodon.py


RUN chmod +x ./entry_point.sh
ENTRYPOINT [ "/app/entry_point.sh" ]
CMD [ "echo", "Default argument from CMD instruction" ]