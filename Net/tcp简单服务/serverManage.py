from tcp_server import *
if __name__ == "__main__":
    b = CreateSocket()  
    
    while True:
        try:
            b.saccept()
        except Exception as e:
            print("error")
            break
        while True:
            try:
                data = b.ResvData()
                b.SendData("send message")
            except:            
                b.CloseServer()
                break
    b.CloseServerdeep()