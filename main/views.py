from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Koka Kola',
        'price': 5000,
        'description': 'Soda berkandungan gula tinggi yang siap memaniskan harimu',
        'stock' : 10
    }

    return render(request, "main.html", context)