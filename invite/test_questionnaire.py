from django.test import TestCase
from . import forms, models, views
import unittest

# test cases for creating questionnaire:
# 1) As ADMIN, I can CREATE A FOOD QUESTIONNAIRE so that I can UNDERSTAND FOOD
#   REQUIREMENTS AND MENU PREFERENCES.
# Given that an admin is logged in, when the menu items have been added to the
#   wedding obj, the food questionnaire is published.


class TestCreateQuestionnaire(TestCase):
    def setUp(self):
        models.Wedding.objects.create(
            wedding_date="2024-03-27",
            starter1="Tomato and basil Soup",
            starter1_ingredients="Tomato, Basil, Veg stock",
            starter2="White crab meat tart, dressed with coastal herbs",
            starter2_ingredients="Crab, Eggs, Flour, Butter, Cream, Pastry",
            main1="Butternut squash ravioli",
            main1_ingredients="butternut squash, Egg, Flour, Butter, Tarragon",
            main2="Monkfish, butterhead lettuce and dill",
            main2_ingredients="Monkfish, lettuce, dill",
            main3="Braised pork with potatos and carrots",
            main3_ingredients="Pork, Potato, Carrot",
            dessert1="Sticky toffee pudding",
            dessert1_ingredients="Syrup, Flour, Egg, Sugar",
            dessert2="Trio of ice cream",
            dessert2_ingredients="Chocolate, Vanilla, Banana, Cream, Sugar",
            dessert3="Cheese Board",
            dessert3_ingredients="Crackers, Cheese, Pickle",
        )

    def test_get_home(self):
        user_id = 1
        response = self.client.get("/profile/<user_id>")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    # def test_quiz_button_visibility(self):


# 2) As A USER, I can ANSWER QUESTIONNAIRES POSTED BY THE BRIDE / GROOM so
#   that I can SHARE THE REQUESTED INFORMATION.
# Given that a user is logged in, when the questionnaire is available, they
#   can add their menu choice via the food questionnaire.


if __name__ == '__main__':
    unittest.main()
