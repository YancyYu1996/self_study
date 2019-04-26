from udp_server import *
if __name__ == "__main__":
    a = udp_server()
    while True:
        a.ResvData()
        a.SendData()
    a.close()
