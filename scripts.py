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


def get_schoolkid():
    while True:
        print('Введите имя ученика:')
        user_input = input()
        try:
            schoolkid = models.Schoolkid.objects.get(full_name__contains=user_input)
        except models.Schoolkid.DoesNotExist:
            print('Не удалось найти ученика с подобным именем, проверьте свой запрос на опечатки')
        except models.Schoolkid.MultipleObjectsReturned:
            print('Запрос вернул более чем одного ученика. Пожалуйста, уточните его')
        else:
            return schoolkid


def get_random_lesson_by_subject(schoolkid):
    while True:
        print('Введите название предмета:')
        user_input = input()
        try:
            subject = models.Subject.objects.get(title=user_input, year_of_study=schoolkid.year_of_study)
        except models.Lesson.DoesNotExist:
            print('Не удалось найти предмет с подобным названием на вашем году обучения,'
                  'проверьте свой запрос на опечатки')
        else:
            lessons = models.Lesson.objects.filter(subject=subject, group_letter=schoolkid.group_letter)

            return random.choice(lessons)


schoolkid = get_schoolkid()
lesson = get_random_lesson_by_subject(schoolkid)

fix_marks(schoolkid)
print(f'Оценки {schoolkid} исправлены')
remove_chastisements(schoolkid)
print(f'Замечания {schoolkid} удалены')
create_commendation(schoolkid, lesson, COMMENDATIONS)
print(f'Создана похвала по предмету {lesson}')
