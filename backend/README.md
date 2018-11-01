# Backend

## Queries

### All Categories
```
query{
  allCategories {
    id
    name
    description
  }
}
```
### All Challenges
```
query {
  allChallenges {
    id
    name
    description
    points
    flag
    show
  }
}
```

## Mutations

### Add Categories
```
mutation{
  addcategory(name:"newname",description:"newdescription") {
    message
  }
}
```
### Add Challenge
```
mutation{
  addChallenge(name:"Crypto 100", description:"Solve this!", points:100, flag:"this-is-a-flag", show:true) {
    message
  }
}
```