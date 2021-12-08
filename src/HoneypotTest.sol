// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.6;

import "ds-test/test.sol";
import "./Honeypot.sol";

abstract contract Hevm {
    function roll(uint x) public virtual;
    function store(address c, bytes32 loc, bytes32 val) public virtual;
}

contract HoneypotTest is DSTest {

    Honeypot honeypot;
    uint honeypotPreBalance;
    uint honeypotPostBalance;
    uint preBalance;
    uint postBalance;

    uint _reward = 0.002 ether;
    string _testPhrase = "Fear is the mind killer.";
    bytes32 _testSecret = 0x225f39d09c92129b734d0c9798ed377be3c1dd954b152700d6d5f0235bf15236;
    string _wrongPhrase = "A time to get and a time to lose.";

    Hevm hevm = Hevm(HEVM_ADDRESS);
    
    receive() external payable {}
    
    function setUp() public {
	honeypot = new Honeypot(_testSecret, _reward);
	payable(address(honeypot)).transfer(1 ether);
    }
}
