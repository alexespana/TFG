from unittest import TestCase   # We don't need a database for testing
from myFindings.views import *  # All views are necessary
from django.urls import reverse, resolve

class TestUrls(TestCase):

    def test_home_url(self):
        url = reverse('home', kwargs={})
        self.assertEquals(resolve(url).func, index)

    def test_about_url(self):
        url = reverse('about', kwargs={})
        self.assertEquals(resolve(url).func, about)


    def test_contact_url(self):
        url = reverse('contact', kwargs={})
        self.assertEquals(resolve(url).func, contact)
        

    def test_team_url(self):    
        url = reverse('team', kwargs={})
        self.assertEquals(resolve(url).func, team)

    def test_excavations_url(self):
        url = reverse('excavations', kwargs={})
        self.assertEquals(resolve(url).func, list_allexcavations)

    def test_add_excavation_url(self):
        url = reverse('add_excavation', kwargs={})
        self.assertEquals(resolve(url).func, add_excavation)

    def test_modify_excavation_url(self):
        url = reverse('modify_excavation', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, modify_excavation)

    def test_delete_excavation_url(self):
        url = reverse('delete_excavation', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, delete_excavation)

    def test_sedimentaryues_url(self):
        url = reverse('sedimentaryues', kwargs={})
        self.assertEquals(resolve(url).func, list_allsedimentaryues)

    def test_add_sedimentaryue_url(self):
        url = reverse('add_sedimentaryue', kwargs={})
        self.assertEquals(resolve(url).func, add_sedimentaryue)

    def test_modify_sedimentaryue_url(self):
        url = reverse('modify_sedimentaryue', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, modify_sedimentaryue)

    def test_delete_sedimentaryue_url(self):
        url = reverse('delete_sedimentaryue', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, delete_sedimentaryue)

    def test_builtues_url(self):
        url = reverse('builtues', kwargs={})
        self.assertEquals(resolve(url).func, list_allbuiltues)

    def test_add_builtue_url(self):
        url = reverse('add_builtue', kwargs={})
        self.assertEquals(resolve(url).func, add_builtue)

    def test_modify_builtue_url(self):
        url = reverse('modify_builtue', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, modify_builtue)

    def test_delete_builtue_url(self):
        url = reverse('delete_builtue', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, delete_builtue)

    def test_facts_url(self):
        url = reverse('facts', kwargs={})
        self.assertEquals(resolve(url).func, list_allfacts)

    def test_add_fact_url(self):    
        url = reverse('add_fact', kwargs={})
        self.assertEquals(resolve(url).func, add_fact)

    def test_modify_fact_url(self):
        url = reverse('modify_fact', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, modify_fact)

    def test_delete_fact_url(self):
        url = reverse('delete_fact', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, delete_fact)

    def test_rooms_url(self):
        url = reverse('rooms', kwargs={})
        self.assertEquals(resolve(url).func, list_allrooms)

    def test_add_room_url(self):
        url = reverse('add_room', kwargs={})
        self.assertEquals(resolve(url).func, add_room)

    def test_modify_room_url(self):
        url = reverse('modify_room', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, modify_room)

    def test_delete_room_url(self):
        url = reverse('delete_room', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, delete_room)

    def test_photos_url(self):
        url = reverse('photos', kwargs={})
        self.assertEquals(resolve(url).func, list_allphotos)

    def test_add_photo_url(self):
        url = reverse('add_photo', kwargs={})
        self.assertEquals(resolve(url).func, add_photo)

    def test_modify_photo_url(self):
        url = reverse('modify_photo', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, modify_photo)

    def test_delete_photo_url(self):
        url = reverse('delete_photo', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, delete_photo)

    def test_inclusions_url(self):
        url = reverse('inclusions', kwargs={})
        self.assertEquals(resolve(url).func, list_allinclusions)

    def test_add_inclusion_url(self):
        url = reverse('add_inclusion', kwargs={})
        self.assertEquals(resolve(url).func, add_inclusion)

    def test_modify_inclusion_url(self):
        url = reverse('modify_inclusion', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, modify_inclusion)

    def test_delete_inclusion_url(self):
        url = reverse('delete_inclusion', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, delete_inclusion)

    def test_sedimentarymaterials_url(self):
        url = reverse('sedimentarymaterials', kwargs={})
        self.assertEquals(resolve(url).func, list_allsedimentarymaterials)

    def test_add_sedimentarymaterial_url(self):
        url = reverse('add_sedimentarymaterial', kwargs={})
        self.assertEquals(resolve(url).func, add_sedimentarymaterial)

    def test_delete_sedimentarymaterial_url(self):
        url = reverse('delete_sedimentarymaterial', kwargs={'nombre': 1})
        self.assertEquals(resolve(url).func, delete_sedimentarymaterial)

    def test_builtmaterials_url(self):
        url = reverse('builtmaterials', kwargs={})
        self.assertEquals(resolve(url).func, list_allbuiltmaterials)

    def test_add_builtmaterial_url(self):
        url = reverse('add_builtmaterial', kwargs={})
        self.assertEquals(resolve(url).func, add_builtmaterial)

    def test_delete_builtmaterial_url(self):
        url = reverse('delete_builtmaterial', kwargs={'nombre': 1})
        self.assertEquals(resolve(url).func, delete_builtmaterial)

    def test_excavationues_url(self):
        url = reverse('excavationues', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, list_excavationues)

    def test_roomfacts_url(self):
        url = reverse('roomfacts', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, list_roomfacts)

    def test_factues_url(self):
        url = reverse('factues', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, list_factues)

    def test_register_url(self):
        url = reverse('register', kwargs={})
        self.assertEquals(resolve(url).func, register)

    def test_send_email_url(self):
        url = reverse('send_email_password_reset', kwargs={})
        self.assertEquals(resolve(url).func, send_email_password_reset)

    def test_generate_report_url(self):
        url = reverse('generate_report', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, generate_report)

    def test_staff_panel_url(self):
        url = reverse('staff_panel', kwargs={})
        self.assertEquals(resolve(url).func, staff_panel)

    def test_change_perms_url(self):
        url = reverse('change_perms', kwargs={'id': 1})
        self.assertEquals(resolve(url).func, change_perms)

    def test_system_logs_url(self):
        url = reverse('system_logs', kwargs={})
        self.assertEquals(resolve(url).func, process_logs)

    def test_download_logs_url(self):
        url = reverse('download_logs', kwargs={})
        self.assertEquals(resolve(url).func, download_logs)
