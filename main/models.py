import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    Represents a question in a poll.
    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime): The date and time when the question was published.
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        Returns True if the object's publication date is within
        the last 24 hours.

        Returns:
            bool: True if published within the last day, False otherwise.
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """
    Represents a choice for a question in a poll.
    Attributes:
        question (Question): The question this choice belongs to.
        choice_text (str): The text of the choice.
        votes (int): The number of votes this choice has received.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
