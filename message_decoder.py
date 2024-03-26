#Simple decoding message script
#Created March 22, 2024
#By Bhupinder Gill
import re

'''
The .txt file that this script takes in needs to be in the following format:
3 World
1 Hello
2 Cat

In this example above, the output message would be: "Hello World".
Basically the script sorts the lines from lowest to highest numbers, then creates a pyramid like this:
  1
 2 3
The last numbers from each row is what word is used in the decoded output message, so "Hello: because of 1, and "World" because of 3.

One issue that might occur is if the last line can't create a pyramid line one word bigger than the previous one, it might cause the
script to crash. However, I have not tested for this scenario, so the actual outcome remains unknown.
'''

def decode(message_file):
    count = 0 #This int variable keeps track of how many words have been read through, for looping purposes.
    message = "" #Where the decoded message is stored.
    line = message_file.readline() #Read first line of txt file.
    while True:
        if count == 0: #Enter this condition if it's the first line that has been read.
            #Next two lines will use regex to isolate the word from the whole string, since the string also has a number character.
            sample = re.compile('[a-zA-z]+')
            word = sample.findall(line)
            message = message + word[0] + " " #Add word to final message, followed by a space.
            count += 1 #Add one to count since first word has been read.
            continue #Restart while loop.
        if count >= 1: #Starting with the second word, the loop will enter this if statement.
            #This for loop condition is how the pyramid structure is done.
            #For example, if this the second time around the while loop, it'll go through the for loop twice
            #and only save the last word. So basically it'll go through word 2, then 3 and only keep 3.
            for i in range(count + 1):
                    line = message_file.readline()
                    if not line: #This condition is for when the loop reaches end of file, it'll exit out and print the final message.
                        return message.strip()
                    sample = re.compile('[a-zA-z]+')
                    word = sample.findall(line)
            message = message + word[0] + " "
            count += 1
    return message.strip()

def natural_sort(list): #Properly sorts string with numbers from lowest to highest value.
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(list, key=alphanum_key)

if __name__ == "__main__":                  
    message_file = open("message.txt", "r") #txt file is read in as read only
    list = sorted(message_file) #Initial sort is stored as a list
    list = natural_sort(list) #This partially sorted list then goes through a proper sort function.
    message_file = open("message.txt", "w") #This txt file is then opened as a writable
    #The new sorted list is written back to the txt file. This is done, because I wrote this script to use a textiowrapper object.
    #But I forgot that I had to first sort it and the sorted text is made into a list, so I lazily write back as a txt file.
    #The proper thing to have done was to rewrite the decode function to use the list, maybe in a future version.
    for item in list:
        message_file.write(item)
    message_file = open("message.txt", "r") #New assorted txt file is read back in.
    print(decode(message_file)) #Print decoded message.
