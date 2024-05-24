import requests
from bs4 import BeautifulSoup


class ScheduleParser():    
    '''Парсер расписания. Выход: двумерный массив (название группы, её расписание)'''

    url = 'https://lks.bmstu.ru/schedule/list'
    session = requests.Session()
    userAgent = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
        
    def parser(self):
        result = None
        try:
            req = self.session.get(self.url, headers=self.userAgent)
            bs = BeautifulSoup(req.text, 'html.parser')
            result = self.soupGroups(bs)
        except:
            print('Error on server!')
        finally:
            print('Parsing is finished')
            return result
    
    
    def soupGroups(self, bs):
        counter = 0
        university = bs.find('div', class_='list-group accordion')
        groups = []
        groups_bs = university.find_all('a', class_='btn btn-primary col-1 rounded schedule-indent')
        for group in groups_bs:
            
            if (counter%170) == 0:
                print(f'{counter//17}% of Parsing...')
            counter += 1
            
            try:
                schedule_bs = self.groupScheduleRequest('https://lks.bmstu.ru' + group.get('href'))
                schedule = self.soupGroupSchedule(schedule_bs)
                groups.append([self._groupName(group.get_text()), schedule])
            except:
                print("One of groups didn't parsed")
                groups.append(None)
        return groups
                
    
    def groupScheduleRequest(self, url):
        req = self.session.get(url, headers=self.userAgent)
        bs = BeautifulSoup(req.text, 'html.parser')
        return bs
        
        
    def soupGroupSchedule(self, bs):
        
        def les_par_changer(par, i):
            lesson_par = {'type' : None, 'name' : None, 'classroom' : None, 'teacher' : None}
            if len(par[i].find_all('i')) == 2:
                lesson_par['type'] = ''
                lesson_par['name'] = par[i].find('span').get_text()
                lesson_par['classroom'] = par[i].find_all('i')[0].get_text()
                lesson_par['teacher'] = par[i].find_all('i')[1].get_text()
            else:
                lesson_par['type'] = par[i].find('i').get_text()
                lesson_par['name'] = par[i].find('span').get_text()
                lesson_par['classroom'] = par[i].find_all('i')[1].get_text()
                lesson_par['teacher'] = par[i].find_all('i')[2].get_text()
            return lesson_par
                
        days_arr = []
        days = bs.find_all('div', class_='col-md-6 d-block d-md-none')
        for day in days:
            lessons_dic = {'8:30' : None, '10:15' : None, '12:00' : None, '13:50' : None, '15:40' : None, '17:25' : None, '19:10' : None}
            lessons = day.find_all('tr')
            lessons_arr = []
            for lesson in lessons:
                if '<td class="bg-grey text-nowrap">' in str(lesson):
                    params = lesson.find_all('td')
                    if len(params)==2:
                        if len(params[1].find_all('i'))==2:
                            lesson_par = {'type' : None, 'name' : None, 'classroom' : None, 'teacher' : None}
                            lesson_par['type'] = ''
                            lesson_par['name'] = params[1].find('span').get_text()
                            lesson_par['classroom'] = ''
                            lesson_par['teacher'] = ''
                            lessons_arr.append([lesson_par])
                        if len(params[1].find_all('i'))==3:
                            lessons_arr.append([les_par_changer(params, 1)])
                    if len(params)==3:
                        if (params[1].get_text()==' ' and params[2].get_text()==' '):
                            lessons_arr.append(None)
                        elif (params[1].get_text()!=' ' and params[2].get_text()==' '):
                            lessons_arr.append([les_par_changer(params, 1), None])
                        elif (params[1].get_text()==' ' and params[2].get_text()!=' '):
                            lessons_arr.append([None, les_par_changer(params, 2)])
                        else:
                            lessons_arr.append([les_par_changer(params, 2), les_par_changer(params, 2)])
            i = 0
            for time in lessons_dic.keys():
                if lessons_arr[i] != None:
                    lessons_dic[time] = lessons_arr[i]
                i+=1
            days_arr.append(lessons_dic)
            
        return days_arr
              
               
    def _groupName(self, name):
        name = name.replace(' ', '')
        return name[1:-1:]     


class ContingentParser():
    
    def getStudents(self, file_name):
        
        with open(file_name, 'r', encoding='utf-8') as f:
            bs = BeautifulSoup(f.read(), 'html.parser')
        
        student_all_info = []
        table = bs.find('table', class_='students-table')
        students = table.find_all('tr')
        for student in students:
            student_all = student.find_all('td')
            try:
                name = student_all[1].get_text()
                stud_bilet = student_all[2].get_text()
                group = self.groupInfo(student_all[3])
                student_all_info.append([stud_bilet, name, group])
            except:
                pass
            
        return student_all_info

    def groupInfo(self, all):
        trash = len(all.find('del').get_text(strip=True))
        return all.get_text(strip=True)[trash::]
