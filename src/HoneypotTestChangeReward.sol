// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.6;

import "./HoneypotTest.sol";


contract HoneypotTestChangeReward is HoneypotTest {

    function test_changeReward(uint32 _newReward) public {
	honeypot.changeReward(_newReward);
	assertEq(honeypot.reward(), _newReward);
    }

    function testFail_changeRewardAsNonOwner(uint32 _newReward) public {
	hevm.store(address(honeypot), bytes32(uint(2)), bytes32(bytes20(HEVM_ADDRESS)));
	honeypot.changeReward(_newReward);
    }

    function proveFail_changeRewardBalances(uint32 _newReward) public {
	preBalance = address(this).balance;
	honeypot.changeReward(_newReward);
	honeypot.scoop(_testPhrase);
	postBalance = address(this).balance;
	assertEq(preBalance + _newReward, postBalance);
    }

    // This fails with symbolic execution with 0 as counterexample. But actually 0 works.
    // Need to read about it later to understand why.
    function test_changeRewardHoneypotBalances(uint32 _newReward) public {
	honeypotPreBalance = address(honeypot).balance;
	honeypot.changeReward(_newReward);
	honeypot.scoopTo(address(this), _testPhrase);
	honeypotPostBalance = address(honeypot).balance;
	assertEq(honeypotPreBalance - _newReward, honeypotPostBalance);
    }
}
