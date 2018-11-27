# YACF
Yet Another CTF Framework

# Deployment
Currently, the only supported method of deploying YACF is through Docker. Docker Compose is recommended to streamline the process.

To do deploy the environment, first ensure that you have docker and docker compose installed on the server/computer. Next, create a file called docker-compose.yml and copy in the following code. 

```
version: '3'

services:
  redis:
    restart: always
    image: redis:5.0.1
    hostname: redis-broker
    ports:
      - "6379:6379"
  
  yacf:
    restart: always
    image: 0xcodes/yacf:0.1-beta
    hostname: yacf.0x.codes
    ports:
      - "80:80"
    links:
      - redis
```
Save this file. Now execute, in the same directory, the following command. 

```
cmd>$: docker-compose up
```

Now go to your web browser and navigate to the IP address of where it is deployed. The application will be listening on port 80. 

Note: The default admin credentials are admin/yacfadmin


# Developers
```
<!-- docker run --name yacf-redis -p 6379:6379 -d redis -->
docker-compose build

```

## Build Vue
```
yarn build

rm -rf ../backend/static/*
cp -r dist/* ../backend/static/

```
- [Bug] Get webpack to append static to css. Current workaround, change it in dist/index manually.

## Things to Fix
- Challenges in the save category cannot have the same point values.
- On challenge solve place unique constraint on backend model to ensure team cannot resubmit flags.
- Build query/mutation to build a team challenge board
 


 ## Things to Add
 - Auto shut off time to hide scoreboard
 - After event has ended, have the option for users to submit writeups
 - Limit number of users that can be on a team
 - Upload for team profile picture
 - Backend code/message system
 - Change submit flag to return one time solve message (Need to create model for this)
 - Make challenge hits. 
 - Make post challenge survey for either user or whole team.


 ## Security

 - [backend] Stop teams from submitting the same flag twice
 - [backend] Restrict endpoint from leaking flag
 - [backend] Check event end time before submitting flag.
