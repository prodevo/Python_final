import tkinter as tk
import vlc

def main():     #відправна точка програми 
    root = tk.Tk()
    
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')   

    root.configure(bg = '#4b3eb0')  #стилізація  вікна
    root.title('Радіо')

    instance = vlc.Instance()
    player = instance.media_player_new()

    radio_url = tk.StringVar()
    radio_url.set('')

    tk.Label(root, text='Введіть посилання на радіо:', bg= '#3eb053', font = ('Inter', 15, 'bold'), pady=10).pack(pady=10) #підказка для користувача про введення посилання на радіо
    entry = tk.Entry(root, textvariable=radio_url, width=50, font = ('Inter', 15, 'bold'), bg= '#b03e51')
    entry.pack(pady=10)

    def play():     #функція, що забезпечує програвання медіа
        url = radio_url.get()
        if url:
            media = instance.media_new(url)
            player.set_media(media)
            player.play()

    def stop():     #функція, що забезпечує зупинку програвання медіа
        player.stop()

    play_button = tk.Button(root, text = 'Грати!', bg= '#3eb053', font = ('Inter', 15, 'bold'), command = play) 
    play_button.pack(pady=10)
    
    stop_button = tk.Button(root, text = 'Стоп', bg= '#3eb053', font = ('Inter', 15, 'bold'), command = stop)
    stop_button.pack(pady=10)

    root.mainloop()

main()  #виклик головної функції