gross_income=float(input('enter your gross income: '))
tax_rate_1=0.14
tax_rate_2=0.25
net_income_1=gross_income-gross_income*0.14
net_income_2=gross_income-(350+(gross_income-2500)*0.25)
if gross_income<2500:
    print(net_income_1)
else:
    print(net_income_2)
