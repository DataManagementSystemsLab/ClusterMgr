# change size
# try iso


variable "hosts" {
  type    = number
  default = 1
}
variable "projname" {
  type    = string
  default = "owhpc-vm2"
}
variable "interface" {
  type    = string
  default = "ens4"
}
variable "memory" {
  type    = string
  default = "4048"
}
variable "vcpu" {
  type    = number
  default = 4
}
locals {
  ips   = [for i in range(var.hosts) : "10.100.14.${format("%s", i + 10)}"]
  names = [for i in range(var.hosts) : "owhpc-vm2-${format("%s", 10+i)}"]
  macs  = [for i in range(var.hosts) : "ae:52:0a:b0:14:${format("%02x", i + 10)}"]
  items = [for i in range(var.hosts) :  "${format("%s", i+10)}"]
}

terraform {
  required_providers {
    libvirt = {
      source = "dmacvicar/libvirt"
    }
  }

   backend "pg" {
    conn_str = "postgres://terraform:terra4pass@10.100.1.0/owcluster"
   }
}

# instance the provider
provider "libvirt" {
  uri = "qemu:///system"
}

# We fetch the latest ubuntu release image from their mirrors
resource "libvirt_volume" "vol-owhpc-vm2-qcow2" {
  count  = var.hosts
  name   = "owhpc-vm2-${count.index}.qcow2"
  pool   = "default" #CHANGE_ME
  source = "/pool/iso/ubuntu22.04.img"
  format = "qcow2"
}

resource "libvirt_cloudinit_disk" "vol-owhpc-vm2-commoninit" {
  count = var.hosts
  name  = "owhpc-vm2-commoninit-${local.names[count.index]}.iso"
  pool  = "default"
  user_data = templatefile("${path.module}/cloud_init.cfg", {
    host_name = local.names[count.index]
    auth_key  = file("~/.ssh/id_vm.pub")
  })
  network_config = templatefile("${path.module}/network_config.cfg", {
    interface = var.interface
    ip_addr   = local.ips[count.index]
    mac_addr  = local.macs[count.index]
  })
}
# Create the machine
resource "libvirt_domain" "dom-owhpc-vm2-ubuntu" {
  count      = var.hosts
  name       = local.names[count.index]
  memory     = "4048"
  vcpu       = 2
  machine    = "pc"
  autostart  = true
#  qemu_agent = true # this is recommended to get ip address
  disk {
    volume_id = libvirt_volume.vol-owhpc-vm2-qcow2[count.index].id
  }

  cloudinit = libvirt_cloudinit_disk.vol-owhpc-vm2-commoninit[count.index].id

  network_interface {
    network_name = "default"
  }
  network_interface {
    bridge    = "br0"
    addresses = [local.ips[count.index]]
    mac       = local.macs[count.index]
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

output "ip" {
  value = local.ips
}

output "mac" {
  value = local.macs
}
# change size
# try iso


variable "hosts" {
  type    = number
  default = 1
}
variable "projname" {
  type    = string
  default = "owhpc-vm1"
}
variable "interface" {
  type    = string
  default = "ens4"
}
variable "memory" {
  type    = string
  default = "4048"
}
variable "vcpu" {
  type    = number
  default = 4
}
locals {
  ips   = [for i in range(var.hosts) : "10.100.15.${format("%s", i + 10)}"]
  names = [for i in range(var.hosts) : "owhpc-vm1-${format("%s", 10+i)}"]
  macs  = [for i in range(var.hosts) : "ae:52:0a:b0:15:${format("%02x", i + 10)}"]
  items = [for i in range(var.hosts) :  "${format("%s", i+10)}"]
}

terraform {
  required_providers {
    libvirt = {
      source = "dmacvicar/libvirt"
    }
  }

   backend "pg" {
    conn_str = "postgres://terraform:terra4pass@10.100.1.0/owcluster"
   }
}

# instance the provider
provider "libvirt" {
  uri = "qemu:///system"
}

# We fetch the latest ubuntu release image from their mirrors
resource "libvirt_volume" "vol-owhpc-vm1-qcow2" {
  count  = var.hosts
  name   = "owhpc-vm1-${count.index}.qcow2"
  pool   = "default" #CHANGE_ME
  source = "/pool/iso/ubuntu22.04.img"
  format = "qcow2"
}

resource "libvirt_cloudinit_disk" "vol-owhpc-vm1-commoninit" {
  count = var.hosts
  name  = "owhpc-vm1-commoninit-${local.names[count.index]}.iso"
  pool  = "default"
  user_data = templatefile("${path.module}/cloud_init.cfg", {
    host_name = local.names[count.index]
    auth_key  = file("~/.ssh/id_vm.pub")
  })
  network_config = templatefile("${path.module}/network_config.cfg", {
    interface = var.interface
    ip_addr   = local.ips[count.index]
    mac_addr  = local.macs[count.index]
  })
}
# Create the machine
resource "libvirt_domain" "dom-owhpc-vm1-ubuntu" {
  count      = var.hosts
  name       = local.names[count.index]
  memory     = "4048"
  vcpu       = 2
  machine    = "pc"
  autostart  = true
#  qemu_agent = true # this is recommended to get ip address
  disk {
    volume_id = libvirt_volume.vol-owhpc-vm1-qcow2[count.index].id
  }

  cloudinit = libvirt_cloudinit_disk.vol-owhpc-vm1-commoninit[count.index].id

  network_interface {
    network_name = "default"
  }
  network_interface {
    bridge    = "br0"
    addresses = [local.ips[count.index]]
    mac       = local.macs[count.index]
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

output "ip" {
  value = local.ips
}

output "mac" {
  value = local.macs
}
