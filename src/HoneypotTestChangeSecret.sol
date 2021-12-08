// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.6;

import "./HoneypotTest.sol";


contract HoneypotTestChangeSecert is HoneypotTest {

    string _newPhrase = "When the fear has gone there will be nothing. Only I will remain.";
    bytes32 _newSecret = 0x746426c2d03bcf9457239d9ec15ac8f0a8a63335134e4678c3c6cedbf0f348d9;
     
    function test_newSecretHashing() public {
	assertEq(keccak256(abi.encodePacked(_newPhrase)), _newSecret);
    }

    function test_changeScretAsOwner() public {
	honeypot.changeSecret(_newSecret);
	assertEq(honeypot.secret(), _newSecret);
    }

    function testFail_changeSecretAsNonOwner() public {
	// This cheatcode assumes owner to be the 3rd state variable of Honeypot
	hevm.store(address(honeypot), bytes32(uint256(2)), bytes32(bytes20(HEVM_ADDRESS)));
	honeypot.changeSecret(_newSecret);
	assertEq(honeypot.secret(), _newSecret);
    }

}
