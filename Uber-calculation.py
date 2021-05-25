annual_income=float(input("annual net income inc surge: £"))
CeLo_fees=float(input("Central London fees: £"))
ccz_fee=float(input("Congestion charge fees: £"))
miles_engaged=float(input("Miles during engaged time:"))


calculation=annual_income-((miles_engaged*0.45)+ccz_fee-CeLo_fees)
percentage=12.07/100
percentage_calculation=calculation*percentage

print(percentage_calculation)
