FROM python:3.8.10
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5555
ENTRYPOINT [ "./start.sh" ]
