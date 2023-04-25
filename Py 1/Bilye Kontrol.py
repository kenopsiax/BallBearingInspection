baska_kutu = "e"
hatali_kutu_say = 0
toplam_kutu_say = 0
iade_bilye_say = 0
toplam_bilye_say = 0
esit_kutu_say = 0
agir_kutu_say = 0
hafif_kutu_say = 0
agir_agirlik_farki_toplam = 0
agir_yuzde_toplam = 0
hafif_agirlik_farki_toplam = 0
hafif_yuzde_toplam = 0
max_bilye_esit = 0
max_bilye_agirligi_esit = 0
max_agirlik = 0
max_agirlik_bilye_say=0
maxfark_degeri = 0
maxfark_yuzdesi = 0
min_yuzde = 100
min_yuzde_deger = 0
while(baska_kutu =="e" or baska_kutu =="E"):
    toplam_kutu_say +=1
    kutu_bilye_sayisi = int(input("Kutudaki bilye sayısını giriniz:"))
    while(kutu_bilye_sayisi < 10):
        kutu_bilye_sayisi = int(input("Hatalı değer girdiniz, Kutudaki bilye sayısını giriniz: "))

    toplam_bilye_say += kutu_bilye_sayisi
    bilye_agirligi = int(input("Sıraki bilyenin mg cinsinden ağrırlığını giriniz: "))
    while (bilye_agirligi <= 0):
        bilye_agirligi = int(input("Sıraki bilyenin mg cinsinden ağrırlığını giriniz:  "))
    a = bilye_agirligi
    sayac = 0
    a_sayac = 1
    b = 0
    b_sayac = 1
    for i in range(kutu_bilye_sayisi - 1 ):
        bilye_agirligi = int(input("Sıraki bilyenin mg cinsinden ağrırlığını giriniz:  "))
        while (bilye_agirligi <= 0):
            bilye_agirligi = int(input("Sıraki bilyenin mg cinsinden ağrırlığını giriniz: "))
        if bilye_agirligi == a :
            a_sayac += 1
        if b == 0:
            if bilye_agirligi != a :
                b = bilye_agirligi
                sayac += 1
                b_sayac +=1
        else:
            if (bilye_agirligi != a and bilye_agirligi != b)  :
                sayac += 1

            if (bilye_agirligi == b ):
                if a_sayac > 2:
                    sayac +=1
                else:
                    b_sayac += 1
        if a_sayac >= 2 and a_sayac == b_sayac :
            sayac == 2


        if (sayac >= 2)  :
            print("Hatalı veri girişi İADEE")
            print("Şuanki kutuda birden fazla hatalı bilye var..")
            hatali_kutu_say += 1
            iade_bilye_say += kutu_bilye_sayisi
            break
    if sayac < 2 :
        if (a > b) and (b != 0) :
            print("Bir bilye diğerlerinden daha hafiftir.")
            hafif_kutu_say +=1
            agirlik_farki = a - b

            print(f'Ağırlık farkının değeri : {agirlik_farki:.2f}')
            agirlik_farki_yuzdesi = agirlik_farki * 100 / a
            print(f"Ağırlık farkının yüzdesi : {agirlik_farki_yuzdesi:.2f}")
            hafif_agirlik_farki_toplam += agirlik_farki
            hafif_yuzde_toplam += agirlik_farki_yuzdesi
            string = "Ağır"
            if maxfark_degeri < agirlik_farki:
                maxfark_degeri = agirlik_farki
                maxfark_yuzdesi = agirlik_farki_yuzdesi
                max_fark_isaret = string
            if min_yuzde > agirlik_farki_yuzdesi:
                min_yuzde = agirlik_farki_yuzdesi
                min_yuzde_deger = agirlik_farki
                min_yuzde_isaret = string
        elif b > a :
            print("Bir bilye diğerlerinden daha ağırdır.")
            agir_kutu_say += 1
            agirlik_farki = b - a
            print(f'Ağırlık farkının değeri : {agirlik_farki:.2f}')
            agirlik_farki_yuzdesi = 100 * agirlik_farki / a
            print(f"Ağırlık farkının yüzdesi : {agirlik_farki_yuzdesi:.2f}")
            agir_agirlik_farki_toplam += agirlik_farki
            agir_yuzde_toplam += agirlik_farki_yuzdesi
            string = "Hafif"
            if maxfark_degeri < agirlik_farki:
                maxfark_degeri = agirlik_farki
                maxfark_yuzdesi = agirlik_farki_yuzdesi
                max_fark_isaret = string
            if min_yuzde > agirlik_farki_yuzdesi:
                min_yuzde = agirlik_farki_yuzdesi
                min_yuzde_deger = agirlik_farki
                min_yuzde_isaret = string

        else:
            print("Kutudaki tüm bilyeler eşit ağırlıkta...")
            esit_kutu_say += 1
            if max_bilye_esit < kutu_bilye_sayisi:
                max_bilye_esit = kutu_bilye_sayisi
                max_bilye_agirligi_esit = bilye_agirligi
            if max_agirlik < bilye_agirligi:
                max_agirlik = bilye_agirligi
                max_agirlik_bilye_say = kutu_bilye_sayisi

    baska_kutu = input("Baska kutu var mı ? (E, e, H, h) ")
    while ((baska_kutu != "e") and (baska_kutu != "E") and (baska_kutu != "h") and (baska_kutu != "H")):
        baska_kutu = input("Hatalı veri girdiniz, baska kutu var mı? (E, e, H, h)")
    if baska_kutu == "h" or baska_kutu =="H":
        break

