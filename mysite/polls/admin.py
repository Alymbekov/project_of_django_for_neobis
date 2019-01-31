from django.contrib import admin
from .models import Question,Choice

class ChoiceInlines(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [

        (None,              {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),


    ]

    inlines = [ChoiceInlines]

admin.site.register(Question,QuestionAdmin)


# Register your models here.
