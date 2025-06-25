import os
import hashlib
import re


# Dosya imzalama (hash değeri oluşturma)
def create_file_signature(file_path):
    """Verilen dosya için bir hash değeri oluşturur ve döndürür."""
    if not os.path.isfile(file_path):  # Dosya var mı kontrol et
        print(f"Dosya bulunamadı: {file_path}")
        create_file(file_path)  # Dosya yoksa oluştur
        # Dosya oluşturulup hash değeri hesaplanır
        return create_file_signature(file_path)

    hash_object = hashlib.sha256()  # SHA-256 algoritması
    try:
        with open(file_path, 'rb') as f:  # Dosyayı binary modda aç
            while chunk := f.read(4096):  # Dosyayı parça parça oku
                hash_object.update(chunk)  # Hash değerini güncelle
        return hash_object.hexdigest()  # Hash değerini hexadecimal formatında döndür
    except Exception as e:
        print(f"Dosya okuma hatası: {e}")
        return None


# Dosya oluşturma fonksiyonu (yeni dosya oluşturur ve içerik ekler)
def create_file(file_name: str) -> str:
    """Dosya oluşturur ve içerisine bir metin ekler."""
    if file_name:
        try:
            # 'w' modu dosyayı sıfırlar ve içerik ekler
            with open(file_name, mode="w", encoding="utf-8") as f:
                print(f"{file_name} ismindeki dosyanız oluşturuldu.")
        except Exception as e:
            print(f"Dosya oluşturulamadı: {e}")
    return file_name


# Hash dosyası oluşturma fonksiyonu (dosyaları kaydeder)
def create_hash_file(file_name: str) -> str:
    """Hash dosyası oluşturur ve içerisine bir metin ekler."""
    try:
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write("Hash dosyası oluşturuldu.\n")  # İçerik ekleyin
            print(f"{file_name} ismindeki dosyanız oluşturuldu.")
    except Exception as e:
        print(f"Hash dosyası oluşturulamadı: {e}")
    return file_name


# Hash değerlerini ve dosya adlarını hash_table.txt dosyasına kaydetme
def create_hash_table(file_name: str):
    if not os.path.isfile('hash_table.txt'):
        create_hash_file('hash_table.txt')  # Hash dosyası yoksa oluşturulmalı

    try:
        hash_value = create_file_signature(file_name)
        if hash_value:  # Hash değeri oluşturulmuşsa
            with open("hash_table.txt", mode="a", encoding="utf-8") as f:
                f.writelines(f"{file_name}: {hash_value}\n")
                print(f"{file_name} dosyasının hash değeri kaydedildi.")
        else:
            print(f"{file_name} için hash değeri oluşturulamadı.")
    except Exception as e:
        print(f"Hash tablo dosyasına yazma hatası: {e}")


# Dosya bütünlüğünü kontrol etme
def check_file_integrity(file_path, original_hash):
    """Verilen dosyanın hash değerini kontrol eder."""
    current_hash = create_file_signature(
        file_path)  # Dosyanın güncel hash değerini al
    if current_hash is None:
        print(f"Dosya bulunamadı: {file_path}. Bütünlük kontrolü yapılamaz.")
        return False  # Dosya yoksa, bütünlük kontrolü yapılamaz
    elif current_hash == original_hash:
        print("Değişiklik yapılmamış.")
        return True  # Hash değerleri eşleşiyorsa, dosya değişmemiştir
    else:
        print(f"Değişiklik yapılmış.\nYeni hash değeri {current_hash}")
        return False  # Hash değerleri eşleşmiyorsa, dosya değiştirilmiş demektir
    

