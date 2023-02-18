// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;
// importing chainlink contracts
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@chainlink/contracts/src/v0.8/ConfirmedOwner.sol";
contract ATestnetConsumer is ChainlinkClient, ConfirmedOwner {
    using Chainlink for Chainlink.Request;
    
    uint256 private constant ORACLE_PAYMENT = (1 * LINK_DIVISIBILITY) / 10; 
    uint256 public NFT;

    event RequestEthereumNFTcreator(
        uint256 indexed blog_content,
        uint256 indexed image0
    );
    //constructor call
    constructor() ConfirmedOwner(msg.sender) {
        setChainlinkToken(0x25cEA86d3309AFA37bEd0412810c5a4d9Ffdb9D7);
    }
    // local host api 
    function requestEthereumPrice(
        address _oracle,
        string memory _jobId
    ) public onlyOwner {
        Chainlink.Request memory req = buildChainlinkRequest(
            stringToBytes32(_jobId),
            address(this),
            this.fulfillEthereumPrice.selector
        );
        req.add(
            "post",
            "http://localhost:8080/"
        );
        req.add("path", "blog_content");
        sendChainlinkRequestTo(_oracle, req, ORACLE_PAYMENT);
    }
    // request fullfilment
    function fulfillEthereumPrice(
        uint256 _blog_content,
        uint256 _image0,
    ) public recordChainlinkFulfillment(_blog_content) {
        emit RequestEthereumNFTcreator(_blog_content, _image0);
        NFT = _image0;
    }

    function getChainlinkToken() public view returns (address) {
        return chainlinkTokenAddress();
    }

    function withdrawLink() public onlyOwner {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(
            link.transfer(msg.sender, link.balanceOf(address(this))),
            "Unable to transfer"
        );
    }
    
    function cancelRequest(
        bytes32 _requestId,
        uint256 _payment,
        bytes4 _callbackFunctionId,
        uint256 _expiration
    ) public onlyOwner {
        cancelChainlinkRequest(
            _requestId,
            _payment,
            _callbackFunctionId,
            _expiration
        );
    }

    function stringToBytes32(
        string memory source
    ) private pure returns (bytes32 result) {
        bytes memory tempEmptyStringTest = bytes(source);
        if (tempEmptyStringTest.length == 0) {
            return 0x0;
        }

        assembly {
            // solhint-disable-line no-inline-assembly
            result := mload(add(source, 32))
        }
    }
}






