
#include <bits/stdc++.h>
#include <chrono>
using namespace std;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define HM unordered_map

inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
MOD = 1e9+7
N = 1e6 + 5

def main():

    T = int(next(inf))

    for i in range(1, T+1):
        
        

        ouf.write("Case #" + str(i) + ": " + ans + "\n")

def solve():

    for i in range
    for(int i = 0; i < k; i++)
        cin >> lef[i];

    cin >> a >> b >> c >> d;

    for(int i = k; i < n; i++)
        lef[i] = ((a*lef[i-2] + b*lef[i-1] + c)%d)+1;

    for(int i = 0; i < k; i++)
        cin >> height[i];

    cin >> a >> b >> c >> d;

    for(int i = k; i < n; i++)
        height[i] = ((a*height[i-2] + b*height[i-1] + c)%d)+1;

    p[0] = (2*w + 2*height[0])%MOD;
    ll product = p[0];

    for(int i = 1; i < n; i++){

        int j = i-1;
        ll maxH = -1;

        while(j >= 0 && (lef[j]+w) >= lef[i]){
            maxH = max(maxH,height[j]);
            j--;
        }

        if(maxH == -1){
            p[i] = p[i-1] + 2*w + 2*height[i];
        }
        else{
            p[i] = p[i-1] + 2*(lef[i] - lef[i-1]);

            if(height[i] > maxH){
                p[i] += 2*(height[i]-maxH);
            }
        }

        p[i] = p[i]%MOD;

        product = (product * p[i])%MOD;
    }

    cout << product << endl;


if __name__ == "__main__":
    main()

int main()
{
    bool flag = 1;
    if(flag){
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    }

    int t;
    cin >> t;
    int i = 1;
    while(t--){
        cin >> n >> k >> w;
        cout << "Case #" << i << ": ";
        solve();
        i++;
    }

    return 0;
}
