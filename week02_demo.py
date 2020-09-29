# Initial balance of the bank account
initial_balance = 200

# Bank statement with all transactions for the past 6 months
statement = [[-119.02, -56.54, 1200, -80, -12.99, -550, -167.90, -5.58, -3.54, -9.99],
             [-138.32, -67.12, 1200, -80, -12.99, -268.10, -550, -92.90, -125.65],
             [-101.44, -48.83, -19.99, -92.12, 1200, -80, -67.33, -12.99, -550, -30.33],
             [-91.98, -45.65, -50, -9.99, 1200, -80, -414.22, -12.99, -550, -9.29, -67.12],
             [-159.53, -27.61, -168.45, 1200, -80, -12.99, -76.94, -550, -28.08, -27.89],
             [-141.97, 1200, -87.78, -80, -12.99, -67.92, -188.09, -550, -4.20, -13.68]]

# Your job: pay monthly 0.5% interest to this account.

# Update the account balance each month: OK!

def account_balance(month, ibalance):
    x = sum(statement[(month-1)]) + ibalance
    return x

def interest(balance, interest):
    x = balance * interest
    return x


total = 0
balance = 200
for i in range(1,7):
    balance = account_balance(i,balance)
    statement[i-1].append(interest(balance,0.005))
    total = sum(statement[i-1]) + total
    print(statement[i-1])
print(total+200)




# Calculate interest each month: OK!
# Pay the total interest (6 months) to the account:
# - pay the total (update the balance for the last month)
# - log that transaction into statement for 6th month.
