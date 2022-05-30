#pragma GCC optimize("Ofast,unroll-loops,no-stack-protector")
#include <bits/stdc++.h>
using namespace std;

#define fore(i, l, r) for (auto i = (l) - ((l) > (r)); i != (r) - ((l) > (r)); i += 1 - 2 * ((l) > (r)))
#define sz(x) int(x.size())
#define all(x) begin(x), end(x)
#define f first
#define s second
#define pb push_back

#ifdef LOCAL
#include "debug.h"
#else
#define debug(...)
#endif

using ld = long double;
using lli = long long;
using ii = pair<int, int>;

map<string, string> mp;

int main() {
  cin.tie(0)->sync_with_stdio(0), cout.tie(0);

  // Mainly because this file is huge >:c
  fstream embeddingsFile("Word2VectEnglish.txt");
  ofstream wordsFile("Word2VectEnglishSortedWords.txt");
  ofstream linesFile("Word2VectEnglishSorted.txt");

  int lines;
  string tmp;
  embeddingsFile >> lines >> tmp;

  cout << lines << " " << tmp << '\n';

  while (lines--) {
    getline(embeddingsFile, tmp);

    stringstream ss(tmp);
    string word, vec;

    ss >> word;
    vec = tmp.substr(sz(word));

    mp[word] = vec;
  }
  embeddingsFile.close();

  for (auto& [word, vec] : mp) {
    wordsFile << word << '\n';
    linesFile << word << " " << vec << '\n';
  }

  wordsFile.close();
  linesFile.close();

  return 0;
}

/* Please, check the following:
 * int overflow, array bounds
 * special cases (n=1?)
 * do smth instead of nothing and stay organized
 * write down your ideas
 * DON'T get stuck on ONE APPROACH!
 * ASK for HELP from your TEAMMATES
 */