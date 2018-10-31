"""
    Hello world `receive.py` example implementation using aioamqp.
    See the documentation for more informations.
"""
# import xmltools
import asyncio
import aioamqp
import sqlite3
import json
import string
import csv
import dicttoxml
import itertools
from xlsxwriter.workbook import Workbook

def dictfetchall(cursor):
    desc = cursor.description
    return [dict(itertools.izip([col[0] for col in desc], row))
            for row in cursor.fetchall()]

@asyncio.coroutine
def callback(channel, body, envelope, properties):
    print(" [x] Received %r" % body)
    path=body.decode().split(" ")[0]
    type=body.decode().split(" ")[1]
    conn = sqlite3.connect(path)
    c = conn.cursor()
    fd = open('C:\\Users\\Cameras\\Desktop\\aioamqp-0.11.0\\sql.sql', 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    f= open('C:\\Users\\Cameras\\Desktop\\test.'+type,'w+')
    if type=='json':
        for command in sqlCommands:
             rows=c.execute(command).fetchall()
             if not c.description:
                columns = []
             else:
                column = [t[0] for t in c.description]
             for row in rows:
                json_dict = {}
                for j in range(len(column)):
                    key_j = column[j]
                    json_dict[key_j] = row[j]
                f.write(json.dumps(json_dict, indent=3))
        conn.close()
    elif type=='xml':
      for command in sqlCommands:
             rows=c.execute(command).fetchall()
             if not c.description:
                columns = []
             else:
                column = [t[0] for t in c.description]
             for row in rows:
                json_dict = {}
                for j in range(len(column)):
                    key_j = column[j]
                    json_dict[key_j] = row[j]
                xml=dicttoxml.dicttoxml(json_dict, attr_type=False)
                f.write(str(xml))
      conn.close()
    elif type=='csv':
        workbook = Workbook('C:\\Users\\Cameras\\Desktop\\test.csv')
        worksheet = workbook.add_worksheet()
        for command in sqlCommands:
            rows=c.execute(command)
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                 worksheet.write(i,j,value)
        workbook.close()
        conn.close()

    f.close()


@asyncio.coroutine
def receive():
    transport, protocol = yield from aioamqp.connect()
    channel = yield from protocol.channel()

    yield from channel.queue_declare(queue_name='b')

    yield from channel.basic_consume(callback, queue_name='b')


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(receive())
event_loop.run_forever()
