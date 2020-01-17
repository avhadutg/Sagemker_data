import os
import subprocess
import sys

val=subprocess.call(["aws", "--version"])
print(val)
if val!=0:
	#os.system('sudo apt install curl unzip')
	os.system('wget "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"')
	os.system('unzip awscli-bundle.zip')
	os.system('sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws')
else:
	os.system("aws configure  ")
	#access_id='AKIAR3LFOVO4FWHBAKEN'
	#=access_id
	#secret_access_id='JP7z9uCju//Chbmfe8KOgaEXsayGONlKjEwQkLAe'
	#=secret_access_id
	#='us-east-1'
#	input()=region
	#output_format='json'
#	input()=output_format
#
	name_of_instance=input('Enter the name of instance: ')
	git_confirmation=input('Do you want to add Git Repository: Y/N ')
	if git_confirmation=='Y':
		name_of_git_repository=input('Enter the name of the git repository: ')
		output='aws sagemaker create-notebook-instance --notebook-instance-name '+name_of_instance +' --instance-type ml.t2.medium --role-arn arn:aws:iam::127451179960:role/MLfullperm --default-code-repository '+name_of_git_repository

	else:
		output='aws sagemaker create-notebook-instance --notebook-instance-name '+name_of_instance +' --instance-type ml.t2.medium --role-arn arn:aws:iam::127451179960:role/MLfullperm'


	os.system(output)

	print('Notebook instance Created')
