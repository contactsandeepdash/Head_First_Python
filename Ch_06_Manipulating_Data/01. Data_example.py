"""
'r' Open a file for reading. This is the default mode and, as such, is optional. When no second argument is
provided, 'r' is assumed. It is also assumed that the file being read from already exists.

'w' Open a file for writing. If the file already contains data, empty the file of its data before continuing.

'a' Open a file for appending. Preserve the file’s contents, adding any new data to the end of the file (compare
this behavior to 'w').

'x' Open a new file for writing. Fail if the file already exists (compare this behavior to 'w' and to 'a').

----------

By default, files open in text mode, where the file is assumed to contain lines of textual data (e.g., ASCII or UTF-8). 

If you are working with nontextual data (e.g., an image file or an MP3), you can specify binary mode by adding “b” to
any of the modes (e.g., 'wb' means “write to a binary data”). 

If you include “+“ as part of the second argument, the file is opened for reading and writing (e.g., 'x+b' means “read from and write to a new binary file”).

"""


"""     Read a file in APPEND mode  """
todos = open('todos.txt', 'a')

"""     Keep on adding data to the txt file     """
print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)

"""     If the file stream not closed, data may not be saved to the file. ALWAYS to close   """
todos.close()

"""     Read the file to get the contents   """
tasks = open('todos.txt')

for chore in tasks:
    """ 6 lines in outout as the print function appends a newline to everything it displays on screen as its default behavior.  """
    print(chore)

    """ To instruct print not to include the second newline, change print(chore) to print(chore, end=''). """
    print(chore, end='')


"""     again close the stream  """
tasks.close()

