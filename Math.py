import random


for i in range(0, 100):
    print("\033[1;31m!!!Lütfen aşağıda belirtilen yönergelere göre bir sayıya basın!!!\033[0m")


    print("\033[1;34m1 = Kolay")
    print("2 = Orta")
    print("3 = Zor")
    print("4 = Çok Zor\033[0m")


    print("\033[1;31mÇıkış yapmak istiyorsanız 'ç' basın\033[0m")


    secim = input("Zorluk seç:")


    if secim == "1":
        sayi1 = random.randint(1, 10)
        sayi2 = random.randint(1, 10)
    elif secim == "2":
        sayi1 = random.randint(30, 40)
        sayi2 = random.randint(30, 40)
    elif secim == "3":
        sayi1 = random.randint(50, 70)
        sayi2 = random.randint(50, 70)
    elif secim == "4":
        sayi1 = random.randint(60, 99)
        sayi2 = random.randint(60, 99)
    elif secim == "ç":
        break


    print("Çarpma işlemi için '*' işareti kullanın")
    print("Bölme işlemi için '/' işaretini kullanın")
    print("Toplama işlemi için '+' işaretini kullanın")
    print("Çıkartma işlemi için '-' işaretini kullanın\033[0m")
    print("\033[1;31mÇıkış yapmak istiyorsanız 'ç' basın\033[0m")
    secim2 = input("\033[1;35mLütfen bir seçim yapınız:\033[0m")


    if secim2 == "*":
        sonuc = sayi1 * sayi2
    elif secim2 == "/":
        sonuc = sayi1 / sayi2
    elif secim2 == "+":
        sonuc = sayi1 + sayi2
    elif secim2 == "-":
        sonuc = sayi1 - sayi2
    elif secim2 == "ç":
        break


    soru = print("Sorunuz:",sayi1, secim2, sayi2)
    bilgi = print("\033[1;32mCevabınızı tuşlayın:", end='')
    cevap = int(input("\033[0m"))


    if sonuc == cevap:
        print("\033[1;32mDoğru\033[0m")
    elif sonuc != cevap:
        print("\033[1;31mYanlış\033[0m")
    elif secim2 == "ç":
        break
    input("Devam etmek istiyorsanız return tuşuna basın")
