from django.contrib import admin

from .models import News,Donat,Elderly,Archive,VideoGalary,PhotoGalary,Comment,Partners,Organizers

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['id','title','description','image','created']

@admin.register(Donat)
class AdminDonat(admin.ModelAdmin):
    list_display = ['id','title','body','image','created']


@admin.register(Elderly)
class AdminElderly(admin.ModelAdmin):
    list_display = ['id','name','surname','this_born','born_place']
            


@admin.register(Archive)
class AdminArchive(admin.ModelAdmin):
    list_display = ['id','name','surname','this_born','born_place']
            

@admin.register(VideoGalary)
class AdminVideoGalary(admin.ModelAdmin):
    list_display = ['id','video_title']
    


@admin.register(PhotoGalary)
class AdminPhotoGalary(admin.ModelAdmin):
    list_display = ['id','photo_title']

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['id','comment_name','comment']
    


@admin.register(Partners)
class AdminPartners(admin.ModelAdmin):
    list_display = ['id','partner_title']


@admin.register(Organizers)
class AdminOrganizers(admin.ModelAdmin):
    list_display = ['id','organ_name']
    