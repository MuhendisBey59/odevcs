print("""*************************************
Hesap Makinesi Programı !!

İşlemler;

1.İşlem:'topla'

2.İşlem:'çıkar

3.İşlem:'çarp'

4.İşlem:'böl'

5.İşlem:'modAl'

************************************* """)
while True:
    a = int(input("Birinci sayıyı giriniz:"))
    b = int(input("İkinci sayıyı giriniz:"))

    islem=input("Lütfen yapacağınız işlemi seçiniz:")

    if (islem=="topla") or (islem=="Topla"):
        print ("{} ile {}'in toplamı {}'dir.".format(a,b,a+b))

    elif (islem=="çıkar") or (islem=='Çıkar'):
        print ("{} ile {}'in farkı {}'dir.".format(a,b,a-b))

    elif (islem=="çarp") or (islem=='Çarp'):
        print ("{} ile {}'in çarpımı {}'dir.".format(a,b,a*b))

    elif (islem=="böl") or (islem=='Böl'):
        print("{} ile {}'in bölümü {}'dir.".format(a,b,a/b))

    elif (islem=="modAl") or (islem=='ModAl'):
        print("mod:",a%b)

    else:
        print("Geçersiz işlem!")
