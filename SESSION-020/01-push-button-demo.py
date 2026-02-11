from tkinter import * 


def ok_button_handler():
    print('OK BUTTON IS CLICKED') 


root_window = Tk()
root_window.title('Push Button Demo') 
root_window.geometry('300x200')


ok_button = Button(root_window)
ok_button.configure(text='Ok', command=ok_button_handler)
ok_button.grid(row=0, column=0)


print('ATA CONTROL FLOW root_window.mainloop() MADHE JAT AHE')
root_window.mainloop() 

print('MALA TERMINATE HO - ASHI ADNYA ALI') 

'''
BEGINNER:

1) ERROR BHARPUR YENAR

2) SOLVE ZALYA-NANTAR APAN ATISHAY MOORKH AHOT KI KAY?
    ASA WATNARE ERROR YENAR

3) PRACTICE ANI REPEATITION NE ASE ERROR KHOOP MINIMIZE
    HOTAT, PAN AYUSHYAT PUDHE ASHA LEVEL CHA ERROR KADHICH
    HONAR NAHI HYACHI KAHIHI GUARANTEE NAHI

4) JAST OVERTHINK KARU NAKA. REPEATITION KARAT RAHA
    MINIMIZATION OF TRIVIAL ERRORS KARAT RAHA
''' 
