import pyautogui
import webbrowser
import pyperclip
import time
from bs4 import BeautifulSoup


class MarksParser():
    def WebParser(self, group_info):
        url = 'https://eu.bmstu.ru' + group_info[1]
        webbrowser.open(url, new=1)
        time.sleep(1)
        pyautogui.moveTo(400,150)
        pyautogui.click(button='right')
        time.sleep(0.1)
        pyautogui.moveTo(500,670, duration=0.8)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.moveTo(1700,315)
        time.sleep(0.5)
        pyautogui.click(button='right')
        pyautogui.moveTo(1700,525)
        time.sleep(0.2)
        pyautogui.moveTo(1800,530, duration=0.3)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')

 
    def writeToFile(self):
        with open('MarksParser/marksHTML.txt', 'w', encoding='utf-8') as f:
            f.write(pyperclip.paste())         
            
          
    def getFile(self):
        with open('MarksParser/MarksLinksIU.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                info = line[:-1:].split(',')
                self.WebParser(info)
                self.writeToFile()
                try:
                    students = MarksSoup().openHTML()
                    MarksSoup().saveToFile(info[0], students[0], students[1])
                except:
                    pass
                with open('MarksParser/marksHTML.txt', 'w',) as f:
                    pass
                
    
    
    def soupFile(self):
        with open('MarksParser/marksHTML.txt', 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
               
       


def HtmlToFile():
    with open('1.html', 'r', encoding='utf-8') as f:
        page = BeautifulSoup(f.read(), 'html.parser')

    faculties = page.find_all('li', class_='eu-tree-leaf')
    for faculty in faculties:
        name = faculty.get_text().replace(' ', '')[2:-1:]
        link = faculty.find('a').get('href')[:-1:]
        with open('MarksParser/MarksLinksIU.txt', 'a') as f:
            f.write(f'{name},{link}\n')
    
class MarksSoup():
    def openHTML(self):
        with open('MarksParser/marksHTML.txt', 'r', encoding='utf-8') as f:
            page = BeautifulSoup(f.read(), 'html.parser')
        subjects = page.find('thead').find_all('th', class_ = 'headcol-discipline')
        list_of_subjects = []
        for subject in subjects:
            subj_info = subject.get_text().split('\n')
            if subj_info[2] == 'М':
                list_of_subjects.append(subj_info[1])
        
        list_of_students = []
        students = page.find('table', class_='standart_table progress_students vertical_hover table-group').find('tbody').find_all('tr')
        for student in students:
            name = student.find('span', class_='fio_3').get_text()
            bilet = student.find('td', class_='headcol hc3').get_text()
            list_of_students.append([self.nameConverter(name), bilet, self.marksConverter(student, len(list_of_subjects))])
        
        return list_of_subjects, list_of_students
        
        
    def saveToFile(self, group_name, group_subj, students):
        with open('MarksParser/AllMarks.txt', 'a') as f:
            f.write(f'{group_name}\n{group_subj}\n{students}\n')
            
    
    def marksConverter(self, info, subj_number):
        all_marks = info.find_all('td', class_='headcol_body')
        marks = []
        for i in range(subj_number):
            mark = all_marks[i].find('span', class_='progress_percent p_all').get_text()
            marks.append(mark)
        return marks
        
    def nameConverter(self, name):
        ar = name.split()
        s = ''
        for i in ar:
            s = s + i + ' '
        return s[:-1]
    
MarksParser().getFile()