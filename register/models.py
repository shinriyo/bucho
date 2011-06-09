from django.db import models

class User(models.Model):
    class Admin:
        pass

    name = models.CharField(maxlength=1024)
    introduction = models.TextField(blank=True, maxlength=8192)
    image = models.ImageField(blank=True, upload_to='image')
    from_year = models.IntegerField(null=True)
    web = models.URLField(blank=True, maxlength=8192)
    blog = models.URLField(blank=True, maxlength=8192)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "name=\"%s\", introduction=\"%s\", from_year=%d, web=\"%s\", blog=\"%s\")" % (self.name, self.introduction, self.from_year, self.web, self.blog)

