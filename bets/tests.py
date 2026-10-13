from django.test import TestCase
from bets.models import Bet, Outcome, Sport, Team, Tournamet, Event
from django.contrib.auth.models import User
from model_bakery import baker
# Create your tests here.

class BetsViewTestCase(TestCase):
    def test_list(self):
        self.assertEqual(1,1)

    def test_get_list(self):
        r = self.client.get('/api/bets')
        print(r)

    def test_get_list_bets(self):
        sport = Sport.objects.create(
            name = "Футбол",
            type = "team"
        )
        team1 = Team.objects.create(
            name = "Спартак",
            sport = sport
        )
        team2 = Team.objects.create(
            name = "Зенит",
            sport = sport
        )
        tournamet = Tournamet.objects.create(
            name = "ЧМ",
            sport = sport,
            country = "Russia"
        )
        event = Event.objects.create(
            status = True, 
            score_home = 1, 
            score_away = 3, 
            tournamet = tournamet, 
            home_team = team1, 
            away_team = team2
        )
        outcome = Outcome.objects.create(
            type="win", 
            result=True, 
            status=True, 
            event=event
        )
        user = User.objects.create(username="testuser")
        bet = Bet.objects.create(
            coef=3.0, 
            sum=1000.0, 
            outcome=outcome, 
            user=user
        )

        r = self.client.get('/api/bets/')
        data = r.json()
        print(data)
        assert bet.coef == data[0]['coef']
        assert bet.sum == data[0]['sum']
        assert bet.outcome.id == data[0]['outcome']
        assert bet.user.id == data[0]['user']
        assert bet.id == data[0]['id']
        assert len(data) == 1

    def test_get_list_outcome(self):
        sport = Sport.objects.create(
            name = "Футбол",
            type = "team"
        )
        team1 = Team.objects.create(
            name = "Спартак",
            sport = sport
        )
        team2 = Team.objects.create(
            name = "Зенит",
            sport = sport
        )
        tournamet = Tournamet.objects.create(
            name = "ЧМ",
            sport = sport,
            country = "Russia"
        )
        event = Event.objects.create(
            status = True, 
            score_home = 1, 
            score_away = 3, 
            tournamet = tournamet, 
            home_team = team1, 
            away_team = team2
        )
        outcome = Outcome.objects.create(
            type="win", 
            result=True, 
            status=True, 
            event=event
        )

        r = self.client.get('/api/outcome/')
        data = r.json()
        print(data)
        assert outcome.type == data[0]['type']
        assert outcome.result == data[0]['result']
        assert outcome.status == data[0]['status']
        assert outcome.event.id == data[0]['event']
        assert outcome.id == data[0]['id']
        assert len(data) == 1

    def test_get_list_sports(self):
        sport = Sport.objects.create(name="Футбол", type="team")

        r = self.client.get('/api/sports/')
        data = r.json()

        assert len(data) == 1
        assert data[0]['id'] == sport.id
        assert data[0]['name'] == sport.name
        assert data[0]['type'] == sport.type

    def test_get_list_teams(self):
        sport = Sport.objects.create(name="Футбол", type="team")
        team = Team.objects.create(name="Спартак", sport=sport)

        r = self.client.get('/api/team/')
        data = r.json()


        assert len(data) == 1
        assert data[0]['id'] == team.id
        assert data[0]['name'] == team.name
        assert data[0]['sport'] == sport.id

    def test_get_list_tournamets(self):
        sport = Sport.objects.create(name="Футбол", type="team")
        tournamet = Tournamet.objects.create(
            name="ЧМ",
            sport=sport,
            country="Russia",
        )

        r = self.client.get('/api/tournamet/')
        data = r.json()

        assert len(data) == 1
        assert data[0]['id'] == tournamet.id
        assert data[0]['name'] == tournamet.name
        assert data[0]['sport'] == sport.id
        assert data[0]['country'] == tournamet.country

    def test_get_list_events(self):
        sport = Sport.objects.create(name="Футбол", type="team")
        team1 = Team.objects.create(name="Спартак", sport=sport)
        team2 = Team.objects.create(name="Зенит", sport=sport)
        tournamet = Tournamet.objects.create(
            name="ЧМ",
            sport=sport,
            country="Russia",
        )
        event = Event.objects.create(
            status=True,
            score_home=1,
            score_away=3,
            tournamet=tournamet,
            home_team=team1,
            away_team=team2,
        )

        r = self.client.get('/api/event/')
        data = r.json() 

        assert len(data) == 1
        assert data[0]['id'] == event.id
        assert data[0]['status'] == event.status
        assert data[0]['score_home'] == event.score_home
        assert data[0]['score_away'] == event.score_away
        assert data[0]['tournamet'] == tournamet.id
        assert data[0]['home_team'] == team1.id
        assert data[0]['away_team'] == team2.id

    def test_create_list_bets(self):
        sport = baker.make(Sport)
        team1 = baker.make(Team, sport=sport)
        team2 = baker.make(Team, sport=sport)
        tournamet = baker.make(Tournamet, sport=sport)
        event = baker.make(Event, tournamet=tournamet, home_team=team1, away_team=team2)
        outcome = baker.make(Outcome, event=event)
        user = baker.make(User)
        bet = baker.make(Bet, outcome=outcome, user=user)

        r = self.client.get('/api/bets/')
        data = r.json()
        print(data)
        assert bet.coef == data[0]['coef']
        assert bet.sum == data[0]['sum']
        assert bet.outcome.id == data[0]['outcome']
        assert bet.user.id == data[0]['user']
        assert bet.id == data[0]['id']
        assert len(data) == 1

    def test_create_list_outcome(self):
        sport = baker.make(Sport)
        team1 = baker.make(Team, sport=sport)
        team2 = baker.make(Team, sport=sport)
        tournamet = baker.make(Tournamet, sport=sport)
        event = baker.make(Event, tournamet=tournamet, home_team=team1, away_team=team2)
        outcome = baker.make(Outcome, event=event)

        r = self.client.get('/api/outcome/')
        data = r.json()
        print(data)
        assert outcome.type == data[0]['type']
        assert outcome.result == data[0]['result']
        assert outcome.status == data[0]['status']
        assert outcome.event.id == data[0]['event']
        assert outcome.id == data[0]['id']
        assert len(data) == 1

    def test_create_list_sports(self):
        sport = baker.make(Sport)

        r = self.client.get('/api/sports/')
        data = r.json()

        assert len(data) == 1
        assert data[0]['id'] == sport.id
        assert data[0]['name'] == sport.name
        assert data[0]['type'] == sport.type

    def test_create_list_teams(self):
        sport = baker.make(Sport)
        team = baker.make(Team, sport=sport)

        r = self.client.get('/api/team/')
        data = r.json()


        assert len(data) == 1
        assert data[0]['id'] == team.id
        assert data[0]['name'] == team.name
        assert data[0]['sport'] == sport.id

    def test_create_list_tournamets(self):
        sport = baker.make(Sport)
        tournamet = baker.make(Tournamet, sport=sport)

        r = self.client.get('/api/tournamet/')
        data = r.json()

        assert len(data) == 1
        assert data[0]['id'] == tournamet.id
        assert data[0]['name'] == tournamet.name
        assert data[0]['sport'] == sport.id
        assert data[0]['country'] == tournamet.country

    def test_create_list_events(self):
        sport = baker.make(Sport)
        team1 = baker.make(Team, sport=sport)
        team2 = baker.make(Team, sport=sport)
        tournamet = baker.make(Tournamet, sport=sport)
        event = baker.make(Event, tournamet=tournamet, home_team=team1, away_team=team2)

        r = self.client.get('/api/event/')
        data = r.json() 

        assert len(data) == 1
        assert data[0]['id'] == event.id
        assert data[0]['status'] == event.status
        assert data[0]['score_home'] == event.score_home
        assert data[0]['score_away'] == event.score_away
        assert data[0]['tournamet'] == tournamet.id
        assert data[0]['home_team'] == team1.id
        assert data[0]['away_team'] == team2.id

    def test_delete_sport(self):
        sports = baker.make("bets.Sport", _quantity=10)
        r = self.client.get("/api/sports/")
        data = r.json()
        assert len(data) == 10
        sport_id_to_delete = sports[3].id
        self.client.delete(f'/api/sports/{sport_id_to_delete}/')
        r = self.client.get("/api/sports/")
        data = r.json()
        assert len(data) == 9
        assert sport_id_to_delete not in [i['id'] for i in data]

    def test_delete_team(self):
        teams = baker.make("bets.Team", _quantity=10)
        r = self.client.get("/api/team/")
        data = r.json()
        assert len(data) == 10
        team_id_to_delete = teams[3].id
        self.client.delete(f'/api/team/{team_id_to_delete}/')
        r = self.client.get("/api/team/")
        data = r.json()
        assert len(data) == 9
        assert team_id_to_delete not in [i['id'] for i in data]

    def test_delete_tournamet(self):
        tournamets = baker.make("bets.Tournamet", _quantity=10)
        r = self.client.get("/api/tournamet/")
        data = r.json()
        assert len(data) == 10
        tournamet_id_to_delete = tournamets[3].id
        self.client.delete(f'/api/tournamet/{tournamet_id_to_delete}/')
        r = self.client.get("/api/tournamet/")
        data = r.json()
        assert len(data) == 9
        assert tournamet_id_to_delete not in [i['id'] for i in data]

    def test_delete_event(self):
        events = baker.make("bets.Event", _quantity=10)
        r = self.client.get("/api/event/")
        data = r.json()
        assert len(data) == 10
        event_id_to_delete = events[3].id
        self.client.delete(f'/api/event/{event_id_to_delete}/')
        r = self.client.get("/api/event/")
        data = r.json()
        assert len(data) == 9
        assert event_id_to_delete not in [i['id'] for i in data]

    def test_delete_outcome(self):
        outcomes = baker.make("bets.Outcome", _quantity=10)
        r = self.client.get("/api/outcome/")
        data = r.json()
        assert len(data) == 10
        outcome_id_to_delete = outcomes[3].id
        self.client.delete(f'/api/outcome/{outcome_id_to_delete}/')
        r = self.client.get("/api/outcome/")
        data = r.json()
        assert len(data) == 9
        assert outcome_id_to_delete not in [i['id'] for i in data]

    def test_delete_bet(self):
        bets = baker.make("bets.Bet", _quantity=10)
        r = self.client.get("/api/bets/")
        data = r.json()
        assert len(data) == 10
        bet_id_to_delete = bets[3].id
        self.client.delete(f'/api/bets/{bet_id_to_delete}/')
        r = self.client.get("/api/bets/")
        data = r.json()
        assert len(data) == 9
        assert bet_id_to_delete not in [i['id'] for i in data]
