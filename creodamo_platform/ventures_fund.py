# ventures_fund.py

class VenturesFund:
    def __init__(self):
        self.partnerships = []
        self.investments = []

    def form_partnership(self, partner):
        self.partnerships.append(partner)

    def track_investments(self):
        for investment in self.investments:
            print(f"Tracking returns for {investment}")
