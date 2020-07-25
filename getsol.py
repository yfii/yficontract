import requests

s = requests.Session()


def getsourcecode(contract_address):
    url = f"http://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey=AWXR3HCJBWXTXAG61BYD43CVUGC2MDA5UG"
    z1 = s.get(url)
    return z1.json()["result"][0]["SourceCode"]


contracts = {
    "yCurveFiRewardsAddress": "0x0001FB050Fe7312791bF6475b96569D83F695C9f",
    "balancerRewardsAddress": "0x033E52f513F9B98e129381c6708F9faA2DEE5db5",
    "yfiAddress": "0xE4E750275C5E6DEfc3fADc4c9FAE58714234e629",
    "claimAddress": "0xcc9EFea3ac5Df6AD6A656235Ef955fBfEF65B862",
    "governanceAddress": "0x3A22dF48d84957F907e67F4313E3D43179040d6E",
    "bpoolAddress": "0x95c4b6c7cff608c0ca048df8b81a484aa377172b",
    "feeRewardsAddress": "0xb01419E74D8a2abb1bbAD82925b19c36C191A701",
}

for name, address in contracts.items():
    source_code = getsourcecode(address)
    with open(f"{name}.sol", "w") as f:
        f.write(source_code)
