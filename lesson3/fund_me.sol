// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    mapping(address => uint256) public addressToAmountFunded;
    address eth2usd = 0x8A753747A1Fa494EC906cE90E9f37563A8AF630e;
    function fund() public payable {
        addressToAmountFunded[msg.sender] += msg.value;
        // what the ETH->USD conversion rate
    }

    function getVersion() public view returns(uint256){
        // found the rinkby address here
        // https://docs.chain.link/docs/ethereum-addresses/#Rinkeby%20Testnet
        AggregatorV3Interface priceFeed = AggregatorV3Interface(eth2usd);
        return priceFeed.version(); // version 4 at the time of exercise
    }

    function getPrice() public view returns(uint256){
        // unpacking data with function return assigned to tuple
        AggregatorV3Interface priceFeed = AggregatorV3Interface(eth2usd);
        (,int256 answer// this is price
          ,,,) = priceFeed.latestRoundData();
        return uint(answer * 10000000000);
    }

    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethAmount * ethPrice) / 1000000000000000000;
        return ethAmountInUsd;
    }
}

// deployed here
// get_version https://rinkeby.etherscan.io/tx/0xc340a9fc6017371ddac84068903dd8ab92b773a8ca2a0d136a8f78a89037a5f3
// get_price https://rinkeby.etherscan.io/tx/0x647237a7e6a301963ed9056b2c4f20ca5fae477737c36a6280e49cb266fb12df
// get_conversion_rate https://rinkeby.etherscan.io/tx/0x63d3bda84cae16b33e1fa3a29b8c8ea0ba5958dd1625101ac988fc9ff93ca04e