import pandas as pd
import numpy as np

def GenerateRowsPrep(df):

	# Generate the number of rows per invoice months
	inv_months = df[['Invoice_Number', 'DateDiffMonths']]
	inv_months = np.repeat(inv_months.Invoice_Number,inv_months.DateDiffMonths)

	# Merge with original dataset to explode rows
	df = pd.merge(df, inv_months, how = 'left', on = 'Invoice_Number')

	# Group by invoice number and running count of months to add
	df["MonthsToAdd"] = df.groupby(['Invoice_Number']).cumcount()

	# Spread revenue
	df.Value = df.Value/df.DateDiffMonths

	return(df)


def get_output_schema():
 	return pd.DataFrame({
 			'Customer_Name' : prep_string(),
 			'Invoice_Number' : prep_int(),
 			'Product' : prep_string(),
 			'Invoice_Start' : prep_date(),
 			'Invoice_End' : prep_date(),
 			'Value' : prep_decimal(),
 			'MonthsToAdd' : prep_int(),
 		});