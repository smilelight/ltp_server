# -*- coding: utf-8 -*-
from ltp import LTP

model_path = r"/root/Data/NLP/Model/LTP"

if __name__ == '__main__':
    ltp = LTP(path=model_path)

    texts = ["我们都是中国人。", "遇到苦难不要放弃，加油吧！奥利给！", "乔丹是一位出生在纽约的美国职业篮球运动员。"]

    # texts = ["曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"]

    seg, hidden = ltp.seg(texts)

    pos = ltp.sdp(hidden)
    print(seg)
    print([len(sent) for sent in seg])
    print(pos)
