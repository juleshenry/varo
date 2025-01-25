w2 = 4.20e69


def general():
    BILLZ = {
        "1st": {"agua": 1e68 * 2},
        "15th": {"pan": 2e68 * 2},
    }
    # fmt:off
    C=lambda x:-sum(v for v in BILLZ[x].values()if type(v)!=str);a,b=C("1st"),C("15th");print(f"{w2}{a}={a+w2}",f"{w2}{b}={b+w2}",f"+:{2*w2}:+,{a+b}-,~{2*w2+a+b}~",sep='\n')
    # fmt:on
'''
monthly_cash_flow = 9, 000, 000

first_half_month = """
x/01 - x/15
$1,000,000 CASH
"""
second_half_month = """
x/16 - x/(28,29,30,31)
$400,000 RENT
"""
bilz_template = first_half_month + second_half_month

def print_bilz(bilz, assets):
    """
    e.g. print_bilz(bilz_template, {"cash": 1000, "savings": 1000})
    examples:
    $1,000,000 CASH
    $1,000,000,000,000 SAVINGS [debit]
    $1,000,001,000 TEMPDEBT [credit]
    """
    print(
        "ITEMIZED CREDITS=",
    )
    for k, v in assets.items():
        print(f"\t*{k} : {v}")
    print(f"\t{sum(assets.values())} NET CREDITS")
    debits = 0
    cc_debt = 0
    reasons = []
    for line in bilz.split("\n"):
        if "$" in line:
            try:
                reasons += [line]
                debit_amount = float(line.split("$")[1].strip().split(" ")[0])
                debits += debit_amount
                if "[credit]" in line:
                    cc_debt += debit_amount
            except:
                print(line, "unparsable")

    print("\n\t* ".join(["ITEMIZED DEBITS="] + reasons))
    print(f"\t${debits} NET DEBIT")
    liquid = sum(assets.values()) - debits + cc_debt
    print(f"{liquid} LIQUID\n{cc_debt} CREDIT CARD DEBT\n{liquid - cc_debt} NET\n")
    print("*" * 100)
    return {"liquid": liquid, "cc_debt": cc_debt}


def generic_spending():
    """Spending due to all bills and expenses, without food, gas, toiletries or savings"""
    payroll = {"cash": monthly_cash_flow}
    austerity = "\n".join(map(lambda a: f"${a}", "abracadabra"))
    total = bilz_template + austerity
    print_bilz(total, payroll)
'''

if __name__ == "__main__":
    general()
