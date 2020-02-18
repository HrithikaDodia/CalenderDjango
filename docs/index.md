Steps to run the Django Calender Project:
•	First of all to run the project you have to clone the project to get the project folder into your machine. For that run –                                                                                            git clone https://github.com/HrithikaDodia/CalenderDjango.git 
By running this command the project folder will be cloned into your current folder.

•	Create a virtual environment –
virtualenv env --no-site-packages

•	Start the virtual environment –
env\Scripts\activate

•	Install Project dependencies –
1.	cd into project folder
2.	pip install -r requirements.txt

•	For migrations run – 
1.	python manage.py makemigrations
2.	python manage.py migrate

•	Creating superuser – 
python manage.py createsuperuser

•	Start server –
python manage.py runserver

APIs(You need to be logged in for accessing them):

•	User Authentication APIs:
1.	create/:  Creating new users
2.	list/: List of users
3.	login/: Login
4.	logout/: Logout
5.	rest-auth/password/change/password: For changing password
6.	rest-auth/password/reset/password: For changing password

•	Calender APIs:
1.	calender/create: Creating new event in calender
2.	calender/update/id: Updating calender event
3.	calender/delete/id: Deleting calender event
4.	calender/list: List of events

•	Other views in the project(these are not api views just normal Django views although these functionalities are provided by the above mentioned api views):
1.	register/: Creating new user

•	api-doc/: Documentation of all apis of this project.


----------------------------------------  THANK YOU -------------------------------------------

