pragma solidity ^0.8.0;

import "./IGalacticToken.sol";

contract GalacticToken {
    string public name = "Galactic Token";
    string public symbol = "GAL";
    uint public totalSupply = 100000000;

    mapping (address => uint) public balances;

    constructor() public {
        balances[msg.sender] = totalSupply;
    }

    function transfer(address recipient, uint amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
    }

    function balanceOf(address owner) public view returns (uint) {
        return balances[owner];
    }
}
