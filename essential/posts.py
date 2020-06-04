import requests

my_data = {"name": "My Name", "email": "myemail@gmail.com"}
r = requests.post("https://tryphp.w3schools.com/demo/welcome.php", data=my_data)

f = open("./myfile.html", "w+")
f.write(r.text)