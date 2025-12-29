import qrcode

img = qrcode.make('https://www.accaglobal.com/gb/en/student/exam-entry-and-administration/exam-timetables.html')
type(img)
img.save("acca_routine.png")