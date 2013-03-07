## Text Parser for NAM Data
fyle = open('nam_data.html', 'r')

text = fyle.read()
charLength = text.__len__()

start_location = text.find('HOUR')
start_quote = text.find('000', start_location)
end = charLength



print(text[start_quote:end])





fyle.close()
