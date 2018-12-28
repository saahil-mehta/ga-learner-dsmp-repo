# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank=pd.read_csv(path)

bank.shape

categorical_var=bank.select_dtypes(include="object")
categorical_var.shape

numerical_var=bank.select_dtypes(include="number")
numerical_var.shape



# code ends here


# --------------
# code starts here
banks=bank.drop(columns="Loan_ID")

banks.isnull().sum().sum()

banks.head(20)

bank_mode=banks.mode()

banks=banks.fillna(bank_mode.iloc[0])
banks

#code ends here


# --------------
# Code starts here


avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'], values='LoanAmount',aggfunc="mean")
avg_loan_amount
# code ends here



# --------------
# code starts here
loan_approved_se=len(banks[(banks.Self_Employed == "Yes") & (banks.Loan_Status == "Y")])

loan_approved_nse=len(banks[(banks.Self_Employed == "No") & (banks.Loan_Status == "Y")])

loan_approved_se,loan_approved_nse
Loan_Status=banks["Loan_Status"].count()

percentage_se=(loan_approved_se/Loan_Status)*100
percentage_se

percentage_nse=(loan_approved_nse/Loan_Status)*100
percentage_nse
# code ends here


# --------------
# code starts here


loan_term=(banks["Loan_Amount_Term"]/12)
banks["Loan_Amount_Term"]=loan_term
banks["Loan_Amount_Term"]

big_loan_term=banks[banks["Loan_Amount_Term"]>=25].shape[0]
big_loan_term
# code ends here


# --------------
# code starts here


loan_groupby=banks.groupby(["Loan_Status"])

loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']

mean_values=loan_groupby.mean()

mean_values
# code ends here


