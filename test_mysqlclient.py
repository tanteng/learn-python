import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="demo")
c = db.cursor()
max_price = 5
c.execute("""SELECT * FROM think_node""")
one = c.fetchone()
print(one)
# (49, 'read', '??', 1, '', None, 30, 3, 0, 0)

all_result = c.fetchall()
print(all_result)

c.close()  # 关闭连接资源

'''
((40, 'Index', '????', 1, '', 1, 1, 2, 0, 0), (39, 'index', '??', 1, '', None, 30, 3, 0, 0), (37, 'resume', '??', 1, '', None, 30, 3, 0, 0), (36, 'forbid', '??', 1, '', None, 30, 3, 0, 0), (3
5, 'foreverdelete', '??', 1, '', None, 30, 3, 0, 0), (34, 'update', '??', 1, '', None, 30, 3, 0, 0), (33, 'edit', '??', 1, '', None, 30, 3, 0, 0), (32, 'insert', '??', 1, '', None, 30, 3, 0,
0), (31, 'add', '??', 1, '', None, 30, 3, 0, 0), (30, 'Public', '????', 1, '', 2, 1, 2, 0, 0), (69, 'Form', '????', 1, '', 1, 1, 2, 0, 2), (7, 'User', '????', 1, '', 4, 1, 2, 0, 2), (6, 'Role
', '????', 1, '', 3, 1, 2, 0, 2), (2, 'Node', '????', 1, '', 2, 1, 2, 0, 2), (1, 'Rbac', 'Rbac????', 1, '', None, 0, 1, 0, 0), (50, 'main', '????', 1, '', None, 40, 3, 0, 0))
'''