import cv2
import serial
import time

# Seri portu başlat (Arduino'nuz hangi portta bağlıysa onu seçin)
arduino = serial.Serial('COM5', 9600)  # 'COM3' Windows için, macOS/Linux'da '/dev/ttyUSB0' veya '/dev/ttyACM0' olabilir
time.sleep(2)  # Arduino'nun başlatılması için kısa bir süre bekleyin

tani = cv2.face.LBPHFaceRecognizer_create()
tani.read('denemee/denemee.yml')

cas = "haarcascade_frontalface_default.xml.txt"
yuzcas = cv2.CascadeClassifier(cas)
font = cv2.FONT_HERSHEY_SIMPLEX

cam = cv2.VideoCapture(0)

# Tanınan kişilerin uyum değerlerinin ortalamasını hesaplamak için bir liste
recognized_confidences = []

# Daha iyi bir eşik değeri belirlemek için birkaç deney yapabiliriz.
threshold = 50.0  # Başlangıç değeri

while True:
    ret, res = cam.read()
    gri = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    yuzler = yuzcas.detectMultiScale(gri, 1.2, 5)

    for (x, y, w, h) in yuzler:
        cv2.rectangle(res, (x-20, y-20), (x+w+20, y+h+20), (0, 255, 0), 4)
        no, uyum = tani.predict(gri[y:y+h, x:x+w])

        # Eğer uyum değeri eşik değerinden düşükse, kişiyi tanırız
        if uyum < threshold:
            if no == 1:
                isim = "tunahan"
            elif no == 2:
                isim = "selen"
            elif no == 3:
                isim = "yunus"
            elif no == 4:
                isim = "mert"
            else:
                isim = "bilinmiyor"


            recognized_confidences.append(uyum)

            arduino.write(b'1')
            time.sleep(3)
            cam.release()
            cv2.destroyAllWindows()
            arduino.write(b'0')
            arduino.close()

        else:
            isim = "bilinmiyor"
            # Tanınmayan yüz algılandığında Arduino'ya komut gönder
            arduino.write(b'0')  # '0' komutunu Arduino'ya gönder, LED'i söndür

        # Eşik değerini dinamik olarak güncelleme
        if len(recognized_confidences) > 0:
            threshold = sum(recognized_confidences) / len(recognized_confidences) + 10  # Ortalama + 10

        cv2.rectangle(res, (x-22, y-90), (x+w+22, y-22), (0, 255, 0), -1)
        cv2.putText(res, isim, (x, y-40), font, 2, (255, 255, 255), 3)

    cv2.imshow('im', res)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break