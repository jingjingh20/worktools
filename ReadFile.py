import os

filepath = 'C:/CGTN/805'
files = [fn for fn in os.listdir(filepath)]
# perhaps filter `files`
string1 = '<roStatus>ERROR'
string2 = 'Parse XML from ncs failed.'

def does_fn_contain_string(filename):
  with open('C:/CGTN/805/' + filename, "r", encoding="utf-8") as blargh:
    content = blargh.read()
    return string2 in content

with open('results.txt', 'w') as output:
  for fn in files:
    if does_fn_contain_string(fn):
      output.write('Current MW in node is: ' + fn +'\n')