FROM huggingface/transformers-pytorch-gpu

RUN mkdir code
ADD code/ /code
WORKDIR /code
RUN pip install pandas
RUN mkdir books

RUN ["python3","main.py"]
CMD ["python3","loop.py"]