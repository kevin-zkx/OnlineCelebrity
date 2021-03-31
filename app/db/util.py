from datetime import datetime

from app.db.base_mysql import SQLManager


def clear_data(data):
    for v in list(data.keys()):
        if data[v] is None:
            del data[v]
    return data

def get_count(tablename, condition):
    db = SQLManager()
    a = db.count_item(tablename, condition)
    db.close()
    # print(a["count"])
    return a["count"]
get_count("cooperation", "c_display")
# def get_insert_sql(table_name, data):
#     # 自动构造update语句
#     sql = 'INSERT INTO %s' % table_name + '(' + ','.join(['%s' % k for k in data]) + ') values(' + ','.join(['%r' % data[k] for k in data]) + ');'
#     return sql
# # "insert into develop(a,b,c,d) values(a_v, b_v, c_v, d_v);"
# table_name = "develop"
# data = {"b": "b_v", "a": "a_v", "d": "d_v", "c": "c_v", "e": 3}
# sql = get_insert_sql(table_name, data)
# print(sql)
# time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# data["addtime"] = time
# sql = get_insert_sql(table_name, data)
# print(sql)
