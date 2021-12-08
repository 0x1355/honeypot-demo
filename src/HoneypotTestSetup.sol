// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.6;

import "./HoneypotTest.sol";

contract HoneypotTestSetup is HoneypotTest {

    function test_keccak256Hashing() public {
	assertEq(keccak256(abi.encodePacked(_testPhrase)), _testSecret);
    }
    
    function test_honeypotBalance() public {
	assertEq(address(honeypot).balance, 1 ether);
    }

    function test_initializeWithSecret() public {
	assertEq(honeypot.secret(), _testSecret);
    }

    function test_hasReward() public {
	assertEq(honeypot.reward(), _reward);
    }

}
