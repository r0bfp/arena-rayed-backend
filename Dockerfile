FROM python:3.9

WORKDIR /

COPY ./ /

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

EXPOSE 8080

ENV PORT 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]