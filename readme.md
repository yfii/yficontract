## 不需要修改 直接部署的合约有


- claimAddress
- yfiaddress


## yCurveFiRewardsAddress
init 
1. setRewardDistribution  给自己
  https://etherscan.io/tx/0x650f186f55235a02a3f04ef08d6ffa6576e2be2351f9899bbc6f948403d94a2c

2. notifyRewardAmount   10000000000000000000000
https://etherscan.io/tx/0xf607f66529da21a1efe4dde7e0d7fb6fdca75b18a605b9d8a7d0a6ad2b9b3b8f


## balancerRewardsAddress
init 
1. setRewardDistribution  给自己
  https://etherscan.io/tx/0x8a9be905ce0b5660d373352e8e4a94d3718c8fa80e8fa27b074ee835222d3445

2. notifyRewardAmount   10000000000000000000000
https://etherscan.io/tx/0xc8942052871f23c9caba18a86ce97aa94b0e7dd0a87202d095d33b69d8d819f2

## yfiaddress

有新的分红合约开始的话，

1. addMinter （yCurveFiRewardsAddress,balancerRewardsAddress)

https://etherscan.io/tx/0x14ddc6dc8a577d7b638be435804f33076c2e6f59492d25c50f2826802320e05f

2. mint (给上面的打币)

数量是 10000000000000000000000个

https://etherscan.io/tx/0x998ba2dfae41a189df1f3d05df7f3a1a1ba5e368e4c172bedbf28f1dd4bd6b72

## claimAddress

直接部署就行

## governanceAddress

init 

1. initialize https://etherscan.io/tx/0x9a5fd6c13088b039ef2d58d86a56d4bcf9a229e968aad9cca3e481eb435d8a56

2. setRewardDistribution 自己
https://etherscan.io/tx/0xe2b5ef06f80f3ba09992192bbcd2780d43c16da26f2e16b554d25565caa46423


## feeRewardsAddress

1. initialize  https://etherscan.io/tx/0xb0a8660d76e47e0f12ff2a5f9aedc7f22e1fa9c873b062a2acd804fa419e559e

2. setRewardDistribution https://etherscan.io/tx/0x8fd1f966205cbc1886e650ca7f1d70366ee04fd48e8d9ce1c56e29ce1fe2b189