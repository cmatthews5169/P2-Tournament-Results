# P2-Tournament-Results
Project 2: Tournament Results (Python/PostgreSQL)

Requirements 

  To utilize the functions built within tournament.py you will need a server running the following:
  -Python (Tested on version 2.7.6)
  -PostgreSQL (Tested on version 9.3.1)
  
Setup

  First you will have to create the "tournament" database. To do this you can SSH into your server using BASH and use the psql command to   get a prompt for the database server. Use the import command \i tournament.sql. This will execute the SQL commands contained within the   the file to setup the tournament database as well as the required tables, columns, and views. 
  
Running Test Cases

  Included in the tournament_file.py are a set of cases to verify that the program tournament.py is functioning correctly. To run these    test cases you can SSH into your server using BASH and issue the following command: "python tournament_test.py". If everything is        running normally you should see the outcome of the 10 test cases followed by "Success!  All tests pass!". 
