import paramiko
import pprint
k = paramiko.RSAKey.from_private_key_file('/home/absentia/Downloads/test-abhilash',password="Absentia01")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("35.200.172.47", username="cloud_absentia", pkey=k )
pprint.pprint('trying to connect')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("(cd /home/cloud_absentia/test; git pull origin master; git status;)")
pprint.pprint(ssh_stdout.read())
