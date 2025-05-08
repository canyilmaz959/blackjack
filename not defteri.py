import time
def f(a):
     return("notunuz:", a)
def e(a):
    return("notunuz:", a)
def c(a):
    return("notunuz:", a)
print(">" * 15, "NOTLAR", "<" * 15)
while True:
    n = input("notlara hoşgeldiniz!\n'e', 'f', 'c' klasörlerinden kayıtlı not seçebilirsiniz.\nçıkmak için herhangi bir tuşa basınız.\nnot almak için 'n'ye basınız: ")
    if n == "n":
       a = input("notunuz: ")
    elif n == "e":
       print("açılıyor...")
       time.sleep(3)
       print(e(a))
    elif n == "f":
       print("açılıyor...")
       time.sleep(3)
       print(f(a))
    elif n == "c":
       print("açılıyor...")
       time.sleep(3)
       print(c(a))
    else:
       print("çıkılıyor...")
       time.sleep(3)
       break
    g = input("zaten kayıt yeri seçtiyseniz 'b' ile başa dönün!\nherhangi bir tuşa basarak çıkabilirsiniz.\nkayıt yeri seçiniz 'e', 'f', 'c': ")
    if g == "e":
       print("başarıyla kaydedildi!")
       s = input("başa dönmek için 'b' tuşuna basınız\nçıkmak için herhangi bir tuşa basınız\naçmak için 'o' tuşuna basınız: ")
       if s == "o":
        print("açılıyor...")
        time.sleep(3)
        print(e(a))
        continue
       elif s == "b":
          print("başa dönülüyor...")
          time.sleep(5)
          continue
       else:
        print("çıkılıyor...")
        time.sleep(3)
        break
    
    if g == "f":
       print("başarıyla kaydedildi!")
       j = input("başa dönmek için 'b' tuşuna basınız\nçıkmak için herhangi bir tuşa basınız\naçmak için 'o' tuşuna basınız")
       if j == "o":
        print("açılıyor...")
        time.sleep(3)
        print(f(a))
        continue
       elif j == "b":
          print("başa dönülüyor...")
          time.sleep(5)
          continue
       else:
        print("çıkılıyor...")
        time.sleep(3)
        break

    if g == "c":
       print("başarıyla kaydedildi!")
       k = input("başa dönmek için 'b' tuşuna basınız\nçıkmak için herhangi bir tuşa basınız\naçmak için 'o' tuşuna basınız")
       if k == "o":
        print("açılıyor...")
        time.sleep(3)
        print(c(a))
        continue
       elif k == "b":
          print("başa dönülüyor...")
          time.sleep(5)
          continue
       else:
        print("çıkılıyor...")
        time.sleep(3)
        break
    elif g == "b":
       print("başa dönülüyor...")
       time.sleep(5)
       continue
    else:
       print("çıkılıyor...")
       time.sleep(3)
       break