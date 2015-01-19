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

