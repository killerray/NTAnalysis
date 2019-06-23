# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     flow
   Description :
   Author :       KillerRay
   date：          2019/6/23
-------------------------------------------------
   Change Activity:
                   2019/6/23:
-------------------------------------------------
"""

class Flow:
    def __init__(self,packet):
        self.tuple4 = packet.tuple4
        self.packetnum = 1;

    def add_packet_to_flow(self,packet):
        self.packetnum+=1

