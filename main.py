import websocket, json
import config

def on_open_connection(websock):
    print("Connection opened!")

    auth_data = {"action" : "authenticate",
                 "data" : {"key_id" : config.KEY_ID, "secret_key": config.SECRET_KEY}
                 }
    websock.send(json.dumps(auth_data))
    # listen for Tesla and Apple stocks at once a minute
    #listen_message = {"action":"listen", "data":{"streams":["AM.TSLA", "AM.AAPL"]}}
    # listen for Tesla trades
    listen_message = {"action":"listen", "data":{"streams":["T.TSLA"]}}
    websock.send(json.dumps(listen_message))


# Guide for Alpaca websocket messages:
# https://alpaca.markets/docs/api-documentation/api-v2/market-data/streaming/
def on_message_receive(websock, message):
    trade = json.loads(message)

    # print auth or listening messages only
    if trade["stream"] == "authorization" or trade["stream"] == "listening":
        print(message)

    # deal with the message here, i.e. buy/sell stock, perform analysis, etc.

    # print price of most recent TSLA trade
    if trade["stream"] == "T.TSLA":
        print(trade["data"]["p"])

def on_close_connection(websock):
    print("Connection closed.")


socket = "wss://data.alpaca.markets/stream"

websock = websocket.WebSocketApp(socket,
                            on_open=on_open_connection,
                            on_message=on_message_receive,
                            on_close=on_close_connection)
websock.run_forever()