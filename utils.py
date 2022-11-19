from datacenter.models import Mark
from datacenter.models import Schoolkid
from datacenter.models import Chastisement


def fix_marks(schoolkid_id):
    klient_marks = Mark.objects.filter(schoolkid=schoolkid_id)
    klient_bad_marks = klient_marks.filter(points__lt=4)
    for bad_mark in klient_bad_marks:
        bad_mark.points = 5
        bad_mark.save()
    return

def remove_chastisement(schoolkid):
    klient_card = Schoolkid.objects.filter(full_name__contains=schoolkid)[0]
    klient_chastisement = Chastisement.objects.filter(schoolkid=klient_card.id)
    klient_chastisement.delete()
    return
