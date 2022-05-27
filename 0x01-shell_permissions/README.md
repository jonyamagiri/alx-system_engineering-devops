This README file contains a description of what each script in the shell-permissions project does

**0-iam_betty**  
Switches the current user to the user betty

**1-who_am_i**  
Prints the effective username of the current user

**2-groups**  
Prints all the groups the current user is part of

**3-new_owner**  
Changes the owner of the file hello to the user betty

**4-empty**  
Creates an empty file called hello

**5-execute**  
Adds execute permission to the owner of the file hello

**6-multiple_permissions**  
Adds execute permission to the owner and the group owner, and read permission to other users, to the file hello

**7-everybody**  
Adds execution permission to the owner, the group owner and the other users, to the file hello

**8-James_Bond**  
Sets permission to the file hello as follows: owner-no permission at all, group-no permission at all, others-all the permissions

**9-John_Doe**  
Sets the mode of the file hello to: -rwxr-x-wx

**10-mirror_permissions**   
Sets the mode of the file hello the same as olleh's mode

**11-directories_permissions**  
Adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files will not be changed

**12-directory_permissions**  
Creates a directory called my_dir with permissions 751 in the working directory

**13-change_group**  
Changes the group owner to school for the file hello

**100-change_owner_and_group**  
Changes the owner to vincent and the group owner to staff for all the files and directories in the working directory

**101-symbolic_link_permissions**  
Changes the owner and the group of _hello to vincent and staff respectively

