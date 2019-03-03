# This script is called by initialize_mode.sh

from polls.models import Choice, Question
from django.utils import timezone

q = Question(question_text="What's up?", pub_date=timezone.now())
q.save()

q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
q.choice_set.create(choice_text='Just hacking again', votes=0)