import tkinter as tk  # Tkinter kütüphanesini GUI oluşturmak için kullandık
from tkinter import messagebox  
import networkx as nx  # NetworkX kütüphanesini grafı oluşturmak için kullandık
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini graf çizimi için kullandık

# n-küp graf çizen fonksiyonun komutları
def n_kupu_ciz(n):
    G = nx.hypercube_graph(n)  # n-küp grafı oluşturan komut
    pozisyon = nx.spring_layout(G)  # Graf düğümlerinin konumunu belirleyen komut
    plt.figure(figsize=(8, 8))  # Graf için bir figür oluşturan komut
    nx.draw_networkx_nodes(G, pozisyon, node_size=800, node_color='yellow')  # Graf düğümlerini çizen komut
    nx.draw_networkx_edges(G, pozisyon, width=2)  # Graf kenarlarını çizmesini sağlayan komut
    nx.draw_networkx_labels(G, pozisyon, font_size=20, font_color='black')  # Graf etiketlerini çizen komut
    plt.title(f"{n}-Küp Grafiği")  # Grafa başlık ekleyen komutu
    plt.show()  # Grafı gösteren komut

# Buton tıklama olayını işleyen fonksiyonun komutları
def ciz_buton_tiklama():
    try:
        n = int(giris.get())  # Kullanıcıdan girilen değeri alan ve tamsayıya çeviren komut
        if n < 0:  # Negatif sayı kontrolü yapan komut
            raise ValueError("Sayı negatif olmamalı.")  # Hata mesajı komutu
        n_kupu_ciz(n)  # n-küp grafi çizen komut
    except ValueError as e:  # Hata yakalama komutu
        messagebox.showerror("Geçersiz Giriş", str(e))  # Hata mesajı gösteren komut

# Tkinter ana pencereyi oluşturan komutlar
kok = tk.Tk()
kok.title("n-Küp Grafiği Çizici")  

# Ana çerçeve oluşturan ve yerleştiren komut
cerceve = tk.Frame(kok)
cerceve.pack(padx=10, pady=10) 

# Kullanıcıya talimat veren bir etiket oluşturan komut
etiket = tk.Label(cerceve, text="küp grafı oluşturmak için bir sayı girin:")
etiket.pack(pady=5)  

# Kullanıcıdan giriş almak için bir giriş kutusu oluşturmasını sağlayan komut
giris = tk.Entry(cerceve)
giris.pack(pady=5)

# Grafı çizmek için bir buton oluşturan komutlar
buton = tk.Button(cerceve, text="Grafı oluştur", command=ciz_buton_tiklama)
buton.pack(pady=5) 

# Tkinter ana döngüsünü başlatan komut
kok.mainloop()