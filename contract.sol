// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReadinessVerification {

    bytes32 public storedHash;

    function storeHash(bytes32 _hash) public {
        storedHash = _hash;
    }

    function verifyHash(bytes32 _hash)
        public
        view
        returns (bool)
        {
        return storedHash == _hash;
    }
}