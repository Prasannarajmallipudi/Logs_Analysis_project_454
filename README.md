# Logs_Analysis_project_454
## Project description

In this project by using a Python program and the psycopg2 module to connect to the database and answer the given questions:

1.What are the most popular three articles of all time?

2.Who are the most popular article authors of all time?

3.On which days did more than 1% of requests lead to errors?

## Procedure:

* First we install vagrant by using command "sudo apt-get install vagrant".

* we install virtualbox by using command "sudo apt-get install virtualbox".

* Create new folder and open a terminal.

* vagrant init hashicrop/precise64.

* vagrant up.

* vagrant ssh.

* sudo apt-get install postgresql.

* sudo apt-get install python-psycopg2.

* Create a role(vagrant).

* create a database(news).

* Download the data from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip .

* Unzip the data to folder location.

* From terminal go to directory cd /vagrant.

* psql -d news -f newsdata.sql .

* Run your python file by python filename.py .

## output
What are the most popular three articles of all time?

    "Candidate is jerk, alleges rival" __ 338647 views
    "Bears love berries, alleges bear" __ 253801 views
    "Bad things gone, say good people" __ 170098 views

  Who are the most popular article authors of all time?

    Ursula La Multa __ 507594 views
    Rudolf von Treppenwitz __ 423457 views
    Anonymous Contributor __ 170098 views
    Markoff Chaney __ 84557 views

  On which days did more than 1% of requests lead to errors?

	July 17, 2016__ 2.3%  errors

