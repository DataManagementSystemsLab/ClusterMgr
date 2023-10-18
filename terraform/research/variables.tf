variable "hosts" {
  type    = number
  default = 9
}
variable "interface" {
  type    = string
  default = "ens4"
}
#variable "memory" {
#  type    = string
#  default = "4048"
#}
variable "vcpu" {
  type    = number
  default = 4
}
locals {
  ips   = [for i in range(var.hosts) : "10.100.5.${format("%s", i + 50)}"]
  names = ["khalefam","pchau1", "emastroc", "vyashaev", "kthomp39", "noutsosc", "jcozzoli", "cpeter16", "balyanr"]
  macs  = [for i in range(var.hosts) : "ae:52:0a:b0:05:${format("%02x", i + 50)}"]
  memory = ["4048", "4048", "4048", "4048", "4048", "4048", "4048","4048", "4048"]	 

}
