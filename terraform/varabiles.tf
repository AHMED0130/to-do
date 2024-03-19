variable "security-group-name" {
  default = "todo-security-group"
  
}

variable "instance-type" {
  default = "t3.micro"
}

variable "key-name" {
  default = "todo-server-key"
}

variable "env_prefix" {
  default = "dev"
  
}