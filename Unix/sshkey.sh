# Checking for existing SSH keys

ls -al ~/.ssh

# the public key should be like "id_rsa.pub"

# To generate a new key

ssh-keygen -t rsa -b 4096 -C "username@emailaddress.com"

Enter a file in which to save the key (/Users/username/.ssh/id_rsa): /Users/username/.ssh/aws-key

# Adding SSH key to the ssh-agent

eval "$(ssh-agent -s)" # this is to make sure ssh-agent is running

ssh-add ~/.ssh/aws-key
