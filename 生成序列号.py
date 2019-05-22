import random,string
chars = string.ascii_letters + string.digits
def get_code(len):
    return (''.join(random.choice(chars) for i in range(len)))
def save_code(value):
    f = open('my_code.txt','a')
    f.write(value)
    f.write('\n')
    f.close()   
while 1:
    length  = int(input('请输入要生成序列号的位数:'))
    code_number =int(input('请输入要生成序列号的个数：'))
    for i in range(code_number):
        val = get_code(length)
        print(val)
        save_code(val)
