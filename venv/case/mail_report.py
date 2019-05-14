from config import settings
from util.opera_db import OperationDB
from util.send_mail import SendMail
import json,time,sys

class MailReport:
    def __init__(self):
        self.op_db = OperationDB()
        self.result = self.get_result()

    def get_result(self):
        result = self.op_db.search_all(settings.RESULT_SQL)
        return result

    def count(self):
        success_count = fail_count = type_all_count = type_index_count = 0
        for res in self.result:
            if res[settings.RESULT]:
                success_count += 1
                r = json.loads(res[settings.RESULT])
                if r[settings.RESULT_TYPE] == "ALL":
                    type_all_count += 1
                elif r[settings.RESULT_TYPE] == "INDEX":
                    type_index_count += 1
            else:
                fail_count += 1
        return success_count,fail_count,type_all_count,type_index_count

    def get_type_case(self):
        type_all_cases = [i[settings.SQL_EXP] for i in self.result if json.loads(i[settings.RESULT])[settings.RESULT_TYPE] == "ALL"]
        type_index_cases = [i[settings.SQL_EXP] for i in self.result if json.loads(i[settings.RESULT])[settings.RESULT_TYPE] == "INDEX"]
        return type_all_cases,type_index_cases

    def send_result_mail(self,report_file=None):
        count_tuple = self.count()
        type_cases = self.get_type_case()
        count = str(int(count_tuple[0]) + int(count_tuple[1]))
        content = settings.EMAIL_CONTENT.format(count, count_tuple[0], count_tuple[1], count_tuple[2], type_cases[0],
                                                count_tuple[3], type_cases[1],report_file,
                                                settings.DB_TYPE,settings.DB_HOST,settings.DB_USER,settings.DB_PASSWD,
                                                settings.DB_NAME,settings.TABLE_NAME)
        s = SendMail()
        sub = settings.EMAIL_SUB.format(time.strftime("%Y-%m-%d %H:%M:%S"))
        s.send_mail(settings.EMAIL_RECEIVER, sub, content)

if __name__ == "__main__":
    m = MailReport()
    #print(m.op_db.search_all(settings.RESULT_SQL))
    m.send_result_mail(sys.argv[1])