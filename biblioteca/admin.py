from django.contrib import admin
from biblioteca.models import Editor, Autor, Libro


# Register your models here.
# admin.site.register(Editor)
# admin.site.register(Autor)
# admin.site.register(Libro)

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email')
    search_fields = ('nombre', 'apellidos')


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editor', 'fecha_publicacion')
    list_filter = ('fecha_publicacion',)
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)
    # fields = ('titulo', 'autores', 'editor', 'portada')
    filter_horizontal = ('autores',)
    raw_id_fields = ('editor',)


admin.site.register(Editor)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
