// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.6;

import "./HoneypotTest.sol";

contract HoneypotTestScoop is HoneypotTest {

    function test_scoopHoneypotBalance() public {
	honeypotPreBalance = address(honeypot).balance;
	honeypot.scoop(_testPhrase);
	honeypotPostBalance = address(honeypot).balance;
	assertEq(honeypotPreBalance - _reward, honeypotPostBalance);
    }

    function test_scoopTesterBalances() public {
	preBalance = address(this).balance;
	(bool success, ) = address(honeypot).call(abi.encodeWithSignature("scoop(string)", _testPhrase));
	require(success);
	postBalance = address(this).balance;
	assertEq(preBalance + _reward, postBalance);
    }

    function testFail_scoopWithWrongPhrase() public {
	honeypot.scoop(_wrongPhrase);
    }

    function testFail_scoopTwiceInSameBlock() public {
	honeypot.scoop(_testPhrase);
	honeypot.scoop(_testPhrase);
    }

    function test_scoopAgainNextBlock() public {
	honeypot.scoop(_testPhrase);
	hevm.roll(block.number + 1);
	honeypot.scoop(_testPhrase);
    }
}
