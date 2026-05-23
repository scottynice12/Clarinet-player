# 🎵 Clarinet Web Application

An interactive, browser-based virtual clarinet application built using Python and the Flask framework. This project demonstrates backend routing, frontend audio initialization, and event-driven user interfaces.

---

## 🚀 Features
* **Interactive UI:** Clickable piano-style keys mapped to responsive instrument audio.
* **Audio Unlocking Architecture:** Bypasses aggressive modern browser security restrictions requiring user interaction before audio initialization.
* **Lightweight Backend:** Built entirely on top of Flask routing for reliable local environments.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your machine:
* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com)

---

## 💻 Installation & Setup

Follow these steps to clone the project, install required dependencies, and get it running locally.

### 1. Clone the Repository
Open your terminal or command prompt and clone this repository to your machine:
```bash
git clone https://github.com
cd YOUR-REPO-NAME
```

### 2. Install Dependencies
Install the required micro-framework libraries via pip:
```bash
pip install flask
```

### 3. Launch the Application
Run the main entry script to spin up the local development server:
```bash
python clarinet_app.py
```

### 4. Access the Application
Once the terminal displays that the server is active, open your favorite browser and navigate to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🎹 How to Play
1. **Unlock the Audio:** Click anywhere on the browser window or select a key. *Modern browsers require a physical user gesture to grant media playback policies.*
2. **Play Notes:** Click the individual white keys to trigger distinct synthesized clarinet notes.

---

## ⚙️ Troubleshooting & Administration

* **Stopping the App:** To shut down the local background server process, click into your active terminal instance and press `Ctrl + C`.
* **Port Conflict Errors (`Address already in use`):** If you are running another local project on port 5000, open `clarinet_app.py` in your text editor. Find the final line and modify the port definition:
  ```python
  app.run(debug=True, port=5001)
  ```
* **Asset Visual Glitches:** If keys fail to align or register animations upon startup, perform a hard cache clearance using `Ctrl + F5` (or `Cmd + Shift + R` on macOS).


