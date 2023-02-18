// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
//importing openzeppelin contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    //constructor of ERC721
    constructor() ERC721("MyNFT", "NFT") {}

    // mintNFT function for minting NFT
    function mintNFT(
        address recepient,
        string memory tokenURI
    ) public onlyOwner returns (uint256) {
        _tokenIds.increment(); // incrementing using increment function in counter
        uint256 newItemId = _tokenIds.current();
        _mint(recepient, newItemId);
        _setTokenURI(newItemId, tokenURI);
        return newItemId; // returning newItemId after minting
    }
}
