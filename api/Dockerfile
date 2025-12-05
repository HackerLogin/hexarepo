FROM python:3.11

WORKDIR /app

COPY . .

# 간단한 테스트 서버 만들기
RUN echo "from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef home(): return 'OK TEST'" > test.py
RUN pip install flask

EXPOSE 5000

CMD ["python3", "test.py"]
