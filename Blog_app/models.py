from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Technology(models.Model):
    class Meta:
        verbose_name_plural = "Technologies"
        verbose_name = "Technology"

    tech_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tech_name


class Post(models.Model):
    heading = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    technology_used = models.ForeignKey(Technology, on_delete=models.CASCADE)
    body = models.TextField()
    code = models.TextField(blank=True)
    image = models.ImageField(upload_to='media')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    post_view = models.IntegerField(default=0)
    link = models.TextField(max_length=600, blank=True)
    file = models.FileField(upload_to='files', blank=True)

    def __str__(self):
        return self.heading


class Profile(User):
    slug = models.SlugField(unique=True, editable=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    about = models.CharField(max_length=100, blank=False, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(max_length=8, blank=True, null=True, default=None)
    hobby = models.CharField(max_length=400, blank=True, null=True)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    mobile = models.CharField(max_length=10, blank=True, null=True, error_messages={'error': 'Check the number'})
    facebook = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    skills = models.ForeignKey(Technology, on_delete=models.CASCADE, blank=True, null=True)
    views = models.IntegerField(default=0, auto_created=True, editable=False)
    profile_image = models.ImageField(upload_to='profile', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(super(Profile, self).username)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:ProfileView', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(help_text='Add Comment')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.user_name)


class Sub_Comment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    sub_comments = models.TextField(help_text='Add Comment')

    def __str__(self):
        return self.sub_comments


class MyIntroduction(models.Model):
    img = models.ImageField(upload_to='profile')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class InterestingCorner(models.Model):
    class Meta:
        verbose_name = "Interesting Corner"
        verbose_name_plural = "Interesting Corners"

    heading = models.CharField(max_length=100, blank=True, null=True)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.heading
