# ltp_server
基于Python的用FastAPI简单封装的LTP服务

## 安装

```shell script
pip install ltp_server
```



## 服务端

### 使用方式

#### 方式一：Python库引用

示例：

```shell script
from ltp_server import Server
if __name__ == '__main__':
    model_path = r"/root/Data/NLP/Model/LTP"
    # server = Server(model_path=model_path)
    # server.run()
    Server(model_path).run()
```

#### 方式二：shell命令

示例：

```shell script
ltp_server --model_path=/root/Data/NLP/Model/LTP
```

### 可用选项

| 参数名     | 是否可选 | 默认值    | 说明                     |
| ---------- | -------- | --------- | ------------------------ |
| model_path | 否       |           | LTP模型路径（绝对路径）  |
| dict_path  | 是       | None      | 用户词表路径（绝对路径） |
| max_window | 是       | 4         | 前向分词最大窗口         |
| host       | 是       | 127.0.0.1 | 服务主机名               |
| port       | 是       | 8000      | 服务监听端口             |

### 服务概览

| 服务功能           | 服务路由    | 请求方式 |
| ------------------ | ----------- | -------- |
| 分句               | /sent_split | POST     |
| 增加自定义词语     | /add_words  | POST     |
| 分词               | /seg        | POST     |
| 词性标注           | /pos        | POST     |
| 命名实体识别       | /ner        | POST     |
| 语义角色标注       | /srl        | POST     |
| 依存句法分析       | /dep        | POST     |
| 语义依存分析（树） | sdp         | POST     |
| 语义依存分析（图） | sdpg        | POST     |

### 请求示例

#### 分句

```bash
### sent_split
POST http://localhost:8000/sent_split
Content-Type: application/json

{
  "texts": ["曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"]
}
```

返回值：

```json
{
  "texts": [
    "曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"
  ],
  "sents": [
    "曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"
  ],
  "status": 0
}
```

#### 增加自定义词语

```bash
### add_words
POST http://localhost:8000/add_words
Content-Type: application/json

{
  "words": ["江大桥"]
}
```



返回值

```json
{
  "status": 0
}
```

#### 分词

```bash
### seg
POST http://localhost:8000/seg
Content-Type: application/json

{
  "texts": ["曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"]
}
```



返回值

```json
{
  "status": 0,
  "texts": [
    "曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"
  ],
  "seg": [
    [
      "曹操",
      "和",
      "司马懿",
      "去",
      "赶集",
      "，",
      "中途",
      "遇",
      "上",
      "关羽",
      "，",
      "一起",
      "吃",
      "了",
      "个",
      "饭",
      "。"
    ]
  ]
}
```

#### 命名实体识别

```bash
### ner
POST http://localhost:8000/ner
Content-Type: application/json

{
"texts": ["曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"]
}
```



返回值

```json
{
  "status": 0,
  "texts": [
    "曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"
  ],
  "seg": [
    [
      "曹操",
      "和",
      "司马懿",
      "去",
      "赶集",
      "，",
      "中途",
      "遇",
      "上",
      "关羽",
      "，",
      "一起",
      "吃",
      "了",
      "个",
      "饭",
      "。"
    ]
  ],
  "ner": [
    [
      [
        "Nh",
        0,
        0
      ],
      [
        "Nh",
        2,
        2
      ],
      [
        "Nh",
        9,
        9
      ]
    ]
  ]
}
```

#### 语义角色标注

```bash
### srl
POST http://localhost:8000/srl
Content-Type: application/json

{
  "texts": ["曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"]
}
```



返回值

```json
{
  "status": 0,
  "texts": [
    "曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"
  ],
  "seg": [
    [
      "曹操",
      "和",
      "司马懿",
      "去",
      "赶集",
      "，",
      "中途",
      "遇",
      "上",
      "关羽",
      "，",
      "一起",
      "吃",
      "了",
      "个",
      "饭",
      "。"
    ]
  ],
  "srl": [
    [
      [],
      [],
      [],
      [
        [
          "A0",
          0,
          2
        ]
      ],
      [
        [
          "A0",
          0,
          2
        ]
      ],
      [],
      [],
      [
        [
          "A0",
          0,
          2
        ],
        [
          "ADV",
          6,
          6
        ],
        [
          "A1",
          9,
          9
        ]
      ],
      [],
      [],
      [],
      [],
      [
        [
          "A0",
          0,
          2
        ],
        [
          "ADV",
          6,
          6
        ],
        [
          "ADV",
          11,
          11
        ],
        [
          "A1",
          14,
          15
        ]
      ],
      [],
      [],
      [],
      []
    ]
  ]
}
```

#### 依存句法分析

```bash
### dep
POST http://localhost:8000/dep
Content-Type: application/json

{
  "texts": ["曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"]
}
```



返回值

