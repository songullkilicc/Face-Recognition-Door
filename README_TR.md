# 🚀 Yüz Tanıma ile Kapı Kontrol Sistemi

## 📌 Proje Hakkında

Bu proje, bilgisayarla görme teknolojisi kullanarak yetkili kişileri tanıyan ve Arduino tabanlı bir sistem ile fiziksel erişimi kontrol eden akıllı bir kapı sistemidir.

Sistem, **yüz tanıma (Python + OpenCV)** ile **gömülü sistemleri (Arduino, servo motor, LED)** birleştirerek gerçek hayattaki biyometrik güvenlik sistemlerini simüle eder.

---

## 🧠 Temel Özellikler

* Yüz tanıma tabanlı kimlik doğrulama
* Python ve Arduino arasında gerçek zamanlı seri iletişim
* Servo motor ile otomatik kapı kontrolü
* Erişim durumunu gösteren LED geri bildirimi
* Modüler sistem yapısı (yazılım + donanım entegrasyonu)

---

## ⚙️ Sistem Mimarisi

1. Python, OpenCV kullanarak yüzleri algılar
2. Tanınan yüzler için seri komut gönderilir
3. Arduino gelen komutları işler:

   * `'0'` → Kapıyı aç (servo motor)
   * `'1'` → Kapıyı kapat
   * `'2'` → LED yak
   * `'3'` → LED söndür

---

## 🔌 Donanım Bileşenleri

* Arduino Uno
* SG90 Servo Motor
* LED
* USB Seri İletişim

---

## 📁 Proje Yapısı

```id="pb4h4u"
Face-Recognition-Door/
│
├── arduino/
│   └── servo_led_control.ino
│
├── python/
│   └── face_recognition_door.py
│
├── diagrams/
│   ├── flowchart.png
│   └── circuit.png
│
└── README.md
```

---

## 📊 Sistem Akışı

<img width="900" height="701" alt="image" src="https://github.com/user-attachments/assets/cee4f8db-6ca6-411d-b85c-69fe86424894" />

---

## 🔧 Devre Tasarımı

<img width="865" height="341" alt="image" src="https://github.com/user-attachments/assets/c46ecc8d-1964-4b3c-aee7-8e82d0b0c980" />


---

## ⚠️ Proje Durumu

Bu repoda sistemin temel bileşenleri yer almaktadır:

* Arduino tabanlı donanım kontrolü
* Python tabanlı yüz tanıma modülü

Projenin bazı kısımları (mobil uygulama ve tam sistem entegrasyonu) veri kaybı nedeniyle bu repoda yer almamaktadır. Ancak mevcut bileşenler sistemin genel mimarisini ve çalışma mantığını göstermektedir.

---

## 🧠 Öğrendiklerim

* Bilgisayarla görme ile gömülü sistemlerin entegrasyonu
* Seri iletişim protokollerinin gerçek zamanlı kullanımı
* Gerçek hayatta yüz tanıma sistemlerinin karşılaştığı zorluklar
* Donanım ve yazılım birlikte çalışırken sistem tasarımı

---

## 🔄 Gelecek Geliştirmeler

* Mobil uygulamanın yeniden geliştirilmesi
* Daha iyi veri setleri ile doğruluk oranının artırılması
* Tam sistem entegrasyonu ve gerçek zamanlı test

---

## 🛠 Kullanılan Teknolojiler

* Python 3
* OpenCV
* Arduino IDE
* Gömülü Sistemler (Servo, LED)

---

## 👥 Ekip

* Selen Songül Kılıç
* Yunus Kuşbey
* Tunahan Yalçın

---

## 📬 İletişim

Sorular veya iş birlikleri için:
📧 [ssongul.kilic0@gmail.com](mailto:ssongul.kilic0@gmail.com)
