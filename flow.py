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
        self.context = {}
        self.is_continue = 1
        self.cliet_tuple2,self.server_tuple2 = Flow.confirm_client_server(packet)

    def add_packet_to_flow(self,packet):
        self.packetnum += 1
        if self.is_continue and int(packet.packetlen) > 0:
            '''if packet.tcpflags == '0x00000011':
                print str(self.tuple4)+str(self.packetnum)
            '''
            self.process_flow(packet)
    @staticmethod
    def confirm_client_server(packet):
        pass

    # process_flow类似的函数可以实现多个，对应多种处理逻辑
    def process_flow(self,pcaket):
        pass