class TangaBank:
    def __init__(self, birinchi="person_1", ikkinchi="person_2"):
        self.birinchi = birinchi
        self.ikkinchi = ikkinchi

        self.mavjud_1 = 3
        self.mavjud_2 = 3
        print("Qurilma ishga tushdi !\n")

    def name_input(self):
        """Odamlarning ismlarini kiritish."""
        self.birinchi = input("Birinchi inson ismi : ")
        self.ikkinchi = input("Ikkinchi inson ismi : ")

    def share_or_steal(self, harakat1, harakat2):

        for i in range(len(harakat1)):

            if harakat1[i] == 'share' and harakat2[i] == 'share':
                self.mavjud_1 += 2
                self.mavjud_2 += 2
            elif harakat1[i] == 'share' and harakat2[i] == 'steal':
                self.mavjud_1 -= 1  
                self.mavjud_2 += 3  
            elif harakat1[i] == 'steal' and harakat2[i] == 'share':
                self.mavjud_1 += 3  
                self.mavjud_2 -= 1  
            elif harakat1[i] == 'steal' and harakat2[i] == 'steal':
                self.mavjud_1 += 0  
                self.mavjud_2 += 0
            else:
                print("Xato kiritilgan!!!")
                return False   
        
    def print_natija(self):
        """Natijalarni chop etish."""
        print(f"{self.birinchi} da {self.mavjud_1} ta tanga!")
        print(f"{self.ikkinchi} da {self.mavjud_2} ta tanga!")


tanga = TangaBank()

while True:
    tanga.name_input()

    
    harakat1 = input(f"\n{tanga.birinchi} 'share' yoki 'steal': ").split(" ")
    harakat2 = input(f"\n{tanga.ikkinchi} 'share' yoki 'steal': ").split(" ")

    
    tanga.share_or_steal(harakat1, harakat2)

    
    tanga.print_natija()

    
    print("\n[1] - Davom etish")
    print("[0] - To'xtatish")
    a = int(input("Tanlang: "))

    if a == 1:
        continue
    elif a == 0:
        print("Dastur yakunlandi.")
        break
    else:
        print(f"Not found: {a}. Xato ma'lumot kiritilgan!")
