--- 

terraform {
    required_providers {
      libvirt = {
        source = "dmacvicar/libvirt"
      }
    }
  
  }
  
  # instance the provider
  provider "libvirt" {
    uri = "qemu:///system"
  }
  # We fetch the latest ubuntu release image from their mirrors
  resource "libvirt_volume" "vol-my_vm-1" {
    name   = "vol-my_vm-1.qcow2"
    pool   = "default" 
    source = "/pool/iso/ubuntu22.04.img"
    format = "qcow2"
  }
  
    resource "libvirt_volume" "vol-cloudinit-my_vm-1" {
     name   = "vol-cloudinit-my_vm-1.qcow2"
     pool  = "default"
     user_data = templatefile("${path.module}/cloud_init.cfg", {
      host_name =  "my_vm"
      auth_key  = file("~/.ssh/id_vm.pub")
    })
    network_config = templatefile("${path.module}/network_config.cfg", {
      interface = "ens4"
      ip_addr   = "10.100.14.1"
      mac_addr  = "ae:52:0a:b0:14:01"
    })
  }
  # Create the machine
  resource "libvirt_domain" "dom-my_vm-1" {
    count      = 1
    name       = "my_vm-1"
    memory     = "4096"
    vcpu       =  "4"
    machine    = "pc"
    autostart  = true
  #  qemu_agent = true # this is recommended to get ip address
    disk {
      volume_id = libvirt_volume.vol-my_vm-1.id
    }
  
    cloudinit = libvirt_cloudinit_disk.vol-cloudinit-my_vm-1.id
  
    network_interface {
      network_name = "default"
    }
    network_interface {
      bridge    = "br0"
      addresses = ["10.100.14.1"]
      mac       = "ae:52:0a:b0:14:01"
    }
    boot_device {
      dev = ["hd", "network"]
    }
  
    # IMPORTANT
    # Ubuntu can hang is a isa-serial is not present at boot time.
    # If you find your CPU 100% and never is available this is why
    console {
      type        = "pty"
      target_port = "0"
      target_type = "serial"
    }
  
    console {
      type        = "pty"
      target_type = "virtio"
      target_port = "1"
    }
  
    graphics {
      type        = "spice"
      listen_type = "address"
      autoport    = "true"
    }
  }
  