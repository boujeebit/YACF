# YACF
Yet Another CTF Framework


# Start up
```
docker run --name yacf-redis -p 6379:6379 -d redis

```


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
