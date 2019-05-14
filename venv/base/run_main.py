from config.data_config import DataConfig
import json
import time
import threading
from util.send_mail import SendMail
from config import settings
from util.opera_db import OperationDB

class RunMain:
    _instance_lock = threading.Lock()

    def __init__(self,data):
        self.data = data
        self.get_field()
        self.op_db = OperationDB()

    def __new__(cls, *args, **kwargs):
        '''
        实现单例模式
        :param args:
        :param kwargs:
        :return:
        '''
        if not hasattr(cls,"_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super().__new__(cls)
        return cls._instance

    def get_field(self):
        dc = DataConfig(self.data)
        self.case_id = dc.get_case_id()
        self.sql_exp = dc.get_sql_exp()
        self.result = dc.get_result()

    def run_main(self):
        r = self.op_db.search_one(self.sql_exp)
        print(settings.BEAUTIFUL_REPORT_CONTENT.format(self.case_id,self.sql_exp,r))
        self.write_res(r)
        return r

    def write_res(self,res):
        dc = DataConfig(self.data)
        res = json.dumps(res)
        para = (res, self.case_id)
        sql = settings.UPDATE_RESULT_SQL
        dc.write_result(sql,para)


if __name__ == "__main__":
    data = {'case_id': 'sql_001', 'case_name': None, 'sql_exp': 'select * from `cases`;', 'result': None}
    r = RunMain(data)
    res = r.run_main()
    # print(res,type(res))



