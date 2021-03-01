import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('story.pdf', 'rb'))
import pyttsx3
speaker = pyttsx3.init()
s = ""
for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    #speaker.say(text)
    s += text
    speaker.runAndWait()
speaker.stop()
speaker.save_to_file(s, 'audio.mp3')
speaker.runAndWait()
