import network
import socket
import machine
import time
import gc

# WiFi credentials
ssid = 'YOUR_WIFI_SSID'
password = 'YOUR_WIFI_PASSWORD'

# Connect to WiFi with retry logic
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(ssid, password)
        retry = 0
        while not wlan.isconnected() and retry < 10:
            retry += 1
            time.sleep(1)
            print('.', end='')
    if wlan.isconnected():
        print('\nConnected!')
        print('IP address:', wlan.ifconfig()[0])
        return wlan
    else:
        print('\nFailed to connect.')
        return None

wlan = connect_wifi()
if wlan is None:
    raise RuntimeError("WiFi connection failed.")

# Set up LED
led = machine.Pin("LED", machine.Pin.OUT)

# Nicer HTML with simple CSS
html = """<!DOCTYPE html>
<html>
<head>
  <title>Pico W LED Control</title>
  <style>
    body {{ font-family: Arial; text-align: center; margin-top: 50px; }}
    button {{ font-size: 24px; padding: 20px 40px; margin: 20px; }}
    h1 {{ color: #333; }}
  </style>
</head>
<body>
  <h1>Pico W LED Control</h1>
  <p>LED is currently: <strong>{}</strong></p>
  <form action="/" method="get">
    <button name="led" value="on">Turn ON</button>
    <button name="led" value="off">Turn OFF</button>
  </form>
</body>
</html>"""

# Start server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket()
server.bind(addr)
server.listen(1)
print("Web server running... Access at http://{}".format(wlan.ifconfig()[0]))

while True:
    try:
        client, addr = server.accept()
        print("Client connected from", addr)
        request = client.recv(1024)
        request = str(request)
        print("Request:", request)

        led_state = "OFF"
        if '/?led=on' in request:
            led.value(1)
            led_state = "ON"
        elif '/?led=off' in request:
            led.value(0)
            led_state = "OFF"

        response = html.format(led_state)
        client.send('HTTP/1.1 200 OK\r\n')
        client.send('Content-Type: text/html\r\n')
        client.send('Connection: close\r\n\r\n')
        client.sendall(response)
        client.close()
        gc.collect()  # Clean up memory

    except Exception as e:
        print("Error:", e)
        client.close()

