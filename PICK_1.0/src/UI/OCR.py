from PIL import Image
import pytesseract

#Opening the PNG file
im = "C:\\Users\\jesus\\OneDrive\\Desktop\\png1.png"

def imagetotext(path):
#Extracting content from PNG
    text = pytesseract.image_to_string(path, lang='eng')

#Printing content
    #print(text)

    p = path.split("\\")
    le = len(p)
    n = p[le-1].split(".")
    t = n[0] + ".txt"
#Converting output into text file
    text_file = open(t, "w")
    text_file.write(text)
    text_file.close()

if __name__ == '__main__':
    imagetotext(im)
