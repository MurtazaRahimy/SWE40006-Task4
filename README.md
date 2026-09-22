SWE40006 — Deployment 4: Docker
Student: Murtaza Rahimy Target Level: Task 4.4 — High Distinction

Structure
task4-2-flask/   Task 4.2 (Credit)         — Flask web app
task4-3-web/     Task 4.3 (Distinction)    — web app with env vars + gunicorn
task4-4-cli/     Task 4.4 (High Distinction) — CLI word-count tool

Docker Hub images
- zal7/task42-flask:1.0
- zal7/task43-web:1.0
- zal7/task44-cli:1.0

Live demo 
https://task43-web-1-0.onrender.com

**How to run it**

Task 4.2:
cd task4-2-flask
docker build -t task42-flask
docker run -d -p 8080:5000 task42-flask

Task 4.3:
cd task4-3-web
docker build -t task43-web .
docker run -d -p 8000:8000 -e APP_TITLE="Task 4.3" -e APP_ENV=local task43-web

Task 4.4:
cd task4-4-cli
docker build -t task44-cli .
docker run -v "$(pwd)/data:/data" task44-cli
cat data/report.txt

