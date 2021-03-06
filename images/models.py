from django.db import models
from PIL import Image
from django.utils.timezone import now


class Images(models.Model):
    image = models.ImageField(upload_to="photos/", blank=True, null=True)
    pub_date = models.DateTimeField("Дата публикации", default=now, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.weight > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
