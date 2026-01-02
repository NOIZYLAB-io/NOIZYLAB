import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('macpro.local', username='rsp_ms', password='yourpass')
stdin, stdout, stderr = client.exec_command('bash /usr/local/bin/noizy_silence.sh')
print(stdout.read().decode())
client.close()
