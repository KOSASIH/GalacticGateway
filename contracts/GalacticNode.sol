pragma solidity ^0.8.0;

import "./IGalacticNode.sol";

contract GalacticNode {
    address private owner;
    string public nodeName;
    uint public nodeType; // 0: Gateway, 1: Router, 2: Bridge

    constructor(string memory _nodeName, uint _nodeType) public {
        owner = msg.sender;
        nodeName = _nodeName;
        nodeType = _nodeType;
    }

    function getNodeInfo() public view returns (string memory, uint) {
        return (nodeName, nodeType);
    }
}
