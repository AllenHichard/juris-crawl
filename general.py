from web import session

cnj = "0102336-13.2018.8.06.0001"
s = session.Session(cnj=cnj)
s.consult_process()
#print(s.returned_processes[0].json())



