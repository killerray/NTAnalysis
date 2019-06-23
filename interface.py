# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     interface
   Description :
   Author :       KillerRay
   date：          2019/6/21
-------------------------------------------------
   Change Activity:
                   2019/6/21:
-------------------------------------------------
"""
import os
from packet import *

from common import packetQ
import thread

from common import flowTable
import threading

# class Interface(threading.Thread):


class Interface:
    pcapFileExtensions = ['.pcap','pcapng','cap']

    def __init__(self, execmd, pcappath, field):
        #threading.Thread.__init__(self)
        self.exeCmd = execmd
        self.pacpPath = pcappath
        self.tsharkFields = field
        self.pcapFilePathList = []

    '''def run(self):
        print "Starting "
        self.process_data()
        print "Exiting "
    '''

    def create_file_list(self, dir):
        if os.path.isfile(dir):
            if self.judge_file_extensions(dir):
                self.pcapFilePathList.append(dir)
        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                newdir = os.path.join(dir, s)
                self.create_file_list(newdir)

    def read_data(self,arg):
        self.create_file_list(self.pacpPath)
        for pcapfilename in self.pcapFilePathList:
            ret = os.popen(self.create_exe_cmd(self.exeCmd, pcapfilename, self.tsharkFields))
            ret = ret.read()
            for line in ret.splitlines():
                p = Packet(line)
                packetQ.put(p)

            '''for p in packetQ:
                print p
            '''
        # print self.pcapFilePathList
        #print str(len(packetQ))

    def process_data(self,arg):
        while True:
            if packetQ.empty():
                continue
            else:
                p = packetQ.get()
                print p

    def statrt(self):
        try:
            thread.start_new_thread(self.read_data, ('read thread',))
            thread.start_new_thread(self.process_data, ('process_thread',))
        except:

            print "Error: unable to start thread"
        while 1:
            pass

    @staticmethod
    def create_exe_cmd(execmd,pcappath,field):
        return execmd+' '+'-r '+pcappath+' '+field

    @staticmethod
    def judge_file_extensions(filename):
        if os.path.splitext(filename)[-1] in Interface.pcapFileExtensions:
            return True
        else:
            return False
