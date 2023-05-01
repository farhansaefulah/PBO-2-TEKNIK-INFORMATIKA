data_files = ["file_1.txt", "file_2.txt", "file_3.txt", "file_4.txt"]
for nama_file in data_files:
    try:
        with open(nama_file) as file:
            data = file.read()
    except FileNotFoundError:
        print("File", nama_file, "tidak ditemukan!")