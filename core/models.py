import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



def profile_image_upload_path(instance, filename):
    return f"profile_pic/{instance.user.username}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(blank=True)
    user_img = models.ImageField(upload_to=profile_image_upload_path, default='blank-profileimg.png')
    user_dob = models.DateField(null=True, blank=True)
    # slug = models.SlugField(unique=True, null=False)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.user.username)
    #     super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


def post_pic_image_upload_path(instance, filename):
    return f"post_pic/{instance.user.username}/{filename}"

class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_img=models.ImageField(upload_to=post_pic_image_upload_path, default='blank-profileimg.png')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"