```json
{
  "status": 0,
  "texts": [
    "曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"
  ],
  "seg": [
    [
      "曹操",
      "和",
      "司马懿",
      "去",
      "赶集",
      "，",
      "中途",
      "遇",
      "上",
      "关羽",
      "，",
      "一起",
      "吃",
      "了",
      "个",
      "饭",
      "。"
    ]
  ],
  "dep": [
    [
      [
        1,
        4,
        "SBV"
      ],
      [
        2,
        3,
        "LAD"
      ],
      [
        3,
        1,
        "COO"
      ],
      [
        4,
        0,
        "HED"
      ],
      [
        5,
        4,
        "COO"
      ],
      [
        6,
        4,
        "WP"
      ],
      [
        7,
        8,
        "ADV"
      ],
      [
        8,
        4,
        "COO"
      ],
      [
        9,
        8,
        "CMP"
      ],
      [
        10,
        8,
        "VOB"
      ],
      [
        11,
        8,
        "WP"
      ],
      [
        12,
        13,
        "ADV"
      ],
      [
        13,
        8,
        "COO"
      ],
      [
        14,
        13,
        "RAD"
      ],
      [
        15,
        16,
        "ATT"
      ],
      [
        16,
        13,
        "VOB"
      ],
      [
        17,
        4,
        "WP"
      ]
    ]
  ]
}
```

#### 语义依存分析（树）

```bash
### sdp
POST http://localhost:8000/sdp
Content-Type: application/json

{
  "texts": ["曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"]
}
```



返回值

```json
{
  "status": 0,
  "texts": [
    "曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"
  ],
  "seg": [
    [
      "曹操",
      "和",
      "司马懿",
      "去",
      "赶集",
      "，",
      "中途",
      "遇",
      "上",
      "关羽",
      "，",
      "一起",
      "吃",
      "了",
      "个",
      "饭",
      "。"
    ]
  ],
  "sdp": [
    [
      [
        1,
        4,
        "AGT"
      ],
      [
        1,
        5,
        "AGT"
      ],
      [
        2,
        3,
        "mRELA"
      ],
      [
        3,
        4,
        "AGT"
      ],
      [
        4,
        0,
        "Root"
      ],
      [
        5,
        4,
        "eSUCC"
      ],
      [
        6,
        5,
        "mPUNC"
      ],
      [
        7,
        8,
        "MANN"
      ],
      [
        8,
        5,
        "eSUCC"
      ],
      [
        9,
        8,
        "mDEPD"
      ],
      [
        10,
        8,
        "DATV"
      ],
      [
        11,
        8,
        "mPUNC"
      ],
      [
        12,
        13,
        "MANN"
      ],
      [
        13,
        8,
        "eSUCC"
      ],
      [
        14,
        13,
        "mDEPD"
      ],
      [
        15,
        16,
        "MEAS"
      ],
      [
        16,
        13,
        "PAT"
      ],
      [
        17,
        13,
        "mPUNC"
      ]
    ]
  ]
}
```

#### 语义依存分析（图）

```bash
### sdpg
POST http://localhost:8000/sdpg
Content-Type: application/json

{
  "texts": ["曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"]
}
```



返回值

```json
{
  "status": 0,
  "texts": [
    "曹操和司马懿去赶集，中途遇上关羽，一起吃了个饭。"
  ],
  "seg": [
    [
      "曹操",
      "和",
      "司马懿",
      "去",
      "赶集",
      "，",
      "中途",
      "遇",
      "上",
      "关羽",
      "，",
      "一起",
      "吃",
      "了",
      "个",
      "饭",
      "。"
    ]
  ],
  "sdpg": [
    [
      [
        1,
        4,
        "AGT"
      ],
      [
        1,
        5,
        "AGT"
      ],
      [
        2,
        3,
        "mRELA"
      ],
      [
        3,
        4,
        "AGT"
      ],
      [
        4,
        0,
        "Root"
      ],
      [
        5,
        4,
        "eSUCC"
      ],
      [
        6,
        5,
        "mPUNC"
      ],
      [
        7,
        8,
        "MANN"
      ],
      [
        8,
        5,
        "eSUCC"
      ],
      [
        9,
        8,
        "mDEPD"
      ],
      [
        10,
        8,
        "DATV"
      ],
      [
        11,
        8,
        "mPUNC"
      ],
      [
        12,
        13,
        "MANN"
      ],
      [
        13,
        8,
        "eSUCC"
      ],
      [
        14,
        13,
        "mDEPD"
      ],
      [
        15,
        16,
        "MEAS"
      ],
      [
        16,
        13,
        "PAT"
      ],
      [
        17,
        13,
        "mPUNC"
      ]
    ]
  ]
}
```

## 客户端

### 使用方式

#### 方式一：Python库使用

示例如下：

```python
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
```

请求结果：

