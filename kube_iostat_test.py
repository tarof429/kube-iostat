import unittest
import main

class KubeIostatTest(unittest.TestCase):

    def test_get_cputimes(self):
        ret = main.get_cpu_times()
        print(ret)

    def test_get_cpupercent(self):
        ret = main.get_cpu_percent()
        print(ret)

    def test_get_cpucount(self):
        ret = main.get_cpu_count()
        print(ret)

if __name__ == '__main__':
    unittest.main()
