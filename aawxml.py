def header(f):
    "Write header"
    f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
    f.write('<quiz>\n')

def footer(f):
    "Write footer"
    f.write('</quiz>\n')
