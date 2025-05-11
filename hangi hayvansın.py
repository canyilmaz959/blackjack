import random
import time
print(">" * 15, "HANGİ HAYVAN", "<" * 15)

def a():
        sev = ["MAYMUNSUN", "ASLANSIN", "KEDİSİN", "GORİLSİN", "YILANSIN", "İNEKSİN", 
           "KÖPEKSİN", "AYISIN", "KUŞSUN", "EŞEKSİN", "ATSIN", "BALIKSIN"]
        return random.choice(sev)
    
def b(hayvan):
    print("SEN TAM BİR! hesaplanıyor........")
    time.sleep(5)
    print("sonuç: ",hayvan)

def to_lower_tr(text):
    replacements = {
        "I": "ı", "İ": "i",
        "Ç": "ç", "Ğ": "ğ", "Ö": "ö",
        "Ş": "ş", "Ü": "ü"
    }
    return ''.join(replacements.get(c, c.lower()) for c in text)

kombinasyon = {}
    
while True:
    çıkış = input(" tekrar oynamak için herhangi bir tuşa, çıkmak için ç ye basın:")
    
    if çıkış.lower() == "ç":
        print("çıkılıyor...")
        time.sleep(5)
        break
    isim = input("isim:")
    soyisim = input("soyisim:")
    
    while True:
        try:
            yaş = int(input("yaş:"))
            break
        except ValueError:
            print("yaşınızı sayı olarak girin!!")
    
    c = [renk.lower() for renk in ["mor", "mavi", "sarı", "yeşil", "kırmızı"]]
    print("renkler:", ", ".join(c))
    reng = to_lower_tr(input("renk seçiniz:").strip())
    
    s = [sehirr.lower() for sehirr in ["istanbul", "ankara", "izmir", "antalya", "trabzon"]]
    print("sehirler:", ", ".join(s))
    sehir = to_lower_tr(input("sehir seçiniz:").strip())
    
    y = [yemekk.lower() for yemekk in ["kebap", "mantı", "lahmacun", "pilav", "köfte"]]
    print("yemekler:", ", ".join(y))
    yemek = to_lower_tr(input("yemek seçiniz:").strip())
    
    u = [ulkee.lower() for ulkee in ["türkiye", "japonya", "fransa", "brezilya", "meksika"]]
    print("ulkeler:", ", ".join(u))
    ulke = to_lower_tr(input("ulke seçiniz:").strip())
    
    anahtar = f"{reng}|{sehir}|{yemek}|{ulke}"
    
    if anahtar in kombinasyon:
      hayvan = kombinasyon[anahtar]
    else:
      hayvan = a()
      kombinasyon[anahtar] = hayvan


    if reng in c and sehir in s and yemek in y and ulke in u:
        b(hayvan)
        continue
    else:
        print("RENGİ SEÇENEKLERDEN SEÇİN!")
        break