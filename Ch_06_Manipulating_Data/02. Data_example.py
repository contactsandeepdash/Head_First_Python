"""     Read a file in APPEND mode  """
todos = open('todos.txt', 'a')

"""     Keep on adding data to the txt file     """
print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)

"""     If the file stream not closed, data may not be saved to the file. ALWAYS to close   """
todos.close()

"""     Read the file to get the contents   """
"""     with clause, no need to close the stream at the end  """
try:
    with open('todos1.txt') as tasks:
        for chore in tasks:
            print(chore, end='')
except (FileExistsError, FileNotFoundError):
    print("The file data is missing.")
except Exception as error:
    print("Some other error occurred", str(error))

