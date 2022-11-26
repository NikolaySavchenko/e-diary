from random import choice

from datacenter.models import Mark
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Subject
from datacenter.models import Commendation


def fix_marks(schoolkid_name):
    client_card = Schoolkid.objects.filter(full_name__contains=schoolkid_name)
    if len(client_card)>1:
        return f'Найдено {len(client_card)} учеников!'
    elif client_card.first() is None:
        return 'Не найдено ни одного ученика с подходящим именем!'
    client_marks = Mark.objects.filter(schoolkid=client_card.first().id)
    client_bad_marks = client_marks.filter(points__lt=4)
    for bad_mark in client_bad_marks:
        bad_mark.points = 5
        bad_mark.save()
    return 'Все ок!'

def remove_chastisement(schoolkid_name):
    client_card = Schoolkid.objects.filter(full_name__contains=schoolkid_name)
    if len(client_card)>1:
        return f'Найдено {len(client_card)} учеников!'
    elif client_card.first() is None:
        return 'Не найдено ни одного ученика с подходящим именем!'
    client_chastisement = Chastisement.objects.filter(schoolkid=client_card.first().id)
    client_chastisement.delete()
    return 'Все ок!'

def create_commendation(schoolkid_name, subject):
    client_card = Schoolkid.objects.filter(full_name__contains=schoolkid_name)
    if len(client_card)>1:
        return f'Найдено {len(client_card)} учеников!'
    elif client_card.first() is None:
        return 'Не найдено ни одного ученика с подходящим именем!'
    lessons = Lesson.objects.filter(year_of_study=client_card.first().year_of_study,
                                    group_letter=client_card.first().group_letter, subject__title=subject)
    compliments = [
        'Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
        'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!',
        'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!',
        'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!',
        'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!'
    ]
    random_compliment = choice(compliments)
    lesson = choice(lessons.reverse()[:5])
    subject_card = Subject.objects.filter(title__contains=subject, year_of_study__contains=lesson.year_of_study)[0]
    Commendation.objects.create(text=random_compliment, created=lesson.date, schoolkid=client_card.first(),
                                subject=subject_card, teacher=lesson.teacher)
    return 'Все ок!'


