# steps
# read the text 
# check for curse words

def read_text ():
    quotes= open("/media/blaite/Segat/Code/g-Course-Udacity-Programming_Foundations_with_Python/movie_quotes.txt")
    file_content = quotes.read()
    print(file_content)
    quotes.close()

read_text ()



