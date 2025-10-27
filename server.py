from flask import Flask, send_file, request, abort
import pyautogui
import os

SECRET = os.getenv("REMOTE_SECRET", "")

app = Flask(__name__)

# optional authentication check
def check_auth():
    if not SECRET:
        return True
    return request.headers.get("X-Remote-Secret") == SECRET

# render the remote control HTML page
@app.route("/")
def index():
    return send_file("remote.html")

# handle next
@app.post("/next")
def next_slide():
    if not check_auth():
        abort(401)
    pyautogui.press("right")
    return ("", 204)

# handle previous
@app.post("/prev")
def prev_slide():
    if not check_auth():
        abort(401)
    pyautogui.press("left")
    return ("", 204)

# run on all interfaces, port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
