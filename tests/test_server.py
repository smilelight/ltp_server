# -*- coding: utf-8 -*-
from ltp_server import Server
if __name__ == '__main__':
    model_path = r"/root/Data/NLP/Model/LTP"
    # server = Server(model_path=model_path)
    # server.run()
    Server(model_path).run(port=8000)
