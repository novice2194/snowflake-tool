#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: BeYoung
# Date: 2023/6/12 22:50
# Software: PyCharm
import logging
import time
from snowflake import Snowflake


def test_generate():
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger("test_generate")
    log.setLevel(logging.DEBUG)

    generate_id = []
    node = Snowflake()
    start = time.time()
    for i in range(int(1e5)):
        _id = node.generate()
        generate_id.append(_id.id)
    assert len(generate_id) == len(set(generate_id))
    print(int((time.time() - start) * 1000), "ms")
