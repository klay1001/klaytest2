#整數格式化輸出
#題目說明：
#請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。
a = eval(input("a"))
b = eval(input("b"))
c = eval(input("c"))
d = eval(input("d"))
print("test1test2test3")
print('|%5d %5d|' %(a, b))
print('|%5d %5d|' %(c, d))
print('|%-5d %-5d|' %(a, b))
print('|%-5d %-5d|' %(c, d))
