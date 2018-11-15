# YACF
Yet Another CTF Framework


# Start up
```
docker run --name yacf-redis -p 6379:6379 -d redis

```

---
## Things to Fix
- Challenges in the save category cannot have the same point values.
- On challenge solve place unique constraint on backend model to ensure team cannot resubmit flags.
- Build query/mutation to build a team challenge board
 
