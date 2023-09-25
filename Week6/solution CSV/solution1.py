from sqlite3 import *

conn = connect("c:\sqlite\week6.db")

curobj = conn.cursor()

create_table = """
create table if not exists result
(
Student_ID integer,
Student_Name text,
Mark1 integer,
Mark2 integer,
Mark3 integer,
Mark4 integer,
Mark5 integer
)
"""

curobj.execute(create_table)

conn.commit()

conn.commit()
