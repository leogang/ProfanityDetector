import urllib.parse

# User must change file extension to desired file.
def read_text():
    quotes = open("/Users/animaltalk/Documents/temp/wittgenstein.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

# Uses Google's "What Do You Love" (wdyl) website as basis for what is 
# considered to be profanity.
def check_profanity(text_to_check):
    # connection = urllib.urlopen("http://wdyl.com/profanity?q=" + text_to_check)
    url = "http://www.wdyl.com/profanity?q="+urllib.parse.quote(text_to_check)
    output = url.read()
    print(output)
    url.close()
    
read_text()
