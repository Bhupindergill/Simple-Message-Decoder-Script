# Simple-Message-Decoder-Script
A simple message decoder script written in Python.

The .txt file that this script takes in needs to be in the following example format:

3 World

1 Hello

2 Cat

In this example above, the output message would be: "Hello World".
Basically the script sorts the lines from lowest to highest based on the numbers, then creates a pyramid like this:

  1
  
 2 3
 
The last numbers from each row is what word is used in the decoded output message, so "Hello: because of 1, and "World" because of 3.

One issue that might occur is if the last line can't create a pyramid line one word bigger than the previous one, it might cause the
script to crash. However, I have not tested for this scenario, so the actual outcome remains unknown.
