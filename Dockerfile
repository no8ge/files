FROM python:3.9.12-slim

WORKDIR /files

COPY . /files

EXPOSE 8004

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["uvicorn","src.main:app","--reload","--port=8004","--host=0.0.0.0" ]


