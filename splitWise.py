class SplitWise:

    def solution(self):

        payment_summary = {
            "hari" : 1200,
            "vibin" : 1400,
            "jhon" : 1000,
            "vishnu" : 0,
            "tom" : 120,
            "avinash" : 0,
            "jini" : 0,
            "asok" : 0
        }


        total_exp = sum(payment_summary.values())

        print(f"Total amount : {total_exp}")

        individual_split = total_exp / len(payment_summary)

        print(f"individual split : {individual_split}")

        result = {k : individual_split - v for k, v in payment_summary.items()}

        print(result)

    
splitinstance = SplitWise()
splitinstance.solution()
