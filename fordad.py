from tkinter import *
from pytube import YouTube
import glob, os

def main():
    ca = os.path.dirname(os.path.abspath(__file__))

    root = Tk()
    root.title('Músicas e vídeos - Paivas')
    root.configure(background='#1e3743')

    largura = 450
    altura = 350
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    root.geometry('%dx%d+%d+%d'% (largura, altura, posx, posy))
    root.resizable(0, 0)
    #root.iconbitmap(ca + r'\imgs\icon.ico')


    def abrirmp4():
        path=os.path.realpath(ca + '\mp4')
        os.startfile(path)

    def abrirmp3():
        path=os.path.realpath(ca + '\mp3')
        os.startfile(path)


    #------------------------------------variaveis--------------------------------

    entry_link = StringVar()

    #--------------------------------------frames---------------------------------
    frame1 = Frame(root, bd= 4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=3)

    frame2 = Frame(root, bd= 4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=3)

    #------------------------------ menu -----------------------------------------------

    meuMenu = Menu(root)

    fileArq = Menu(meuMenu, tearoff=0)
    meuMenu.add_cascade(label='Arquivo', menu= fileArq)
    fileArq.add_command(label='Abrir MP3', command=abrirmp3)

    root.config(menu=meuMenu)

    #--------------------------------------Widgets--------------------------------
    img = PhotoImage(file=ca + r'\imgs\yt_img.png')

    label_imagem = Label(frame2, image=img)

    #----------------------- TopLevel 
    def abrir():
        top = Toplevel()
        top.title('Info')
        top.geometry('600x90')
        top.resizable(0, 0)
        Label_info = Label(top, text='''Você deve pegar a URL (link) do vídeo no YouTube para converter e baixar o arquivo MP3.
    Ele será baixado na mesma pasta em que está o executável. (se você baixar duas vezes vai ter o mp3 e o mp4)
    É provável que o programa trave ao baixar, mas relaxa, ele só está carregando.
    Aproveite!
    ''').pack()

    cmd = Button(frame1, text='Como usar', command=abrir).place(relx=0.01, rely=0.15)

    #------------------- da URL

    url_label = Label(frame2, text='Insira a URL:')
    url_entry = Entry(frame2, textvariable=entry_link)

    #----------------- Confirmar

    def confirmar():

        yt1 = YouTube(entry_link.get())
        video = yt1.streams.filter(only_audio=True).first()
        downloaded_file = video.download(ca + '\mp3')
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        os.rename(downloaded_file, new_file)

        confirmar_button.place_forget()

        entry_link.set('')

        proximo_button.place(relx=.85, rely=.85)
        message_feito.place(relx=.45, rely=.8)

    confirmar_button = Button(frame2, text='Baixar', command=confirmar)

    #------------------ Próximo

    def proximo():
        message_feito.place_forget()
        proximo_button.place_forget()
        confirmar_button.place(relx=.85, rely=.85)

    proximo_button = Button(frame2, text='Próximo', command=proximo)

    #-------------------------------------Layout----------------------------------

    frame1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.15)
    frame2.place(relx=0.02, rely= 0.2, relwidth=0.96, relheight=0.77)

    url_label.place(relx=.25, rely=.5)
    url_entry.place(relx=.42, rely=.5, relwidth=0.3111)

    label_imagem.place(relx=.25, rely=0.2)

    confirmar_button.place(relx=.25, rely=.6, relwidth=0.485)

    message_feito = Message(root, text='Pronto!')

    #-----------------------------------------------------------------------------

    root.mainloop()
if __name__ == '__main__':
    main()