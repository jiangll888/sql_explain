import sys,os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.join(os.path.dirname(os.getcwd()),"Lib\\site-packages\\"))
from BeautifulReport import BeautifulReport
import unittest,time
from util.opera_db import OperationDB
import ddt
from config import settings
from base.run_main import RunMain

op_db = OperationDB()
data = op_db.search_all(settings.TEST_CASE_SQL)

@ddt.ddt
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 清除以前的测试结果
        op_db.sql_DML(settings.CLEAR_RESULT_SQL)

    @ddt.data(*data)
    @ddt.unpack
    def test(self, *args, **kwargs):
        r = RunMain(kwargs)
        self.res = r.run_main()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    filename = time.strftime("%Y-%m-%d %H-%M-%S")
    BeautifulReport(suite).report(description="sql执行计划",filename=filename,log_path="../report")