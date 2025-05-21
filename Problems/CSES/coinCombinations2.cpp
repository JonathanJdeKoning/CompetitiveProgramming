#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int mod = 1000000007;
vector<int> coins;
vector<vector<int>> dp;

int main() {
    int numCoins, targetSum;
    cin >> numCoins >> targetSum;

    coins = vector<int>(numCoins);
    for (int i=0;i<numCoins;i++) cin >> coins[i];
    sort(coins.begin(), coins.end());

    dp.resize(numCoins+1);
    for (int i=0; i<numCoins+1; i++) dp[i].resize(targetSum+1);
    dp[coins.size()][0] = 1;
    
    for (int target=0; target < targetSum+1; target++) {
        for (int i = numCoins - 1; i > -1; i--) {

            dp[i][target] = dp[i+1][target];
            if (coins[i] <= target)
                dp[i][target] += dp[i][target - coins[i]];
            dp[i][target]%=mod;

        }
    }

    cout << dp[0][targetSum]%mod;
}