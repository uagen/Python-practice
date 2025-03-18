"""
使用while嵌套循环打印九九乘法表
"""

#定义外层循环控制变量
i = 1
while i <= 9:
  #定义内层循环控制变量
  j = 1
  while j <= i:
    #内层的print语句，不要换行，通过制表符对齐
    print(f"{j} * {i} = {j * i}\t, end='')
    j += 1
  i += 1
  print()
