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
                'sents': [],
                "status": 0
            }
            try:
                sents = self._ltp.sent_split(item.texts)
                ret['sents'] = sents
            except Exception:
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["add_words"])
        def add_words(words: Words):  # 增加自定义词语
            ret = {
                'status': 0
            }
            try:
                self._ltp.add_words(words=words.words, max_window=words.max_window)
            except Exception:
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["seg"])
        def seg(item: Item):  # 分词
            ret = {
                'status': 0,
                'texts': item.texts,
                'seg': [],
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                ret['seg'] = seg
            except Exception:
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["pos"])
        def pos(item: Item):  # 词性标注
            ret = {
                'status': 0,
                'texts': item.texts,
                'seg': [],
                'pos': []
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.pos(hidden)
                ret['seg'] = seg
                ret['pos'] = res
            except Exception:
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["ner"])
        def ner(item: Item):  # 命名实体识别
            ret = {
                'status': 0,
                'texts': item.texts,
                'seg': [],
                'ner': [],
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.ner(hidden)
                ret['seg'] = seg
                ret['ner'] = res
            except Exception:
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["srl"])
        def srl(item: Item):  # 语义角色标注
            ret = {
                'status': 0,
                'texts': item.texts,
                'seg': [],
                'srl': [],
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.srl(hidden)
                ret['seg'] = seg
                ret['srl'] = res
            except Exception:
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["dep"])
        def dep(item: Item):  # 依存句法分析
            ret = {
                'status': 0,
                'texts': item.texts,
                'seg': [],
                'dep': [],
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.dep(hidden)
                ret['seg'] = seg
                ret['dep'] = res
            except Exception:
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["sdp"])
        def sdp(item: Item):  # 语义依存分析（树）
            ret = {
                'status': 0,
                'texts': item.texts,
                'seg': [],
                'sdp': [],
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.sdp(hidden)
                ret['seg'] = seg
                ret['sdp'] = res
            except Exception:
                ret['status'] = 1
            return ret

        @self._app.post(config["route_path"]["sdpg"])
        def sdpg(item: Item):  # 语义依存分析（图）
            ret = {
                'status': 0,
                'texts': item.texts,
                'seg': [],
                'sdpg': [],
            }
            try:
                seg, hidden = self._ltp.seg(item.texts)
                res = self._ltp.sdp(hidden)
                ret['seg'] = seg
                ret['sdpg'] = res
            except Exception:
                ret['status'] = 1
            return ret

    def run(self, host: str = config["default_host"], port: Union[int, str] = config["default_port"]):
        uvicorn.run(self._app, host=host, port=port)


def run_server(model_path: str, dict_path: str = None, max_window: int = int(config["default_max_window"]),
               host: str = config["default_host"], port: Union[int, str] = config["default_port"]):
    Server(model_path, dict_path=dict_path, max_window=max_window).run(host=host, port=port)


def run():
    Fire(run_server)