print("Üretim hatası olan kutu sayısı : ", hatali_kutu_say)
hatali_kutu_yuzdesi = hatali_kutu_say * 100 / toplam_kutu_say
print(f"Üretim hatası olan kutuların tüm kutular içerisindeki yüzdesi :  {hatali_kutu_yuzdesi:.2f}")
print("İade edilen bilye sayısı : ", iade_bilye_say)
kabul_bilye_say = toplam_bilye_say - iade_bilye_say
print("Kabul edilen bilye sayısı : ", kabul_bilye_say )
print("Tüm bilyelerin eşit ağırlıkta olduğu kutu sayısı : ", esit_kutu_say)
print("Bir bilyenin diğerlerinden ağır olduğu kutu sayısı : ", agir_kutu_say)
print("Bir bilyenin diğerlerinden hafif olduğu kutu sayısı : ", hafif_kutu_say)
satin_alinan_kutu_say = toplam_kutu_say - hatali_kutu_say
esit_yuzde = esit_kutu_say * 100 / satin_alinan_kutu_say
hafif_yuzde = hafif_kutu_say * 100 / satin_alinan_kutu_say
agir_yuzde = agir_kutu_say * 100 / satin_alinan_kutu_say
print(f"Tüm bilyelerin eşit ağırlıkta olduğu kutu sayısının satın alınan kutular içindeki yüzdesi:{esit_yuzde:.2f}")
print(f"Bir bilyenin diğerinden daha ağır olduğu kutu sayısının satın alınan kutular içindeki yüzdesi:{agir_yuzde:.2f}")
print(f"Bir bilyenin diğerinden daha hafif olduğu kutu sayısının satın alınan kutular içindeki yüzdesi: {hafif_yuzde:.2f}")

w = agir_agirlik_farki_toplam / agir_kutu_say
print(f"Bir bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı değerlerinin ortalaması: {w:.2f}")
u = agir_yuzde_toplam / agir_kutu_say
print(f"Bir bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı yüzdelerinin ortalaması: {u:.2f}")

p= hafif_agirlik_farki_toplam / hafif_kutu_say
print(f"Bir bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı değerlerinin ortalaması: {p:.2f}")
o = hafif_yuzde_toplam / hafif_kutu_say
print(f"Bir bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı yüzdelerinin ortalaması: {u:.2f}")

print("Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en çok sayıda bilye olan kutudaki bilye sayısı: ", max_bilye_esit)
print("Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en çok sayıda bilye olan kutudaki bir bilyenin ağırlığı: ", max_bilye_agirligi_esit)
print("Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en ağır bilyeler olan kutudaki bilye sayısı: ",max_agirlik_bilye_say)
print("Tüm bilyelerin eşit ağırlıkta olduğu kutular arasında, içinde en ağır bilyeler olan kutudaki bir bilyenin ağırlığı: ",max_agirlik)

print("Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının değeri: ",maxfark_degeri)
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının yüzdesi: {maxfark_yuzdesi:.2f}")
print("Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının işareti:" ,max_fark_isaret)

print("Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının değeri:",min_yuzde)
print(f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının yüzdesi: {min_yuzde_deger:.2f}")
print("Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın yüzdesinin en küçük olduğu ağırlık farkının işareti: ",min_yuzde_isaret)
