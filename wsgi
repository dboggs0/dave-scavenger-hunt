[uwsgi]
http-socket = :$(PORT)
master = true
processes = 1
die-on-term = true

memory-report = true