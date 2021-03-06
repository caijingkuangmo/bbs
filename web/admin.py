from django.contrib import admin
import models
# Register your models here.

class Category_admin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(models.Article)
admin.site.register(models.ArticleHref)
admin.site.register(models.ArticlePicture)
admin.site.register(models.Category,Category_admin)
admin.site.register(models.Comment)
admin.site.register(models.ThumbUp)
admin.site.register(models.UserGroup)
admin.site.register(models.UserProfile)
