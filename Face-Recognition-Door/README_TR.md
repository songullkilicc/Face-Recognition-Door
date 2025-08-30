# Yüz Tanıma Kapı Sistemi

## Proje Açıklaması
Bu proje, Python, Arduino ve mobil uygulama kullanılarak yapılan bir yüz tanıma kapı sistemidir. 
Sistem, yetkili kişileri tanır ve tanınan kişileri kapıyı açarak veya ışığı yakarak karşılar. 
Mobil uygulama üzerinden de kapı uzaktan kontrol edilebilir (tek fotoğraf ile).

## Bileşenler
- **Python Kodu:** OpenCV ile yüz tanıma yapar ve Arduino ile seri iletişim kurar.
- **Arduino Kodu:** Kapı için servo motoru ve LED'i kontrol eder.
- **Mobil Uygulama:** Uzaktan kapıyı kontrol etmeye olanak sağlar (fotoğraf tabanlı).

## Özellikler
- Birden fazla yetkili kullanıcıyı tanıyabilir
- Tanınan yüz için kapıyı otomatik açar
- Tanınan yüz algılandığında LED yanar
- Mobil uygulama üzerinden uzaktan kontrol
- Daha iyi doğruluk için ayarlanabilir tanıma eşiği

## Çalışma Prensibi
1. Python kodu kameradan video alır.
2. Algılanan yüzler eğitimli modellerle karşılaştırılır.
3. Tanınan bir yüz bulunursa:
   - Arduino servo motor ile kapıyı açar.
   - LED yanar.
   - Mobil uygulama ile işlem tetiklenebilir.
4. Tanınmayan yüzlerde kapı kapalı kalır ve LED söner.

## Notlar
- Mobil uygulama kodu dahil değildir; yalnızca Python ve Arduino kısımları mevcuttur.
- Python ve Arduino kodları açıklamalarla belgelenmiştir.

## Teknolojiler
- Python 3
- OpenCV
- Arduino IDE
- Servo motor
- LED
- Mobil uygulama arayüzü (fotoğraf tabanlı kontrol)

## Yazar
- Selen Songül Kılıç
- Yunus Kuşbey
- Tunahan Yalçın