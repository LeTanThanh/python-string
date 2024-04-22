if __name__ == "__main__":
  # Introducing to Python string
  message = 'This is a string in Python'
  print(message)

  message = "This is also a string"
  print(message)

  message = "It's a string"
  print(message)

  message = '"Beautiful is better than ugly.". Said Tim Peters'
  print(message)

  message = 'It\'s also a valid string'
  print(message)

  message = r'C:\Python\bin'
  print(message)

  help_message = """Usage: mysql command
      -h hostname
      -d database name
      -u username
      -p password
  """
  print(help_message)

  # Using variables in Python strings with the f-strings
  name = "John"
  message = f"Hi {name}"
  print(message)

  # Concatenating Python strings
  greeting = 'Good' 'Morning!'
  print(greeting)

  greeting = 'Good '
  time = 'Afternoon'
  greeting = greeting + time
  print(greeting)

  # Access string elements
  str = "Python String"
  print(str[0])   # P
  print(str[1])   # y
  print(str[-1])  # g
  print(str[-2])  # n

  # Getting the length of a string
  str = "Python String"
  str_len = len(str)
  print(str_len)

  # Slicing strings
  str = "Python String"

  """
  returns a substring that includes the character from the index 0 (included) to 2 (excluded)
  """
  print(str[0:2]) # Py

  """
  The syntax for slicing is as follows:
  string[start:end]
  The substring always includes the character at the start and excludes the string at the end.
  The start and end are optional.
  If you omit the start, it defaults to zero.
  If you omit the end, it defaults to the string's length.
  """

  # Python strings are immutable

  """
  Python strings are immutable.
  It means that you cannot change the string.
  For example, you'll get an error if you update one or more characters in a string:
  """
  str = "Python String"
  # str[0] = 'J'
  # TypeError

  """
  When you want to modify a string, you need to create a new one from the existing string.
  For example:
  """
  str = "Python String"
  new_str = "J" + str[1:]
  print(str)
  print(new_str)
