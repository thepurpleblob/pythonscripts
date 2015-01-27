import sys
import pymysql
import pprint
import aawlib
import aawxml

# instantiate PrettyPrint for debugging
pp = pprint.PrettyPrinter(indent=4);

# check command line arguments
if len(sys.argv) != 2:
    print('Usage: python3 aaw.py <xmlfile>')
    sys.exit(1)

# output file
filename = sys.argv[1]
f = open(filename, 'w')
aawxml.header(f)

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
    tt.fullname = course[1].strip()
    tt.shortname = course[2].strip()
    print("Processing course " + tt.fullname)
    aawxml.category(f, '$cat1$/'+tt.fullname)

    # get writings in current course
    writings = aawlib.getwritings(conn, tt.courseid)

    # iterate over writings
    for writing in writings:
        tt.writingid = writing[0]
        tt.name = writing[2].strip()
        tt.intro = writing[3].strip()
        print("    Writing activity " + tt.name);
        aawxml.category(f, '$cat1$/'+tt.shortname+'/'+tt.name)

        # get tasks in current writing
        tasks = aawlib.gettasks(conn, tt.writingid)

        # iterate over tasks
        for task in tasks:
            tt.taskid = task[0]
            tt.tasktype = str(task[2])
            tt.tasktypeid = task[3]
            tt.difficulty = task[4]
            print( "        Task " + tt.tasktype + " difficulty " + str(tt.difficulty))

            # handler for task type
            if tt.tasktype == 'multiplechoice':
                aawlib.multiplechoice(f, conn, tt)
            elif tt.tasktype == 'wordclick':
                aawlib.wordclick(f, conn, tt)
            elif tt.tasktype == 'freetext':
                aawlib.freetext(f, conn, tt)
            elif tt.tasktype == 'selectcat':
                aawlib.selectcat(f, conn, tt)
            else:
                print( "            Tasktype not recognised!")

aawxml.footer(f)
f.close() 
