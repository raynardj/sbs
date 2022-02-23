// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0;

contract SimpleStorage {
    // this will get initialized to 0!
    uint256 favoriteNumber;
    //types
    // bool favoriteBool = true;
    // string favoriteString = "String";
    // int256 favoriteInt = -5;
    // address favoriteAddress = 0x3Ca11126482b8899A1C70293b2fb78A9e06bB2Fe;
    // bytes32 favoriteBytes = "cat";

    struct People{
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string  => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public {
        // store value cost gas
        favoriteNumber = _favoriteNumber;
    }
    function retrieve() public view returns(uint256) {
        return favoriteNumber + favoriteNumber;
    }
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({favoriteNumber:_favoriteNumber, name:_name}));
        nameToFavoriteNumber[_name]=_favoriteNumber;
    }
}

// https://rinkeby.etherscan.io/tx/0xa93e1814c71b9475efa8f9c8c7d6ac658169315eb1d358501c3bacdc486b2b04