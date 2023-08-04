from django.db import models
from django.urls import reverse

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)

DIFFICULTY = (
    ("VE", "Very Easy"),
    ("E", "Easy"),
    ("M", "Medium"),
    ("H", "Hard"),
    ("VH", "Very Hard"),
)


# Create your models here.
class Trick(models.Model):
    name = models.CharField(max_length=20)
    difficulty = models.CharField(
        max_length=2,
        choices=DIFFICULTY,
        default="vh",
    )

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("tricks_details", kwargs={"pk": self.id})


class Dog(models.Model):
    name = models.CharField(max_length=20)
    breed = models.CharField(max_length=50)
    behavior = models.TextField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=8, choices=GENDER, default="male")
    tricks = models.ManyToManyField(Trick)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("details", kwargs={"dog_id": self.id})


class Playdate(models.Model):
    date = models.DateTimeField("Schedule Play Date(use yyyy/mm/dd 00:00)")
    length = models.IntegerField("How many hours")
    name = models.CharField("Your Name", max_length=30)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} is going to take them on {self.date}"

    class Meta:
        ordering = ["-date"]
