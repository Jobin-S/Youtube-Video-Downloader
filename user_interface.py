import video_Downloader
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

save_path = './Downloaded'
link = StringVar

main_window = Tk()
main_window.geometry("600x500+350+100")
main_window.title("HD Youtube Video Downloader")


class download:
    def download(self):
        global link
        video_link = link_holder.get()
        link = video_link
        print(video_link)
        if link == '':
            messagebox.showerror(title='Warning', message="please paste youtube video link")
        video_Downloader.download_video(link=video_link, save_path=save_path)


def browse_folder():
    global save_path
    folder_path = filedialog.askdirectory()
    path_label.configure(text=folder_path)
    save_path = folder_path


x = download()

title = Label(main_window, text="Paste You Link Here", font=("bold", 22), fg="#FF0000", )
link_holder = Entry(main_window, textvariable=link, border=5, relief='sunken')
download_btn = Button(main_window, text="Download", bg='#2ecc71', relief='raised', fg='#ecf0f1', font=("bold", 12),
                      command=x.download)
path_label = Label(main_window, text=save_path, font=('regular', 10), bg='GRAY', fg='WHITE', width=49)
browse_button = Button(main_window, text='Browse Folder', font=('regular', 10), command=browse_folder)

title.place(x=150, y=10)
link_holder.place(x=50, y=50, width=400, height=30)
download_btn.place(x=470, y=48, width=100)
path_label.place(x=50, y=90)
browse_button.place(x=470, y=90)

main_window.mainloop()
