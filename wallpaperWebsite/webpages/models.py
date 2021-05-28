from django.db import models

class Design(models.Model):
    design_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="media/team/%Y/%m/",null=True)
    description = models.TextField()

    def __str__(self):
        return self.design_name

    def get_absolute_url():
        return reverse('webpage_view', args=[str(self.id)])