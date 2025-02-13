import tkinter as tk
import vlc
import os

def main():     #відправна точка програми 

    path = 'url.txt'

    def save(url): #зберігає URL у файл "url.txt"
        with open(path, 'w') as file:
            file.write(url)
    
    def load(): #завантажує URL з файлу "url.txt"
        if os.path.exists(path):
            with open(path, 'r') as file:
                return file.read().strip()
        return ''
    
    root = tk.Tk()
    
    radio_url = tk.StringVar()
    radio_url.set(load()) 

    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')   

    root.configure(bg = '#4b3eb0')  #стилізація  вікна
    root.title('Радіо')

    try:
        instance = vlc.Instance()
        player = instance.media_player_new()
    except Exception as e:
        print('Помилка ініціалізації бібліотеки VLC:', e)
        return

    tk.Label(root, text='Введіть посилання на радіо:', bg= '#3eb053', font = ('Inter', 15, 'bold'), pady=10).pack(pady=10) #підказка для користувача про введення посилання на радіо
    entry = tk.Entry(root, textvariable=radio_url, width=50, font = ('Inter', 15, 'bold'), bg= '#b03e51')
    entry.pack(pady=10)

    def play():     #функція, що забезпечує програвання медіа
        try:
            url = radio_url.get().strip()
            if not url:
                print('Помилка! Пустий URL!')
                return

            save(url)
            media = instance.media_new(url)
            player.set_media(media)
            player.play()

        except Exception as e:
            print('Помилка програвання:', e)


    def stop():     #функція, що забезпечує зупинку програвання медіа
        player.stop()

    play_button = tk.Button(root, text = 'Грати!', bg= '#3eb053', font = ('Inter', 15, 'bold'), command = play) 
    play_button.pack(pady=10)
    
    stop_button = tk.Button(root, text = 'Стоп', bg= '#3eb053', font = ('Inter', 15, 'bold'), command = stop)
    stop_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":      #виклик головної функції
    main()  
