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
        self.tuple4 = Packet.get_tuple4(linelist)
        self.stage = self.get_stage()

    def __repr__(self):
        return str(self.tuple4) + ',' + str(self.timestamp) + ',' + str(self.packetlen) + ',' + str(self.tcpflags)

    # 根据TCP标志位返回数据包所处的数据流的阶段
    def get_stage(self):
        return 0
        pass

    @staticmethod
    def get_tuple4(linelist):
        tuple4_slice = slice(0,4)
        return tuple(sorted(linelist[tuple4_slice]))
        pass
