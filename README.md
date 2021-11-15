# Adjust assignment

## Docker setup
### Clone your repo
    git clone https://github.com/Rashiddev/adjust_assignment.git

### Make sure docker is installed on your system and run following commands inside your project directory:

    docker-compose build
    docker-compose up

### Interact with the API on this URL:
    http://127.0.0.1:8000/api/schema/swagger/

### Given test scenarios:
   1. [http://127.0.0.1:8001/api/app_performances/?date_to=2017-05-31&group_by=channel,country&fields=channel,country,impressions,clicks&ordering=-clicks](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
   2. [http://127.0.0.1:8001/api/app_performances/?date_from=2017-05-01&date_to=2017-05-31&os=ios&group_by=date&ordering=-date&fields=date,installs](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
   3. [http://127.0.0.1:8001/api/app_performances/?date=2017-06-01&country=US&group_by=os&ordering=-revenue&fields=os,revenue](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
   4. [http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi]([http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi))


### Login to admin panel to import/export excel data:
    url: http://127.0.0.1:8001/admin/
    username: admin
    password: admin@123$

## Development Steps

1. Install <b>git</b> on the system.
2. Open shell/command prompt and run following command to clone the project:
    <br>`git clone https://github.com/Rashiddev/adjust_assignment.git`


3. Make sure <b>python3</b> and <b>pip3</b> are installed on the system.
4. Once inside the project's root directory, install requirements using the following command:
    <br>Note: It's recommended to create a virtual environment and install requirements there.
    <br>`pip install -r ./requirements/local.txt`

5. Run this command inside the project directory to start the server:
    <br>`python3 manage.py runserver 8000`

6. Following URL will open swagger UI from where all the project APIs can be accessed:
    http://127.0.0.1:8000/api/schema/swagger/

7. Here are the URLs for 4 mentioned scenarios:
   1. [http://127.0.0.1:8001/api/app_performances/?date_to=2017-05-31&group_by=channel,country&fields=channel,country,impressions,clicks&ordering=-clicks](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
   2. [http://127.0.0.1:8001/api/app_performances/?date_from=2017-05-01&date_to=2017-05-31&os=ios&group_by=date&ordering=-date&fields=date,installs](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
   3. [http://127.0.0.1:8001/api/app_performances/?date=2017-06-01&country=US&group_by=os&ordering=-revenue&fields=os,revenue](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
   4. [http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi]([http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi))

### Data import from excel
User can import the Excel data into the system from admin panel. Kindly login to admin using below url:
    
    url: http://127.0.0.1:8001/admin/
    username: admin
    password: admin@123$

Once logged in, go to **App Performance** and use import/export actions to import or export data.

## Tests
Following command can be used to run test cases:


    python manage.py test


