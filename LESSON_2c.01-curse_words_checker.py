import urllib

# steps
# read the text
# check for curse words

def read_text ():
    quotes= open("/media/blaite/Segat/Code/g-Course-Udacity-Programming_Foundations_with_Python/movie_quotes.txt")
    file_content = quotes.read()
    #print(file_content)
    quotes.close()
    check_profanity(file_content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    # print(output)
    connection.close()
    if "true" in output:
        print ("Profanity alert!")
    elif "false" in output:
        print ("Profanity not detected. Woho! Awesome")
    else:
        print ("Sth went wrong")

read_text ()
