# -*- coding: utf-8 -*-
import httpx

test_url = "http://localhost:8000/dep"

test_body = {
    "texts": ["乔丹是一位出生在纽约的美国职业篮球运动员。"]
}

r = httpx.post(test_url, json=test_body)
print(r.json())
