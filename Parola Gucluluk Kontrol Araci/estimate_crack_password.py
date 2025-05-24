import math as m
import re as r

def estimate_crack_time(password_ : str):
    # Parolanın kırılma süresini döndürür.
    charset_size = 0
    
    if r.search(r'[a-z]',password_):
        charset_size += 26
    if r.search(r'[A-Z]', password_):
        charset_size += 26
    if r.search(r'[0-9]', password_):
        charset_size += 10
    if r.search(r'[\W]', password_):
        charset_size += 33
    
    total_combinations = charset_size ** len(password_)
    
    guesses_per_second = 1e9 # saniyede 1 milyar parola deneme
    
    seconds = total_combinations / guesses_per_second
    
    return format_time(seconds)


def format_time(seconds):
    if seconds < 1:
        return "1 saniyeden az!"
    intervals = (
        ('yıl', 31536000), # 1 yıl
        ('gün', 86400), # 1 gün
        ('saat', 3600), # 1 saat
        ('dakika', 60), # 1 dakika 
        ('saniye', 1),  # 1 saniye
    )
    
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append(f"{int(value)} {name}")
    return ', '.join(result)
