# Week 1
* What's Javascript VM used for?
* Distinguish between such following scopes of variable
    * external, public, internal, private
* Why store data cost gas fee? -it'a transaction
* What's the block of variable means, defind by which pair of puctuation?
* What 2 keywords can define the function, in a way it won't cause a transaction
    * view, pure
    * public variables are view functions
* What's the syntax of define a new oop class/ type?
```sol
struct Person {
    string name;
    uint age;
}
```
* Waht's analogy of array and mapping in python?
* How to define array and mapping in solidity?
```sol
People[] public people;
people.push(new Person(...));
```

```sol
mapping(address => uint) public balances;
balances[msg.sender] = 100;
```

