pragma solidity ^0.8.0;

import "./IGalacticGateway.sol";

contract GalacticGateway {
    address private owner;
    mapping (address => bool) public authorizedNodes;

    constructor() public {
        owner = msg.sender;
    }

    function addNode(address node) public onlyOwner {
        authorizedNodes[node] = true;
    }

    function removeNode(address node) public onlyOwner {
        authorizedNodes[node] = false;
    }

    function getNodeStatus(address node) public view returns (bool) {
        return authorizedNodes[node];
    }
}
