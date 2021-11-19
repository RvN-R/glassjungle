from django.test import TestCase
from .forms import CreateRatingForm


class TestCreateRatingForm(TestCase):

    def test_create_rating_form_valid(self):
        form = CreateRatingForm(
            {"comment": "TestComment", "rating": "4"}
        )
        self.assertTrue(form.is_valid())

    def test_comment_error_returned(self):
        form = CreateRatingForm(
            {"comment": "", "rating": "4"}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        