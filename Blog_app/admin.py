from django.contrib import admin
from .models import Post, Profile, Comment, Technology, MyIntroduction, InterestingCorner

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Technology)
admin.site.register(MyIntroduction)
admin.site.register(InterestingCorner)
