# Test results
## Rinkeby Test

```shell
brownie test -s --network rinkeby
```

Meanwhile it downloads the compiler like following, 0.4.26 is for ```LinkToken.sol```, 0.6.0 is for ```MockOracle.sol``` and ```Lottery.sol```.
```
Downloading from https://solc-bin.ethereum.org/macosx-amd64/solc-macosx-amd64-v0.4.26+commit.4563c3fc
Downloading from https://solc-bin.ethereum.org/macosx-amd64/solc-macosx-amd64-v0.6.6+commit.6c089d02
```

And it takes really long time 
```
Brownie v1.18.1 - Python development framework for Ethereum

============================================================================== test session starts ===============================================================================
platform darwin -- Python 3.7.4, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Users/salvor/.local/pipx/venvs/eth-brownie/bin/python
cachedir: .pytest_cache
hypothesis profile 'brownie-verbose' -> verbosity=2, deadline=None, max_examples=50, stateful_step_count=10, report_multiple_bugs=False, database=DirectoryBasedExampleDatabase(PosixPath('/Users/salvor/.brownie/hypothesis'))
rootdir: /Users/salvor/github/sbs/lesson7/lottery
plugins: eth-brownie-1.18.1, forked-1.4.0, web3-5.27.0, xdist-1.34.0, hypothesis-6.27.3
collected 6 items                                                                                                                                                                

tests/test_lottery_intergration.py::test_can_pick_winner RUNNING
Waiting for https://api-rinkeby.etherscan.io/api to process contract...
Verification submitted successfully. Waiting for result...
Verification complete. Result: Already Verified
Deployed lottery!
contract lottery:0x57B3F779700645AdD526B3D301456274620D6b46
current account: 0x3Ca11126482b8899A1C70293b2fb78A9e06bB2Fe
Fund contract!
tests/test_lottery_intergration.py::test_can_pick_winner PASSED
tests/test_lottery_unit.py::test_get_entrance_fee SKIPPED
tests/test_lottery_unit.py::test_cant_enter_unless_started SKIPPED
tests/test_lottery_unit.py::test_can_start_and_enter_lottery SKIPPED
tests/test_lottery_unit.py::test_can_end_lottery SKIPPED
tests/test_lottery_unit.py::test_can_pick_winner_correctly SKIPPED

==================================================================== 1 passed, 5 skipped in 817.47s (0:13:37) ====================================================================

```

## Development Test
```shell
brownie test -s
```

```
Launching 'ganache-cli --accounts 10 --hardfork istanbul --gasLimit 12000000 --mnemonic brownie --port 8545'...

tests/test_lottery_intergration.py::test_can_pick_winner SKIPPED
tests/test_lottery_unit.py::test_get_entrance_fee RUNNING
Deployed!
Deployed lottery!
expected_entrance_fee:25000000000000000 25000000000000000
tests/test_lottery_unit.py::test_get_entrance_fee PASSED
tests/test_lottery_unit.py::test_cant_enter_unless_started RUNNING
Deployed lottery!
Transaction sent: 0xfbdf0afb737f0254a2560fa10758f37439372de0a30d64dd0e041063f0f2faea
tests/test_lottery_unit.py::test_cant_enter_unless_started PASSED
tests/test_lottery_unit.py::test_can_start_and_enter_lottery RUNNING
Deployed lottery!
tests/test_lottery_unit.py::test_can_start_and_enter_lottery PASSED
tests/test_lottery_unit.py::test_can_end_lottery RUNNING
Deployed lottery!
Fund contract!
tests/test_lottery_unit.py::test_can_end_lottery PASSED
tests/test_lottery_unit.py::test_can_pick_winner_correctly RUNNING
Deployed lottery!
Fund contract!
tests/test_lottery_unit.py::test_can_pick_winner_correctly PASSED

5 passed, 1 skipped in 6.51s
```