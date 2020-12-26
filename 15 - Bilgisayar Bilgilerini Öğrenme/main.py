# coding=utf-8

"""
    Bilgisayar bilgilerini öğrenme
    Bu benim bilgisayarım için doğru bir şekilde çalıştı.
    Ama sizin bilgisayarınızda farklılık gösterebilir veya çalışmayadabilir.
    Eğer Ubuntu kullanıyorsanız %75 doğru çalışacaktır.

"""

import platform as b 
                
print(b)
print("""
    İşletim sistemi : {}   
    Bilgisayar adı  : {}
    Sürüm           : {}
    Sürüm tarihi    : {}
""".format(
    b.system(),  # burayı kestim
    b.node(),    # sadece node kullandım
    b.release(), # burası ve alt satır aynı kalıyor
    b.version))   

"""
    Uygulamayı çalıştırdığınızda böyle bir sonuç elde etmeniz lazım

    İşletim sistemi : Linux x86_64
    Bilgisayar adı  : l50a1d2
    Sürüm           : 4.13.0-36-generic
    Sürüm tarihi    : #40-Ubuntu SMP Fri Feb 16 20:07:48 UTC 2018

"""
