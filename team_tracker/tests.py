
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Player
from .forms import TeamForm, PlayerForm
from django.urls import reverse

# Test for models
class TeamModelTest(TestCase):
    def setUp(self):
        self.team1 = Team.objects.create(city="New York", mascot="Mascot1")
        self.player1 = Player.objects.create(first_name="John", last_name="Doe")
        self.player1.teams.add(self.team1)
    
    def test_player_creation(self):
        self.assertEqual(self.player1.first_name, "John")
        self.assertEqual(self.player1.last_name, "Doe")
        self.assertEqual(self.player1.teams.first(), self.team1)

class PlayerModelTest(TestCase):

    def setUp(self):
        self.team = Team.objects.create(city="Seattle", mascot="Seahawks")
        self.player = Player.objects.create(first_name="John", last_name="Doe")
        self.player.teams.add(self.team)
        self.player.refresh_from_db()

    def test_player_creation(self):
        self.assertEqual(self.player.first_name, "John")
        self.assertEqual(self.player.last_name, "Doe")
        self.assertEqual(self.player.teams.first(), self.team)

    def test_player_assigned_to_team(self):
        self.assertTrue(self.player.teams.filter(id=self.team.id).exists())

# Test for views
class HomePageViewTest(TestCase):

    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

# Test for forms
class TeamFormTest(TestCase):
    def test_team_form_valid_data(self):
        form = TeamForm(data={
            'city': "New York", 
            'mascot': "Tiger",
        })
        self.assertTrue(form.is_valid())

    def test_team_form_no_data(self):
        form = TeamForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

class PlayerFormTest(TestCase):
    def test_player_form_valid_data(self):
        form = PlayerForm(data={
            'first_name': "John",
            'last_name': "Doe",
        })
        self.assertTrue(form.is_valid())

    def test_player_form_no_data(self):
        form = PlayerForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)