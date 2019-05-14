CASE_ID = "case_id"
CASE_NAME = "case_name"
SQL_EXP = "sql_exp"
RESULT = "result"

EXPLAIN = "explain {}"
TEST_CASE_SQL = "select * from `sql_cases`;"
CLEAR_RESULT_SQL = "update `sql_cases` set result='';"
UPDATE_RESULT_SQL = "update sql_cases set result=%s where case_id=%s;"
RESULT_SQL = "select {},{},{} from `sql_cases`;".format(CASE_ID,SQL_EXP,RESULT)
RESULT_TYPE = "type"

DB_TYPE = "mysql"
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PORT = 3306
DB_PASSWD = "122901"
DB_NAME = "testing"
TABLE_NAME = "`sql_cases`"

BEAUTIFUL_REPORT_CONTENT = "case_id: {}\n sql语句: {}\n 执行结果: {}"

EMAIL_CONTENT = "本次sql 执行计划执行了{}个测试用例，其中运行成功{}个，运行失败{}个。"\
        "其中type为ALL的sql有{}个,为{},其中type为INDEX的sql有{}个,为{}。\n"\
        "测试报告地址: {}\n"\
        "可在数据库中查看运行结果，数据库类型为{}，数据库地址:{}，数据库用户名:{}，密码:{}，数据库库名:{}，表名:{}"


EMAIL_SUB = "sql 执行计划测试报告   {}"
EMAIL_RECEIVER = ["jiangliulin@163.com"]