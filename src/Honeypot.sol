// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.6;

contract Honeypot {

    bytes32 public secret;
    uint lastScoopedBlock;
    address owner;
    uint public reward;

    constructor(bytes32 _secret, uint _reward) payable {
	secret = _secret;
	owner = msg.sender;
	reward = _reward;
    }

    modifier oncePerBlock() {
	require(lastScoopedBlock != block.number);
	lastScoopedBlock = block.number;
	_;
    }

    modifier isOwner() {
	require(owner == msg.sender);
	_;
    }
       
    function scoopTo(address _receiver, string calldata _phrase) public oncePerBlock {
	require(keccak256(abi.encodePacked(_phrase)) == secret);
	payable(_receiver).transfer(reward);
    }

    function scoop(string calldata _phrase) public oncePerBlock {
	require(keccak256(abi.encodePacked(_phrase)) == secret);
	payable(msg.sender).transfer(reward);   
    }

    function changeSecret(bytes32 _newSecret) public isOwner {	
	secret = _newSecret;
    }

    function changeReward(uint _newReward) public isOwner {
	reward = _newReward;
    }
    
    receive() external payable {
	
    }
}
