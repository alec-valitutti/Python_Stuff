#hw7.py
#Alec Valitutti
#2/14/2020
#opens reads edits text files




def readingFunc(name, var):
    text_file1 = open("readDoc.txt","r")
    whole_thing = text_file1.read()
    print(whole_thing)
    text_file1.close()

def writingFunc(name, var):
    text_file = open("readDoc.txt","w")    
    print("Type what you want to add to this document:")
    text_file.write(input())
    text_file.close()
    


def main():
    readingFunc("readDoc.txt", "r")
    writingFunc("readDoc.txt", "w")
    readingFunc("readDoc.txt", "r")

main()
