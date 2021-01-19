from django.db import models

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=300)

    def __str__(self):
        return self.tag


class Items(models.Model):
    title = models.CharField(max_length=20, blank=False)
    price = models.IntegerField(default=0, null=False)
    image = models.ImageField(
        blank=False, upload_to="images", default="default.jpg")
    tags = models.ManyToManyField(Tag, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    owner = models.ForeignKey(
        'auth.user', related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
