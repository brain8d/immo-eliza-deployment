FROM python:3.10.9
WORKDIR /api
COPY api/. /api
COPY /api/models/. /api/models
<<<<<<< HEAD
COPY requirements.txt /api
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "uvicorn" ]
EXPOSE 8000
CMD ["--host", "0.0.0.0 ", "--port", "8000", "main:app"]
=======
COPY api/main.py /api/main.py
COPY requirements.txt /api
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
>>>>>>> 5e21f91de55b49a16ba80cda1dde6a279db4d53b
