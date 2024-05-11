import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String


engine = create_engine("postgresql+psycopg2://admin_timetable:cde#4rfv@localhost/timetabledb")
engine.connect()

metadata = MetaData()

timetable = Table('timetable', metadata,
                  Column('id', Integer(), primary_key=True, autoincrement=True),
                        Column('group_title', String(10), nullable=False),
                        Column('day_week', String(12), nullable=False),
                        Column('lesson_time', String(6), nullable=True),
                        Column('lesson_type', String(12), nullable=True),
                        Column('lesson_title', String(200), nullable=False),
                        Column('cabinet', String(20), nullable=True),
                        Column('teacher', String(200), nullable=True),
                        Column('week_type', String(1), nullable=True)
                  )


metadata.create_all(engine)



groups = [['ИУ1-21Б',
           [{'8:30': [{'type': '(сем)', 'name': 'Разработка GUI приложений', 'classroom': '114л', 'teacher': 'Николаев А. А.'}],
             '10:15': [{'type': '(сем)', 'name': 'Иностранный язык', 'classroom': 'каф. Л2', 'teacher': ''}],
             '12:00': [{'type': '(лаб)', 'name': 'Разработка GUI приложений', 'classroom': '602', 'teacher': 'Николаев А. А.'}, {'type': '(лаб)', 'name': 'Разработка GUI приложений', 'classroom': '602', 'teacher': 'Николаев А. А.'}],
             '13:50': [{'type': '', 'name': 'ФКиС 14.30 Измайлово', 'classroom': '', 'teacher': ''}],
             '15:40': None,
             '17:25': None,
             '19:10': None},
            {'8:30': None, '10:15': [{'type': '(сем)', 'name': 'Интегралы и дифференциальные уравнения', 'classroom': '145л', 'teacher': 'Велищанский М. А.'}], '12:00': [{'type': '(лек)', 'name': 'Интегралы и дифференциальные уравнения', 'classroom': '224л', 'teacher': 'Велищанский М. А.'}], '13:50': [{'type': '(лек)', 'name': 'CAD', 'classroom': '739л', 'teacher': 'Викулов А. Н.'}, {'type': '(лек)', 'name': 'CAD', 'classroom': '739л', 'teacher': 'Викулов А. Н.'}], '15:40': [{'type': '(сем)', 'name': 'CAD', 'classroom': '1108л', 'teacher': 'Викулов А. Н.'}], '17:25': None, '19:10': [{'type': '(лаб)', 'name': 'CAD', 'classroom': '114л', 'teacher': 'Викулов А. Н.'}, None]}, {'8:30': None, '10:15': [{'type': '(сем)', 'name': 'Элективный курс по физической культуре и спорту', 'classroom': 'каф. ФВ', 'teacher': ''}], '12:00': [{'type': '(сем)', 'name': 'Интегралы и дифференциальные уравнения', 'classroom': '255л', 'teacher': 'Велищанский М. А.'}, None], '13:50': [{'type': '(сем)', 'name': 'История России', 'classroom': '255л', 'teacher': 'Ахмедова С. С.'}], '15:40': [{'type': '(лек)', 'name': 'Линейная алгебра и функции нескольких переменных', 'classroom': '218л', 'teacher': 'Марченко В. В.'}], '17:25': None, '19:10': None}, {'8:30': [{'type': '(сем)', 'name': 'Физика', 'classroom': '520', 'teacher': 'Небритова О. А.'}, None], '10:15': [{'type': '(лек)', 'name': 'Физика', 'classroom': '323', 'teacher': 'Юрасов Н. И.'}], '12:00': [None, {'type': '(лаб)', 'name': 'Физика', 'classroom': '249.4', 'teacher': 'Люлюкин В. С., Юрасов Н. И.'}], '13:50': None, '15:40': None, '17:25': None, '19:10': None}, {'8:30': [{'type': '(лек)', 'name': 'Прикладная механика', 'classroom': '255л', 'teacher': 'Обносов К. Б.'}], '10:15': [{'type': '(сем)', 'name': 'Прикладная механика', 'classroom': '255л', 'teacher': 'Обносов К. Б.'}], '12:00': [{'type': '(сем)', 'name': 'Линейная алгебра и функции нескольких переменных', 'classroom': '619л', 'teacher': 'Труб Н. В.'}], '13:50': None, '15:40': None, '17:25': None, '19:10': None}, {'8:30': None, '10:15': None, '12:00': [{'type': '', 'name': 'Самостоятельная работа', 'classroom': '', 'teacher': ''}], '13:50': None, '15:40': None, '17:25': None, '19:10': None}]]]

week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

for group in groups:
    group_title = group[0]
    days = group[1]
    for day in range(6):
        times = days[day].keys()
        lessons = days[day].items()
        for lesson in lessons:
            if lesson is not None:
                if len(lesson) == 1:
                    pass
                else:
                    pass

            ins = timetable.insert().values(
                group_title=group_title,
                day_week=week_days[day],
                lesson_time='',
                lesson_type='',
                lesson_title='',
                cabinet='',
                teacher='',
                week_type=''
            )



