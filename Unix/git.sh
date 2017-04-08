git config --global user.name "Firstname Lastname"
git config --global user.email "emailaddress@gmail.com"
git config --global color.ui "auto"

#to clone a repo
git clone https://github.com/USERNAME/REPOSITORY.git

#to sync
git pull

#create git repo
git init

echo "Introduction" > README.md
git add README.md

git commit -m "Initial Commit: README added"

git add . # to upload everything

git commit -m "New Commit"

git push # to push from local to github

git status # to check repo status

# to sync a forked repo from the original repo

# first, add remote from original repository in your forked repository as upstream:
git remote add upstream https://github.com/REPO-YOU-FORKED-FROM.git
git fetch upstream
# then update the forked repo from the upstream
git pull upstream master
