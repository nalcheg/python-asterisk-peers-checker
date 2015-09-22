#!/usr/bin/python

import commands,MySQLdb
commands.getstatusoutput('asterisk -x "sip show peers" > /tmp/sipshowpeers')

import config
db = MySQLdb.connect(config.dbhost,config.dbuser,config.dbpassword,config.dbname)
cursor = db.cursor()

with open('/tmp/sipshowpeers') as f:
    content = f.readlines()

i = 1;
while (content[i][0] <> "s"):
    row = content[i].split()
    peer = row[0].split('/')
    peer = peer[0]
    ip = row[1]
    state = 0
    ping = "0"

    if len(row) > 8 :
        ping = row[7].split('(')
        ping = ping[1]
        state = 1

    sql = "SELECT state,peer FROM amon WHERE peer='%s' order by id desc limit 1" % ( peer )
    try:
        cursor.execute(sql)
        if cursor.rowcount == 0 :
            insert_sql="INSERT INTO amon (peer,state,ping,ip) VALUES ('%s',%d,'%s','%s')" % (peer,state,ping,ip)
            try:
                cursor.execute(insert_sql)
                db.commit()
            except:
                print "insert failed"
                db.rollback()
        else:
            staterow = cursor.fetchone()
            if staterow[0] != state :
                insert_sql="INSERT INTO amon (peer,state,ping,ip) VALUES ('%s',%d,'%s','%s')" % (peer,state,ping,ip)
                try:
                    cursor.execute(insert_sql)
                    db.commit()
                except:
                    print "insert failed"
                    db.rollback()
    except:
        print "Error: unable to fetch data from table"
    i=i+1

db.close()
    
