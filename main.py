import websocket, json
import config

def on_open_connection(ws):
    print("Connection opened!")

    auth_data = {"action" : "authenticate",
                 "data" : {"key_id" : config.KEY_ID, "secret_key": config.SECRET_KEY}
                 }
    ws.send(json.dumps(auth_data))
    listen_message = {"action":"listen", "data":{"streams":["T.TSLA"]}}
    ws.send(json.dumps(listen_message))


def on_message_receive(ws, message):
    print("Message:")
    print(message)

def on_close_connection(ws):
    print("Connection closed.")


socket = "wss://data.alpaca.markets/stream"

ws = websocket.WebSocketApp(socket,
                            on_open=on_open_connection,
                            on_message=on_message_receive,
                            on_close=on_close_connection)
ws.run_forever()