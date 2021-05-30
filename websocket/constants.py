class State:
    """ Connnection states """

    CONNECTING = 1
    CONNECTED = 2
    DISCONNECTED = 3


class SendEvent:
    """Lists events that application can send.
    ACCEPT - Sent by the application when it wishes to accept an incoming connection.
    SEND - Sent by the application to send a data message to the client.
    CLOSE - Sent by the application to tell the server to close the connection.
        If this is sent before the socket is accepted, the server must close
        the connection with a HTTP 403 error code (Forbidden), and not complete
        the WebSocket handshake; this may present on some browsers as
        a different WebSocket error code (such as 1006, Abnormal Closure).
    """

    ACCEPT = "websocket.accept"
    SEND = "websocket.send"
    CLOSE = "websocket.close"


class ReceiveEvent:
    """Enumerates events that application can receive from protocol server.
    CONNECT - Sent to the application when the client initially
        opens  a connection and is about to finish the WebSocket handshake.
        This message must be responded to with either an Accept message or a Close message
        before the socket will pass websocket.receive messages.
    RECEIVE - Sent to the application when a data message is received from the client.
    DISCONNECT - Sent to the application when either connection to the client is lost,
        either from the client closing the connection,
        the server closing the connection, or loss of the socket.
    """

    CONNECT = "websocket.connect"
    RECEIVE = "websocket.receive"
    DISCONNECT = "websocket.disconnect"
