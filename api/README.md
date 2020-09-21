# Instructions
1. Enable virtual env on your local machine
    1. Windows User: python -m venv env
    2. Mac User: python3 -m venv env
2. Run Flask App
    1. Windows User: python app.py
    2. Mac User: python3 app.py
3. Run Flask App via Docker Container
    * docker build -t flaskapp:latest .
    * docker run -it -p 5000:5000 flaskapp
    * docker run -it -d -p 5000:5000 flaskapp (automatically runs in background)
4.  Flask app runs on http://localhost:5000/