# Huats 2023 oscstarterkit
from pythonosc import udp_client

def victor():
    receive_ip = "127.0.0.1"
    receive_port = 4869
    addr = "/print"
    message = "LEVANTASEEE"

    send_message(receive_ip,receive_port,addr,message)

def send_message(receiver_ip, receiver_port, address, message):
    try:
        # Create an OSC client to send messages
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

        # Send an OSC message to the receiver
        client.send_message(address, message)

        print("Message sent successfully.")
    except:
        print("Message not sent")

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.92"        # wlan ip
PORT = 6942

addr = "/print"
msg = "LEVANTASEEEE"

send_message(PI_A_ADDR, PORT, addr, msg)


