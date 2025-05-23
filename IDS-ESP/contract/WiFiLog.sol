// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract IntrusionDemo {
    mapping(bytes32 => bool) public knownIntrusions;

    event IntrusionAdded(bytes32 indexed hash);
    event IntrusionDetected(bytes32 indexed hash);

    function addIntrusionHash(string memory signature) public {
        bytes32 hash = keccak256(abi.encodePacked(signature));
        knownIntrusions[hash] = true;
        emit IntrusionAdded(hash);
    }

    function checkForIntrusion(string memory incomingSignal) public returns (bool) {
        bytes32 hash = keccak256(abi.encodePacked(incomingSignal));
        if (knownIntrusions[hash]) {
            emit IntrusionDetected(hash);
            return true;
        }
        return false;
    }
}
