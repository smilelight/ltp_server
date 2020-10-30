# -*- coding: utf-8 -*-
import os
from typing import Union, List

import httpx
import yaml


CONFIG_PATH = "config.yml"

with open(os.path.join(os.path.dirname(__file__), CONFIG_PATH)) as file:
    config = yaml.safe_load(file.read())


class Client:
    def __init__(self, host: str = config["default_host"], port: Union[int, str] = config["default_port"]):
        self._base_url = "http://{host}:{port}".format(host=host, port=port)

    def sent_split(self, texts: List[str]):
        try:
            res = httpx.post(self._base_url + config["route_path"]["sent_split"],
                             json={
                                "texts": texts
                             })
            return res.json()
        except Exception:
            return {
                "status": 1
            }

    def add_words(self, words: List[str], max_window: int = 4):
        try:
            res = httpx.post(self._base_url + config["route_path"]["add_words"],
                             json={
                                 "words": words,
                                 "max_window": max_window
                             })
            return res.json()
        except Exception:
            return {
                "status": 1
            }

    def seg(self, texts: List[str]):
        try:
            res = httpx.post(self._base_url + config["route_path"]["seg"],
                             json={
                                 "texts": texts
                             })
            return res.json()
        except Exception:
            return {
                "status": 1
            }

    def pos(self, texts: List[str]):
        try:
            res = httpx.post(self._base_url + config["route_path"]["pos"],
                             json={
                                 "texts": texts
                             })
            return res.json()
        except Exception:
            return {
                "status": 1
            }

    def ner(self, texts: List[str]):
        try:
            res = httpx.post(self._base_url + config["route_path"]["ner"],
                             json={
                                 "texts": texts
                             })
            return res.json()
        except Exception:
            return {
                "status": 1
            }

    def srl(self, texts: List[str]):
        try:
            res = httpx.post(self._base_url + config["route_path"]["srl"],
                             json={
                                 "texts": texts
                             })
            return res.json()
        except Exception:
            return {
                "status": 1
            }

    def dep(self, texts: List[str]):
        try:
            res = httpx.post(self._base_url + config["route_path"]["dep"],
                             json={
                                 "texts": texts
                             })
            return res.json()
        except Exception:
            return {
                "status": 1
            }

    def sdp(self, texts: List[str]):
        try:
            res = httpx.post(self._base_url + config["route_path"]["sdp"],
                             json={
                                 "texts": texts
                             })
            return res.json()
        except Exception:
            return {
                "status": 1
            }

    def sdpg(self, texts: List[str]):
        try:
            res = httpx.post(self._base_url + config["route_path"]["sdpg"],
                             json={
                                 "texts": texts
                             })
            return res.json()
        except Exception:
            return {
                "status": 1
            }
