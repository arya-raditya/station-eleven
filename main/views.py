from django.shortcuts import render

def show_main(request):
    context = {
        'shop_name' : 'Station Eleven',
        'name' : 'Arya Raditya Kusuma',
        'class' : 'PBP F',

        'nama_prod' : 'KokaKola',
        'harga_prod' : 5000,
        'deskripsi_prod' : 'soda dengan kandungan gula tinggi cocok utk pengidap diabetes'
    }

    return render(request, "main.html", context)