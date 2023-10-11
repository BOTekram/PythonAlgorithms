'''
Description of the Dynamic Programming Solution:


dp is a list of length target+1, where dp[i] 
will eventually contain the shortest combination of coins that sum to i.

Nested Loops:
-We initialize dp[0] = [] because it takes zero coins to make the value zero.

-The outer loop iterates over eacg value from 1 to the target (12 in this case)
-The inner loop iterates over each coin in the given coin set (1, 5, 6, 9)

Check and Update:
- value - coin >= 0 cgecks if the coin is not too big for the current valye we are considering
-dp[value - coin] is not None checks if it's possible to make the value (value - coin) with the aviable coins. 
 if  it's possible, then adding coin would make the value 'value'.
-if dp[value] is None or len(dp[value - coin]) + 1 < len(dp[value]) : This line checks if either:
  - We haven't found a combination for the current value yet (dp[value] is None) or,
  -The new combination we're considering is shorter than the one we've already found.
If either of these conditions is met, we update dp[value] with the new, shorter combination.

Result
- AT the end, dp[target] contains the shortest combin tations of coins that sum up to the target value. In this case, that's 12
'''


def coin_combinations(target, coins):
    # Initialize a list to store the combinations needed to achieve each value up to target
    dp = [None] * (target + 1) 
    dp[0] = [] #base case. The line sets dp[0] to an empty list indicating that it takes zero coins to make the value 0
    
    # Loop through each value up to target
    for value in range(1, target + 1): 
        for coin in coins:
            if value - coin >= 0 and dp[value - coin] is not None:
                # If it's possible to achieve (value - coin), then it's possible to achieve value
                if dp[value] is None or len(dp[value - coin]) + 1 < len(dp[value]):
                    dp[value] = dp[value - coin] + [coin]
    
    return dp[target]

target = 12
coins = [1, 5, 6, 9]
result = coin_combinations(target, coins)

if result:
    print(f"The coin combination to get {target} Dogecoin is {result}")
else:
    print(f"It is not possible to get {target} Dogecoin with the given coin types.")
