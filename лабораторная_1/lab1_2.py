disk_volume_mb = 1.44 # MB
pages_per_book = 100
lines_per_page = 50
symbols_per_line = 25
symbol_volume = 4 # bytes

disk_volume_b = 1.44 * 1024 * 1024
symbols_per_book = symbols_per_line * lines_per_page * pages_per_book
book_volume = symbols_per_book * symbol_volume
books_per_disk = int(disk_volume_b / book_volume)
print("Количество книг, помещающихся на дискету:", books_per_disk)
