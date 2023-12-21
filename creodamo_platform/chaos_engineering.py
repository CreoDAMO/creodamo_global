import asyncio
from creolang import CreoLangInterpreter
from proof_of_creo import ProofOfCreoValidator
from prometheus_client import Summary
from typing import List, Dict

# Prometheus metrics
execution_latency = Summary('contract_execution_latency', 'Latency of smart contract execution (in seconds)')

class BlockchainService:
    def __init__(self) -> None:
        self.creolang_interpreter = CreoLangInterpreter()
        self.proof_of_creo_validator = ProofOfCreoValidator()

    async def execute_smart_contract(self, contract: Dict[str, str]) -> Dict:
        code = contract["code"]
        params = contract["parameters"]

        # Validate the contract
        self.proof_of_creo_validator.validate(code, params)

        # Execute the contract
        start_time = asyncio.get_event_loop().time()
        result = await self.creolang_interpreter.execute(code, params)
        end_time = asyncio.get_event_loop().time()

        # Record the execution latency
        execution_latency.observe(end_time - start_time)

        return {"result": result, "duration": end_time - start_time}

    async def execute_batch(self, contracts: List[Dict[str, str]]) -> List[Dict]:
        tasks = [asyncio.create_task(self.execute_smart_contract(contract)) for contract in contracts]
        return await asyncio.gather(*tasks)

# Example usage
async def main():
    blockchain_service = BlockchainService()

    # Define smart contracts
    contracts = [
        {"code": "contract_1_code", "parameters": {}},
        {"code": "contract_2_code", "parameters": {}},
    ]

    # Execute contracts in batch
    results = await blockchain_service.execute_batch(contracts)
    print("Batch Execution Results:", results)

if __name__ == "__main__":
    asyncio.run(main())
