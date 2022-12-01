from django.test import TestCase


class TestViews(TestCase):

    def test_get_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_invite(self):
        response = self.client.get("/invite/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'invite.html')

    def test_get_gallary(self):
        response = self.client.get("/info/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info.html')

    def test_get_contact(self):
        response = self.client.get("/gallery/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')
