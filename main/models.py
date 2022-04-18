from django.db import models

class RepoInformation(models.Model):
    """
    The scrapped data will be saved in this model
    """
    name_project = models.CharField(max_length=100)
    all_repos = models.SmallIntegerField()
    #average_stars = models.IntegerField()

