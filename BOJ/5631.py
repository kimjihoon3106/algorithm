# 맨아래 python 코드가 맞긴한데 memory와 timeout 시간을 맞추는걸 해결하지 못해서 
# 결국 아래 c++로 바꿔서 해결함..
"""
#include<bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    int case_num = 1;
    
    while(cin >> n && n != 0) {
        vector<pair<long long, long long>> houses(n);
        
        for(int i = 0; i < n; i++) {
            long long x, y;
            cin >> x >> y;
            houses[i] = {x, y};
        }
        
        long long ax, ay, bx, by;
        int q;
        cin >> ax >> ay >> bx >> by >> q;
        
        vector<pair<long long, long long>> dist_pairs;
        for(int i = 0; i < n; i++) {
            long long da_sq = (houses[i].first - ax) * (houses[i].first - ax) + 
                            (houses[i].second - ay) * (houses[i].second - ay);
            long long db_sq = (houses[i].first - bx) * (houses[i].first - bx) + 
                            (houses[i].second - by) * (houses[i].second - by);
            dist_pairs.push_back({da_sq, db_sq});
        }
        
        sort(dist_pairs.begin(), dist_pairs.end());
        
        vector<long long> dist_a_only(n);
        vector<long long> all_dist_b(n);
        for(int i = 0; i < n; i++) {
            dist_a_only[i] = dist_pairs[i].first;
            all_dist_b[i] = dist_pairs[i].second;
        }
        
        vector<long long> dist_b_sorted = all_dist_b;
        sort(dist_b_sorted.begin(), dist_b_sorted.end());
        
        cout << "Case " << case_num << ":\n";
        
        for(int i = 0; i < q; i++) {
            long long r1, r2;
            cin >> r1 >> r2;
            
            long long r1_sq = r1 * r1;
            long long r2_sq = r2 * r2;
            
            int count_a = upper_bound(dist_a_only.begin(), dist_a_only.end(), r1_sq) - dist_a_only.begin();
            int count_b = upper_bound(dist_b_sorted.begin(), dist_b_sorted.end(), r2_sq) - dist_b_sorted.begin();
            
            int pack_count_2 = 0;
            for(int j = 0; j < count_a; j++) {
                if(dist_pairs[j].second <= r2_sq) {
                    pack_count_2++;
                }
            }
            
            int pack_count_1 = count_a + count_b - 2 * pack_count_2;
            int protected_count = pack_count_1 + pack_count_2;
            int unprotected = max(0, n - protected_count - pack_count_2);
            
            cout << unprotected << "\n";
        }
        
        case_num++;
    }
    
    return 0;
}
"""

"""
import sys

def get_unprotected(h_with_n):
    house = len(h_with_n)
    pack = 0
    for r in h_with_n:
        if r == 2:
            pack += 2
        elif r == 1:
            pack += 1
    return max(house - pack, 0)

def get_case(n):

    h_location = [0 for _ in range(n)]
    current = 0
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        h_location[current] = (x, y)
        current += 1

    ax, ay, bx, by, q = map(int, sys.stdin.readline().split())

    n_range = []
    while True:
        line = sys.stdin.readline().split()
        if line[0] == '0':
            break

        if len(line) == 2:
            n_r_a, n_r_b = map(float, line)
            n_range.append([n_r_a, n_r_b])
    
    result = [0 for _ in range(len(n_range))]
    current = 0
    for r1, r2 in n_range:
        h_with_n = []
        r1_sq = r1 * r1
        r2_sq = r2 * r2
        for hx, hy in h_location:
            risk = 0
            if (hx - ax) ** 2 + (hy - ay) ** 2 <= r1_sq:
                risk += 1
            if (hx - bx) ** 2 + (hy - by) ** 2 <= r2_sq:
                risk += 1
            h_with_n.append(risk)
        result[current] = get_unprotected(h_with_n)
        current += 1

    return result

def main():
    case_num = 1
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        result = get_case(n)
        print(f"Case {case_num}:")
        answer = ""
        print('\n'.join(map(str, result)))
        case_num +=1 

if __name__ == "__main__":
    main()
"""