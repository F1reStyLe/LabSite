from django.contrib import admin
from .models import *


@admin.register(Base)
class AdminBase(admin.ModelAdmin):
    pass


@admin.register(Analysis)
class AdminAnalysis(admin.ModelAdmin):
    pass

@admin.register(PigmentGroup)
class AdminPigmentGroup(admin.ModelAdmin):
    pass


@admin.register(Pigment)
class AdminPigment(admin.ModelAdmin):
    pass


@admin.register(PigmentPaste)
class AdminPigmentPaste(admin.ModelAdmin):
    pass


@admin.register(Enamel)
class AdminEnamel(admin.ModelAdmin):
    pass
