git checkout appleseed
appleseed gen hello-world ./hello.py
git add ./hello.py
git commit -m "Appleseed Changes"
git checkout master
git merge appleseed
