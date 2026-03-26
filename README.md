# Commix Demo: OS Command Injection

This repository contains a simple Flask application that acts as a fake network diagnostic tool. It is intentionally vulnerable to OS command injection for educational and demonstration purposes. This guide will walk you through how to set up the vulnerable environment and how to exploit it using Commix.

## Understanding the Vulnerability

### OS Command Injection vs. SQL Injection
Most people are familiar with SQL injection, where an attacker manipulates user input to force a database to execute malicious queries. OS command injection relies on the exact same logic, but the target is different. Instead of tricking a database, you are tricking the server's underlying operating system. If a web application passes user input directly to a system shell without sanitizing it, an attacker can append their own terminal commands and take control of the server.

### Enter Commix
To automate this kind of attack, we use Commix (Command Injection Exploiter). You can think of it as the SQLMap equivalent for command injections. It automatically tests different ways to break out of the intended command and, if successful, provides you with a remote pseudo-shell.

To find a way in, Commix targets the data your browser sends to the server. When you interact with a web application, you send HTTP requests. These requests include parameters, which are the visible data inputs like the variables in a URL string, and headers, which are hidden pieces of metadata your browser sends behind the scenes. Commix tests these by injecting various payloads to see if the server blindly executes them.

## How to Reproduce the Demo

### 1. Set Up the Vulnerable Server
First, we need to get the vulnerable Flask server code. Open your terminal and clone this repository, then navigate into the project folder. Once inside, create a virtual environment to keep the project dependencies isolated from your main system.

```bash
git clone https://github.com/DiDawn/demoCommix.git
cd demoComix
python -m venv venv
```

Next, activate the virtual environment. 
If you are on Linux or macOS:
```bash
source venv/bin/activate
```

If you are on Windows:
```bash
.\venv\Scripts\activate
```

With the environment active, install Flask and start the vulnerable application:
```bash
pip install flask
python app.py
```
The server should now be running locally, typically on port 5000. Leave this terminal open.

### 2. Prepare the Attacker Environment
Open a second terminal window to act as the attacker. We need to get Commix. You can pull the repository directly from GitHub:

```bash
git clone https://github.com/commixproject/commix.git
cd commix
```

### 3. Run the Exploit
We already know the vulnerable parameter in our Flask app is `address`, so we will point Commix directly at it. Run this command:

```bash
python commix.py --url="http://127.0.0.1:5000/?address=127.0.0.1"
```

Commix will start analyzing the target. It might ask you a few questions during the process, such as whether you want to test other parameters or if you recognize the underlying operating system. You can usually accept the defaults or answer based on your own machine.

Once it confirms the vulnerability, it will ask if you want to spawn a pseudo-terminal shell. Answer Y (yes), and you will drop into an os_shell prompt. From there, you can type standard terminal commands like `whoami`, `ls`, or `pwd` to verify that you have successfully exploited the server.

## Disclaimer
This project is for educational purposes only. Do not use Commix or the techniques described here against systems you do not own or have explicit permission to test. The author is not responsible for any misuse or damage caused by this information.
