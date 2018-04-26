# Logon to EC2 

ssh -i  ~/.ssh/aws-key  ec2-user@[private ip address without bracket]
#ssh -i /path/my-key-pair.pem ec2-user@public_dns_name

# Move data to EC2

scp -i [private SSH key path(no brackets)] [data file path] ec2-user@[instance private IP]:[new location]

#e.g. (first create the directory ~/data/ on the EC2 instance)

scp -i ~/.ssh/aws-key ~/Documents/mytable.csv ec2-user@10.205.75.216:~/data/

# download data from EC2

scp -i ~/.ssh/aws-key ec2-user@10.205.75.216:~/data/mytable.csv ~/Documents/

# Move data from S3 to EBS

aws s3 cp s3://bucket_name/datafile.csv data/datafile.csv

# Open jupyter notebook

ssh -L 2018:localhost:2018 -i ~/.ssh/aws-key ec2-user@[private ip address without bracket]
jupyter notebook --port=2018

# then open browser and go to localhost:2018
# may need to paste what's after "token=" into the browser password
