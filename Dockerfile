FROM base_image:latest

RUN mkdir code
ADD code/ /code
WORKDIR /code

RUN mkdir books
RUN mkdir model

RUN ["python","book_importer.py"]
CMD ["python","loop.py"]