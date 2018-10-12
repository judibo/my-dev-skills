from django.db import models
from django.contrib.auth.models import User

SKILL_LEVEL = (
    (1, 'Fundamental Awareness'),
    (2, 'Novice'),
    (3, 'Intermediate'),
    (4, 'Advanced'),
    (5, 'Expert'),
)

# Create your models here.
class Skill(models.Model):
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_level = models.IntegerField(
        choices=SKILL_LEVEL,
        default=SKILL_LEVEL[0][0]
    )

