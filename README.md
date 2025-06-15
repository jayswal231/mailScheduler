# 🕑 Django mailScheduler App with Celery & RabbitMQ

A simple reminder scheduler built with Django, Celery, and RabbitMQ. It lets users log in, schedule reminders,
and receive email notifications at the specified time.

---

## 🚀 Features

- User authentication (login/logout)
- Schedule reminders with subject, message, and email
- Celery for background task execution
- RabbitMQ as the message broker
- Gmail SMTP for sending emails

---

## 📦 Requirements

- Python 3.12+
- Django 5.1+
- RabbitMQ
- Celery

---

## 🛠️ Installation
for Ubuntu

sudo apt update
sudo apt install rabbitmq-server
sudo service rabbitmq-server start
pip install celery


## start server 
- python manage.py runserver

## start celery worker
- celery -A mailScheduler worker --loglevel=info
