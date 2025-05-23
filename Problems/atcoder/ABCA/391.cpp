#include "dekodingTemplate.hpp"

int main() {
    unordered_map<char, char> mp = {{'N', 'S'},{'E','W'}};

    string s;
    cin >> s;
    for (auto p : mp) {
        mp[p.second] = p.first;
    }
    for (char c : s) {
        cout << mp[c];
    }
}