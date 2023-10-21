# change size
# try iso

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



variable "hosts_1" {
  type    = number
  default = 1
}

variable "interface_1" {
  type    = string
  default = "ens4"
}

locals {
  ips_1   = [for i in range(var.hosts_1) : "10.100.14.${format("%s", i + 10)}"]
  names_1 = [for i in range(var.hosts_1) : "owhpc-vm_1-${format("%s", 10+i)}"]
  macs_1  = [for i in range(var.hosts_1) : "ae:52:0a:b0:14:${format("%02x", i + 10)}"]
  items_1 = [for i in range(var.hosts_1) :  "${format("%s", i+10)}"]
}

# We fetch the latest ubuntu release image from their mirrors
resource "libvirt_volume" "vol-owhpc-vm_1-qcow2" {
  count  = var.hosts_1
  name   = "owhpc-vm_1-${count.index}.qcow2"
  pool   = "default" #CHANGE_ME
  source = "/pool/iso/ubuntu22.04.img"
  format = "qcow2"
}

resource "libvirt_cloudinit_disk" "vol-owhpc-vm_1-commoninit" {
  count = var.hosts_1
  name  = "owhpc-vm_1-commoninit-${local.names_1[count.index]}.iso"
  pool  = "default"
  user_data = templatefile("${path.module}/cloud_init.cfg", {
    host_name = local.names_1[count.index]
    auth_key  = file("~/.ssh/id_vm.pub")
  })
  network_config = templatefile("${path.module}/network_config.cfg", {
    interface = var.interface_1
    ip_addr   = local.ips_1[count.index]
    mac_addr  = local.macs_1[count.index]
  })
}
# Create the machine
resource "libvirt_domain" "dom-owhpc-vm_1-ubuntu" {
  count      = var.hosts_1
  name       = local.names_1[count.index]
  memory     = "4048"
  vcpu       = 2
  machine    = "pc"
  autostart  = true
#  qemu_agent = true # this is recommended to get ip address
  disk {
    volume_id = libvirt_volume.vol-owhpc-vm_1-qcow2[count.index].id
  }

  cloudinit = libvirt_cloudinit_disk.vol-owhpc-vm_1-commoninit[count.index].id

  network_interface {
    network_name = "default"
  }
  network_interface {
    bridge    = "br0"
    addresses = [local.ips_1[count.index]]
    mac       = local.macs_1[count.index]
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

output "ip_1" {
  value = local.ips_1
}

output "mac_1" {
  value = local.macs_1
}



variable "hosts_2" {
  type    = number
  default = 1
}

variable "interface_2" {
  type    = string
  default = "ens4"
}

locals {
  ips_2   = [for i in range(var.hosts_2) : "10.100.14.${format("%s", i + 10)}"]
  names_2 = [for i in range(var.hosts_2) : "owhpc-vm_2-${format("%s", 10+i)}"]
  macs_2  = [for i in range(var.hosts_2) : "ae:52:0a:b0:14:${format("%02x", i + 10)}"]
  items_2 = [for i in range(var.hosts_2) :  "${format("%s", i+10)}"]
}

# We fetch the latest ubuntu release image from their mirrors
resource "libvirt_volume" "vol-owhpc-vm_2-qcow2" {
  count  = var.hosts_2
  name   = "owhpc-vm_2-${count.index}.qcow2"
  pool   = "default" #CHANGE_ME
  source = "/pool/iso/ubuntu22.04.img"
  format = "qcow2"
}

resource "libvirt_cloudinit_disk" "vol-owhpc-vm_2-commoninit" {
  count = var.hosts_2
  name  = "owhpc-vm_2-commoninit-${local.names_2[count.index]}.iso"
  pool  = "default"
  user_data = templatefile("${path.module}/cloud_init.cfg", {
    host_name = local.names_2[count.index]
    auth_key  = file("~/.ssh/id_vm.pub")
  })
  network_config = templatefile("${path.module}/network_config.cfg", {
    interface = var.interface_2
    ip_addr   = local.ips_2[count.index]
    mac_addr  = local.macs_2[count.index]
  })
}
# Create the machine
resource "libvirt_domain" "dom-owhpc-vm_2-ubuntu" {
  count      = var.hosts_2
  name       = local.names_2[count.index]
  memory     = "4048"
  vcpu       = 2
  machine    = "pc"
  autostart  = true
#  qemu_agent = true # this is recommended to get ip address
  disk {
    volume_id = libvirt_volume.vol-owhpc-vm_2-qcow2[count.index].id
  }

  cloudinit = libvirt_cloudinit_disk.vol-owhpc-vm_2-commoninit[count.index].id

  network_interface {
    network_name = "default"
  }
  network_interface {
    bridge    = "br0"
    addresses = [local.ips_2[count.index]]
    mac       = local.macs_2[count.index]
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

output "ip_2" {
  value = local.ips_2
}

output "mac_2" {
  value = local.macs_2
}

