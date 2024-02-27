FROM python:3.10.9
WORKDIR /api
COPY api/. /api
COPY /api/models/. /api/models
COPY requirements.txt /api
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "uvicorn" ]
EXPOSE 8000
CMD ["--host", "0.0.0.0 ", "--port", "8000", "main:app"]