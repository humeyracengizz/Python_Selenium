print("ahc is here")

#string = metinsel ifade
baslik = "taşıt kredisi"
print(baslik)

baslik = "ihtiyaç kredisi"
print(baslik)

#int, integer tam sayı
vade = 36
ekVade = 12
print(vade)
vade2 = "36"
print(vade2)

#float, decimal, double
aylikOdeme = 200.50

#bool, boolean
yuksekMi = True

#matematiksel Operatörler
print(2 + 7)
print(vade + 12)
print(vade + ekVade)
print(ekVade / vade)
# % bölümünde kalan
print(11 % 2) 

#Mantıksal Operatörler
print(1==1)
print(5 > 42)
print( 7 < 7)

#or and
print(1 > 2 or 5 > 2)
print(1 > 2 and 4 <5) 
print(1 > 2 or 5 < 7 and 1 == 1)

#if else if
sayi1 = 24
sayi2 = 27

#indent
if sayi1 > sayi2:
    print("sayi1 küçüktür")
    print("if bloğunda")
elif sayi1 == sayi2:
    print("sayilar eşit")
else:
    print("sayi2 sayi1 den büyüktür")
