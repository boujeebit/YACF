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

### Login
```
mutation{
  login(username:"mickey", password:"password1"){
    id
  }
}
```


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

### Add Team
```
mutation {
  addteam(name:"WEEEEEEE!", accesscode:"code1234"){
		message
  }
}
```

### Submit Flag
```
mutation {
  submitflag(challenge:4, flag:"a9a7ea821ceae25be636986af888ab0e"){
    message
  }
}
```