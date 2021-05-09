f = open('file.txt','w')
# 2.写入内容
f.write("test")
# 3.保存文件
f.close() # 关闭文件

f = open('file.txt','r')
# 2.写入内容
content = f.read()
f.seek(0)
content += f.read()
print(content)
# 3.保存文件
f.close() # 关闭文件