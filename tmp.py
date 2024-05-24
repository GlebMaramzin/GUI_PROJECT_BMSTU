# def tmp():
#     students = ContingentParser().getStudents('facs/юр')
#     for student in students:
#         current_student = Students(studbilet=student[0], fio=student[1], grupa=student[2], facult='юр')
#         with app.app_context():
#             db.session.add(current_student)
#             db.session.flush()
#             db.session.commit()


# insert_data = {}
# def tmp2():
#     groups = ScheduleParser().parser()
#     week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
#     for group in groups:
#         insert_data['group_title'] = group[0]
#         days = group[1]
#         for day_num in range(6):
#             insert_data['week_day'] = week_days[day_num]
#             for lesson_time, lesson_inf in days[day_num].items():
#                 if lesson_inf is not None:
#                     insert_data['lesson_time'] = lesson_time
#                     if len(lesson_inf) == 1:
#                         insert_data['lesson_type'] = lesson_inf[0]['type']
#                         insert_data['lesson_title'] = lesson_inf[0]['name']
#                         insert_data['cabinet'] = lesson_inf[0]['classroom']
#                         insert_data['teacher'] = lesson_inf[0]['teacher']
#                         insert_data['week_type'] = ''
#                     else:
#                         if lesson_inf[0] is not None:
#                             insert_data['lesson_type'] = lesson_inf[0]['type']
#                             insert_data['lesson_title'] = lesson_inf[0]['name']
#                             insert_data['cabinet'] = lesson_inf[0]['classroom']
#                             insert_data['teacher'] = lesson_inf[0]['teacher']
#                             insert_data['week_type'] = 'ч'
#                         if lesson_inf[1] is not None:
#                             insert_data['lesson_type'] = lesson_inf[1]['type']
#                             insert_data['lesson_title'] = lesson_inf[1]['name']
#                             insert_data['cabinet'] = lesson_inf[1]['classroom']
#                             insert_data['teacher'] = lesson_inf[1]['teacher']
#                             insert_data['week_type'] = 'з'
#
#                     ins = Timetable(
#                         group_title=insert_data['group_title'],
#                         day_week=insert_data['week_day'],
#                         lesson_time=insert_data['lesson_time'],
#                         lesson_type=insert_data['lesson_type'],
#                         lesson_title=insert_data['lesson_title'],
#                         cabinet=insert_data['cabinet'],
#                         teacher=insert_data['teacher'],
#                         week_type=insert_data['week_type']
#                     )
#                     with app.app_context():
#                         db.session.add(ins)
#                         db.session.flush()
#                         db.session.commit()