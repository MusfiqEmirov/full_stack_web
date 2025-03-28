from django.db import models
from django.core.validators import MinLengthValidator


class Genre(models.Model):
    name = models.CharField(max_length=100) # janr modeli

    def __str__(self):
        return self.name


class Contact(models.Model): # elaqelernen bagli model
    adress = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return self.adress


class Person(models.Model): # sexsi heyyetle bagli model

    # sadece bas herfleri alib cinsi teyin etmek
    genders = (
        ("M","Male"),
        ("F","Female")
    )
    
    # sadece bas herfleri alib peweni  teyin etmek
    duty_types = (
        ("1","Crew"),
        ("2","Cast"),
        ("3","Director"),
        ("4","Writer"),
    )

    firts_name = models.CharField( max_length=50)   
    last_name =models.CharField(max_length=100)
    biograpyh = models.CharField(max_length=3000)
    image_name = models.CharField(max_length=100) 
    date_of_birth = models.DateField()
    gender = models.CharField("Cinsiyyet",max_length=1, choices=genders)
    duty_type = models.CharField("Vezife",max_length=1, choices=duty_types) 
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, blank=True, null=True)   # teke tek elaqe. bir sexsin 1 adresi ve her adresa bir sexs

    class Meta:
        verbose_name = "shexs" # clasin tekliyini ve cutluyuunu mueeyyen edir
        verbose_name_plural = "shexsler"

    @property
    def full_name(self): # bawligi ad soyad yazdirmagcun adminde
        return f"{self.firts_name}{self.last_name}"
    
    full_name.fget.short_description = "ad soyad"

    def __str__(self):
        duty_select_num = int(self.duty_type)-1 # nomreni aliriq
        duty_selected = self.duty_types[duty_select_num][1] #duty_typesden nomreye gore deyeri alib
        return f"{self.firts_name}{self.last_name} ({duty_selected})"
    

class Movie(models.Model): # filmlerin modeli
    title = models.CharField("bawliq",max_length=100)
    description = models.TextField(validators=[MinLengthValidator(20)])
    image_name = models.CharField(max_length=50)
    image_cover = models.CharField(max_length=50)
    date = models.DateField()
    slug = models.SlugField(unique=True, db_index=True)
    budget = models.DecimalField(max_digits=19, decimal_places=2)
    language = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    people = models.ManyToManyField(Person) # coxa cox elaqe.bir filmin cox persanali,persanalin ise cox filmi
    genres = models.ManyToManyField(Genre) # coxa cox elaqe.bir filmin cox janri,ferqli janrlarda da cox film


    class Meta:
        verbose_name = "film" # clasin tekliyini ve cutluyuunu mueeyyen edir
        verbose_name_plural = "filmler"

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)  
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)  # bire cox elaqe.1 filmin cox videosu ola biler

    def __str__(self):
        return self.title





