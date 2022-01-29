import sys

##### FUNCTIONS #####
# Convert a sting into a list removing empty spaces.
def string_2_list(string):
  string_list = list(string.replace(" ", ""))
  return string_list

# Convert a symbol on its ASCII
def char2int(char):
  symbol_to_ascii = ord(char)
  return symbol_to_ascii

# Convert a ASCII into its symbol
def int2char(int):
  ascii_to_symbol = chr(int)
  return ascii_to_symbol

# Uppercase a string and remove spaces
def upper_no_spaces(string):
  upper_no_spaces = string.upper()
  upper_no_spaces = upper_no_spaces.replace(" ", "")
  return upper_no_spaces

# Verify Uppercase
def verify_upper(string):
  import re
  if not re.match("(^[A-Z]*$)|( )", string):
    return False
  else:
    return True

# Split string
def split(s, n): 
  splited = []
  while s:
    splited.append(s[:n])
    s = s[n:]
  splited = ' '.join(splited)
  return splited
##### FUNCTIONS ##### 

# Missing argument error message
help = """
Missing argument!

VALID ARGUMENTS
-e encrypt message
-d decrypt message
"""

# Argument verification
if 1 == 1:
  availableOpt = ["-d", "-e"]
  if len(sys.argv) == 1 or sys.argv[1] not in availableOpt:
    print ("\033[31m" + help + "\033[0m")
    exit()

# Define strings by argument
if (sys.argv[1] == '-d'):
  status = 'decrypted'
else:
  status = 'encrypted'

# ASCII correction parameter A --> 65
z = 65

# Clear message
print ("Enter the message to be " + status + " (lowercase will change to uppercase, spaces will be removed)")
input_message = input()
input_message = upper_no_spaces(input_message)
# Verify input is only A-Z
if verify_upper(input_message) == False:
  print ("\033[31m" + "Only capital letters [A-Z] are allowed!" +"\033[0m")
  exit()
# Convert string to list
input_message_list = string_2_list(input_message)
l = length_message = len(input_message_list)

# Key
print("Enter the key (lowercase will change to uppercase, spaces will be removed)")
key = input()
key = upper_no_spaces(key)
# Verify input is only A-Z
if verify_upper(key) == False:
  print ("\033[31m" + "Only capital letters [A-Z] are allowed!" +"\033[0m")
  exit()
# Convert string to list
key_list = string_2_list(key)
length_key = len(key_list)

# Verify if message and key have the same lenght
if length_message != length_key:
  print ("\n" + "\033[31m" + "Message and key have different length!"+"\033[0m")
  print ("\t" + "message lenght:",length_message)
  print ("\t" + "key lenght:", length_key)
  exit()

# Convert symbol to ASCII
ascii_message = {}
for i in range (l):
  input_message_list[i] = char2int(input_message_list[i]) - z
  key_list[i] = char2int(key_list[i]) - z

# Sum lists if -e or subtract if -d
if (sys.argv[1] == '-d'):
  ascii_message = [(x - y) % 26 for x, y in zip(input_message_list, key_list)]
else: 
  ascii_message = [(x + y) % 26 for x, y in zip(input_message_list, key_list)]

# Convert ascii list message to symbol
for i in range (l):
  ascii_message[i] = int2char(ascii_message[i] + z)

# Convert list to string and split in groups of 5
ascii_message = (''.join(ascii_message))
print ("\n" + status + " message:\n","\t"+"\033[91m" + (split(ascii_message,5)) + "\033[0m")
