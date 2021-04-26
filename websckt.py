import websocket

ws = websocket.WebSocket()
ws.connect('ws://192.168.31.69')
print('connected to websocket server')


while True:
    str = input('say something ')
    ws.send(str)
    result = ws.recv()
    print('Recieved '+result)