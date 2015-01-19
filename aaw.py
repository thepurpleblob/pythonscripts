import pymysql
import pprint
import aawlib

# instantiate PrettyPrint for debugging
pp = pprint.PrettyPrinter(indent=4);

# connect to aaw db
conn = pymysql.connect(host='localhost', user='root', db='aaw');

# get courses
courses = aawlib.getcourses(conn)

# iterate over courses
for course in courses:
    courseid = course[0]
    fullname = course[1]
    shortname = course[2]
    print("Processing course " + fullname)

    
