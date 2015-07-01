def header(f):
    "Write header"
    f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
    f.write('<quiz>\n')
    return

def footer(f):
    "Write footer"
    f.write('</quiz>\n')
    return

def category(f, cat):
    "Write category pseudo-question"
    f.write('<question type="category">\n')
    f.write('  <category><text>'+cat+'</text></category>\n')
    f.write('</question>')
    return

def mcqmain(f, qid, intro, qtext):
    "Write main part of multiple choice question"
    f.write('<question type="multichoice">\n')
    f.write('  <name><text>MCQ question ' + str(qid) + '</text></name>\n')
    f.write('  <questiontext format="html">\n')
    f.write('    <text><![CDATA[' + intro.rstrip() + '<br /><br /><b>' + qtext.rstrip() + '</b>]]></text>\n')
    f.write('  </questiontext>\n')
    return

def mcqanswer(f, atext, feedback):
    "Write answer parts of multiple choice question"
    f.write('  <answer format="html">\n')
    f.write('    <text><![CDATA[' + atext + ']]></text>\n')
    f.write('    <feedback><text><![CDATA[' + feedback.rstrip() + ']]></text></feedback>\n')
    f.write('  </answer>\n')
    return

def questionclose(f):
    "Close any question"
    f.write('</question>\n\n')
    return

def essaymain(f, essayid, intro, problemtext, sampleanswer, explanationtext):
    "Write main part of essay question"
    f.write('<question type="essay">\n')
    f.write('  <name><text>Essay question ' + str(essayid) + '</text></name>\n')
    f.write('  <questiontext format="html">\n')
    f.write('    <text><![CDATA[' + intro.rstrip() + '<br /><br /><b>"' + problemtext.rstrip() + '"</b>]]></text>\n')
    f.write('  </questiontext>\n')
    f.write('  <generalfeedback>\n')
    f.write('    <text><![CDATA[Sample answer, "' + sampleanswer + '"<br /><br /><b>' + explanationtext + '</b>]]></text>\n')
    f.write('  </generalfeedback>\n')
    return
