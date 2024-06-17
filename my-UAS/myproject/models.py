from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class License(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20)
    issued_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.license_number

class Course(models.Model):
    title = models.CharField(max_length=100)
    participants = models.ManyToManyField(Person, related_name='enrolled_courses')

    def __str__(self):
        return self.title
    
'relasi one-to-one, one-to-many, dan many-to-many dalam Django,'
'mari kita buat tiga tabel: User, Profile, dan Course.'
'Kita akan menggunakan User dan Profile untuk menunjukkan relasi one-to-one,'
'User dan Course untuk menunjukkan relasi many-to-many,'
'dan asumsi bahwa satu User dapat mendaftar ke banyak Course.'
'Untuk one-to-many, kita akan asumsikan bahwa setiap Course memiliki satu'
'Instructor (yang juga merupakan User), tetapi satu Instructor bisa mengajar banyak Course.'

'Relasi One-to-One (Profile ke User):'
'Relasi ini digunakan untuk menambahkan informasi tambahan tentang User.' 
'Setiap User hanya bisa memiliki satu Profile, dan setiap Profile hanya'
'terkait dengan satu User. Ini berguna untuk kasus-kasus seperti menyimpan' 
'bio, foto profil, atau informasi lain yang spesifik untuk setiap pengguna.' 
'Relasi ini dibuat dengan OneToOneField.'

'Relasi Many-to-Many (Course ke User melalui students):'
'Relasi ini memungkinkan banyak User (dalam hal ini, students)'
'untuk mendaftar di banyak Course. Sebuah Course bisa diambil' 
'oleh banyak students, dan satu User bisa mendaftar di banyak Course.'
'Ini menunjukkan relasi many-to-many yang khas, dimana tidak ada batasan' 
'jumlah Course yang bisa diikuti oleh User atau jumlah User yang bisa' 
'mendaftar di Course. Relasi ini dibuat dengan ManyToManyField.'

'Relasi One-to-Many (Course ke User melalui instructor):'
'Setiap Course memiliki satu instructor (yang merupakan User),' 
'tetapi satu instructor bisa mengajar lebih dari satu Course.' 
'Ini adalah contoh dari relasi one-to-many. Dalam Django, relasi'
'ini diimplementasikan menggunakan ForeignKey di sisi Course. Ini' 
'menunjukkan bahwa setiap baris di tabel Course mengacu pada baris'
'di tabel User, tetapi satu User bisa diacu oleh banyak baris di tabel Course.'