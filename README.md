# YACF

Yet Another CTF Framework!

YACF is still under development and should not be use in production yet. Good things to come!

# Deployment

Currently, the only supported method of deploying YACF is through Docker. Docker Compose is recommended to streamline the process.

To do deploy the environment, first ensure that you have docker and docker compose installed on the server/computer. Once verified, run the following commands

```
$: curl https://raw.githubusercontent.com/0xCODEs/YACF/master/scripts/docker-compose.yml -o docker-compose.yml
$: docker-compose up
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

- On challenge solve place unique constraint on backend model to ensure team cannot resubmit flags.

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
- [backend] Check event end time before submitting flag.
- [backend] Hide team access code
