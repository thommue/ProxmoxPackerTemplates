import json
from typing import List
from pydantic import BaseModel


class ProxmoxNode(BaseModel):
    node_name: str
    vm_id: int


class PackerConfig(BaseModel):
    proxmox_api_url: str
    proxmox_api_token_id: str
    proxmox_api_token_secret: str
    template_name: str
    template_description: str
    iso_file: str
    iso_storage_pool: str
    disk_size: str
    storage_pool: str
    storage_pool_type: str
    cores: str
    memory: str
    network_bridge: str
    packer_bind_address: str
    ssh_username: str
    path_to_ssh_key_file: str
    ssh_public_key: str
    proxmox_nodes: List[ProxmoxNode]
    tags: str
    keyboard_layout: str
    timezone: str


class Config:
    def __init__(self, path_to_config_json: str):
        self.config = self._read_config(path_to_config_json=path_to_config_json)

    def get_config_obj(self) -> PackerConfig:
        proxmox_nodes = []
        for node in self.config['proxmox_nodes']:
            proxmox_nodes.append(
                ProxmoxNode(
                    node_name=node['name'],
                    vm_id=node["vm_id"]
                )
            )
        return PackerConfig(
            proxmox_api_url=self.config['proxmox_api_url'],
            proxmox_api_token_id=self.config['proxmox_api_token_id'],
            proxmox_api_token_secret=self.config['proxmox_api_token_secret'],
            template_name=self.config['template_name'],
            template_description=self.config['template_description'],
            iso_file=self.config['iso_file'],
            iso_storage_pool=self.config['iso_storage_pool'],
            disk_size=self.config['disk_size'],
            storage_pool=self.config['storage_pool'],
            storage_pool_type=self.config['storage_pool_type'],
            cores=self.config['cores'],
            memory=self.config['memory'],
            network_bridge=self.config['network_bridge'],
            packer_bind_address=self.config['packer_bind_address'],
            ssh_username=self.config['ssh_username'],
            path_to_ssh_key_file=self.config['path_to_ssh_key_file'],
            ssh_public_key=self.config["ssh_public_key"],
            proxmox_nodes=proxmox_nodes,
            tags=self.config["tags"],
            keyboard_layout=self.config["keyboard_layout"],
            timezone=self.config["timezone"]
        )

    @staticmethod
    def _read_config(path_to_config_json: str) -> dict:
        # read in the config file
        with open(path_to_config_json, "r") as config_file:
            return json.load(config_file)
