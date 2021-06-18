'''

攝氏('C)轉換成為華氏('F)程式
讓使用者輸入 攝氏溫度
然後印出 華氏溫度

'''

celsius = input('請輸入攝氏:' )
celsius = float(celsius)

fahrenheit = celsius * ( 9 / 5 ) + 32
print('華氏:', fahrenheit, '°F')