FILEPATH="todo1.txt"


def get_todos(filepath=FILEPATH):
  """It reads the todo text file and returns 
   the list in a list format """
  with open(filepath,"r") as file:
    todos_local=file.readlines()
  return todos_local

# print(help(get_todos))

def write_todos(todos_arg,filepath=FILEPATH):
  """ To write the todo items in text file. """
  with open(filepath,"w") as file:
    file.writelines(todos_arg)
  return None


#print (__name__)
if __name__=="__main__":
    print("you are running directly :")
    print(get_todos())

    