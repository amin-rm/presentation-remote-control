# Simple 2-Command Remote Control

This is a simple and easy-to-use 2-button remote for controlling a presentation.

It is designed for students who need a quick solution to control their slides during a project or thesis presentation without needing a specialized remote.
The application works by simulating Left and Right arrow key presses.

It runs in the browser, so you can use it on any internet-enabled device (Android, iOS, laptops, tablets, etc.).
No Bluetooth pairing or special configuration is required.

## Prerequisites

- Python must be installed on the presentation PC.
- Both the controller device and the PC must be connected to the same network (same Wi-Fi or a mobile hotspot).
- Make sure port 5000 on the PC is accessible (check firewall settings).
- Get the LAN IP address of the PC.
- (Optional) Set a secret to secure the remote.

## How to Run

### On the Presentation PC

```bash
# Install required packages
pip install -r requirements.txt

# Run the server
python server.py
```

You should see output similar to:

```
* Running on http://0.0.0.0:5000
```

### On the Controller Device (Phone, Tablet, or Laptop)

1. Open a web browser.
2. Visit `http://[your_pc_ip]:5000` (for example, `http://192.168.1.10:5000`).
3. If you set a secret, enter it in the input field and click "Use".
4. Use the **PREV** and **NEXT** buttons to control the slides.

## Optional: Setting a Secret

To protect the remote from unwanted access on the same network, you can set a secret key using an environment variable.

```bash
export REMOTE_SECRET="your_secret_here"
python server.py
```

When accessing the remote page, enter the same secret in the input field before using the buttons.

## Controls

- Tap the **PREV** and **NEXT** buttons to move slides backward or forward.
- Swipe left or right to change slides.
- Double-tap the screen to toggle fullscreen.
- If you are using a laptop as the controller, the arrow keys also work.

## Troubleshooting

- Make sure both devices are on the same network.
- Check that the IP address is correct.
- Ensure port 5000 is open in the firewall settings.
- If nothing happens when pressing the buttons, verify the server is still running.
