#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    const int MOD = 1000000007;
    int numCoins, target;
    cin >> numCoins >> target;
    vector<int> coins(numCoins);
    vector<int> dp(target+1, 0);
    for (int i= 0; i< numCoins;i++) {
        int coin; cin >> coin;
        if (coin <= target) {
            coins[i] = coin;
            dp[coin]++;
        }
    }
    sort(coins.begin(), coins.end());
    dp[0] = 0;
    for (int i =0; i< target+1; i++) {
        for (int coin : coins) {
            if (i - coin >= 0)
                dp[i] = (dp[i] + dp[i-coin]) % MOD;
            else break;
        }
    }
    cout << dp[target] % MOD;

}