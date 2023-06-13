#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: BeYoung
# Date: 2023/6/12 17:37
# Software: PyCharm
"""
pysnowflake provides a simple Twitter snowflake generator and parser.
"""
import time
from threading import Lock


class ID:
    __id: int
    __machine_size: int
    __sequence_size: int
    __epoch: int

    def __init__(self, snowflake_id=0, machine_size=10,
                 sequence_size=12, epoch=1288834974657):
        """
        :param snowflake_id: snowflake id
        :param machine_size: min=1, max=21
        :param sequence_size: min=1, max=21
        :param epoch: min=0, max=now()
        Note: machine_size + sequence.size <= 22
        """

        # check snowflake id
        if snowflake_id < 0 or snowflake_id >= (1 << 63):
            raise f"snowflake_id must between 0 and {(1 << 63)}" \
                  f"but now is {snowflake_id}"

        # check machine size
        if machine_size < 0 or machine_size > 21:
            raise f"machine_size must be between 0 and 21, " \
                  f"but now is {machine_size}"

        # check sequence size
        if sequence_size < 0 or sequence_size > 21:
            raise f"sequence_size must be between 0 and 21, " \
                  f"but now is {sequence_size}"

        # check epoch
        if epoch < 0 or epoch >= int(time.time() * 1000):
            raise f"machine_id must be between 0 and now({int(time.time() * 1000)}), " \
                  f"but now is {epoch}"

        self.__id = snowflake_id
        self.__machine_size = machine_size
        self.__sequence_size = sequence_size
        self.__epoch = epoch

    @property
    def id(self):
        return self.__id

    @property
    def epoch(self):
        return self.__epoch

    @property
    def timestamp(self):
        return self.__id >> (self.__machine_size + self.__sequence_size) + self.__epoch

    def machine_id(self):
        return (self.__id >> self.__sequence_size) & ((1 << self.__machine_size) - 1)

    def __str__(self):
        return str(self.__id)


class Snowflake:
    __epoch: int
    __sequence = 0
    __sequence_size: int
    __sequence_mask: int
    __machine_id: int
    __machine_size: int
    __machine_shift: int
    __timestamp_size = 41
    __timestamp_shift: int
    __lock = None

    def __init__(self, machine_id=0, machine_size=10,
                 sequence_size=12, epoch=1288834974657):
        """
        :param machine_id: min=0, max=(1<<machine_size)-1
        :param machine_size: min=1, max=21
        :param sequence_size: min=1, max=21
        :param epoch: min=0, max=now(), default: twitter epoch

        Note: machine_size + sequence.size <= 22
        """
        if machine_size < 0 or machine_size > 21:
            raise f"machine_size must be between 0 and 21, " \
                  f"but now is {machine_size}"

        if sequence_size < 0 or sequence_size > 21:
            raise f"sequence_size must be between 0 and 21, " \
                  f"but now is {sequence_size}"

        if machine_id < 0 or machine_size >= (1 << machine_size):
            raise f"machine_id must be between 0 and {1 << machine_size}, " \
                  f"but now is {machine_id}"

        if epoch < 0 or epoch >= int(time.time() * 1000):
            raise f"machine_id must be between 0 and now({int(time.time() * 1000)}), " \
                  f"but now is {epoch}"

        self.__epoch = epoch
        self.__sequence_size = sequence_size
        self.__sequence_mask = (1 << sequence_size) - 1
        self.__machine_id = machine_id
        self.__machine_size = machine_size
        self.__machine_shift = sequence_size
        self.__timestamp_shift = sequence_size + machine_size
        self.__lock = Lock()

    def generate(self) -> ID:
        """
        generate a snowflake id
        :return: id class
        """
        with self.__lock:
            now = int(time.time() * 1000) - self.__epoch
            _id = 0
            _id |= ((now << self.__timestamp_shift) |
                    (self.__machine_id << self.__machine_shift) |
                    self.__sequence)
            node = ID(snowflake_id=_id,
                      machine_size=self.__machine_size,
                      sequence_size=self.__sequence_size)
            self.__sequence = (self.__sequence + 1) & self.__sequence_mask
            return node

    @classmethod
    def parse(cls, snowflake_id=0, machine_size=10,
              sequence_size=12, epoch=1288834974657) -> ID:
        """
       :param snowflake_id: snowflake id
       :param machine_size: min=1, max=21
       :param sequence_size: min=1, max=21
       :param epoch: min=0, max=now()
       Note: machine_size + sequence.size <= 22
       """
        return ID(snowflake_id, machine_size, sequence_size, epoch)

    @property
    def epoch(self):
        return self.__epoch

    @property
    def machine(self):
        return self.__machine_id, self.__machine_size

    def __str__(self):
        return str(self.__dir__())

    def __next__(self):
        return self.generate()
