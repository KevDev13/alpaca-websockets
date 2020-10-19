import websocket, json
import config_secret as config
# If you're using this code from GitHub, remove the line above, and uncomment the line below.
#import config

def on_open_connection(ws):
    print("Connection opened!")

    auth_data = {"action" : "authenticate",
                 "data" : {"key_id" : config.KEY_ID, "secret_key": config.SECRET_KEY}
                 }
    ws.send(json.dumps(auth_data))
    # listen for Tesla and Apple stocks at once a minute
    listen_message = {"action":"listen", "data":{"streams":["AM.TSLA", "AM.AAPL"]}}
    # listen for Tesla stock at tick level
    #listen_message = {"action":"listen", "data":{"streams":["T.TSLA"]}}
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