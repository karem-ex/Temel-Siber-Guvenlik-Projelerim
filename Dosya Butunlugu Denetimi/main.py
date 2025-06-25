from functions import *


# Ana program:
if __name__ == "__main__":
    print("""### Hash kontrol programına hoşgeldiniz ###
          İşlemler:
          1- Dosya Oluşturma
          2- Dosya Kontrol
          3- Çıkış
          """)

    # Kullanıcıdan işlem seçmesini istiyoruz
    process = input("Bir işlem seçiniz (1/2/3): ")

    try:
        if process == "1":
            # Dosya ismini alalım
            file_path = input("Dosyanızın ismini yazınız: ")
            signature = create_file_signature(file_path)
            if signature:
                print(f"Dosyanın imzası (hash değeri): {signature}")
                # Dosyayı hash_table.txt dosyasına kaydedelim.
                create_hash_table(file_path)
            else:
                print("Dosya bulunamadı...")

        elif process == "2":
            # Hash kontrolü yapmak için dosya ismini alalım
            file_path = input(
                "Kontrol etmek istediğiniz dosyanın ismini yazınız: ")

            # hash_table.txt dosyasını açalım
            with open('hash_table.txt', 'r', encoding='utf-8') as f:
                # Dosyayı satır satır okuyalım
                found = False
                for line in f:
                    # Hash ve dosya ismini regex ile ayıralım
                    match = re.match(r'(.+):\s*([a-f0-9]{64})', line.strip())
                    if match:
                        dosya_ismi = match.group(1)  # Dosya ismi
                        hash_degeri = match.group(2)  # Hash değeri
                        if dosya_ismi == file_path:
                            found = True
                            print(f"Dosya İsmi: {dosya_ismi}")
                            print(f"Hash Değeri: {hash_degeri}\n")

                            # Dosyanın bütünlüğünü kontrol edelim
                            check_file_integrity(dosya_ismi, hash_degeri)
                            break
                if not found:
                    print(
                        f"{file_path} dosyası hash_table.txt dosyasında bulunamadı.")

        elif process == "3":
            print("Çıkılıyor...")

        else:
            print("Lütfen geçerli bir işlem giriniz!!!")

    except FileNotFoundError:
        print("Dosyanız bulunamadı.")
