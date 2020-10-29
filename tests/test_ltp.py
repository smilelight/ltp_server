# -*- coding: utf-8 -*-
from ltp import LTP

model_path = r"/root/Data/NLP/Model/LTP"

if __name__ == '__main__':
    ltp = LTP(path=model_path)

    seg, hidden = ltp.seg(["曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"])

    pos = ltp.pos(hidden)
    print(seg)
    print(pos)
