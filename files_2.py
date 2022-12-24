intro = open("intro.txt", "w")
for i in range(5):
    intro.write("hello world\n")
    intro.write("My name is Atul Tiwari\nI am pursuing Btech\nI am aspiring to be a Full Stack Developer\n\n")

intro.close()