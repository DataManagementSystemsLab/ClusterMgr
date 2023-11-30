import paramiko
import time
import crypt
# Connect to the remote machine using SSH
def run_command_remotely_asroot(host, username, password, commands):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(host, username=username, password=password)
		root_command = f'sudo su - '
		root_shell = ssh.invoke_shell()
		root_shell.send(root_command + '\n')
		#root_shell.send(password + '\n')
		time.sleep(0.1)
		while not root_shell.recv_ready():
			pass
		output = root_shell.recv(4096).decode('utf-8')
		print(output)
		print("---------login----------------")
		
		for command in commands:
			print(command)
			root_shell.send(command + '\n')
			time.sleep(0.1)
			while not root_shell.recv_ready():
				pass
			output = root_shell.recv(4096).decode('utf-8')
			print(output)
	
	except Exception as e:
		print(f"An error occurred: {str(e)}")

	finally:
		if ssh:
			ssh.close()


class AddUser:
	def __init__(self, username, password):
		self.username = username
		self.password = password
	def __str__(self) -> str:
		hashedpassword = crypt.crypt(self.password)
		return f"useradd -m {self.username} -p '{hashedpassword} -s /bin/bash'"

