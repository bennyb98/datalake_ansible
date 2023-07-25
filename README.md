# datalake_ansible

To run: ansible-playbook -i inventory main.yml

![Screenshot (14)](https://github.com/bennyb98/datalake_ansible/assets/139473239/e78bc3c1-b27c-4843-99d9-8adc2e578e08)

Files description:
--> librDL.yml : checks and installs all the necessary libraries and apps 
--> Mongovars.yml : Parameter file to compile with your data regarding the MongoDB query
--> MongoUPDOWN.yml : File containing the upload of the csv/json given in Mongovars and the download of the query
--> inventory: A folder containing all files needed for the run of the playbook (hosts, etc)
--> adacloud.ca.chain + app-cred-AC_ig-openrc.sh + clouds.yaml : CLI interface Auth Certification
--> data.csv: data to upload on MongoDB as an example
--> parameters.yml: Parameter file to customize the VM we create with create_vm.yml
--> create_vm.yml: file creating a VM Openstack with CentOS as image where we developed the datalake
--> crud_plain.yml: FASTAPI 
