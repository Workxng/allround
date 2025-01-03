from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Wisata(models.Model):
    nama = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=100)
    deskripsi = models.TextField(max_length=1000)
    gambar = models.ImageField(upload_to='wisata', null=True, blank=True)

    def __str__(self):
        return f"{self.nama}"
    
class Review(models.Model):
    wisata = models.ForeignKey(Wisata, related_name='reviews', on_delete=models.CASCADE, default=1)
    nama = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True, null=True)  # Komentar review
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Validasi 1-5
        help_text="Rating dari 1 sampai 5"
    )

    def __str__(self):
        return f"{self.wisata} - {self.rating}" 