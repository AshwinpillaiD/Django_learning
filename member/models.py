from django.db import models
from django.contrib.auth.models  import User
from datetime import date

# Create your models here.
class Blogmodel(models.Model):
    name=models.CharField(max_length=49)
    author=models.ForeignKey(User, verbose_name="Name", on_delete=models.SET_NULL ,null=True)
    description=models.TextField(help_text="Write your Blog")
    post_at=models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.name +"->"+str(self.author)

class Blog_commmad(models.Model):
    description=models.TextField(help_text="Write your command")
    author=models.ForeignKey(User, verbose_name="Name", on_delete=models.SET_NULL ,null=True)
    commited_date=models.DateField( auto_now_add=True)
    bolg=models.ForeignKey(Blogmodel, verbose_name=("Blog"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.author)
