import sys
import pprint
import aawxml
from lxml.html.clean import Cleaner

pp = pprint.PrettyPrinter(indent=4);

def clean_word(text):
    "Remove MS Word style crap"
    cleaner = Cleaner(style=True)
    try:
        cleantext = cleaner.clean_html(text)
    except:
        cleantext = text
    return text

#
# Get the list of courses
#
def getcourses(conn):
    cur = conn.cursor();
    sql = 'SELECT DISTINCT w.course AS courseid, fullname, shortname '
    sql += 'FROM mdl_writing w JOIN mdl_course c '
    sql += 'ON (w.course = c.id) '
    cur.execute(sql)
    courses = cur.fetchall()
    cur.close()
    return courses

# 
# get the list of writing activities within a course
#
def getwritings(conn, courseid):
    cur = conn.cursor()
    sql = 'SELECT * FROM mdl_writing WHERE course=' + str(courseid)
    cur.execute(sql)
    writings = cur.fetchall()
    cur.close()
    return writings

# 
# get the list of tasks within a writing activity
#
def gettasks(conn, writingid):
    cur = conn.cursor()
    sql = 'SELECT * FROM mdl_writingtask WHERE writingid=' + str(writingid)
    cur.execute(sql)
    tasks = cur.fetchall()
    cur.close()
    return tasks

#
# Handle multiplechoice
#
def multiplechoice(f, conn, tt):

    # Get the question intro
    cur = conn.cursor()
    sql = 'SELECT * FROM mdl_writing_mcq WHERE id=' + str(tt.tasktypeid)
    cur.execute(sql)
    mcq = cur.fetchone()
    cur.close()
    intro = clean_word(mcq[1])
    print( 'INTRO ' + intro )

    # get the question(s) for the above
    cur = conn.cursor();
    sql = 'SELECT * FROM mdl_writing_mcq_question where mcq_id=' + str(tt.tasktypeid)
    sql += ' ORDER BY question_number'
    cur.execute(sql)
    questions = cur.fetchall()
    cur.close

    # iterate over questions and get answers
    for question in questions:
        qid = question[0]
        qtext = clean_word(question[2])
        question_number = question[3]
        print( '    QUESTION ' + str(question_number) + ' ' + qtext )
        cur = conn.cursor()
        sql = 'SELECT * FROM mdl_writing_mcq_answer WHERE question_id=' + str(qid)
        cur.execute(sql)
        answers = cur.fetchall()

        # must be 2 or more answers or question is bogus
        if len(answers) < 2:
            print( '        **ERROR** Not enough answers. Rejecting' )
            return
        cur.close
        aawxml.mcqmain(f, qid, intro, qtext)

        # interate over answers
        for answer in answers:
            atext = clean_word(answer[2])
            feedback = clean_word(answer[3])
            print( '        ANSWER: ' + atext)
            print( '        FEEDBACK: ' + feedback)
            aawxml.mcqanswer(f, atext, feedback)
       
        # close question
        aawxml.questionclose(f)
 
    return

#
# Handle wordclick
#
def wordclick(f, conn, tt):
    return

#
# Handle freetext
#
def freetext(f, conn, tt):

    # Get the question intro
    cur = conn.cursor()
    sql = 'SELECT * FROM mdl_writing_freetext WHERE id=' + str(tt.tasktypeid)
    cur.execute(sql)
    freetext = cur.fetchone()
    cur.close()
    essayid = freetext[0]
    if freetext[1]:
        intro = clean_word(freetext[1])
    else:
        intro = ''
    problemtext = clean_word(freetext[2])
    sampleanswer = clean_word(freetext[3])
    explanationtext = clean_word(freetext[4])
    print( 'INTRO ' + intro )
    aawxml.essaymain(f, essayid, intro, problemtext, sampleanswer, explanationtext)
    aawxml.questionclose(f)
    return
#
# Handle selectcat
#
def selectcat(f, conn, tt):
    return
