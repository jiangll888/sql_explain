from config import settings
from util.opera_db import OperationDB
import json

class DataConfig:

    def __init__(self,data):
        self.db_data = data
        self.op_db = OperationDB()

    def get_case_id(self):
        return self.db_data and self.db_data[settings.CASE_ID]

    def get_case_name(self):
        return self.db_data and self.db_data[settings.CASE_NAME]

    def get_sql_exp(self):
        return self.db_data and settings.EXPLAIN.format(self.db_data[settings.SQL_EXP])

    def get_result(self):
        return self.db_data and self.db_data[settings.RESULT] and json.loads(self.db_data[settings.RESULT])

    def write_result(self,sql,param=None):
        self.op_db.sql_DML(sql,param)

if __name__ == "__main__":
    data = {'case_id': 'sql_001', 'case_name': None, 'sql_exp': 'select * from `cases`;',
      'result': '{"id": 1, "select_type": "SIMPLE", "table": "cases", "type": "ALL", "possible_keys": null, "key": null, "key_len": null, "ref": null, "rows": 6, "Extra": ""}'}
    d = DataConfig(data)
    print(d.get_result())
    #d.write_result(settings.UPDATE_RESULT_SQL,("pass","sql_001"))


