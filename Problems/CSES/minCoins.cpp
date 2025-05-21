#include <iostream>
#include <vector>

int main() {
    int N, K;
    std::cin >> N >> K;
    std::vector<int> coins(N);
    for(int&coin : coins) std::cin >> coin;
    
    std::vector<int> dp(K+1, 1e9);

    dp[0] = 0;
    for (int i = 1; i < K+1; i++) {
        for (int coin : coins) {
            if (i - coin >= 0) {
                dp[i] = std::min(dp[i], 1 + dp[i-coin]);
            }
        }
    }
    int ans = dp[K];
    
    std::cout << (dp[K] == 1e9? -1 : dp[K]); 
}