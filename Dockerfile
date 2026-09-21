FROM python:3.13
RUN mkdir code
ADD code/ /code
WORKDIR /code
RUN pip install pandas
RUN mkdir books
RUN ["python","main.py"]
CMD ["python","loop.py"]