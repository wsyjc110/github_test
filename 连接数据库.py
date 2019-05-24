import MySQLdb as mdb
import random,string
chars = string.ascii_letters + string.digits
def get_code(len):
    return (''.join(random.choice(chars) for i in range(len)))
def save_code(value):
    f = open('my_code.txt','a')
    f.writelines(value)
    f.write('\n')
    f.close()   

length  = int(input('请输入要生成序列号的位数:'))
code_number = int(input('请输入要生成序列号的个数：'))
for i in range(code_number):
    val = get_code(length)
    save_code(val)
    print(val)
db = mdb.connect('localhost','root','root','mytest',charset='utf8')
cursor =db.cursor()
f = open('my_code.txt')
for line in f.readlines():
    cursor.execute("insert into t1 (code) values ('%s')"%(line.strip()))
    db.commit()
f.close()
print('执行完毕！！！！')




