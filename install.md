# Readme

Command for Ansible
```
ansible-playbook -i inventory.ini --extra-vars "ansible_ssh_user=sysadmin ansible_ssh_password= otp=" users.yml
```
```
ansible-playbook -i inventory.ini - users.yml
```
  
  ### ssh
```
eval $(ssh-agent)
ssh-add
```
  
 ```  
ansible playbook -k (you specify sudo password)
```
  
  
### Installation steps For a fresh physical servers:

 1. install cloud strike
 2. install MS defender
 3. install pam
 4. From ansible1@raduis server, run the following playbooks
	 1. lvm
	 2. kvm
	 3. download iso
	 4. packages
5. resize images
6. add security_driver= "none" to /etc/libvirt/qemu.conf

  

### software to install
--------------------
 - Apache Sedona
- Apache Iceberg
- Ray.io
- scylladb
- Pandas
- Polar
- databases
- duckdb
- postgresql
- mysql
- llm models
- lama
- Hadoop
- Spark
- performance monitoring
- SLURM


## to add

bypass gpu


http://download.nvidia.com/XFree86/Linux-x86_64/515.43.04/README/kernel_open.html

https://askubuntu.com/questions/1406888/ubuntu-22-04-gpu-passthrough-qemu