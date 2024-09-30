from django.db import models

class LunchMenu(models.Model):
    Week = models.CharField(
        max_length=6,
        choices=[
            ('week1', 'week1'),
            ('week2', 'week2'),
            ('week3', 'week3'),
            ('week4', 'week4')
        ]
    )
    Day = models.CharField(
        max_length=15,
        choices=[
            ('monday', 'monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday')
        ]
    )
    Menu = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.Week} - {self.Day}"