```json
{'texts': ['乔丹是一位出生在纽约的美国职业篮球运动员。'], 'sents': ['乔丹是一位出生在纽约的美国职业篮球运动员。'], 'status': 0}
{'status': 0, 'texts': ['乔丹是一位出生在纽约的美国职业篮球运动员。'], 'seg': [['乔丹', '是', '一', '位', '出生', '在', '纽约', '的', '美国', '职业', '篮球', '运动员', '。']]}
{'status': 0, 'texts': ['乔丹是一位出生在纽约的美国职业篮球运动员。'], 'seg': [['乔丹', '是', '一', '位', '出生', '在', '纽约', '的', '美国', '职业', '篮球', '运动员', '。']], 'pos': [['nh', 'v', 'm', 'q', 'v', 'p', 'ns', 'u', 'ns', 'n', 'n', 'n', 'wp']]}
{'status': 0, 'texts': ['乔丹是一位出生在纽约的美国职业篮球运动员。'], 'seg': [['乔丹', '是', '一', '位', '出生', '在', '纽约', '的', '美国', '职业', '篮球', '运动员', '。']], 'ner': [[['Nh', 0, 0], ['Ns', 6, 6], ['Ns', 8, 8]]]}
{'status': 0, 'texts': ['乔丹是一位出生在纽约的美国职业篮球运动员。'], 'seg': [['乔丹', '是', '一', '位', '出生', '在', '纽约', '的', '美国', '职业', '篮球', '运动员', '。']], 'srl': [[[], [['A0', 0, 0], ['A1', 2, 11]], [], [], [['A1', 5, 6], ['A0', 9, 11]], [], [], [], [], [], [], [], []]]}
{'status': 0, 'texts': ['乔丹是一位出生在纽约的美国职业篮球运动员。'], 'seg': [['乔丹', '是', '一', '位', '出生', '在', '纽约', '的', '美国', '职业', '篮球', '运动员', '。']], 'dep': [[[1, 2, 'SBV'], [2, 0, 'HED'], [3, 4, 'ATT'], [4, 12, 'ATT'], [5, 12, 'ATT'], [6, 5, 'CMP'], [7, 6, 'POB'], [8, 5, 'RAD'], [9, 12, 'ATT'], [10, 12, 'ATT'], [11, 12, 'ATT'], [12, 2, 'VOB'], [13, 2, 'WP']]]}
{'status': 0, 'texts': ['乔丹是一位出生在纽约的美国职业篮球运动员。'], 'seg': [['乔丹', '是', '一', '位', '出生', '在', '纽约', '的', '美国', '职业', '篮球', '运动员', '。']], 'sdp': [[[1, 2, 'EXP'], [2, 0, 'Root'], [3, 4, 'MEAS'], [4, 12, 'MEAS'], [5, 12, 'rEXP'], [6, 7, 'mRELA'], [7, 5, 'LOC'], [8, 5, 'mDEPD'], [9, 12, 'FEAT'], [10, 11, 'FEAT'], [10, 12, 'FEAT'], [11, 12, 'FEAT'], [12, 2, 'LINK'], [13, 2, 'mPUNC']]]}
{'status': 0, 'texts': ['乔丹是一位出生在纽约的美国职业篮球运动员。'], 'seg': [['乔丹', '是', '一', '位', '出生', '在', '纽约', '的', '美国', '职业', '篮球', '运动员', '。']], 'sdpg': [[[1, 2, 'EXP'], [2, 0, 'Root'], [3, 4, 'MEAS'], [4, 12, 'MEAS'], [5, 12, 'rEXP'], [6, 7, 'mRELA'], [7, 5, 'LOC'], [8, 5, 'mDEPD'], [9, 12, 'FEAT'], [10, 11, 'FEAT'], [10, 12, 'FEAT'], [11, 12, 'FEAT'], [12, 2, 'LINK'], [13, 2, 'mPUNC']]]}
```

#### 方式二：自己通过http请求调用

略

## 参考

- [HIT-SCIR/ltp: Language Technology Platform](https://github.com/HIT-SCIR/ltp)
- [ltp/quickstart.rst at master · HIT-SCIR/ltp](https://github.com/HIT-SCIR/ltp/blob/master/docs/quickstart.rst)
- [python fire使用指南_coordinate的博客-CSDN博客](https://blog.csdn.net/qq_17550379/article/details/79943740)
- [命令行脚本 — Python Packaging Tutorial](https://python-packaging-zh.readthedocs.io/zh_CN/latest/command-line-scripts.html)
- [玩转 Python 命令行：4 大主流工具库的对比 - Python猫的个人空间 - OSCHINA - 中文开源技术交流社区](https://my.oschina.net/u/4051725/blog/4379955)
- [用它5分钟以后，我放弃用了四年的 Flask_涛哥聊Python-CSDN博客](https://blog.csdn.net/wuShiJingZuo/article/details/104111961)