
   
```
   sudo apt install -y gcc nvidia-driver-535-server-open nvidia-cuda-toolkit
   sudo apt update
   sudo shutdown -r now
   sudo apt update && sudo apt upgrade
   nvcc -help
   pip3 install torch torchvision torchaudio
```
https://drakeor.com/2022/02/16/kvm-gpu-passthrough-tutorial/


First, we need to make sure if iommu is enabled
sudo dmesg |grep -e IOMMU

if not, open  /etc/default/grub
add ```

GRUB_CMDLINE_LINUX_DEFAULT="intel_iommu=on"
```

Then, you need to
``` 
 sudo update-grub
```
then, reboot

vfio are added by default I guess that you do not have to specify them 

 vfio
 vfio_iommu_type1
 vfio_pci
 vfio_virqfd



Reference: https://leduccc.medium.com/simple-dgpu-passthrough-on-a-dell-precision-7450-ebe65b2e648e

https://pve.proxmox.com/wiki/PCI(e)_Passthrough



Other links

https://ubuntu.com/server/docs/gpu-virtualization-with-qemu-kvm
https://devicetests.com/enable-gpu-passthrough-qemu-ubuntu

Ubuntu server
https://releases.ubuntu.com/22.04.3/ubuntu-22.04.3-live-server-amd64.iso




echo "blacklist nouveau" | sudo tee /etc/modprobe.d/blacklist-nouveau.conf          
echo "options nouveau modeset=0" | sudo tee -a /etc/modprobe.d/blacklist-nouveau.conf
sudo update-initramfs -u      




---------------------------------


installed nvidia-driver-535 on vM
one the server nvidia-driver-535-server-open

need to blacklist nouva and set 


echo "blacklist nouveau" | sudo tee /etc/modprobe.d/blacklist-nouveau.conf          
echo "options nouveau modeset=0" | sudo tee -a /etc/modprobe.d/blacklist-nouveau.conf
sudo update-initramfs -u                                                         
sudo reboot   