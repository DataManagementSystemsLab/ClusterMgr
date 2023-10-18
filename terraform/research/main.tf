#ansible-galaxy collection install community.mysql
# fix qemu-agent
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
resource "libvirt_volume" "rvm-ubuntu-qcow2" {
  count  = var.hosts
  name   = "rvm-qcow2${count.index}"
  pool   = "default" #CHANGE_ME
  source = "/pool/iso/ubuntu22.04.img"
  format = "qcow2"
}

resource "libvirt_cloudinit_disk" "rvm-commoninit" {
  count = var.hosts
  name  = "rvm-commoninit-${local.names[count.index]}.iso"
  pool  = "default"
  user_data = templatefile("${path.module}/cloud_init.cfg", {
    host_name = local.names[count.index]
    user_name = local.names[count.index]
    auth_key  = file("~/.ssh/id_vm.pub")
  })
  network_config = templatefile("${path.module}/network_config.cfg", {
    interface = var.interface
    ip_addr   = local.ips[count.index]
    mac_addr  = local.macs[count.index]
    
  })
}
# Create the machine
resource "libvirt_domain" "rvm-domain-ubuntu" {
 
  count      = var.hosts
  name       = local.names[count.index]
  memory     = local.memory[count.index]
  vcpu       = local.vcpu [count.index]
  machine    = "pc"
  autostart  = true
  qemu_agent = true # this is recommended to get ip address
  disk {
    volume_id = libvirt_volume.rvm-ubuntu-qcow2[count.index].id
  }

  cloudinit = libvirt_cloudinit_disk.rvm-commoninit[count.index].id

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
