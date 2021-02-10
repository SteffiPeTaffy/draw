import paho.mqtt.client as mqtt
import time

broker_address = 'broker.emqx.io'
broker_port = 1883

client = mqtt.Client('SteffiPeTaffy')

client.connect(broker_address, broker_port)

topic = "lieblingswelt/draw"
yellow = [254, 254, 84]
black = [0, 0, 0]
white = [254, 254, 254]
red = [254, 0, 0]

face = [
    [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
     yellow, yellow],
    [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
     yellow, yellow],
    [yellow, black, black, black, black, black, yellow, yellow, yellow, yellow, black, black, black, black, black,
     yellow],
    [black, white, white, white, white, white, black, yellow, yellow, black, white, white, white, white, white, black],
    [black, white, white, black, white, white, black, yellow, yellow, black, white, white, black, white, white, black],
    [black, white, white, black, white, white, black, yellow, yellow, black, white, white, black, white, white, black],
    [black, white, white, white, white, white, black, yellow, yellow, black, white, white, white, white, white, black],
    [yellow, black, black, black, black, black, yellow, yellow, yellow, yellow, black, black, black, black, black,
     yellow],
    [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
     yellow, yellow],
    [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
     yellow, yellow],
    [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
     yellow, yellow],
    [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
     yellow, yellow],
    [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
     yellow, yellow],
    [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
     yellow, yellow],
    [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
     yellow, yellow],
    [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow,
     yellow, yellow]
]

for x in range(16):
    for y in range(16):
        colour = face[x][y]
        message = [y, x, colour[0], colour[1], colour[2]]
        client.publish(topic, bytearray(message))
        time.sleep(0.2)

for i in range(5):
    # from mid to right
    client.publish(topic, bytearray([3, 4, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([3, 5, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([4, 4, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([4, 5, black[0], black[1], black[2]]))

    client.publish(topic, bytearray([12, 4, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([12, 5, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([13, 4, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([13, 5, black[0], black[1], black[2]]))
    time.sleep(2)

    # from right to mid
    client.publish(topic, bytearray([4, 4, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([4, 5, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([3, 4, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([3, 5, black[0], black[1], black[2]]))

    client.publish(topic, bytearray([13, 4, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([13, 5, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([12, 4, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([12, 5, black[0], black[1], black[2]]))
    time.sleep(2)

    # from mid to left
    client.publish(topic, bytearray([3, 4, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([3, 5, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([2, 4, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([2, 5, black[0], black[1], black[2]]))

    client.publish(topic, bytearray([12, 4, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([12, 5, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([11, 4, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([11, 5, black[0], black[1], black[2]]))
    time.sleep(2)

    # from left to mid
    client.publish(topic, bytearray([2, 4, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([2, 5, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([3, 4, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([3, 5, black[0], black[1], black[2]]))

    client.publish(topic, bytearray([11, 4, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([11, 5, white[0], white[1], white[2]]))
    client.publish(topic, bytearray([12, 4, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([12, 5, black[0], black[1], black[2]]))
    time.sleep(2)

    # closed mouth
    client.publish(topic, bytearray([3, 13, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([4, 13, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([5, 13, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([6, 13, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([7, 13, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([8, 13, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([9, 13, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([10, 13, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([11, 13, black[0], black[1], black[2]]))
    time.sleep(1)

    # slightly opened mouth
    client.publish(topic, bytearray([3, 12, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([4, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([5, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([6, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([7, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([8, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([9, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([10, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([11, 12, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([4, 11, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([5, 11, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([6, 11, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([7, 11, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([8, 11, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([9, 11, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([10, 11, black[0], black[1], black[2]]))
    time.sleep(1)

    # fully opened mouth
    client.publish(topic, bytearray([3, 12, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([4, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([5, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([6, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([7, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([8, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([9, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([10, 12, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([11, 12, black[0], black[1], black[2]]))

    client.publish(topic, bytearray([3, 11, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([4, 11, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([5, 11, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([6, 11, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([7, 11, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([8, 11, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([9, 11, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([10, 11, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([11, 11, black[0], black[1], black[2]]))

    client.publish(topic, bytearray([3, 10, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([4, 10, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([5, 10, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([6, 10, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([7, 10, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([8, 10, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([9, 10, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([10, 10, red[0], red[1], red[2]]))
    client.publish(topic, bytearray([11, 10, black[0], black[1], black[2]]))

    client.publish(topic, bytearray([4, 9, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([5, 9, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([6, 9, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([7, 9, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([8, 9, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([9, 9, black[0], black[1], black[2]]))
    client.publish(topic, bytearray([10, 9, black[0], black[1], black[2]]))
    time.sleep(2)

    # no mouth
    client.publish(topic, bytearray([3, 12, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([4, 12, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([5, 12, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([6, 12, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([7, 12, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([8, 12, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([9, 12, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([10, 12, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([11, 12, yellow[0], yellow[1], yellow[2]]))

    client.publish(topic, bytearray([3, 11, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([4, 11, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([5, 11, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([6, 11, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([7, 11, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([8, 11, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([9, 11, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([10, 11, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([11, 11, yellow[0], yellow[1], yellow[2]]))

    client.publish(topic, bytearray([3, 10, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([4, 10, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([5, 10, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([6, 10, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([7, 10, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([8, 10, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([9, 10, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([10, 10, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([11, 10, yellow[0], yellow[1], yellow[2]]))

    client.publish(topic, bytearray([4, 9, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([5, 9, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([6, 9, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([7, 9, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([8, 9, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([9, 9, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([10, 9, yellow[0], yellow[1], yellow[2]]))

    client.publish(topic, bytearray([3, 13, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([4, 13, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([5, 13, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([6, 13, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([7, 13, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([8, 13, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([9, 13, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([10, 13, yellow[0], yellow[1], yellow[2]]))
    client.publish(topic, bytearray([11, 13, yellow[0], yellow[1], yellow[2]]))
    time.sleep(1)

client.disconnect()
print('done!')
