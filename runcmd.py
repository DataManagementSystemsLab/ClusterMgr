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
		root_shell.send(password + '\n')
		time.sleep(0.1)
		while not root_shell.recv_ready():
			pass
		output = root_shell.recv(4096).decode('utf-8')
		print(output)
		print("---------login----------------")
		
		for command in commands:
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
		return f"useradd -m {self.username} -p '{hashedpassword}'"

username = 'sysadmin'
host = '10.100.6.50'
password = 'linux'




#new_username = 'new_usera'
#new_password = '1234'
#	create_user_command = f'useradd -m {new_username} && passwd {new_username}'
