from django.contrib import admin
from .models import Location, Conteiner, Food, Tag, Clothe, Medicine

admin.site.register(Location)
admin.site.register(Conteiner)
admin.site.register(Clothe)
admin.site.register(Medicine)
admin.site.register(Food)
admin.site.register(Tag)

