import socket

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius
  
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1"), 5939))
    
    print(f'Server is listening on')
    print(f'Pending')
    
    while True:
      csocket, address = s.accept()
      print("Received from %s" % str(address))
      fahrenheit = csocket.recv(1204).decode()
      celsius = fahrenheit_to_celsius(float(fahrenheit))
      celsius = round(celsius, 2)
      celsius = str(celsius)
      csocket.send(celsius.encode())
 main()
