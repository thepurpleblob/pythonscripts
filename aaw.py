import sys
import pymysql
import pprint
import aawlib

# instantiate PrettyPrint for debugging
pp = pprint.PrettyPrinter(indent=4);

# holder for current data hierarchy
class ttclass:
    pass

# connect to aaw db
conn = pymysql.connect(host='localhost', user='root', db='aaw');

# get courses
courses = aawlib.getcourses(conn)

# iterate over courses
tt = ttclass()
for course in courses:
    tt.courseid = course[0]
    tt.fullname = course[1]
    tt.shortname = course[2]
    print("Processing course " + tt.fullname)

    # get writings in current course
    writings = aawlib.getwritings(conn, tt.courseid)

    # iterate over writings
    for writing in writings:
        tt.writingid = writing[0]
        tt.name = writing[2]
        tt.intro = writing[3]
        print("    Writing activity " + tt.name);

        # get tasks in current writing
        tasks = aawlib.gettasks(conn, tt.writingid)

        # iterate over tasks
        for task in tasks:
            tt.taskid = task[0]
            tt.tasktype = task[2]
            tt.tasktypeid = task[3]
            tt.difficulty = task[4]
            print( "        Task " + tt.tasktype + " difficulty " + str(tt.difficulty))

            # handler for task type
            if tt.tasktype == 'multiplechoice':
                aawlib.multiplechoice(conn, tt)
            elif tt.tasktype == 'wordclick':
                aawlib.wordclick(conn, tt)
            elif tt.tasktype == 'freetext':
                aawlib.freetext(conn, tt)
            elif tt.tasktype == 'selectcat':
                aawlib.freetext(conn, tt)
            else:
                print( "            Tasktype not recognised!")

    
