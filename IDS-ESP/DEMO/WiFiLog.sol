// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract WiFiLog {
event LogCreated(string hash, uint256 timestamp, string zone);
function createLog(string memory _hash, string memory _zone) public {
    emit LogCreated(_hash, block.timestamp, _zone);
}

}
