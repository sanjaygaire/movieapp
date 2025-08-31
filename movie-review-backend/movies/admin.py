from django.contrib import admin

from movies.models import Review,   Movie
admin.site.register(Movie)
admin.site.register(Review)
