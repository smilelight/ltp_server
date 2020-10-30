# -*- coding: utf-8 -*-
from ltp_server import Client

if __name__ == '__main__':
    client = Client()
    texts = ["乔丹是一位出生在纽约的美国职业篮球运动员。"]

    print(client.sent_split(texts))
    print(client.seg(texts))
    print(client.pos(texts))
    print(client.ner(texts))
    print(client.srl(texts))
    print(client.dep(texts))
    print(client.sdp(texts))
    print(client.sdpg(texts))
