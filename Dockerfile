FROM python:3

WORKDIR /src
COPY main.py requirements.txt ./
RUN pip install virtualenv && \
    virtualenv env && \
    . ./env/bin/activate && \
    ./env/bin/pip install -r requirements.txt

ENV FLASK_APP main.py    
CMD ["./env/bin/flask", "run", "--host=0.0.0.0"]

EXPOSE 5000