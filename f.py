import random
import time

def hazne_doldur():
    """Hazneye rastgele bir mermi yerleştirir (1-6)."""
    return random.randint(1, 6)

def ates_et(mermi_pozisyonu, hazne_index):
    """Tetik çekildiğinde mermi çıkıp çıkmadığını kontrol eder."""
    return mermi_pozisyonu == hazne_index

def oyuncu_sec(aktif_oyuncular, ates_eden):
    """Tetik çeken oyuncu hariç rastgele bir hedef seçer."""
    hedefler = [o for o in aktif_oyuncular if o != ates_eden]
    return random.choice(hedefler)

def rus_ruleti():
    oyuncular = [f"Oyuncu{i+1}" for i in range(6)]
    mermi = hazne_doldur()
    hazne_index = 1

    print("Rus Ruleti başlıyor!")
    print("Mermi rastgele yerleştirildi.\n")

    while len(oyuncular) > 1:
        for oyuncu in list(oyuncular):
            if len(oyuncular) == 1:
                break

            hedef = oyuncu_sec(oyuncular, oyuncu)
            print(f"{oyuncu}, {hedef} kişisine silah doğrultuyor.")
            time.sleep(1)

            if ates_et(mermi, hazne_index):
                print(f"Bum! {hedef} vuruldu.")
                oyuncular.remove(hedef)
                # Yeni mermi yerleştir
                mermi = hazne_doldur()
                hazne_index = 0  # yeni tur başlat
            else:
                print("Tetik çekildi ama silah boş!")
            
            # Hazneyi sıradaki pozisyona çevir
            hazne_index = (hazne_index % 6) + 1

    print(f"\nHayatta kalan tek kişi: {oyuncular[0]}")

if __name__ == "__main__":
    rus_ruleti()

            
        