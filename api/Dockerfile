FROM python:3.10.9
WORKDIR /api
COPY api/. /api
COPY /api/model/. /api/model
COPY api/main.py /api/main.py
COPY requirements.txt /api
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000