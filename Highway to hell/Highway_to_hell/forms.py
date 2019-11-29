from django.forms import ModelForm
from django import forms
from Highway_to_hell.models import Highway,UserWant
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5)
)


class CheckForm(ModelForm):
    class Meta:
        model = UserWant
        fields = ['startDate', 'start_point', 'finish_point']
        labels = {
            'start_point': _('출발지'),
            'finish_point': _('도착지'),
        }
        help_texts = {
            'start_point': _('출발지을 입력해주세요.'),
            'finish_point': _('도착지를 입력해주세요.'),
        }
