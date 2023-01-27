FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
ENV SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ENV ALGORITHM=HS256
ENV ACCESS_TOKEN_EXPIRE_MINUTES=30
ENV HOST_DB=sql_book
ENV USER_DB=root
ENV PASSWORD_DB=12345
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]