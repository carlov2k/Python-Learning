import pexpect
ping = pexpect.popen_spawn.PopenSpawn('ping -c 5 localhost')
result = ping.expect([pexpect.EOF,pexpect.TIMEOUT])
print(ping.before)