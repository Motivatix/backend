from . import BaseTestCase


class TestAchievementsByPerson(BaseTestCase):
    def test_get_achievements_by_person(self):
        expected = {'achievements': [{'age': 21,
                                      'description': 'Founded Apple Computer '
                                                     'Company with Wozniak'},
                                     {'age': 50,
                                      'description': 'Stanford speech'}]}
        response = self.client.get('/achievements/Steve_Jobs/')
        self.assertItemsEqual(response.json['achievements'],
                              expected['achievements'])
        self.assertTrue(response.status_code == 200)

    def test_not_found(self):
        response = self.client.get('/achievements/No_one/')
        self.assertTrue(response.status_code == 404)
