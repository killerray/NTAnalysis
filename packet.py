# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     packet
   Description :
   Author :       KillerRay
   date：          2019/6/21
-------------------------------------------------
   Change Activity:
                   2019/6/21:
-------------------------------------------------
"""


class Packet:  # 如果用tshark获取信息发生变化，需要重写Packet类的__init__方法，增加新的成员变量
    def __init__(self, line):
        linelist = line.split(',')
        self.srcip, self.dstip, self.srcport, self.dstport, self.timestamp, self.packetlen, self.tcpflags = linelist
        self.tuple4 = tuple([self.srcip, self.dstip, self.srcport, self.dstport])

    def __repr__(self):
        return str(self.tuple4) + ',' + str(self.timestamp) + ',' + str(self.packetlen) + ',' + str(self.tcpflags)
