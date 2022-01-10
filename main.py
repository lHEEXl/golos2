import speech_recognition
import webbrowser
from tkinter import *


# window = Tk()
# window.title('Hello')
# window.configure(bg='#123123')
# window.geometry('500x300')
# btn = Button(text="Welcome",
#             bg='#000', 
#             fg='#339',
#             font="Arial 14",
#             justify='center',
#             state='normal',
#             highlightcolor = '#f00')
# btn.pack()


sr= speech_recognition.Recognizer()
sr.pause_threshold = 0.5
def glava():
    def open_browser():
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
        webbrowser.get('Chrome').open_new_tab('porno365.biz')


    def listen_command():
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic , duration=0.5)
                audio = sr.listen(source=mic)
                query= sr.recognize_google(audio_data=audio,language='ru-RU').lower()
                    
                return query
        except speech_recognition.UnknownValueError:
            return "Dam... Вынь хуй изо рта"


    def greeting():
            ### Привет функция###
        return 'Привет даун!'
     
     
    # def vixod():
        
    #     print("Пока еблан")
    #     break       

    def create_tasks(): 
        print ("Что седня этот еблан захочет?")
        query= listen_command()
        with open('todo-list.txt','a') as file:
            file.write(f'| {query}\n')
        return f'Еблан, я сделал это {query}'

    def main():
        query= listen_command() 
        if query == 'привет':    
            print(greeting())
            
        elif query == 'порно':
            print(open_browser())
            
        elif query == "работать":
                print(create_tasks())  
                
        elif query == "выход":
            print("Пока еблан")
            exit()   
            
        
            
        else:
            print("Dam... Вынь хуй изо рта")
            


    if __name__== '__main__':
        main()
# window.mainloop()
    
glava()

while True:
    glava()
    
    
