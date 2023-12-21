import os
import subprocess
from utils.create_obj import Config
from utils.templating import render_packer_file, render_user_data
from utils.file_handling import create_temp_folder, handle_node_file_structure, remove_temp_folder


# get the config obj
config_class = Config(path_to_config_json='config.json')
config = config_class.get_config_obj()

# deployment skript
root_folder_for_packer = os.path.join(os.getcwd(), config.template_folder)

# change dir to root folder for packer
os.chdir(root_folder_for_packer)

# generate a temporary file structure for packer
folder_path = create_temp_folder()

# now loop over each node and create the template
for node in config.proxmox_nodes:
    tmp_path = handle_node_file_structure(folder_path=folder_path, node=node)

    # generate the templates
    render_packer_file(root_path=root_folder_for_packer, tmp_path=tmp_path, config_obj=config, node=node)
    render_user_data(root_path=root_folder_for_packer, tmp_path=tmp_path, config_obj=config)

    # now cd to node dir
    os.chdir(tmp_path)

    # packer command
    command = ["packer", "build", fr".\{node.node_name}.pkr.hcl"]
    process = subprocess.Popen(command, shell=True)
    process.wait()
    print(process)

    # change back to root
    os.chdir(root_folder_for_packer)

remove_temp_folder(folder_path=folder_path)