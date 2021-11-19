import random

from datacenter import models


COMMENDATIONS = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
                 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!',
                 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!',
                 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!',
                 'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!',
                 'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!',
                 'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!',
                 'Теперь у тебя точно все получится!']


def fix_marks(schoolkid):
    bad_marks = models.Mark.objects.filter(schoolkid=schoolkid, points__in=(2, 3))
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    kid_chastisements = models.Chastisement.objects.filter(schoolkid=schoolkid)
    kid_chastisements.delete()


def create_commendation(schoolkid, lesson, commendations_list):
    commendation = random.choice(commendations_list)
    models.Commendation.objects.create(
        text=commendation,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
        created=lesson.date
    )
