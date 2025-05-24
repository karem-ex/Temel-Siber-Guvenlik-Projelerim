from password_check import check_password_strength,flag
from estimate_crack_password import estimate_crack_time

print("""
    Parola Güçlülük Kontrol Aracına Hoşgeldiniz.
    
    Amacımız: Kullanıcının girdiği şifrenin güvenli olup olmadığını analiz eden bir araç. 
    Uzunluk, karakter çeşitliliği (büyük harf, küçük harf, sayı, sembol), sözlükte olup olmama gibi kriterlere bakar.
    """)

while flag:

    choice = input("""
    Lütfen bir seçim yapınız
    1- Parola Kontrol
    2- Parola Test Etme
    Aracımızdan çıkmak için 'q' yada 'quit' yazıp çıkabilirsiniz....
    ---> """)
    
    if choice.lower() == 'q' or choice.lower() == 'quit':
        flag = False
    elif choice == '1':
        get_password = input("Lütfen parolanızı yazınız: ")
        print(check_password_strength(get_password))
    elif choice == '2':
        get_password = input("Lütfen parolanızı yazınız: ")
        print("Kırılma Süresi:",estimate_crack_time(get_password))
    else:
        print("Lütfen 1 veya 2 seçeneklerinden birini seçin...")
        continue
    
    
