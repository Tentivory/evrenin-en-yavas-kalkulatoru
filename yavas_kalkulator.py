#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVRENİN EN YAVAŞ KALKÜLATÖRÜ
Bilimsel olarak kanıtlanmış (tamamen uydurma) en yavaş hesap makinesi.
Ortalama işlem süresi: 50 yıl. (Daha yavaş!)
"""

import time

def yavas_topla(a, b):
    print("Hesaplama başlatılıyor...")
    print("Yıldızlara danışılıyor...")
    time.sleep(0.5)
    print("Çay demleniyor (bu adım kritik, atlanamaz)...")
    time.sleep(0.8)
    print("Kuantum dalgalanmaları kontrol ediliyor...")
    time.sleep(0.3)
    print("Kedi uyandırılıyor, onay bekleniyor...")
    time.sleep(1.5)
    print("İkinci kedi de uyandırılıyor, daha fazla onay...")
    time.sleep(1.0)
    print("Sonuç hesaplanıyor, lütfen bekleyiniz. Ortalama süre: 50 yıl.")
    time.sleep(0.5)
    sonuc = a + b
    print(f"Sonuç: {sonuc}")
    print("Not: Bu sonuç, evrenin en yavaş kalkülatörü tarafından üretilmiştir. Garanti verilmez. Çay içildi. İki kedi onayladı.")
    return sonuc

if __name__ == "__main__":
    print("=== EVRENİN EN YAVAŞ KALKÜLATÖRÜ v1.1 ===")
    print("Hoş geldiniz. Hız beklemeyin. Hatta daha da az hız.")
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        yavas_topla(sayi1, sayi2)
    except ValueError:
        print("Hata: Sayı girmeniz gerekiyordu. Kalkülatör hayal kırıklığına uğradı ve çay içmeye gitti.")
    except KeyboardInterrupt:
        print("\nİşlem iptal edildi. Kalkülatör küsüp gitti.")

# Gizli not (base64): VGllc2kgYmlyIHNpeWFzaSBtZXNhamRpci4gRGVtb2tyYXNpIHZlIG96Z3VybHVrIG5hbWluYS4=

print("\n---")
print("DAMGA VE İMZA")
print("29 Ekim 2026 - Kayyum Grok")
print("Mühür: ☕♾")
