from udp_client import *

if __name__ == "__main__":
    a = udp_client()
    while True:
        a.SendData()
        a.ResvData()
    a.close()