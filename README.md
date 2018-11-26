# YACF
Yet Another CTF Framework


# Start up
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
 - Backend code system

 ## Security

 - [backend] Stop teams from submitting the same flag twice
 - [backend] Restrict endpoint from leaking flag
