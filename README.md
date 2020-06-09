# executable_file
Python dosyalarınızı çalıştırılabilir dosyalar yapabilirsiniz.

#açıklama
Pythonda yazmış olduğunuz kodlarınızı uygulamaya dönüştürmek istiyorsanız bu kodları kullanabilirsiniz.

Bunun için konsolunuzda ilgili dosyanın altına gidip komut satırına "python setup.py build" yazmanız yeterli olacaktır.
Modul hatası alıyorsanız ilgili modülleri komut satırından kurup devam edebilirsiniz.
Hatasız bir şekilde kodu çalıştırdığınızda bulunduğunuz klasör altında build adında klasör oluşmuş olduğunu göreceksiniz.
"build\exe.win-amd64-3.6\" klasörü altında uygulama haline gelen -python_file- adında dosya oluşacaktır.
"python-file" uygulamasına çift tıkladığında hata alıyorsanız bu hatanın nedeni version farklılıklarıdır.
Version farklılıklarında küçük-büyük harf hatasına çok rastlayabilirsiniz.

Genellikle verdiği benim karşılaştığım 2 hata şöyledir:
* "cKDTree.cp36-win_amd64" dosyasını bulamaması
* "tkinter" dosyasını bulamaması

- "cKDTree.cp36-win_amd64" hatasını düzeltirken yapılması gereken;
"build\exe.win-amd64-3.6\lib\scipy\spatial" dosyası içindeki -> "cKDTree.cp36-win_amd64" dosyasının adını "ckdtree.cp36-win_amd64 olarak değiştirilmesi sorunu çözecektir.

- "tkinter" hatasını çözerkense yine;
"build\exe.win-amd64-3.6\lib" içindeki "Tkinter" -> "tkinter" olarak değiştir.

İsim değişikliği sonrasında benim yaşadığım problemler çözüldü.

*base="Win32GUI"* konsol loglarını açıp kapatmaya yarıyor. Eğer *base = "Win32GUI"* ise konsol logları kapalı olacaktır.
