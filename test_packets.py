import unittest
from interface import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        exeCmd = r'D:\Wireshark\tshark.exe'
        pcapFilepath=r'E:\smb'
        tsharkFiels=r'-Y "ip && tcp" -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e frame.time_epoch -e tcp.len -e tcp.flags -E separator=,'

        IF = Interface(exeCmd,pcapFilepath,tsharkFiels)
        IF.statrt()

if __name__ == '__main__':
    unittest.main()
