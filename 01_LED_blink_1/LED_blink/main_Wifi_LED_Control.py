import network
import socket
import machine
import time

# Replace these with your WiFi credentials
ssid = ''
password = ''

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to WiFi...", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(1)
print("\nConnected!")
print("IP address:", wlan.ifconfig()[0])

# Set up LED (using onboard LED as example)
led = machine.Pin("LED", machine.Pin.OUT)

# HTML page template
html = """
<!DOCTYPE html>
<html>
    <head> <title>Pico W LED Control</title> </head>
    <body>
        <h1>Pico W LED Control</h1>
        <p>LED is currently: {}</p>
        <form action="/" method="get">
            <button name="led" value="on" type="submit">Turn ON</button>
            <button name="led" value="off" type="submit">Turn OFF</button>
        </form>
    </body>
</html>
"""

# Start the web server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket()
server.bind(addr)
server.listen(1)

print("Web server running... Access at http://{}".format(wlan.ifconfig()[0]))

while True:
    client, addr = server.accept()
    print("Client connected from", addr)
    request = client.recv(1024)
    request = str(request)
    print("Request:", request)

    # Parse request
    led_on = "LED is OFF"
    if '/?led=on' in request:
        led.value(1)
        led_on = "LED is ON"
    elif '/?led=off' in request:
        led.value(0)
        led_on = "LED is OFF"

    response = html.format(led_on)
    client.send('HTTP/1.1 200 OK\n')
    client.send('Content-Type: text/html\n')
    client.send('Connection: close\n\n')
    client.sendall(response)
    client.close()

