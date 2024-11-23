[![Week 12 Dockerized Application](https://github.com/nogibjj/Cindy_Gao_week12_DockerizedApplication/actions/workflows/actions.yml/badge.svg)](https://github.com/nogibjj/Cindy_Gao_week12_DockerizedApplication/actions/workflows/actions.yml)

# Cindy_Gao_week12_DockerizedApplication
This project is a simple Flask-based web application designed to send health reminders for water consumption, stand-up activities, and daily exercises. The app will periodically display reminders to the user and can be deployed as a Docker container. <br><br>

## Project Overview:
The **Health Reminder App** is a simple web app that helps users maintain healthy habits. It sends reminders for:

**Drinking water** – reminds users to drink water regularly.<br>
**Standing up** – encourages users to take breaks and stretch.<br>
**Daily exercise** – motivates users to do some physical activity.<br>
The app is built with Flask and Docker, making it easy to deploy and run on any system. It’s designed to help people stay on track with basic health goals in a simple and convenient way.<br><br>

## Project Structure:
``` plaintext
CINDY_GAO_WEEK12_DOCKERIZEDAPPLICATION
│
├── .devcontainer/
│   └── devcontainer.json
│
├── .github/
│   └── workflows/
│       └── actions.yml
│
├── .vscode/
│   └── settings.json
│
├── images/
│   └── terminal_dicker.jpg
│   └── docker_log.jpg
│
├── .gitignore
│
├── app.py
├── Dockerfile
├── Makefile
├── README.md
└── requirements.txt
```

Here’s a sample README for your project:

---

## Getting Started
### Installation

1. Clone the repository:

```bash
git clone https://github.com/JiaxinGao1997/health-reminder-app.git
cd health-reminder-app
```

2. Build and run the Docker image:

```bash
docker build -t health-reminder-app .
docker run -d -p 8080:5000 health-reminder-app
```

3. Open the app in your browser by visiting `http://localhost:8080`.
![image](https://github.com/user-attachments/assets/c010c032-5914-4a80-bca3-6b670b5111af)

### Docker Hub

The Docker image is pushed to Docker Hub for easy access and deployment. You can pull the image using the following command:

```bash
docker pull jiaxingao1997/health-reminder-app:latest
```

### Logs

To view logs from the container, use the following command:

```bash
docker logs <container_id>
```
![docker_log](https://github.com/user-attachments/assets/6e39f3e6-2592-43a2-9524-379c81f1225b)

### Pushing to Docker Hub

To push the Docker image to Docker Hub:

```bash
docker tag health-reminder-app jiaxingao1997/health-reminder-app:latest
docker push jiaxingao1997/health-reminder-app:latest
```
![dockerhub](https://github.com/user-attachments/assets/7f65d94b-3836-4dfe-8540-16e30f1b037c)

