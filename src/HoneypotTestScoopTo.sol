// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.6;

import "./HoneypotTest.sol";


contract HoneypotTestScoopTo is HoneypotTest {
    function test_scoopToHoneypotBalances() public {
	honeypotPreBalance = address(honeypot).balance;
	honeypot.scoopTo(address(this), _testPhrase);
	honeypotPostBalance = address(honeypot).balance;
	assertEq(honeypotPreBalance - _reward, honeypotPostBalance);
    }

    function test_scoopToWalletBalances() public {
	preBalance = address(this).balance;
	(bool success, ) = address(honeypot).call(abi.encodeWithSignature("scoopTo(address,string)", address(this), _testPhrase));
	require(success);
	postBalance = address(this).balance;
	assertEq(preBalance + _reward, postBalance);
    }

    function testFail_scoopToWithWrongPhraseReverts() public {
	honeypot.scoopTo(address(this), _wrongPhrase);
    }

    function testFail_scoopToTwiceInSameBlock() public {
	honeypot.scoopTo(address(this), _testPhrase);
	honeypot.scoopTo(address(this), _testPhrase);
    }

    function test_scoopToAgainNextBlock() public {
	honeypot.scoopTo(address(this), _testPhrase);
	hevm.roll(block.number + 1);
	honeypot.scoopTo(address(this), _testPhrase);
    }
}
