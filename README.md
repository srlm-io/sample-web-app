# sample-web-app

This is a simple web app/game showing how to use websockets and an in-memory "database" to create a simple interactive multiplayer game.

# Server Setup

You can run this anywhere that takes Python, but AWS Lightsail seems to be a simplified version of EC2 that is pretty easy to get going.

1. Go to https://lightsail.aws.amazon.com/ls/webapp/home/instances. You may need to create an AWS account
1. Create an instance of Ubuntu 20.04.
1. Under the instance "Networking" settings under "IPv4 Firewall" add a new rule: Custom, TCP, port 8080.
1. Create a static IP and attach to that instance
1. On settings panel for the instance, click the big "Connect with SSH" button
1. Follow the instructions below to install the prerequisites and start the server


# Install Prerequisites and start the server

```bash
sudo apt update
sudo apt install python3 python3-pip

python3 -m pip install flask flask_socketio

git clone https://github.com/srlm-io/sample-web-app.git
cd sample-web-app

# If on the server, run tmux so that it keeps going even after you exit, use `tmux attach` to join again later
tmux

python3 main.py
```
