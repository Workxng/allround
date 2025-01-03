from django.shortcuts import render, get_object_or_404, redirect
from .models import Wisata, Review

# Create your views here.
def home(request):
    searchNama = request.GET.get('nama')
    if searchNama:
        wisatas = Wisata.objects.filter(nama__icontains=searchNama)
    else:
        wisatas = Wisata.objects.all()
    return render(request, 'home.html', {'searchNama':searchNama,'wisatas' : wisatas})

def about(request):
    return render(request,'about.html')

def detail(request, wisata_id):
    wisata = get_object_or_404(Wisata, pk=wisata_id)
    reviews = wisata.reviews.all()

    if request.method == 'POST':
        nama = request.POST.get('nama')
        keterangan = request.POST.get('keterangan')
        rating = request.POST.get('rating')

        # Validasi manual
        if not nama or not rating:
            return render(request, 'detail.html', {
                'wisata': wisata,
                'reviews': reviews,
                'error': "Nama dan rating harus diisi!",
            })

        # Simpan review ke database
        Review.objects.create(
            nama=nama,
            keterangan=keterangan,
            rating=rating,
            wisata=wisata
        )
        return redirect('detail', wisata_id=wisata.pk)

    context = {
        'wisata': wisata,
        'reviews': reviews,
    }
    return render(request, 'detail.html', context)
