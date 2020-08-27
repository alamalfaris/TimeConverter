def timeconverter(second):
    if (type(second) != int or type(second) == float or type(second) == str or second > 359999): # Buat pengkondisian jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, maupun memasukkan string
        return 'Invalid input!'                                           # Maka, akan keluar notifikasi. Invalid Input
    else:
        second = second % (24 * 3600)  # Untuk mengkonvert input detik lebih dari 86.400   
        hour = second // 3600          # Mengkonvert dari satuan detik ke satuan jam 
        second = second % 3600         # Untuk mengkonvert input detik supaya menjadi lebih kecil dari konvert detik sebelumnya
        minute = second // 60          # Mengkonvert satuan detik menjadi satuan menit
        second = second % 60           # Mengkonvert detik menjadi lebih kecil lagi dari sebelumnya karena range digit hanya 00-59
        return 'Konversi : %02d:%02d:%02d' % (hour, minute, second)   # Mengembalikan nilai dalam string dengan format jam, menit, dan detik. Dimana masing2 satuan memiliki 2 digit angka
    
detik = int(input('Masukkan detik: '))
print(timeconverter(detik))