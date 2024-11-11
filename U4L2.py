import turtle

def modify(ln):
  # Strips everything except the essential string
  # ln = one line of data from first column to the carriage return
  #
  mod_string = ""
  badChars = ['"', ','] # chars to remove
  ln = ln.strip() # clean out non-printable chars
  for c in ln:
    if c not in badChars:
      mod_string = mod_string + c
  return mod_string # line of data should now be clean

fh = open("smiley_emoji_mod.xpm", "r") # open a file handle
color_data = fh.readline()
color_data = int(modify(color_data))
[cols, rows, colors] = color_data.split()
rows = int(rows)
cols = int(cols)
colors = int(colors)
colorData = {} # a dictionary of symbols and colors

for i in range(colors):
  cLine = fh.readline()
  cLine = modify(cLine)
  [sym, c, color] = cLine.split()
  colorData[sym] = color # add a new dictionary entry
