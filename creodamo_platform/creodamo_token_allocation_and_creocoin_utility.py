class CreoDAMO:
    def __init__(self, total_supply: int):
        self.total_supply = total_supply
        self.cdt_allocation = 1.5 * 10**9
        self.creo_allocation = 5 * 10**9

    def allocate_tokens(self):
        # Community Development (20%)
        community_dev_allocation = int(self.total_supply * 0.20)

        # Founders' Reserve (15%)
        founders_reserve_allocation = int(self.total_supply * 0.15)

        # Governance & Regulatory Reserves (15%)
        governance_reserve_allocation = int(self.total_supply * 0.15)

        # Token Sale Funds (15%)
        token_sale_funds_allocation = int(self.total_supply * 0.15)

        # Ecosystem Growth Funds (15%)
        ecosystem_growth_funds_allocation = int(self.total_supply * 0.15)

        # Advisors, Team & Bounty (10%)
        advisors_team_bounty_allocation = int(self.total_supply * 0.10)

        # Treasury Funds (10%)
        treasury_funds_allocation = int(self.total_supply * 0.10)

        return (
            community_dev_allocation,
            founders_reserve_allocation,
            governance_reserve_allocation,
            token_sale_funds_allocation,
            ecosystem_growth_funds_allocation,
            advisors_team_bounty_allocation,
            treasury_funds_allocation,
        )

    def coin_utility(self):
        cdt_utility = {
            "platform_access": True,
            "community_rewards": True,
            "governance_participation": True,
            "partnership_fostering": True,
        }

        creo_utility = {
            "platform_access": True,
            "community_rewards": True,
            "governance_participation": True,
            "partnership_fostering": True,
        }

        return cdt_utility, creo_utility


# Instantiate CreoDAMO with total supply of 6.5 billion tokens
creo_damo = CreoDAMO(6.5 * 10**9)

# Allocate tokens according to the strategies
community_dev, founders_reserve, governance_reserve, token_sale_funds, \
    ecosystem_growth_funds, advisors_team_bounty, treasury_funds = creo_damo.allocate_tokens()

# Get coin utility details
cdt_utility, creo_utility = creo_damo.coin_utility()

# Print the allocations and coin utility
print(f"Token Allocations:")
print(f"Community Development: {community_dev}")
print(f"Founders' Reserve: {founders_reserve}")
print(f"Governance & Regulatory Reserves: {governance_reserve}")
print(f"Token Sale Funds: {token_sale_funds}")
print(f"Ecosystem Growth Funds: {ecosystem_growth_funds}")
print(f"Advisors, Team & Bounty: {advisors_team_bounty}")
print(f"Treasury Funds: {treasury_funds}")

print("\nCoin Utility:")
print("CDT Utility:")
print(cdt_utility)

print("\nCreo Utility:")
print(creo_utility)
```
