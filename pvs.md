
Step 1 – Find out information about existing LVM
------------------------------------------------

LVM Storage Management divided into three parts:

1.  **Physical Volumes (PV)** – Actual disks (e.g. /dev/sda, /dev,sdb, /dev/vdb and so on)
2.  **Volume Groups (VG)** – Physical volumes are combined into volume groups. (e.g. my_vg = /dev/sda + /dev/sdb.)
3.  **Logical Volumes (LV)** – A volume group is divided up into logical volumes (e.g. my\_vg divided into my\_vg/data, my\_vg/backups, my\_vg/home, my_vg/mysqldb and so on)

Type the following commands to find out information about each part.

### How to display physical volumes (pv)

Type the following pvs command to see info about physical volumes:  
`$ sudo pvs`  
Sample outputs:  

[![Fig.01: How to display information about LVM physical volumes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20610%20130'%3E%3C/svg%3E)<br>![Fig.01: How to display information about LVM physical volumes](https://www.cyberciti.biz/media/new/faq/2017/02/pvs-command-to-display-lvm-physical-volumes.jpg)](https://www.cyberciti.biz/faq/howto-add-disk-to-lvm-volume-on-linux-to-increase-size-of-pool/pvs-command-to-display-lvm-physical-volumes/)

Fig.01: How to display information about LVM physical volumes

So currently my LVM include a physical volume (actual disk) called /dev/vda5. To see detailed attributes information, type:  
`$ sudo pvdisplay`  
Sample outputs:  

[![Fig.02: See attributes of a physical volume (PV)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20599%20263'%3E%3C/svg%3E)<br>![Fig.02: See attributes of a physical volume (PV)](https://www.cyberciti.biz/media/new/faq/2017/02/pvdisplay-show.jpg)](https://www.cyberciti.biz/faq/howto-add-disk-to-lvm-volume-on-linux-to-increase-size-of-pool/pvdisplay-show/)

Fig.02: See attributes of a physical volume (PV)

From above output it is clear that our volume group named ubuntu-box-1-vg is made of a physical volume named /dev/vda5.

### How to display information about LVM volume Groups (vg)

Type any one of the following vgs command/vgdisplay command to see information about volume groups and its attributes:  
`$ sudo vgs`  
OR  
`$ sudo vgdisplay`  
Sample outputs:  

[![Fig.03: How to see information about LVM volume groups (vg)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20599%20488'%3E%3C/svg%3E)<br>![Fig.03: How to see information about LVM volume groups (vg)](https://www.cyberciti.biz/media/new/faq/2017/02/howto-see-lvm-volume-groups-infomation.jpg)](https://www.cyberciti.biz/faq/howto-add-disk-to-lvm-volume-on-linux-to-increase-size-of-pool/howto-see-lvm-volume-groups-infomation/)

Fig.03: How to see information about LVM volume groups (vg)

### How to display information about LVM logical volume (lv)

Type any one of the following lvs command/lvdisplay command to see information about volume groups and its attributes:  
`$ sudo lvs`  
OR  
`$ sudo lvdisplay`  
Sample outputs:  

[![Fig.04: How to display information about logical volumes (lv)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20599%20679'%3E%3C/svg%3E)<br>![Fig.04: How to display information about logical volumes (lv)](https://www.cyberciti.biz/media/new/faq/2017/02/howto-see-display-information-lvm-logical-volumes.jpg)](https://www.cyberciti.biz/faq/howto-add-disk-to-lvm-volume-on-linux-to-increase-size-of-pool/howto-see-display-information-lvm-logical-volumes/)

Fig.04: How to display information about logical volumes (lv)  

My ubuntu-box-1-vg volume group divided into two logical volumes:

1.  /dev/ubuntu-box-1-vg/root – Root file system
2.  /dev/ubuntu-box-1-vg/swap_1 – Swap space

Based upon above commands, you can get a basic idea how LVM organizes storage device into Physical Volumes (PV), Volume Groups (VG), and Logical Volumes (LV):  

[![Fig.05: How LVM organizes storage device into Physical Volumes (PV), Volume Groups (VG), & Logical Volumes (LV)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20307'%3E%3C/svg%3E)<br>![Fig.05: How LVM organizes storage device into Physical Volumes (PV), Volume Groups (VG), & Logical Volumes (LV)](https://www.cyberciti.biz/media/new/faq/2017/02/understanding-LVM-Architecture.jpg)](https://www.cyberciti.biz/faq/howto-add-disk-to-lvm-volume-on-linux-to-increase-size-of-pool/understanding-lvm-architecture/)

Fig.05: How LVM organizes storage device into Physical Volumes (PV), Volume Groups (VG), & Logical Volumes (LV)

Step 2 – Find out information about new disk
--------------------------------------------

You need to add a new disk to your server. In this example, for demo purpose I added a new disk drive, and it has 5GiB size. To find out information about new disks run:  
`$ sudo fdisk -l`  
OR  
`$ sudo fdisk -l | grep '^Disk /dev/'`  
Sample outputs:  

[![Fig.06: Find out installed disk names on Linux](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20599%20267'%3E%3C/svg%3E)<br>![Fig.06: Find out installed disk names on Linux](https://www.cyberciti.biz/media/new/faq/2017/02/list-linux-disks-using-fdisk-lcommand.jpg)](https://www.cyberciti.biz/faq/howto-add-disk-to-lvm-volume-on-linux-to-increase-size-of-pool/list-linux-disks-using-fdisk-lcommand/)

Fig.06: Find out installed disk names on Linux

Another option is to scan for all devices visible to LVM2:  
`$ sudo lvmdiskscan`  
Sample outputs:

  /dev/ram0                   \[      64.00 MiB\] 
  /dev/ubuntu-box-1-vg/root   \[      37.49 GiB\] 
  /dev/ram1                   \[      64.00 MiB\] 
  /dev/ubuntu-box-1-vg/swap_1 \[       2.00 GiB\] 
  /dev/vda1                   \[     487.00 MiB\] 
  /dev/ram2                   \[      64.00 MiB\] 
  /dev/ram3                   \[      64.00 MiB\] 
  /dev/ram4                   \[      64.00 MiB\] 
  /dev/ram5                   \[      64.00 MiB\] 
 /dev/vda5                   \[      39.52 GiB\] LVM physical volume
  /dev/ram6                   \[      64.00 MiB\] 
  /dev/ram7                   \[      64.00 MiB\] 
  /dev/ram8                   \[      64.00 MiB\] 
  /dev/ram9                   \[      64.00 MiB\] 
  /dev/ram10                  \[      64.00 MiB\] 
  /dev/ram11                  \[      64.00 MiB\] 
  /dev/ram12                  \[      64.00 MiB\] 
  /dev/ram13                  \[      64.00 MiB\] 
  /dev/ram14                  \[      64.00 MiB\] 
  /dev/ram15                  \[      64.00 MiB\] 
 /dev/vdb                    \[       5.00 GiB\] 
  2 disks
  18 partitions
  0 LVM physical volume whole disks
  1 LVM physical volume

Step 3 – Create physical volumes (pv) on new disk named /dev/vdb
----------------------------------------------------------------

Type the following command:  
`$ sudo pvcreate /dev/vdb`  
Sample outputs:

  Physical volume "/dev/vdb" successfully created

Now run the following command to verify:  
`$ sudo lvmdiskscan -l`  
Sample outputs:

  WARNING: only considering LVM devices
  /dev/vda5                   \[      39.52 GiB\] LVM physical volume
  /dev/vdb                    \[       5.00 GiB\] LVM physical volume
  1 LVM physical volume whole disk
  1 LVM physical volume

Step 4 – Add newly created pv named /dev/vdb to an existing lv
--------------------------------------------------------------

Type the following command to add a physical volume /dev/vdb to “ubuntu-box-1-vg” volume group:  
`$ sudo vgextend ubuntu-box-1-vg /dev/vdb`  
Sample outputs:

  Volume group "ubuntu-box-1-vg" successfully extended

Finally, you need extend the /dev/ubuntu-box-1-vg/root to create total 45GB (/dev/vdb (5G)+ existing /dev/ubuntu-box-1-vg/root (40G))  
`$ sudo lvm lvextend -l +100%FREE /dev/ubuntu-box-1-vg/root`  
Sample outputs:

  Size of logical volume ubuntu-box-1-vg/root changed from 37.49 GiB (9597 extents) to 42.52 GiB (10885 extents).
  Logical volume root successfully resized.

However, if you run df -h or any other command you will still see /dev/ubuntu-box-1-vg/root as 40G. You need to run the following command to enlarge the filesystem created inside the “root” volume:  
`$ sudo resize2fs -p /dev/mapper/ubuntu--box--1--vg-root`  
Sample outputs:

resize2fs 1.42.13 (17-May-2015)
Filesystem at /dev/mapper/ubuntu--box--1--vg-root is mounted on /; on-line resizing required
old\_desc\_blocks = 3, new\_desc\_blocks = 3
The filesystem on /dev/mapper/ubuntu--box--1--vg-root is now 11146240 (4k) blocks long.

Verify it again using the [df command](https://www.cyberciti.biz/faq/df-command-examples-in-linux-unix/ "How to use df command in Linux / Unix {with examples}") or mount command. For example:  
`$ mount  
$ mount | [grep](https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/ "How to use grep command in Linux/ Unix with examples") '/dev/mapper/ubuntu'`  
OR  
`$ df -H`  
Sample outputs:

Filesystem                           Size  Used Avail Use% Mounted on
udev                                 1.1G     0  1.1G   0% /dev
tmpfs                                146M   12M  135M   9% /run
**/dev/mapper/ubuntu--box--1--vg-root   45G  2.3G   41G   6% /**
tmpfs                                512M     0  512M   0% /dev/shm
tmpfs                                5.3M     0  5.3M   0% /run/lock
tmpfs                                512M     0  512M   0% /sys/fs/cgroup
/dev/vda1                            495M  109M  361M  24% /boot
tmpfs                                103M     0  103M   0% /run/user/0



# lvextend -L+1G /dev/myvg/homevol
# resize2fs /dev/myvg/homevol