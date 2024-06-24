pragma solidity ^0.8.0;

import "./IGalacticOracle.sol";

contract GalacticOracle {
    address private owner;
    mapping (address => uint) public nodeData;

    constructor() public {
        owner = msg.sender;
    }

    function updateNodeData(address node, uint data) public {
        nodeData[node] = data;
    }

    function getNodeData(address node) public view returns (uint) {
        return nodeData[node];
    }
}
