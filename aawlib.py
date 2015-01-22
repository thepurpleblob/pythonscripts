import sys
import pprint

pp = pprint.PrettyPrinter(indent=4);

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
def multiplechoice(conn, tt):

    # Get the question intro
    cur = conn.cursor()
    sql = 'SELECT * FROM mdl_writing_mcq WHERE id=' + str(tt.tasktypeid)
    cur.execute(sql)
    mcq = cur.fetchone()
    cur.close()
    intro = mcq[1];
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
        qtext = question[2]
        question_number = question[3]
        print( '    QUESTION ' + str(question_number) + ' ' + qtext )
        cur = conn.cursor()
        sql = 'SELECT * FROM mdl_writing_mcq_answer WHERE question_id=' + str(qid)
        cur.execute(sql)
        answers = cur.fetchall()
        cur.close

        # interate over answers
        for answer in answers:
            atext = answer[2]
            feedback = answer[3]
            print( '        ANSWER: ' + atext)
            print( '        FEEDBACK: ' + feedback)
        
    return

#
# Handle wordclick
#
def wordclick(conn, tt):
    return

#
# Handle freetext
#
def freetext(conn, tt):
    return
#
# Handle selectcat
#
def selectcat(conn, tt):
    return
