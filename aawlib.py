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
def multiplechoice(conn, tt):
    return
