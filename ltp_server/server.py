# -*- coding: utf-8 -*-
import os
from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from ltp import LTP
from fire import Fire
import yaml

CONFIG_PATH = "config.yml"

with open(os.path.join(os.path.dirname(__file__), CONFIG_PATH)) as file:
    config = yaml.safe_load(file.read())


class Item(BaseModel):
    texts: List[str]


class Words(BaseModel):
    words: List[str]
    max_window: int = 4


class Server:
    def __init__(self, model_path: str, dict_path: str = None, max_window: int = 4):
        self._app = FastAPI()
        self._ltp = LTP(path=model_path)
        if dict_path:
            self._ltp.init_dict(path=dict_path, max_window=max_window)
        self._init()

    def _init(self):
        @self._app.post(config["route_path"]["sent_split"])
        def sent_split(item: Item):  # 分句
            ret = {
                'texts': item.texts,
                'res': [],
                "status": 0
            }
            try:
                res = self._ltp.sent_split(item.texts)
                ret['res'] = res
            except Exception as e:
                print(e)
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["add_words"])
        def add_words(words: Words):  # 增加自定义词语
            ret = {
                'status': 0
            }
            try:
                self._ltp.add_words(words=words.words, max_window=words.max_window)
            except Exception as e:
                print(e)
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["seg"])
        def seg(item: Item):  # 分词
            ret = {
                'status': 0,
                'texts': item.texts,
                'res': [],
            }
            try:
                res, hidden = self._ltp.seg(item.texts)
                ret['res'] = res
            except Exception as e:
                print(e)
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["pos"])
        def pos(item: Item):  # 词性标注
            ret = {
                'status': 0,
                'texts': item.texts,
                'res': [],
                'seg': []
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.pos(hidden)
                tmp = []
                for seg_sent, pos_sent in zip(seg, res):
                    tmp.append(tuple(zip(seg_sent, pos_sent)))
                ret['res'] = tmp
                ret['seg'] = seg
            except Exception as e:
                print(e)
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["ner"])
        def ner(item: Item):  # 命名实体识别
            ret = {
                'status': 0,
                'texts': item.texts,
                'res': [],
                'seg': []
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.ner(hidden)
                tmp = []
                for seg_sent, ner_sent in zip(seg, res):
                    tmp_item = []
                    for ner_item in ner_sent:
                        tmp_item.append((''.join(seg_sent[ner_item[1]:ner_item[2]+1]), ner_item[0], ner_item[1], ner_item[2]))
                    tmp.append(tmp_item)
                ret['res'] = tmp
                ret['seg'] = seg
            except Exception as e:
                print(e)
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["srl"])
        def srl(item: Item):  # 语义角色标注
            ret = {
                'status': 0,
                'texts': item.texts,
                'res': [],
                'seg': []
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.srl(hidden)
                tmp = []
                for seg_sent, srl_sent in zip(seg, res):
                    tmp_item = []
                    for idx, srl_item in enumerate(srl_sent):
                        if not srl_item:
                            continue
                        tmp_item.append((seg_sent[idx], idx, [(item[0], seg_sent[item[1]: item[2]+1], item[1], item[2]) for item in srl_item]))
                    tmp.append(tmp_item)
                ret['res'] = tmp
                ret['seg'] = seg
            except Exception as e:
                print(e)
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["dep"])
        def dep(item: Item):  # 依存句法分析
            ret = {
                'status': 0,
                'texts': item.texts,
                'res': [],
                'seg': []
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.dep(hidden)
                tmp = []
                for seg_sent, dep_sent in zip(seg, res):
                    tmp_item = []
                    for dep_item in dep_sent:
                        tmp_word = seg_sent[dep_item[1] - 1] if dep_item[1] > 0 else "ROOT"
                        tmp_item.append((dep_item[0], seg_sent[dep_item[0]-1], dep_item[1], tmp_word, dep_item[2]))
                    tmp.append(tmp_item)
                ret['res'] = tmp
                ret['seg'] = seg
            except Exception as e:
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["sdp"])
        def sdp(item: Item):  # 语义依存分析（树）
            ret = {
                'status': 0,
                'texts': item.texts,
                'res': [],
                'seg': []
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.sdp(hidden)
                tmp = []
                for seg_sent, sdp_sent in zip(seg, res):
                    tmp_item = []
                    for sdp_item in sdp_sent:
                        tmp_word = seg_sent[sdp_item[1] - 1] if sdp_item[1] > 0 else "ROOT"
                        tmp_item.append((sdp_item[0], seg_sent[sdp_item[0]-1], sdp_item[1], tmp_word, sdp_item[2]))
                    tmp.append(tmp_item)
                ret['res'] = tmp
                ret['seg'] = seg
            except Exception as e:
                print(e)
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["sdpg"])
        def sdpg(item: Item):  # 语义依存分析（图）
            ret = {
                'status': 0,
                'texts': item.texts,
                'res': [],
                'seg': []
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.sdp(hidden)
                tmp = []
                for seg_sent, sdpg_sent in zip(seg, res):
                    tmp_item = []
                    for sdpg_item in sdpg_sent:
                        tmp_word = seg_sent[sdpg_item[1] - 1] if sdpg_item[1] > 0 else "ROOT"
                        tmp_item.append((sdpg_item[0], seg_sent[sdpg_item[0]-1], sdpg_item[1], tmp_word, sdpg_item[2]))
                    tmp.append(tmp_item)
                ret['res'] = tmp
                ret['seg'] = seg
            except Exception as e:
                print(e)
                ret['status'] = 1
            return ret

    def run(self, host: str = config["default_host"], port: Union[int, str] = config["default_port"]):
        uvicorn.run(self._app, host=host, port=port)


def run_server(model_path: str, dict_path: str = None, max_window: int = int(config["default_max_window"]),
               host: str = config["default_host"], port: Union[int, str] = config["default_port"]):
    Server(model_path, dict_path=dict_path, max_window=max_window).run(host=host, port=port)


def run():
    Fire(run_server)


