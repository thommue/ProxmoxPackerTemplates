# Proxmox Template Wizard with Packer 🚀

Transform your Proxmox cluster with my sleek Python script! Craft Packer templates across all nodes with ease and 
direct the magic with a simple config file. Quick, efficient, and totally cool - your Proxmox setup just got an 
awesome upgrade!

## The available Versions:

- Ubuntu Server 20.04 -- blank, fresh image
- Ubuntu Server 20.04 -- with: docker and docker-compose
- Ubuntu Server 20.04 -- with: keepalive and haproxy and the corresponding config file
- Ubuntu Server 22.04 -- blank, fresh image
- Ubuntu Server 22.04 -- with: docker and docker-compose
- Ubuntu Server 22.04 -- with: docker and docker-compose ready for terraform
- Ubuntu Server 22.04 -- with: containerd, kubelet, kubeadm, kubectl -- perfect template to start with kubectl (v1.29)

If you wanna include other ones, feel free to clone or fork.
Have fun with the templates

## Build
Each version can be used identically, but there are some requirements for this build:

- the iso image on your local machine (on a cluster on each node), in your local storage.
- packer need to be installed on your machine where you want to run the script
- also the packer proxmox plugin is needed
- a proxmox api-token
- install the requirements.txt in your virtual env

In the example config file, you have all needed infos, what you have to fill out (like cores, ram, etc...). The 
``template_folder`` part, is the part, where you can decide which version you want, like ubuntu-server-20-04. So if you 
have chosen this folder then the folder name simply would be ``ubuntu-server-20-04``, then you will get a blank template
from ubuntu 20-04, where you then afterwords can clone from.


```json
{
  "template_folder": "folder_of_this_repo_for_the_template_like_ubuntu-server-20-04",
  "proxmox_api_url": "<url_of_your_proxmox_node>",
  "proxmox_api_token_id": "<api_id>",
  "proxmox_api_token_secret": "<api_secret>",
  "template_name": "<name_which_the_template_has>",
  "template_description": "<description_of_your_template>",
  "iso_file": "local:iso/<name_of_the_ubuntu_iso_file>",
  "iso_storage_pool": "local",
  "disk_size": "<disk_size>",
  "storage_pool": "<storage_pool>",
  "storage_pool_type": "<storage_type>",
  "cores": "4",
  "memory": "4092",
  "network_bridge": "vmbr0",
  "packer_bind_address": "<ip_address_of_your_machine_with_the_script>",
  "ssh_username": "<your_username_what_you_want_to_have>",
  "path_to_ssh_key_file": "</path/to/your/ssh_key>",
  "ssh_public_key": "<public_ssh_key>",
  "proxmox_nodes": [
    {
      "name": "<name_of_node>",
      "vm_id": 900
    }
  ],
  "tags": "template;ubuntu-server-....",
  "keyboard_layout": "de",
  "timezone": "<needed_timezone>"
}
```

The proxmox_nodes can be a list of multiple ones like:

```json
{
    "proxmox_nodes": [
      {
      "name": "<name_of_node>",
      "vm_id": 900
      }, 
      {
      "name": "<name_of_node>",
      "vm_id": 901
    }
  ]
}

```

So if you have filled out the ``config.json`` and placed it in the folder, where the ``deployment.py`` file in the folder is located,
you are good to go. Just run the skript ``deployment.py`` and the templates
will be added to your proxmox node. You watch the progress direct in proxmox, there the VM should pop up and then under
the console you can watch the progress.

Depending you proxmox node and on how much core and ram you have given, this could take some time, especially for a
big cluster.
