from multiprocessing import Process, Lock
import time
import os
import webbrowser
from tkinter import *


def f1(lock, id, sleepTime):
    lock.acquire()
    print("I'm P" + str(id) + " Process ID: " + str(os.getpid()))
    lock.release()
    time.sleep(sleepTime)


def startRollCall(lock, id, name="Javier"):
    lock.acquire()
    print("I'm P" + str(id) + " Process ID: " + str(os.getpid()))
    lock.release()
    with open('Asistencia.txt', 'w') as f:
        f.write("PASE DE LISTA" + "\nNombre del estudiante: " + "\n")
        f.write(''.join(name))


def openWebsite(lock, id):
    lock.acquire()
    print("I'm P" + str(id) + " Process ID: " + str(os.getpid()))
    lock.release()
    webbrowser.open("http://portafoliosfit.um.edu.mx/saulobosquez/")


def writeNote(lock, id, names=[]):
    lock.acquire()
    print("I'm P" + str(id) + " Process ID: " + str(os.getpid()))
    lock.release()
    with open('Asistencia.txt', 'at') as f:
        f.write(' '.join(names))
        f.close()


def process1():
    start = time.time()
    p1.start()
    p1.join()
    end = time.time()
    processWindow.config(state=NORMAL)
    processWindow.insert(END, "\nI'm Process P1, finished in: ~{0:.2f}".format(end-start) + " sec")
    processWindow.config(state=DISABLED)


def process2():
    start = time.time()
    p2.start()
    p2.join()
    end = time.time()
    processWindow.config(state=NORMAL)
    processWindow.insert(END, "\nI'm Process P2, finished in: ~{0:.2f}".format(end - start) + " sec")
    processWindow.config(state=DISABLED)


def process3():
    start = time.time()
    p3.start()
    p3.join()
    end = time.time()
    processWindow.config(state=NORMAL)
    processWindow.insert(END, "\nI'm Process P3, finished in: ~{0:.2f}".format(end - start) + " sec")
    processWindow.config(state=DISABLED)


def process4():
    start = time.time()
    p4.start()
    p4.join()
    end = time.time()
    processWindow.config(state=NORMAL)
    processWindow.insert(END, "\nI'm Process P4, finished in: ~{0:.2f}".format(end - start) + " sec")
    processWindow.config(state=DISABLED)


def clearTextInput():
    processWindow.config(state=NORMAL)
    processWindow.delete("1.0", "end")


if __name__ == '__main__':
    lock = Lock()
    names = ['\nCeline', '\nAlex', '\nMiguel', '\nFredy']
    p1 = Process(target=f1, args=(lock, 1, 3,))
    p2 = Process(target=openWebsite, args=(lock, 2))
    p3 = Process(target=startRollCall, args=(lock, 3))
    p4 = Process(target=writeNote, args=(lock, 4, names))
    # Create the root window
    window = Tk()

    # Set window title
    window.title('Multi-Thread Processing')

    # Set window size
    window.geometry("500x600")
    window.resizable(False, False)

    # Set window background color
    window.config(background="rosy brown")

    # Create a File Explorer label
    label_file_explorer = Label(window, text="Multi-Thread Processing", width=100, height=4, bg="rosy brown", font=("Helvetica", 14))
    button_knn = Button(window, text="Begin Process 1", command=process1)
    button_trees = Button(window, text="Begin Process 2", command=process2)
    button_logi = Button(window, text="Begin Process 3", command=process3)
    button_svm = Button(window, text="Begin Process 4", command=process4)

    processWindow = Text(window, width=40, height=10, borderwidth=5, font=("Helvetica", 14))
    processWindow.config(state=NORMAL)
    processWindow.insert(END, "Main Process ID: " + str(os.getpid()))
    button_clear = Button(window, text="Clear", command=clearTextInput)
    button_exit = Button(window, text="Exit", command=exit)

    # Pack method is chosen for placing the widgets at respective positions
    # in a table like structure by specifying rows and columns
    label_file_explorer.pack(padx=10)
    button_knn.pack(padx=10, pady=(0, 5))
    button_trees.pack(padx=10, pady=(0, 5))
    button_logi.pack(padx=10, pady=(0, 5))
    button_svm.pack(padx=10)
    processWindow.pack(padx=10, pady=10)
    button_clear.pack(padx=10, pady=(0, 5))
    button_exit.pack(padx=10)

    # Let the window wait for any events
    window.mainloop()

