from django.contrib import admin
from movie.models import Movie, Genre, Person, Contact, Video

class MovieAdmin(admin.ModelAdmin): # adminde Movie cedvelinin grorunusu
    list_display = ("title","is_active", "is_home",) # bawliq activler
    prepopulated_fields = {"slug": ("title",)} # avto slug yaratmag
    list_filter = ("genres", "language", "is_active", "is_home",) # neye gore filter elemek
    search_fields = ("title", "description",) # neye gore axtariw

class PersonAdmin(admin.ModelAdmin): # adminda Person cedvelninin gorunusu
    list_display = ("full_name","gender","duty_type",) # property olaraq aldiq full name olaraq geri qaytaririq 
    list_filter = ("gender","duty_type",) # cinse ve vezifeye gore flterleme
    search_fields = ("firts_name", "last_name",) # ada ve soyada gore filtl=


admin.site.register(Movie,MovieAdmin)
admin.site.register(Genre)
admin.site.register(Person, PersonAdmin)
admin.site.register(Contact)
admin.site.register(Video)


