FROM python:3.11-slim

WORKDIR /code 

COPY ./requirements.txt ./

COPY ./sources.list /etc/apt/sources.list

RUN rm -rf /etc/apt/sources.list.d/* && apt-get update && apt-get install git -y && apt-get install curl -y

RUN pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple && pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
