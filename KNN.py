import random
import math

noktalar = [] # Noktaların Oluşturulması
              # Creating Points
for _ in range(16):
    x = random.uniform(0, 5)
    y = random.uniform(0, 5)
    noktalar.append((x, y))
    
sonuclar = {} # Noktaların Birbirlerine Olan Uzaklıklarının Ölçülmesi ve Komşuları İle Eşleştirilmesi
              # Measuring the Distances of Points from Each Other and Matching them with Their Neighbors
for i, nokta1 in enumerate(noktalar):
    mesafeler = []
    for j, nokta2 in enumerate(noktalar):
        if i != j: 
            mesafeler.append((j, math.sqrt((nokta1[0] - nokta2[0])**2 + (nokta1[1] - nokta2[1])**2))) # Noktalar arasındaki mesafeyi ölçen fonksiyon
                                                                                                      # Function that measures the distance between points
    mesafeler.sort(key=lambda x: x[1])
    eyk = mesafeler[:3]
    sonuclar[i] = [komsu[0] for komsu in eyk]   

# Bütün Sonuçların Yazdırılması
# Printing All Results
print("Noktaların Konumları:") # Noktaların Konumlarının Yazdırılması
                               # Printing the Locations of Points 
for i, nokta in enumerate(noktalar):
    print(f"{i}.Nokta: ({nokta[0]:.2f}, {nokta[1]:.2f})") # Noktaların konumlarının ekrana yazdırılması
                                                          # Printing the positions of the points on the screen
    
print("\nEn Yakın Komşular:") # Noktaların Komşularının Yazdırılması
                              # Printing Neighborhoods of Points
for nokta_id, komsular in sonuclar.items():
    print(f"{nokta_id}.Nokta için en yakın 3 komşu:{komsular}") # Noktaların komşularının ekrana yazdırılması
                                                                # Printing neighbors of points to the screen
    
    
    
    
    
    
    
    
import matplotlib.pyplot as plt

# Noktaları ve bağlantıları görselleştir
plt.figure(figsize=(8, 8))
plt.title("Noktalar ve En Yakın Komşuları")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")

# Noktaları çiz
for i, nokta in enumerate(noktalar):
    plt.scatter(nokta[0], nokta[1], label=f"Nokta {i}", s=50)
    plt.text(nokta[0] + 0.1, nokta[1], f"{i}", fontsize=9)

# Komşularla bağlantı çizgileri çiz
for nokta_id, komsular in sonuclar.items():
    for komsu_id in komsular:
        nokta1 = noktalar[nokta_id]
        nokta2 = noktalar[komsu_id]
        plt.plot([nokta1[0], nokta2[0]], [nokta1[1], nokta2[1]], 'r--', linewidth=0.8)

# Görselleştirme
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
