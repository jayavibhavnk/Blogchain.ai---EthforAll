// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
//importing openzeppelin contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// OpenSea proxy registry contract
contract OwnableDelegateProxy {

}

contract ProxyRegistry {
    mapping(address => OwnableDelegateProxy) public proxies;
}

// MyNFT contract based on ERC721 contract
contract MyNFT is ERC721, Ownable {
    string public ipfsLink;
    address proxyRegistryAddress;

    constructor(
        string memory _name,
        string memory _symbol,
        string memory _ipfsLink,
        address _proxyRegistryAddress
    ) ERC721(_name, _symbol) {
        ipfsLink = _ipfsLink;
        proxyRegistryAddress = _proxyRegistryAddress;
    }

    function setIPFSLink(string memory _ipfsLink) public onlyOwner {
        ipfsLink = _ipfsLink;
    }

    function isApprovedForAll(
        address owner,
        address operator
    ) public view override returns (bool) {
        // Whitelist OpenSea proxy for easy trading
        ProxyRegistry proxyRegistry = ProxyRegistry(proxyRegistryAddress);
        if (address(proxyRegistry.proxies(owner)) == operator) {
            return true;
        }

        return super.isApprovedForAll(owner, operator);
    }
}
