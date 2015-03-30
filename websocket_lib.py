from websocket import create_connection

def test_connection(send_text):
    ws = create_connection("ws://echo.websocket.org")
    print "Test Websockets - Sending '" + send_text + "'" #Hello, World'..."
    #ws.send("Hello, World")
    ws.send(send_text)
    print "Sent"
    print "Receiving..."
    result =  ws.recv()
    print "Received '%s'" % result
    ws.close()

def send_message(connection, send_text):
    print "Sending '" + send_text + "'" #Hello, World'..."
    connection.send(send_text)
    #result = connection.recv()

def blockchain_info_connection(send_text):
    print "Sending '" + send_text + "' to Blockchain.info" #Hello, World'..."
    ws.send(send_text)
    print "Sent"

    #while 1:
    print "Waiting for data..."
    result =  ws.recv()
    print "Received '%s'" % result



# Send Websocket message
#send_text = '{"op":"ping_block"}' # Returns the latest block
#send_text = '{"op":"ping_tx"}' # Returns the latest tx
#send_text = '{"op":"blocks_sub"}' # Subscribe to blocks
#send_text = '{"op":"unconfirmed_sub"}' # Subscribe to unconfirmed transactions
#send_message(ws, send_text)

#test_connection("test")
