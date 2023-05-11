from django.db import models

class Team(models.Model):
    city = models.CharField(max_length=100, help_text='Enter the city where the team is based.')
    mascot = models.CharField(max_length=100, help_text='Enter the team mascot name.')

    class Meta:
        unique_together = (('city', 'mascot'),)
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return f"{self.city} {self.mascot}"

class Player(models.Model):
    first_name = models.CharField(max_length=100, help_text='Enter the player\'s first name.')
    last_name = models.CharField(max_length=100, help_text='Enter the player\'s last name.')
    teams = models.ManyToManyField('Team', related_name='players')
    
    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.id:
            # Player is being created
            super().save(*args, **kwargs)
            self.teams.add(self.team)
        else:
            # Player is being updated
            super().save(*args, **kwargs)