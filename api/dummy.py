staticProblems = [{'history': 'Let s be some string consisting of symbols " 0" or " 1" . Let\' '
             's call a string t a substring of string s, if there exists such '
             "number 1≤l≤| s| −| t| + 1 that t= slsl+ 1. . . sl+ | t| −1. Let' "
             's call a substring t of string s unique, if there exist only one '
             'such l. For example, let s= " 1010111" . A string t= " 010" is '
             'an unique substring of s, because l= 2 is the only one suitable '
             'number. But, for example t= " 10" isn\' t a unique substring of '
             's, because l= 1 and l= 3 are suitable. And for example t= " 00" '
             "at all isn' t a substring of s, because there is no suitable l. "
             'Today Vasya solved the following problem at the informatics '
             'lesson: given a string consisting of symbols " 0" and " 1" , the '
             'task is to find the length of its minimal unique substring. He '
             'has written a solution to this problem and wants to test it. He '
             'is asking you to help him. You are given 2 positive integers n '
             'and k, such that ( nmod, where ( x 2) is operation of taking '
             'remainder of x by dividing on 2. Find any string s consisting of '
             'n symbols " 0" or " 1" , such that the length of its minimal '
             'unique substring is equal to k.',
  'input': 'The first line contains two integers n and k, separated by spaces '
           '( 1 ≤k ≤n ≤100 000, ( k 2) = ( n 2) ) .',
  'note': "In the first test, it' s easy to see, that the only unique "
          'substring of string s = " 1111" is all string s, which has length '
          '4. In the second test a string s = " 01010" has minimal unique '
          'substring t = " 101" , which has length 3. In the third test a '
          'string s = " 1011011" has minimal unique substring t = " 110" , '
          'which has length 3.',
  'output': 'Print a string s of length n, consisting of symbols " 0" and " 1" '
            '. Minimal length of the unique substring of s should be equal to '
            'k. You can find any suitable string. It is guaranteed, that there '
            'exists at least one such string.',
  'title': 'The minimal unique substring',
  'topics': ['constructive algorithms', 'math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1158/B'},
 {'history': 'During a normal walk in the forest, Katie has stumbled upon a '
             'mysterious code! However, the mysterious code had some '
             'characters unreadable. She has written down this code as a '
             'string c consisting of lowercase English characters and '
             'asterisks ( " * " ) , where each of the asterisks denotes an '
             'unreadable character. Excited with her discovery, Katie has '
             'decided to recover the unreadable characters by replacing each '
             'asterisk with arbitrary lowercase English letter ( different '
             'asterisks might be replaced with different letters) . Katie has '
             'a favorite string s and a not- so- favorite string t and she '
             'would love to recover the mysterious code so that it has as many '
             'occurrences of s as possible and as little occurrences of t as '
             "possible. Formally, let' s denote f( x, y) as the number of "
             'occurrences of y in x ( for example, f( aababa, ab) = 2) . Katie '
             'wants to recover the code c′ conforming to the original c, such '
             'that f( c′, s) −f( c′, t) is largest possible. However, Katie is '
             'not very good at recovering codes in general, so she would like '
             'you to help her out.',
  'input': 'The first line contains string c ( 1≤| c| ≤1000) — the mysterious '
           'code . It is guaranteed that c consists of lowercase English '
           'characters and asterisks " * " only. The second and third line '
           'contain strings s and t respectively ( 1≤| s| , | t| ≤50, s= ̸t) . '
           'It is guaranteed that s and t consist of lowercase English '
           'characters only.',
  'note': 'In the first example, for c′ equal to " katie" f( c′, s) = 1 and f( '
          'c′, t) = 0, which makes f( c′, s) −f( c′, t) = 1 which is the '
          'largest possible. In the second example, the only c′ conforming to '
          'the given c is " caat" . The corresponding f( c′, s) −f( c′, t) = '
          '1−2= −1. In the third example, there are multiple ways to recover '
          'the code such that f( c′, s) −f( c′, t) is largest possible, for '
          'example " aaa" , " aac" , or even " zaz" . The value of f( c′, s) '
          '−f( c′, t) = 0 for all of these recovered codes. In the fourth '
          'example, the optimal recovered code c′ would be " ccc" . The '
          'corresponding f( c′, s) −f( c′, t) = 2.',
  'output': 'Print a single integer — the largest possible value of f( c′, s) '
            '−f( c′, t) of the recovered code.',
  'title': 'Mysterious Code',
  'topics': ['dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1163/D'},
 {'history': 'A telephone number is a sequence of exactly 11 digits, where the '
             'first digit is 8. For example, the sequence 80011223388 is a '
             'telephone number, but the sequences 70011223388 and '
             '80000011223388 are not. You are given a string s of length n, '
             'consisting of digits. In one operation you can delete any '
             'character from string s. For example, it is possible to obtain '
             'strings 112, 111 or 121 from string 1121. You need to determine '
             'whether there is such a sequence of operations ( possibly empty) '
             ', after which the string s becomes a telephone number.',
  'input': 'The first line contains one integer t ( 1≤t≤100) — the number of '
           'test cases. The first line of each test case contains one integer '
           'n ( 1≤n≤100) — the length of string s. The second line of each '
           'test case contains the string s ( | s| = n) consisting of digits.',
  'note': 'In the first test case you need to delete the first and the third '
          'digits. Then the string 7818005553535 becomes 88005553535.',
  'output': 'For each test print one line. If there is a sequence of '
            'operations, after which s becomes a telephone number, print YES. '
            'Otherwise, print NO.',
  'title': 'Telephone Number',
  'topics': ['brute force', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1167/A'},
 {'history': 'Everyone knows that two consecutive ( adjacent) " minus" signs '
             'can be replaced with a single " plus" sign. You are given the '
             'string s, consisting of " plus" and " minus" signs only. Zero or '
             'more operations can be performed with it. In each operation you '
             'can choose any two adjacent " minus" signs, and replace them '
             'with a single " plus" sign. Thus, in one operation, the length '
             'of the string is reduced by exactly 1. You are given two strings '
             's and t. Determine if you can use 0 or more operations to get '
             'the string t from the string s.',
  'input': 'The first line of the input contains an integer k ( 1≤k≤105) , '
           'denoting the number of test cases in the input. The following '
           'lines contain descriptions of the test sets, each set consists of '
           'two lines. First comes the line containing s ( the length of the '
           'line s does not exceed 2⋅105) , then comes the line containing t ( '
           'the length of the line t does not exceed 2⋅105) . The lines s and '
           't are non- empty, and they contain only " plus" and " minus" '
           'signs. The sum of the lengths of lines s over all test cases in '
           'the input does not exceed 2⋅105. Similarly, the sum of the lengths '
           'of lines t over all test cases in the input does not exceed 2⋅105.',
  'note': ' ',
  'output': 'Print k lines: the i- th line must contain YES if the answer to '
            'the i- th test case is positive, otherwise NO. Print YES and NO '
            'using uppercase letters only.',
  'title': 'Minus and Minus Give Plus',
  'topics': ['*special', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1170/C'},
 {'history': 'Recall that string a is a subsequence of a string b if a can be '
             'obtained from b by deletion of several ( possibly zero or all) '
             'characters. For example, for the string a= " wowwo" , the '
             'following strings are subsequences: " wowwo" , " wowo" , " oo" , '
             '" wow" , " " , and others, but the following are not '
             'subsequences: " owoo" , " owwwo" , " ooo" . The wow factor of a '
             'string is the number of its subsequences equal to the word " '
             'wow" . Bob wants to write a string that has a large wow factor. '
             'However, the " w" key on his keyboard is broken, so he types two '
             '" v" s instead. Little did he realise that he may have '
             'introduced more " w" s than he thought. Consider for instance '
             'the string " ww" . Bob would type it as " vvvv" , but this '
             'string actually contains three occurrences of " w" : " vvvv" " '
             'vvvv" " vvvv" For example, the wow factor of the word " vvvovvv" '
             'equals to four because there are four wows: " vvvovvv" " '
             'vvvovvv" " vvvovvv" " vvvovvv" Note that the subsequence " '
             'vvvovvv" does not count towards the wow factor, as the " v" s '
             'have to be consecutive. For a given string s, compute and output '
             'its wow factor. Note that it is not guaranteed that it is '
             'possible to get s from another string replacing " w" with " vv" '
             '. For example, s can be equal to " vov" .',
  'input': 'The input contains a single non- empty string s, consisting only '
           'of characters " v" and " o" . The length of s is at most 106.',
  'note': 'The first example is explained in the legend.',
  'output': 'Output a single integer, the wow factor of s.',
  'title': 'WOW Factor',
  'topics': ['dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1178/B'},
 {'history': 'Alice bought a Congo Prime Video subscription and was watching a '
             "documentary on the archaeological findings from Factor' s Island "
             'on Loch Katrine in Scotland. The archaeologists found a book '
             'whose age and origin are unknown. Perhaps Alice can make some '
             'sense of it? The book contains a single string of characters " '
             'a" , " b" and " c" . It has been pointed out that no two '
             'consecutive characters are the same. It has also been '
             'conjectured that the string contains an unusually long '
             'subsequence that reads the same from both sides. Help Alice '
             'verify this by finding such subsequence that contains at least '
             'half of the characters of the original string, rounded down. '
             "Note that you don' t have to maximise the length of it. A string "
             'a is a subsequence of a string b if a can be obtained from b by '
             'deletion of several ( possibly, zero or all) characters.',
  'input': 'The input consists of a single string s ( 2≤| s| ≤106) . The '
           'string s consists only of characters " a" , " b" , " c" . It is '
           'guaranteed that no two consecutive characters are equal.',
  'note': 'In the first example, other valid answers include " cacac" , " '
          'caac" , " aca" and " ccc" .',
  'output': 'Output a palindrome t that is a subsequence of s and | t| ≥⌊| s| '
            '2⌋. If there are multiple solutions, you may print any of them. '
            "You don' t have to maximise the length of t. If there are no "
            'solutions, output a string " IMPOSSIBLE" ( quotes for clarity) .',
  'title': 'Archaeology',
  'topics': ['brute force', 'constructive algorithms', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1178/E'},
 {'history': 'Dima worked all day and wrote down on a long paper strip his '
             'favorite number n consisting of l digits. Unfortunately, the '
             "strip turned out to be so long that it didn' t fit in the Dima' "
             's bookshelf. To solve the issue, Dima decided to split the strip '
             'into two non- empty parts so that each of them contains a '
             'positive integer without leading zeros. After that he will '
             'compute the sum of the two integers and write it down on a new '
             'strip. Dima wants the resulting integer to be as small as '
             'possible, because it increases the chances that the sum will fit '
             'it in the bookshelf. Help Dima decide what is the minimum sum he '
             'can obtain.',
  'input': 'The first line contains a single integer l ( 2≤l≤100000) — the '
           "length of the Dima' s favorite number. The second line contains "
           "the positive integer n initially written on the strip: the Dima' s "
           'favorite number. The integer n consists of exactly l digits and it '
           'does not contain leading zeros. Dima guarantees, that there is at '
           'least one valid way to split the strip.',
  'note': 'In the first example Dima can split the number 1234567 into '
          'integers 1234 and 567. Their sum is 1801. In the second example '
          'Dima can split the number 101 into integers 10 and 1. Their sum is '
          '11. Note that it is impossible to split the strip into " 1" and " '
          '01" since the numbers can\' t start with zeros.',
  'output': 'Print a single integer — the smallest number Dima can obtain.',
  'title': 'Split a Number',
  'topics': ['greedy', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1181/B'},
 {'history': 'You have a given picture with size w×h. Determine if the given '
             'picture has a single " + " shape or not. A " + " shape is '
             'described below: A " + " shape has one center nonempty cell. '
             'There should be some ( at least one) consecutive non- empty '
             'cells in each direction ( left, right, up, down) from the '
             'center. In other words, there should be a ray in each direction. '
             'All other cells are empty. Find out if the given picture has '
             'single " + " shape.',
  'input': 'The first line contains two integers h and w ( 1≤h, w≤500) — the '
           'height and width of the picture. The i- th of the next h lines '
           'contains string si of length w consisting " . " and " * " where " '
           '. " denotes the empty space and " * " denotes the non- empty '
           'space.',
  'note': 'In the first example, the given picture contains one " + " . In the '
          'second example, two vertical branches are located in a different '
          'column. In the third example, there is a dot outside of the shape. '
          'In the fourth example, the width of the two vertical branches is 2. '
          'In the fifth example, there are two shapes. In the sixth example, '
          'there is an empty space inside of the shape.',
  'output': 'If the given picture satisfies all conditions, print " YES" . '
            'Otherwise, print " NO" . You can output each letter in any case ( '
            'upper or lower) .',
  'title': 'Plus from Picture',
  'topics': ['dfs and similar', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1182/B'},
 {'history': 'You are given n words, each of which consists of lowercase '
             'alphabet letters. Each word contains at least one vowel. You are '
             'going to choose some of the given words and make as many '
             'beautiful lyrics as possible. Each lyric consists of two lines. '
             'Each line consists of two words separated by whitespace. A lyric '
             'is beautiful if and only if it satisfies all conditions below. '
             'The number of vowels in the first word of the first line is the '
             'same as the number of vowels in the first word of the second '
             'line. The number of vowels in the second word of the first line '
             'is the same as the number of vowels in the second word of the '
             'second line. The last vowel of the first line is the same as the '
             'last vowel of the second line. Note that there may be consonants '
             'after the vowel. Also, letters " a" , " e" , " o" , " i" , and " '
             'u" are vowels. Note that " y" is never vowel. For example of a '
             'beautiful lyric, " hello hellooowww" " whatsup yowowowow" is a '
             'beautiful lyric because there are two vowels each in " hello" '
             'and " whatsup" , four vowels each in " hellooowww" and " '
             'yowowowow" ( keep in mind that " y" is not a vowel) , and the '
             'last vowel of each line is " o" . For example of a not beautiful '
             'lyric, " hey man" " iam mcdic" is not a beautiful lyric because '
             '" hey" and " iam" don\' t have same number of vowels and the '
             'last vowels of two lines are different ( " a" in the first and " '
             'i" in the second) . How many beautiful lyrics can you write from '
             'given words? Note that you cannot use a word more times than it '
             'is given to you. For example, if a word is given three times, '
             'you can use it at most three times.',
  'input': 'The first line contains single integer n ( 1≤n≤105) — the number '
           'of words. The i- th of the next n lines contains string si '
           'consisting lowercase alphabet letters — the i- th word. It is '
           'guaranteed that the sum of the total word length is equal or less '
           'than 106. Each word contains at least one vowel.',
  'note': 'In the first example, those beautiful lyrics are one of the '
          "possible answers. Let' s look at the first lyric on the sample "
          'output of the first example. " about proud hooray round" forms a '
          'beautiful lyric because " about" and " hooray" have same number of '
          'vowels, " proud" and " round" have same number of vowels, and both '
          'lines have same last vowel. On the other hand, you cannot form any '
          'beautiful lyric with the word " codeforces" . In the second '
          'example, you cannot form any beautiful lyric from given words. In '
          'the third example, you can use the word " same" up to three times.',
  'output': 'In the first line, print m — the number of maximum possible '
            'beautiful lyrics. In next 2m lines, print m beautiful lyrics ( '
            'two lines per lyric) . If there are multiple answers, print any.',
  'title': 'Beautiful Lyrics',
  'topics': ['data structures', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1182/C'},
 {'history': 'The only difference between the easy and the hard versions is '
             'constraints. A subsequence is a string that can be derived from '
             'another string by deleting some or no symbols without changing '
             'the order of the remaining symbols. Characters to be deleted are '
             'not required to go successively, there can be any gaps between '
             'them. For example, for the string " abaca" the following strings '
             'are subsequences: " abaca" , " aba" , " aaa" , " a" and " " ( '
             'empty string) . But the following strings are not subsequences: '
             '" aabaca" , " cb" and " bcaa" . You are given a string s '
             'consisting of n lowercase Latin letters. In one move you can '
             'take any subsequence t of the given string and add it to the set '
             "S. The set S can' t contain duplicates. This move costs n−| t| , "
             'where | t| is the length of the added subsequence ( i. e. the '
             'price equals to the number of the deleted characters) . Your '
             'task is to find out the minimum possible total cost to obtain a '
             'set S of size k or report that it is impossible to do so.',
  'input': 'The first line of the input contains two integers n and k ( '
           '1≤n≤100, 1≤k≤1012) — the length of the string and the size of the '
           'set, correspondingly. The second line of the input contains a '
           'string s consisting of n lowercase Latin letters.',
  'note': 'In the first example we can generate S = " asdf" , " asd" , " adf" '
          ', " asf" , " sdf" . The cost of the first element in S is 0 and the '
          'cost of the others is 1. So the total cost of S is 4.',
  'output': 'Print one integer — if it is impossible to obtain the set S of '
            'size k, print - 1. Otherwise, print the minimum possible total '
            'cost to do it.',
  'title': 'Subsequences (hard version)',
  'topics': ['dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1183/H'},
 {'history': 'Methodius received an email from his friend Polycarp. However, '
             "Polycarp' s keyboard is broken, so pressing a key on it once may "
             'cause the corresponding symbol to appear more than once ( if you '
             'press a key on a regular keyboard, it prints exactly one symbol) '
             '. For example, as a result of typing the word " hello" , the '
             'following words could be printed: " hello" , " hhhhello" , " '
             'hheeeellllooo" , but the following could not be printed: " hell" '
             ', " helo" , " hhllllooo" . Note, that when you press a key, the '
             'corresponding symbol must appear ( possibly, more than once) . '
             'The keyboard is broken in a random manner, it means that '
             'pressing the same key you can get the different number of '
             'letters in the result. For each word in the letter, Methodius '
             'has guessed what word Polycarp actually wanted to write, but he '
             'is not sure about it, so he asks you to help him. You are given '
             'a list of pairs of words. For each pair, determine if the second '
             "word could be printed by typing the first one on Polycarp' s "
             'keyboard.',
  'input': 'The first line of the input contains one integer n ( 1≤n≤105) — '
           'the number of pairs to check. Further input contains n '
           'descriptions of pairs. The first line of each description contains '
           'a single non- empty word s consisting of lowercase Latin letters. '
           'The second line of the description contains a single non- empty '
           'word t consisting of lowercase Latin letters. The lengths of both '
           'strings are not greater than 106. It is guaranteed that the total '
           'length of all words s in the input is not greater than 106. Also, '
           'it is guaranteed that the total length of all words t in the input '
           'is not greater than 106.',
  'note': ' ',
  'output': 'Output n lines. In the i- th line for the i- th pair of words s '
            'and t print YES if the word t could be printed by typing the word '
            's. Otherwise, print NO.',
  'title': 'Email from Polycarp',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1185/B'},
 {'history': 'The letters shop showcase is a string s, consisting of n '
             'lowercase Latin letters. As the name tells, letters are sold in '
             'the shop. Letters are sold one by one from the leftmost to the '
             'rightmost. Any customer can only buy some prefix of letters from '
             'the string s. There are m friends, the i- th of them is named '
             'ti. Each of them is planning to estimate the following value: '
             'how many letters ( the length of the shortest prefix) would s/ '
             'he need to buy if s/ he wanted to construct her/ his name of '
             'bought letters. The name can be constructed if each letter is '
             'presented in the equal or greater amount. For example, for s= " '
             'arrayhead" and ti= " arya" 5 letters have to be bought ( " '
             'arrayhead" ) . For example, for s= " arrayhead" and ti= " harry" '
             '6 letters have to be bought ( " arrayhead" ) . For example, for '
             's= " arrayhead" and ti= " ray" 5 letters have to be bought ( " '
             'arrayhead" ) . For example, for s= " arrayhead" and ti= " r" 2 '
             'letters have to be bought ( " arrayhead" ) . For example, for s= '
             '" arrayhead" and ti= " areahydra" all 9 letters have to be '
             'bought ( " arrayhead" ) . It is guaranteed that every friend can '
             'construct her/ his name using the letters from the string s. '
             'Note that the values for friends are independent, friends are '
             'only estimating them but not actually buying the letters.',
  'input': 'The first line contains one integer n ( 1≤n≤2⋅105) — the length of '
           'showcase string s. The second line contains string s, consisting '
           'of exactly n lowercase Latin letters. The third line contains one '
           'integer m ( 1≤m≤5⋅104) — the number of friends. The i- th of the '
           'next m lines contains ti ( 1≤| ti| ≤2⋅105) — the name of the i- th '
           'friend. It is guaranteed that m∑i= 1| ti| ≤2⋅105.',
  'note': ' ',
  'output': 'For each friend print the length of the shortest prefix of '
            'letters from s s/ he would need to buy to be able to construct '
            'her/ his name of them. The name can be constructed if each letter '
            'is presented in the equal or greater amount. It is guaranteed '
            'that every friend can construct her/ his name using the letters '
            'from the string s.',
  'title': 'Letters Shop',
  'topics': ['binary search', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1187/B'},
 {'history': 'After playing Neo in the legendary " Matrix" trilogy, Keanu '
             'Reeves started doubting himself: maybe we really live in virtual '
             'reality? To find if this is true, he needs to solve the '
             "following problem. Let' s call a string consisting of only "
             'zeroes and ones good if it contains different numbers of zeroes '
             'and ones. For example, 1, 101, 0000 are good, while 01, 1001, '
             'and 111000 are not good. We are given a string s of length n '
             'consisting of only zeroes and ones. We need to cut s into '
             'minimal possible number of substrings s1, s2, . . . , sk such '
             'that all of them are good. More formally, we have to find '
             'minimal by number of strings sequence of good strings s1, s2, . '
             '. . , sk such that their concatenation ( joining) equals s, i. '
             'e. s1+ s2+ ⋯+ sk= s. For example, cuttings 110010 into 110 and '
             '010 or into 11 and 0010 are valid, as 110, 010, 11, 0010 are all '
             "good, and we can' t cut 110010 to the smaller number of "
             "substrings as 110010 isn' t good itself. At the same time, "
             "cutting of 110010 into 1100 and 10 isn' t valid as both strings "
             "aren' t good. Also, cutting of 110010 into 1, 1, 0010 isn' t "
             "valid, as it isn' t minimal, even though all 3 strings are good. "
             'Can you help Keanu? We can show that the solution always exists. '
             'If there are multiple optimal answers, print any.',
  'input': 'The first line of the input contains a single integer n ( 1≤n≤100) '
           '— the length of the string s. The second line contains the string '
           's of length n consisting only from zeros and ones.',
  'note': "In the first example, the string 1 wasn' t cut at all. As it is "
          'good, the condition is satisfied. In the second example, 1 and 0 '
          "both are good. As 10 isn' t good, the answer is indeed minimal. In "
          "the third example, 100 and 011 both are good. As 100011 isn' t "
          'good, the answer is indeed minimal.',
  'output': 'In the first line, output a single integer k ( 1≤k) — a minimal '
            'number of strings you have cut s into. In the second line, output '
            'k strings s1, s2, . . . , sk separated with spaces. The length of '
            'each string has to be positive. Their concatenation has to be '
            'equal to s and all of them have to be good. If there are multiple '
            'answers, print any.',
  'title': 'Keanu Reeves',
  'topics': ['strings'],
  'url': 'https://codeforces.com/problemset/problem/1189/A'},
 {'history': 'You are given three strings s, t and p consisting of lowercase '
             'Latin letters. You may perform any number ( possibly, zero) '
             'operations on these strings. During each operation you choose '
             'any character from p, erase it from p and insert it into string '
             's ( you may insert this character anywhere you want: in the '
             'beginning of s, in the end or between any two consecutive '
             'characters) . For example, if p is aba, and s is de, then the '
             'following outcomes are possible ( the character we erase from p '
             'and insert into s is highlighted) : aba → ba, de → ade; aba → '
             'ba, de → dae; aba → ba, de → dea; aba → aa, de → bde; aba → aa, '
             'de → dbe; aba → aa, de → deb; aba → ab, de → ade; aba → ab, de → '
             'dae; aba → ab, de → dea; Your goal is to perform several ( maybe '
             'zero) operations so that s becomes equal to t. Please determine '
             'whether it is possible. Note that you have to answer q '
             'independent queries.',
  'input': 'The first line contains one integer q ( 1≤q≤100) — the number of '
           'queries. Each query is represented by three consecutive lines. The '
           'first line of each query contains the string s ( 1≤| s| ≤100) '
           'consisting of lowercase Latin letters. The second line of each '
           'query contains the string t ( 1≤| t| ≤100) consisting of lowercase '
           'Latin letters. The third line of each query contains the string p '
           '( 1≤| p| ≤100) consisting of lowercase Latin letters.',
  'note': 'In the first test case there is the following sequence of '
          'operation: s= ab, t= acxb, p= cax; s= acb, t= acxb, p= ax; s= acxb, '
          't= acxb, p= a. In the second test case there is the following '
          'sequence of operation: s= a, t= aaaa, p= aaabbcc; s= aa, t= aaaa, '
          'p= aabbcc; s= aaa, t= aaaa, p= abbcc; s= aaaa, t= aaaa, p= bbcc.',
  'output': 'For each query print YES if it is possible to make s equal to t, '
            'and NO otherwise. You may print every letter in any case you want '
            '( so, for example, the strings yEs, yes, Yes and YES will all be '
            'recognized as positive answer) .',
  'title': 'From S To T',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1194/C'},
 {'history': 'Amugae has a sentence consisting of n words. He want to compress '
             "this sentence into one word. Amugae doesn' t like repetitions, "
             'so when he merges two words into one word, he removes the '
             'longest prefix of the second word that coincides with a suffix '
             'of the first word. For example, he merges " sample" and " '
             'please" into " samplease" . Amugae will merge his sentence left '
             'to right ( i. e. first merge the first two words, then merge the '
             'result with the third word and so on) . Write a program that '
             'prints the compressed word after the merging process ends.',
  'input': 'The first line contains an integer n ( 1≤n≤105) , the number of '
           "the words in Amugae' s sentence. The second line contains n words "
           'separated by single space. Each words is non- empty and consists '
           "of uppercase and lowercase English letters and digits ( ' A' , ' "
           "B' , . . . , ' Z' , ' a' , ' b' , . . . , ' z' , ' 0' , ' 1' , . . "
           ". , ' 9' ) . The total length of the words does not exceed 106.",
  'note': ' ',
  'output': 'In the only line output the compressed word after the merging '
            'process ends as described in the problem.',
  'title': 'Compress Words',
  'topics': ['brute force',
             'hashing',
             'implementation',
             'string suffix structures',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1200/E'},
 {'history': 'A class of students wrote a multiple- choice test. There are n '
             'students in the class. The test had m questions, each of them '
             'had 5 possible answers ( A, B, C, D or E) . There is exactly one '
             'correct answer for each question. The correct answer for '
             'question i worth ai points. Incorrect answers are graded with '
             'zero points. The students remember what answers they gave on the '
             "exam, but they don' t know what are the correct answers. They "
             'are very optimistic, so they want to know what is the maximum '
             'possible total score of all students in the class.',
  'input': 'The first line contains integers n and m ( 1≤n, m≤1000) — the '
           'number of students in the class and the number of questions in the '
           'test. Each of the next n lines contains string si ( | si| = m) , '
           'describing an answer of the i- th student. The j- th character '
           'represents the student answer ( A, B, C, D or E) on the j- th '
           'question. The last line contains m integers a1, a2, . . . , am ( '
           '1≤ai≤1000) — the number of points for the correct answer for every '
           'question.',
  'note': 'In the first example, one of the most optimal test answers is " '
          'ABCD" , this way the total number of points will be 16. In the '
          'second example, one of the most optimal test answers is " CCC" , '
          'this way each question will be answered by exactly one student and '
          'the total number of points is 5+ 4+ 12= 21.',
  'output': 'Print a single integer — the maximum possible total score of the '
            'class.',
  'title': 'Important Exam',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1201/A'},
 {'history': 'You have a string ss — a sequence of commands for your toy '
             'robot. The robot is placed in some cell of a rectangular grid. '
             "He can perform four commands: ' W' — move one cell up; ' S' — "
             "move one cell down; ' A' — move one cell left; ' D' — move one "
             'cell right. Let Grid( s) Grid( s) be the grid of minimum '
             'possible area such that there is a position in the grid where '
             'you can place the robot in such a way that it will not fall from '
             'the grid while running the sequence of commands ss. For example, '
             'if s= DSAWWAWs= DSAWWAW then Grid( s) Grid( s) is the 4×34×3 '
             'grid: you can place the robot in the cell ( 3, 2) ( 3, 2) ; the '
             "robot performs the command ' D' and moves to ( 3, 3) ( 3, 3) ; "
             "the robot performs the command ' S' and moves to ( 4, 3) ( 4, 3) "
             "; the robot performs the command ' A' and moves to ( 4, 2) ( 4, "
             "2) ; the robot performs the command ' W' and moves to ( 3, 2) ( "
             "3, 2) ; the robot performs the command ' W' and moves to ( 2, 2) "
             "( 2, 2) ; the robot performs the command ' A' and moves to ( 2, "
             "1) ( 2, 1) ; the robot performs the command ' W' and moves to ( "
             "1, 1) ( 1, 1) . You have 44 extra letters: one ' W' , one ' A' , "
             "one ' S' , one ' D' . You' d like to insert at most one of these "
             'letters in any position of sequence ss to minimize the area of '
             'Grid( s) Grid( s) . What is the minimum area of Grid( s) Grid( '
             's) you can achieve?',
  'input': 'The first line contains one integer TT ( 1≤T≤10001≤T≤1000) — the '
           'number of queries. Next TT lines contain queries: one per line. '
           'This line contains single string ss ( 1≤| s| ≤2⋅1051≤| s| ≤2⋅105, '
           "si∈W, A, S, Dsi∈W, A, S, D) — the sequence of commands. It' s "
           "guaranteed that the total length of ss over all queries doesn' t "
           'exceed 2⋅1052⋅105.',
  'note': 'In the first query you have to get string DSAWWD_ AWDSAWWD⎯⎯⎯AW. In '
          'second and third queries you can not decrease the area of Grid( s) '
          'Grid( s) .',
  'output': 'Print TT integers: one per query. For each query print the '
            'minimum area of Grid( s) Grid( s) you can achieve.',
  'title': 'You Are Given a WASD-string...',
  'topics': ['brute force',
             'data structures',
             'dp',
             'greedy',
             'implementation',
             'math',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1202/C'},
 {'history': 'The subsequence is a sequence that can be derived from another '
             'sequence by deleting some elements without changing the order of '
             'the remaining elements. You are given an integer n. You have to '
             'find a sequence s consisting of digits 1, 3, 7 such that it has '
             'exactly n subsequences equal to 1337. For example, sequence '
             '337133377 has 6 subsequences equal to 1337: 3371_ 33_ 3_ 77_ ( '
             'you can remove the second and fifth characters) ; 3371_ 3_ 33_ '
             '77_ ( you can remove the third and fifth characters) ; 3371_ 3_ '
             '3_ 377_ ( you can remove the fourth and fifth characters) ; '
             '3371_ 33_ 3_ 7_ 7 ( you can remove the second and sixth '
             'characters) ; 3371_ 3_ 33_ 7_ 7 ( you can remove the third and '
             'sixth characters) ; 3371_ 3_ 3_ 37_ 7 ( you can remove the '
             'fourth and sixth characters) . Note that the length of the '
             'sequence s must not exceed 105. You have to answer t independent '
             'queries.',
  'input': 'The first line contains one integer t ( 1≤t≤10) — the number of '
           'queries. Next t lines contains a description of queries: the i- th '
           'line contains one integer ni ( 1≤ni≤109) .',
  'note': ' ',
  'output': 'For the i- th query print one string si ( 1≤| si| ≤105) '
            'consisting of digits 1, 3, 7. String si must have exactly ni '
            'subsequences 1337. If there are multiple such strings, print any '
            'of them.',
  'title': 'Print a 1337-string...',
  'topics': ['combinatorics', 'constructive algorithms', 'math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1202/D'},
 {'history': 'You are given a string t and n strings s1, s2, . . . , sn. All '
             'strings consist of lowercase Latin letters. Let f( t, s) be the '
             'number of occurences of string s in string t. For example, f( '
             '′aaabacaa′, ′aa′) = 3, and f( ′ababa′, ′aba′) = 2. Calculate the '
             'value of n∑i= 1n∑j= 1f( t, si+ sj) , where s+ t is the '
             'concatenation of strings s and t. Note that if there are two '
             'pairs i1, j1 and i2, j2 such that si1+ sj1= si2+ sj2, you should '
             'include both f( t, si1+ sj1) and f( t, si2+ sj2) in answer.',
  'input': 'The first line contains string t ( 1≤| t| ≤2⋅105) . The second '
           'line contains integer n ( 1≤n≤2⋅105) . Each of next n lines '
           'contains string si ( 1≤| si| ≤2⋅105) . It is guaranteed that n∑i= '
           '1| si| ≤2⋅105. All strings consist of lowercase English letters.',
  'note': ' ',
  'output': 'Print one integer — the value of n∑i= 1n∑j= 1f( t, si+ sj) .',
  'title': 'You Are Given Some Strings...',
  'topics': ['brute force', 'string suffix structures', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1202/E'},
 {'history': 'The only difference between easy and hard versions is the length '
             'of the string. You can hack this problem only if you solve both '
             'problems. Kirk has a binary string s ( a string which consists '
             'of zeroes and ones) of length n and he is asking you to find a '
             'binary string t of the same length which satisfies the following '
             'conditions: For any l and r ( 1≤l≤r≤n) the length of the longest '
             'non- decreasing subsequence of the substring slsl+ 1. . . sr is '
             'equal to the length of the longest non- decreasing subsequence '
             'of the substring tltl+ 1. . . tr; The number of zeroes in t is '
             'the maximum possible. A non- decreasing subsequence of a string '
             'p is a sequence of indices i1, i2, . . . , ik such that i1< i2< '
             '. . . < ik and pi1≤pi2≤. . . ≤pik. The length of the subsequence '
             'is k. If there are multiple substrings which satisfy the '
             'conditions, output any.',
  'input': 'The first line contains a binary string of length not more than '
           '2000.',
  'note': 'In the first example: For the substrings of the length 1 the length '
          'of the longest non- decreasing subsequnce is 1; For l= 1, r= 2 the '
          'longest non- decreasing subsequnce of the substring s1s2 is 11 and '
          'the longest non- decreasing subsequnce of the substring t1t2 is 01; '
          'For l= 1, r= 3 the longest non- decreasing subsequnce of the '
          'substring s1s3 is 11 and the longest non- decreasing subsequnce of '
          'the substring t1t3 is 00; For l= 2, r= 3 the longest non- '
          'decreasing subsequnce of the substring s2s3 is 1 and the longest '
          'non- decreasing subsequnce of the substring t2t3 is 1; The second '
          'example is similar to the first one.',
  'output': 'Output a binary string which satisfied the above conditions. If '
            'there are many such strings, output any of them.',
  'title': 'Kirk and a Binary String (easy version)',
  'topics': ['brute force', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1204/D1'},
 {'history': 'The only difference between easy and hard versions is the length '
             'of the string. You can hack this problem if you solve it. But '
             'you can hack the previous problem only if you solve both '
             'problems. Kirk has a binary string s ( a string which consists '
             'of zeroes and ones) of length n and he is asking you to find a '
             'binary string t of the same length which satisfies the following '
             'conditions: For any l and r ( 1≤l≤r≤n) the length of the longest '
             'non- decreasing subsequence of the substring slsl+ 1. . . sr is '
             'equal to the length of the longest non- decreasing subsequence '
             'of the substring tltl+ 1. . . tr; The number of zeroes in t is '
             'the maximum possible. A non- decreasing subsequence of a string '
             'p is a sequence of indices i1, i2, . . . , ik such that i1< i2< '
             '. . . < ik and pi1≤pi2≤. . . ≤pik. The length of the subsequence '
             'is k. If there are multiple substrings which satisfy the '
             'conditions, output any.',
  'input': 'The first line contains a binary string of length not more than '
           '105.',
  'note': 'In the first example: For the substrings of the length 1 the length '
          'of the longest non- decreasing subsequnce is 1; For l= 1, r= 2 the '
          'longest non- decreasing subsequnce of the substring s1s2 is 11 and '
          'the longest non- decreasing subsequnce of the substring t1t2 is 01; '
          'For l= 1, r= 3 the longest non- decreasing subsequnce of the '
          'substring s1s3 is 11 and the longest non- decreasing subsequnce of '
          'the substring t1t3 is 00; For l= 2, r= 3 the longest non- '
          'decreasing subsequnce of the substring s2s3 is 1 and the longest '
          'non- decreasing subsequnce of the substring t2t3 is 1; The second '
          'example is similar to the first one.',
  'output': 'Output a binary string which satisfied the above conditions. If '
            'there are many such strings, output any of them.',
  'title': 'Kirk and a Binary String (hard version)',
  'topics': ['data structures', 'greedy', 'math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1204/D2'},
 {'history': "You are given integers n, k. Let' s consider the alphabet "
             'consisting of k different elements. Let beauty f( s) of the '
             'string s be the number of indexes i, 1≤i< | s| , for which '
             'prefix of s of length i equals to suffix of s of length i. For '
             'example, beauty of the string abacaba equals 2, as for i= 1, 3 '
             'prefix and suffix of length i are equal. Consider all words of '
             'length n in the given alphabet. Find the expected value of f( s) '
             '2 of a uniformly chosen at random word. We can show that it can '
             "be expressed as PQ, where P and Q are coprime and Q isn' t "
             'divided by 109+ 7. Output P⋅Q−1mod109+ 7.',
  'input': 'The first and the only line contains two integers n, k ( 1≤n≤105, '
           '1≤k≤109) — the length of a string and the size of alphabet '
           'respectively.',
  'note': 'In the first example, there are 9 words of length 2 in alphabet of '
          'size 3 — aa, ab, ac, ba, bb, bc, ca, cb, cc. 3 of them have beauty '
          '1 and 6 of them have beauty 0, so the average value is 13. In the '
          'third example, there is only one such word, and it has beauty 99, '
          'so the average value is 992.',
  'output': 'Output a single integer — P×Q−1mod109+ 7.',
  'title': 'Expected Value Again',
  'topics': ['combinatorics', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1205/E'},
 {'history': "Mishka' s favourite experimental indie band has recently dropped "
             'a new album! Songs of that album share one gimmick. Each name si '
             'is one of the following types: 1 c — a single lowercase Latin '
             'letter; 2 j c — name sj ( 1≤j< i) with a single lowercase Latin '
             "letter appended to its end. Songs are numbered from 1 to n. It' "
             's guaranteed that the first song is always of type 1. Vova is '
             "rather interested in the new album but he really doesn' t have "
             'the time to listen to it entirely. Thus he asks Mishka some '
             'questions about it to determine if some song is worth listening '
             'to. Questions have the following format: i t — count the number '
             'of occurrences of string t in si ( the name of the i- th song of '
             'the album) as a continuous substring, t consists only of '
             "lowercase Latin letters. Mishka doesn' t question the purpose of "
             'that information, yet he struggles to provide it. Can you please '
             "help Mishka answer all Vova' s questions?",
  'input': 'The first line contains a single integer n ( 1≤n≤4⋅105) — the '
           'number of songs in the album. Each of the next n lines contains '
           'the desciption of the i- th song of the album in the following '
           'format: 1 c — si is a single lowercase Latin letter; 2 j c — si is '
           'the name sj ( 1≤j< i) with a single lowercase Latin letter '
           'appended to its end. The next line contains a single integer m ( '
           "1≤m≤4⋅105) — the number of Vova' s questions. Each of the next m "
           "lines contains the desciption of the j- th Vova' s question in the "
           'following format: i t ( 1≤i≤n, 1≤| t| ≤4⋅105) — count the number '
           'of occurrences of string t in si ( the name of the i- th song of '
           'the album) as a continuous substring, t consists only of lowercase '
           "Latin letters. It' s guaranteed that the total length of question "
           "strings t doesn' t exceed 4⋅105.",
  'note': 'Song names of the first example: d da dad dada dadad dadada dadadad '
          'dadadada d do dok doki dokid dokido dokidok dokidoki do dok doki '
          'dokidoki Thus the occurrences for each question string are: string '
          '" da" starts in positions [ 1, 3, 5, 7] in the name " dadadada" ; '
          'string " dada" starts in positions [ 1, 3, 5] in the name " '
          'dadadada" ; string " ada" starts in positions [ 2, 4, 6] in the '
          'name " dadadada" ; string " dada" starts in positions [ 1, 3] in '
          'the name " dadada" ; no occurrences of string " dada" in the name " '
          'dad" ; string " doki" starts in position [ 1] in the name " doki" ; '
          'string " ok" starts in position [ 2] in the name " doki" ; string " '
          'doki" starts in positions [ 1, 5] in the name " dokidoki" ; string '
          '" doki" starts in position [ 1] in the name " dokidok" ; string " '
          'd" starts in position [ 1] in the name " d" ; no occurrences of '
          'string " a" in the name " d" ; string " doki" starts in positions [ '
          '1, 5] in the name " dokidoki" .',
  'output': 'For each question print a single integer — the number of '
            'occurrences of the question string t in the name of the i- th '
            'song of the album as a continuous substring.',
  'title': 'Indie Album',
  'topics': ['data structures',
             'dfs and similar',
             'hashing',
             'string suffix structures',
             'strings',
             'trees'],
  'url': 'https://codeforces.com/problemset/problem/1207/G'},
 {'history': 'Koala Land consists of m bidirectional roads connecting n '
             'cities. The roads are numbered from 1 to m by order in input. It '
             'is guaranteed, that one can reach any city from every other '
             'city. Koala starts traveling from city 1. Whenever he travels on '
             "a road, he writes its number down in his notebook. He doesn' t "
             'put spaces between the numbers, so they all get concatenated '
             'into a single number. Before embarking on his trip, Koala is '
             'curious about the resulting number for all possible '
             'destinations. For each possible destination, what is the '
             'smallest number he could have written for it? Since these '
             'numbers may be quite large, print their remainders modulo 109+ '
             '7. Please note, that you need to compute the remainder of the '
             'minimum possible number, not the minimum possible remainder.',
  'input': 'The first line contains two integers n and m ( 2≤n≤105, n−1≤m≤105) '
           ', the number of cities and the number of roads, respectively. The '
           'i- th of the following m lines contains integers xi and yi ( 1≤xi, '
           'yi≤n, xi= ̸yi) , representing a bidirectional road between cities '
           'xi and yi. It is guaranteed, that for any pair of cities there is '
           'at most one road connecting them, and that one can reach any city '
           'from every other city.',
  'note': ' ',
  'output': 'Print n−1 integers, the answer for every city except for the '
            'first city. The i- th integer should be equal to the smallest '
            'number he could have written for destination i+ 1. Since this '
            'number may be large, output its remainder modulo 109+ 7.',
  'title': 'Koala and Notebook',
  'topics': ['data structures',
             'dfs and similar',
             'graphs',
             'shortest paths',
             'strings',
             'trees'],
  'url': 'https://codeforces.com/problemset/problem/1209/F'},
 {'history': 'Polycarp really likes writing the word " kotlin" . He wrote this '
             'word several times in a row without spaces. For example, he '
             'could write the string like " kotlinkotlinkotlinkotlin" . '
             'Polycarp sliced ( cut) the written string into n pieces and '
             'mixed them. As a result, he has n strings s1, s2, . . . , sn and '
             'he can arrange them in the right order, concatenate ( join) all '
             'of them and get a string like " kotlinkotlin. . . kotlin" . Help '
             'Polycarp to find the right order of strings s1, s2, . . . , sn, '
             'so that if he writes the strings in this order, he will get the '
             'word " kotlin" or the sequence of this word. Pay attention that '
             'you must use all given strings and you must use each string only '
             'once.',
  'input': 'The first line of the input contains one integer n ( 1≤n≤105) — '
           "the number of Polycarp' s strings. Next lines of the input contain "
           "n Polycarp' s strings. Total sum of their lengths doesn' t exceed "
           "3⋅105. It' s guaranteed that there is the right order of "
           'arrangement the strings that if you concatenate them into one '
           'string, you will get some non- empty sequence of the word " '
           'kotlin" .',
  'note': ' ',
  'output': 'Print n different integers p1, p2, . . . , pn ( 1≤pi≤n) , where '
            'pi is an index of the string that should be the i- th in a '
            'required concatenation. In other words, the result of '
            'concatenation sp1+ sp2+ ⋯+ spn must be in the form " '
            'kotlinkotlin. . . kotlin" . If there are many solutions, print '
            'any of them.',
  'title': 'kotlinkotlinkotlinkotlin...',
  'topics': ['*special', 'graphs', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1211/F'},
 {'history': 'Authors have come up with the string s consisting of n lowercase '
             'Latin letters. You are given two permutations of its indices ( '
             'not necessary equal) p and q ( both of length n) . Recall that '
             'the permutation is the array of length n which contains each '
             'integer from 1 to n exactly once. For all i from 1 to n−1 the '
             'following properties hold: s[ pi] ≤s[ pi+ 1] and s[ qi] ≤s[ qi+ '
             '1] . It means that if you will write down all characters of s in '
             'order of permutation indices, the resulting string will be '
             'sorted in the non- decreasing order. Your task is to restore any '
             'such string s of length n consisting of at least k distinct '
             'lowercase Latin letters which suits the given permutations. If '
             'there are multiple answers, you can print any of them.',
  'input': 'The first line of the input contains two integers n and k ( '
           '1≤n≤2⋅105, 1≤k≤26) — the length of the string and the number of '
           'distinct characters required. The second line of the input '
           'contains n integers p1, p2, . . . , pn ( 1≤pi≤n, all pi are '
           'distinct integers from 1 to n) — the permutation p. The third line '
           'of the input contains n integers q1, q2, . . . , qn ( 1≤qi≤n, all '
           'qi are distinct integers from 1 to n) — the permutation q.',
  'note': ' ',
  'output': 'If it is impossible to find the suitable string, print " NO" on '
            'the first line. Otherwise print " YES" on the first line and '
            'string s on the second line. It should consist of n lowercase '
            'Latin letters, contain at least k distinct characters and suit '
            'the given permutations. If there are multiple answers, you can '
            'print any of them.',
  'title': 'Unstable String Sort',
  'topics': ['data structures',
             'dfs and similar',
             'dsu',
             'graphs',
             'greedy',
             'implementation',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1213/F'},
 {'history': 'Nikolay got a string s of even length n, which consists only of '
             "lowercase Latin letters ' a' and ' b' . Its positions are "
             'numbered from 1 to n. He wants to modify his string so that '
             "every its prefix of even length has an equal amount of letters ' "
             "a' and ' b' . To achieve that, Nikolay can perform the following "
             'operation arbitrary number of times ( possibly, zero) : choose '
             'some position in his string and replace the letter on this '
             "position with the other letter ( i. e. replace ' a' with ' b' or "
             "replace ' b' with ' a' ) . Nikolay can use no letters except ' "
             "a' and ' b' . The prefix of string s of length l ( 1≤l≤n) is a "
             'string s[ 1. . l] . For example, for the string s= " abba" there '
             'are two prefixes of the even length. The first is s[ 1. . . 2] = '
             '" ab" and the second s[ 1. . . 4] = " abba" . Both of them have '
             "the same number of ' a' and ' b' . Your task is to calculate the "
             'minimum number of operations Nikolay has to perform with the '
             'string s to modify it so that every its prefix of even length '
             "has an equal amount of letters ' a' and ' b' .",
  'input': 'The first line of the input contains one even integer n ( '
           '2≤n≤2⋅105) — the length of string s. The second line of the input '
           'contains the string s of length n, which consists only of '
           "lowercase Latin letters ' a' and ' b' .",
  'note': 'In the first example Nikolay has to perform two operations. For '
          "example, he can replace the first ' b' with ' a' and the last ' b' "
          "with ' a' . In the second example Nikolay doesn' t need to do "
          'anything because each prefix of an even length of the initial '
          "string already contains an equal amount of letters ' a' and ' b' .",
  'output': 'In the first line print the minimum number of operations Nikolay '
            'has to perform with the string s to modify it so that every its '
            "prefix of even length has an equal amount of letters ' a' and ' "
            "b' . In the second line print the string Nikolay obtains after "
            'applying all the operations. If there are multiple answers, you '
            'can print any of them.',
  'title': 'Prefixes',
  'topics': ['strings'],
  'url': 'https://codeforces.com/problemset/problem/1216/A'},
 {'history': 'Alice became interested in periods of integer numbers. We say '
             'positive X integer number is periodic with length L if there '
             'exists positive integer number P with L digits such that X can '
             'be written as PPPP. . . P. For example: X= 123123123 is periodic '
             'number with length L= 3 and L= 9X= 42424242 is periodic number '
             'with length L= 2, L= 4 and L= 8X= 12345 is periodic number with '
             'length L= 5For given positive period length L and positive '
             'integer number A, Alice wants to find smallest integer number X '
             'strictly greater than A that is periodic with length L.',
  'input': 'First line contains one positive integer number L ( 1≤L≤105) '
           'representing length of the period. Second line contains one '
           'positive integer number A ( 1≤A≤10100000) .',
  'note': 'In first example 124124 is the smallest number greater than 123456 '
          'that can be written with period L = 3 ( P = 124) . In the second '
          'example 100100 is the smallest number greater than 12345 with '
          'period L = 3 ( P= 100)',
  'output': 'One positive integer number representing smallest positive number '
            'that is periodic with length L and is greater than A.',
  'title': 'Periodic integer number',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1219/C'},
 {'history': 'When Serezha was three years old, he was given a set of cards '
             'with letters for his birthday. They were arranged into words in '
             "the way which formed the boy' s mother favorite number in binary "
             'notation. Serezha started playing with them immediately and '
             "shuffled them because he wasn' t yet able to read. His father "
             'decided to rearrange them. Help him restore the original number, '
             'on condition that it was the maximum possible one.',
  'input': 'The first line contains a single integer n ( 1⩽) — the length of '
           'the string. The second line contains a string consisting of '
           "English lowercase letters: ' z' , ' e' , ' r' , ' o' and ' n' . It "
           'is guaranteed that it is possible to rearrange the letters in such '
           'a way that they form a sequence of words, each being either " '
           'zero" which corresponds to the digit 0 or " one" which corresponds '
           'to the digit 1.',
  'note': 'In the first example, the correct initial ordering is " zero" . In '
          'the second example, the correct initial ordering is " oneonezero" .',
  'output': 'Print the maximum possible number in binary notation. Print '
            'binary digits separated by a space. The leading zeroes are '
            'allowed.',
  'title': 'Cards',
  'topics': ['implementation', 'sortings', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1220/A'},
 {'history': 'Mike and Ann are sitting in the classroom. The lesson is boring, '
             'so they decided to play an interesting game. Fortunately, all '
             'they need to play this game is a string s and a number k ( 0≤k< '
             '| s| ) . At the beginning of the game, players are given a '
             'substring of s with left border l and right border r, both equal '
             'to k ( i. e. initially l= r= k) . Then players start to make '
             'moves one by one, according to the following rules: A player '
             'chooses l′ and r′ so that l′≤l, r′≥r and s[ l′, r′] is '
             'lexicographically less than s[ l, r] . Then the player changes l '
             'and r in this way: l: = l′, r: = r′. Ann moves first. The '
             "player, that can' t make a move loses. Recall that a substring "
             's[ l, r] ( l≤r) of a string s is a continuous segment of letters '
             'from s that starts at position l and ends at position r. For '
             'example, " ehn" is a substring ( s[ 3, 5] ) of " aaaehnsvz" and '
             '" ahz" is not. Mike and Ann were playing so enthusiastically '
             'that they did not notice the teacher approached them. '
             "Surprisingly, the teacher didn' t scold them, instead of that he "
             'said, that he can figure out the winner of the game before it '
             'starts, even if he knows only s and k. Unfortunately, Mike and '
             'Ann are not so keen in the game theory, so they ask you to write '
             'a program, that takes s and determines the winner for all '
             'possible k.',
  'input': 'The first line of the input contains a single string s ( 1≤| s| '
           '≤5⋅105) consisting of lowercase English letters.',
  'note': ' ',
  'output': 'Print | s| lines. In the line i write the name of the winner ( '
            'print Mike or Ann) in the game with string s and k= i, if both '
            'play optimally',
  'title': 'Substring Game in the Lesson',
  'topics': ['games', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1220/C'},
 {'history': 'You are given two strings of equal length s and t consisting of '
             'lowercase Latin letters. You may perform any number ( possibly, '
             'zero) operations on these strings. During each operation you '
             'choose two adjacent characters in any string and assign the '
             'value of the first character to the value of the second or vice '
             'versa. For example, if s is " acbc" you can get the following '
             'strings in one operation: " aabc" ( if you perform s2= s1) ; " '
             'ccbc" ( if you perform s1= s2) ; " accc" ( if you perform s3= s2 '
             'or s3= s4) ; " abbc" ( if you perform s2= s3) ; " acbb" ( if you '
             'perform s4= s3) ; Note that you can also apply this operation to '
             'the string t. Please determine whether it is possible to '
             'transform s into t, applying the operation above any number of '
             'times. Note that you have to answer q independent queries.',
  'input': 'The first line contains one integer q ( 1≤q≤100) — the number of '
           'queries. Each query is represented by two consecutive lines. The '
           'first line of each query contains the string s ( 1≤| s| ≤100) '
           'consisting of lowercase Latin letters. The second line of each '
           'query contains the string t ( 1≤| t| ≤100, | t| = | s| ) '
           'consisting of lowercase Latin letters.',
  'note': 'In the first query, you can perform two operations s1= s2 ( after '
          'it s turns into " aabb" ) and t4= t3 ( after it t turns into " '
          'aabb" ) . In the second query, the strings are equal initially, so '
          'the answer is " YES" . In the third query, you can not make strings '
          's and t equal. Therefore, the answer is " NO" .',
  'output': 'For each query, print " YES" if it is possible to make s equal to '
            't, and " NO" otherwise. You may print every letter in any case '
            'you want ( so, for example, the strings " yEs" , " yes" , " Yes" '
            ', and " YES" will all be recognized as positive answer) .',
  'title': 'Strings Equalization',
  'topics': ['strings'],
  'url': 'https://codeforces.com/problemset/problem/1223/B'},
 {'history': 'The problem was inspired by Pied Piper story. After a challenge '
             "from Hooli' s compression competitor Nucleus, Richard pulled an "
             'all- nighter to invent a new approach to compression: middle- '
             'out. You are given two strings ss and tt of the same length nn. '
             'Their characters are numbered from 11 to nn from left to right ( '
             'i. e. from the beginning to the end) . In a single move you can '
             'do the following sequence of actions: choose any valid index ii '
             '( 1≤i≤n1≤i≤n) , move the ii- th character of ss from its '
             'position to the beginning of the string or move the ii- th '
             'character of ss from its position to the end of the string. '
             "Note, that the moves don' t change the length of the string ss. "
             'You can apply a move only to the string ss. For example, if s= '
             's= " test" in one move you can obtain: if i= 1i= 1 and you move '
             'to the beginning, then the result is " test" ( the string '
             "doesn' t change) , if i= 2i= 2 and you move to the beginning, "
             'then the result is " etst" , if i= 3i= 3 and you move to the '
             'beginning, then the result is " stet" , if i= 4i= 4 and you move '
             'to the beginning, then the result is " ttes" , if i= 1i= 1 and '
             'you move to the end, then the result is " estt" , if i= 2i= 2 '
             'and you move to the end, then the result is " tste" , if i= 3i= '
             '3 and you move to the end, then the result is " tets" , if i= '
             '4i= 4 and you move to the end, then the result is " test" ( the '
             "string doesn' t change) . You want to make the string ss equal "
             'to the string tt. What is the minimum number of moves you need? '
             'If it is impossible to transform ss to tt, print - 1.',
  'input': 'The first line contains integer qq ( 1≤q≤1001≤q≤100) — the number '
           'of independent test cases in the input. Each test case is given in '
           'three lines. The first line of a test case contains nn ( '
           '1≤n≤1001≤n≤100) — the length of the strings ss and tt. The second '
           'line contains ss, the third line contains tt. Both strings ss and '
           'tt have length nn and contain only lowercase Latin letters. There '
           'are no constraints on the sum of nn in the test ( i. e. the input '
           'with q= 100q= 100 and all n= 100n= 100 is allowed) .',
  'note': 'In the first example, the moves in one of the optimal answers are: '
          'for the first test case s= s= " iredppipe" , t= t= " piedpiper" : " '
          'iredppipe" →→ " iedppiper" →→ " piedpiper" ; for the second test '
          'case s= s= " estt" , t= t= " test" : " estt" →→ " test" ; for the '
          'third test case s= s= " tste" , t= t= " test" : " tste" →→ " etst" '
          '→→ " test" .',
  'output': 'For every test print minimum possible number of moves, which are '
            'needed to transform ss into tt, or - 1, if it is impossible to '
            'do.',
  'title': 'Middle-Out',
  'topics': ['constructive algorithms', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1231/E'},
 {'history': 'The string t1t2. . . tk is good if each letter of this string '
             'belongs to at least one palindrome of length greater than 1. A '
             'palindrome is a string that reads the same backward as forward. '
             'For example, the strings A, BAB, ABBA, BAABBBAAB are '
             'palindromes, but the strings AB, ABBBAA, BBBA are not. Here are '
             'some examples of good strings: t = AABBB ( letters t1, t2 belong '
             'to palindrome t1. . . t2 and letters t3, t4, t5 belong to '
             'palindrome t3. . . t5) ; t = ABAA ( letters t1, t2, t3 belong to '
             'palindrome t1. . . t3 and letter t4 belongs to palindrome t3. . '
             '. t4) ; t = AAAAA ( all letters belong to palindrome t1. . . t5) '
             '; You are given a string s of length n, consisting of only '
             'letters A and B. You have to calculate the number of good '
             'substrings of string s.',
  'input': 'The first line contains one integer n ( 1≤n≤3⋅105) — the length of '
           'the string s. The second line contains the string s, consisting of '
           'letters A and B.',
  'note': 'In the first test case there are six good substrings: s1. . . s2, '
          's1. . . s4, s1. . . s5, s3. . . s4, s3. . . s5 and s4. . . s5. In '
          'the second test case there are three good substrings: s1. . . s2, '
          's1. . . s3 and s2. . . s3.',
  'output': 'Print one integer — the number of good substrings of string s.',
  'title': 'AB-string',
  'topics': ['binary search', 'combinatorics', 'dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1238/D'},
 {'history': 'This problem is different from the hard version. In this version '
             'Ujan makes exactly one exchange. You can hack this problem only '
             'if you solve both problems. After struggling and failing many '
             'times, Ujan decided to try to clean up his house again. He '
             'decided to get his strings in order first. Ujan has two distinct '
             'strings s and t of length n consisting of only of lowercase '
             'English characters. He wants to make them equal. Since Ujan is '
             'lazy, he will perform the following operation exactly once: he '
             'takes two positions i and j ( 1≤i, j≤n, the values i and j can '
             'be equal or different) , and swaps the characters si and tj. Can '
             'he succeed? Note that he has to perform this operation exactly '
             'once. He has to perform this operation.',
  'input': 'The first line contains a single integer k ( 1≤k≤10) , the number '
           'of test cases. For each of the test cases, the first line contains '
           'a single integer n ( 2≤n≤104) , the length of the strings s and t. '
           'Each of the next two lines contains the strings s and t, each '
           'having length exactly n. The strings consist only of lowercase '
           'English letters. It is guaranteed that strings are different.',
  'note': 'In the first test case, Ujan can swap characters s1 and t4, '
          'obtaining the word " house" . In the second test case, it is not '
          'possible to make the strings equal using exactly one swap of si and '
          'tj.',
  'output': 'For each test case, output " Yes" if Ujan can make the two '
            'strings equal and " No" otherwise. You can print each letter in '
            'any case ( upper or lower) .',
  'title': 'Character Swap (Easy Version)',
  'topics': ['strings'],
  'url': 'https://codeforces.com/problemset/problem/1243/B1'},
 {'history': 'This problem is different from the easy version. In this version '
             'Ujan makes at most 2n swaps. In addition, k≤1000, n≤50 and it is '
             'necessary to print swaps themselves. You can hack this problem '
             'if you solve it. But you can hack the previous problem only if '
             'you solve both problems. After struggling and failing many '
             'times, Ujan decided to try to clean up his house again. He '
             'decided to get his strings in order first. Ujan has two distinct '
             'strings s and t of length n consisting of only of lowercase '
             'English characters. He wants to make them equal. Since Ujan is '
             'lazy, he will perform the following operation at most 2n times: '
             'he takes two positions i and j ( 1≤i, j≤n, the values i and j '
             'can be equal or different) , and swaps the characters si and tj. '
             "Ujan' s goal is to make the strings s and t equal. He does not "
             'need to minimize the number of performed operations: any '
             'sequence of operations of length 2n or shorter is suitable.',
  'input': 'The first line contains a single integer k ( 1≤k≤1000) , the '
           'number of test cases. For each of the test cases, the first line '
           'contains a single integer n ( 2≤n≤50) , the length of the strings '
           's and t. Each of the next two lines contains the strings s and t, '
           'each having length exactly n. The strings consist only of '
           'lowercase English letters. It is guaranteed that strings are '
           'different.',
  'note': ' ',
  'output': 'For each test case, output " Yes" if Ujan can make the two '
            'strings equal with at most 2n operations and " No" otherwise. You '
            'can print each letter in any case ( upper or lower) . In the case '
            'of " Yes" print m ( 1≤m≤2n) on the next line, where m is the '
            'number of swap operations to make the strings equal. Then print m '
            'lines, each line should contain two integers i, j ( 1≤i, j≤n) '
            'meaning that Ujan swaps si and tj during the corresponding '
            'operation. You do not need to minimize the number of operations. '
            'Any sequence of length not more than 2n is suitable.',
  'title': 'Character Swap (Hard Version)',
  'topics': ['strings'],
  'url': 'https://codeforces.com/problemset/problem/1243/B2'},
 {'history': 'Recently Polycarp noticed that some of the buttons of his '
             'keyboard are malfunctioning. For simplicity, we assume that '
             "Polycarp' s keyboard contains 26 buttons ( one for each letter "
             'of the Latin alphabet) . Each button is either working fine or '
             'malfunctioning. To check which buttons need replacement, '
             'Polycarp pressed some buttons in sequence, and a string s '
             'appeared on the screen. When Polycarp presses a button with '
             'character c, one of the following events happened: if the button '
             'was working correctly, a character c appeared at the end of the '
             'string Polycarp was typing; if the button was malfunctioning, '
             'two characters c appeared at the end of the string. For example, '
             'suppose the buttons corresponding to characters a and c are '
             'working correctly, and the button corresponding to b is '
             'malfunctioning. If Polycarp presses the buttons in the order a, '
             'b, a, c, a, b, a, then the string he is typing changes as '
             'follows: a → abb → abba → abbac → abbaca → abbacabb → abbacabba. '
             'You are given a string s which appeared on the screen after '
             'Polycarp pressed some buttons. Help Polycarp to determine which '
             'buttons are working correctly for sure ( that is, this string '
             'could not appear on the screen if any of these buttons was '
             "malfunctioning) . You may assume that the buttons don' t start "
             'malfunctioning when Polycarp types the string: each button '
             'either works correctly throughout the whole process, or '
             'malfunctions throughout the whole process.',
  'input': 'The first line contains one integer t ( 1≤t≤100) — the number of '
           'test cases in the input. Then the test cases follow. Each test '
           'case is represented by one line containing a string s consisting '
           'of no less than 1 and no more than 500 lowercase Latin letters.',
  'note': ' ',
  'output': 'For each test case, print one line containing a string res. The '
            'string res should contain all characters which correspond to '
            'buttons that work correctly in alphabetical order, without any '
            'separators or repetitions. If all buttons may malfunction, res '
            'should be empty.',
  'title': 'Broken Keyboard',
  'topics': ['brute force', 'strings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1251/A'},
 {'history': 'A palindrome is a string t which reads the same backward as '
             'forward ( formally, t[ i] = t[ | t| + 1−i] for all i∈[ 1, | t| ] '
             ') . Here | t| denotes the length of a string t. For example, the '
             'strings 010, 1001 and 0 are palindromes. You have n binary '
             'strings s1, s2, . . . , sn ( each si consists of zeroes and/ or '
             'ones) . You can swap any pair of characters any number of times '
             '( possibly, zero) . Characters can be either from the same '
             'string or from different strings — there are no restrictions. '
             'Formally, in one move you: choose four integer numbers x, a, y, '
             'b such that 1≤x, y≤n and 1≤a≤| sx| and 1≤b≤| sy| ( where x and y '
             'are string indices and a and b are positions in strings sx and '
             'sy respectively) , swap ( exchange) the characters sx[ a] and '
             'sy[ b] . What is the maximum number of strings you can make '
             'palindromic simultaneously?',
  'input': 'The first line contains single integer Q ( 1≤Q≤50) — the number of '
           'test cases. The first line on each test case contains single '
           'integer n ( 1≤n≤50) — the number of binary strings you have. Next '
           'n lines contains binary strings s1, s2, . . . , sn — one per line. '
           "It' s guaranteed that 1≤| si| ≤50 and all strings constist of "
           'zeroes and/ or ones.',
  'note': 'In the first test case, s1 is palindrome, so the answer is 1. In '
          "the second test case you can' t make all three strings palindromic "
          'at the same time, but you can make any pair of strings palindromic. '
          "For example, let' s make s1= 0110, s2= 111111 and s3= 010000. In "
          'the third test case we can make both strings palindromic. For '
          'example, s1= 11011 and s2= 100001. In the last test case s2 is '
          'palindrome and you can make s1 palindrome, for example, by swapping '
          's1[ 2] and s1[ 3] .',
  'output': 'Print Q integers — one per test case. The i- th integer should be '
            'the maximum number of palindromic strings you can achieve '
            'simultaneously performing zero or more swaps on strings from the '
            'i- th test case.',
  'title': 'Binary Palindromes',
  'topics': ['greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1251/B'},
 {'history': 'You have a grid G containing R rows ( numbered from 1 to R, top '
             'to bottom) and C columns ( numbered from 1 to C, left to right) '
             'of uppercase characters. The character in the rth row and the '
             'cth column is denoted by Gr, c. You also have Q strings '
             'containing uppercase characters. For each of the string, you '
             'want to find the number of occurrences of the string in the '
             'grid. An occurrence of string S in the grid is counted if S can '
             'be constructed by starting at one of the cells in the grid, '
             'going right 0 or more times, and then going down 0 or more '
             'times. Two occurrences are different if the set of cells used to '
             'construct the string is different. Formally, for each string S, '
             'you would like to count the number of tuples ⟨r, c, Δr, Δc⟩ such '
             'that: 1≤r≤R and r≤r+ Δr≤R 1≤c≤C and c≤c+ Δc≤C S= Gr, cGr, c+ 1. '
             '. . Gr, c+ ΔcGr+ 1, c+ Δc. . . Gr+ Δr, c+ Δc',
  'input': 'Input begins with a line containing three integers: R C Q ( 1≤R, '
           'C≤500; 1≤Q≤200000) representing the size of the grid and the '
           'number of strings, respectively. The next R lines each contains C '
           'uppercase characters representing the grid. The cth character on '
           'the rth line is Gr, c. The next Q lines each contains a string S '
           'containing uppercase characters. The length of this string is a '
           'positive integer not more than 200000. The sum of the length of '
           'all Q strings combined is not more than 200000.',
  'note': 'Explanation for the sample input/ output # 1 There are 2 '
          'occurrences of " ABC" , represented by the tuples ⟨1, 1, 1, 1⟩ and '
          '⟨1, 1, 0, 2⟩. There are 3 occurrences of " BC" , represented by the '
          'tuples ⟨1, 2, 0, 1⟩, ⟨1, 2, 1, 0⟩, and ⟨2, 1, 0, 1⟩. There is 1 '
          'occurrence of " BD" , represented by the tuple ⟨2, 1, 1, 0⟩. There '
          'is no occurrence of " AC" . There are 2 occurrences of " A" , '
          'represented by the tuples ⟨1, 1, 0, 0⟩ and ⟨3, 2, 0, 0⟩.',
  'output': 'For each query in the same order as input, output in a line an '
            'integer representing the number of occurrences of the string in '
            'the grid.',
  'title': 'Find String in a Grid',
  'topics': ['data structures', 'dp', 'strings', 'trees'],
  'url': 'https://codeforces.com/problemset/problem/1252/D'},
 {'history': 'You are given two strings s and t both of length n and both '
             'consisting of lowercase Latin letters. In one move, you can '
             'choose any length len from 1 to n and perform the following '
             'operation: Choose any contiguous substring of the string s of '
             'length len and reverse it; at the same time choose any '
             'contiguous substring of the string t of length len and reverse '
             'it as well. Note that during one move you reverse exactly one '
             'substring of the string s and exactly one substring of the '
             'string t. Also note that borders of substrings you reverse in s '
             'and in t can be different, the only restriction is that you '
             'reverse the substrings of equal length. For example, if len= 3 '
             'and n= 5, you can reverse s[ 1. . . 3] and t[ 3. . . 5] , s[ 2. '
             '. . 4] and t[ 2. . . 4] , but not s[ 1. . . 3] and t[ 1. . . 2] '
             '. Your task is to say if it is possible to make strings s and t '
             'equal after some ( possibly, empty) sequence of moves. You have '
             'to answer q independent test cases.',
  'input': 'The first line of the input contains one integer q ( 1≤q≤104) — '
           'the number of test cases. Then q test cases follow. The first line '
           'of the test case contains one integer n ( 1≤n≤2⋅105) — the length '
           'of s and t. The second line of the test case contains one string s '
           'consisting of n lowercase Latin letters. The third line of the '
           'test case contains one string t consisting of n lowercase Latin '
           'letters. It is guaranteed that the sum of n over all test cases '
           'does not exceed 2⋅105 ( ∑n≤2⋅105) .',
  'note': ' ',
  'output': 'For each test case, print the answer on it — " YES" ( without '
            'quotes) if it is possible to make strings s and t equal after '
            'some ( possibly, empty) sequence of moves and " NO" otherwise.',
  'title': 'Equalizing Two Strings',
  'topics': ['constructive algorithms', 'sortings', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1256/F'},
 {'history': "Let' s call an array t dominated by value v in the next "
             'situation. At first, array t should have at least 2 elements. '
             "Now, let' s calculate number of occurrences of each number num "
             'in t and define it as occ( num) . Then t is dominated ( by v) if '
             '( and only if) occ( v) > occ( v′) for any other number v′. For '
             'example, arrays [ 1, 2, 3, 4, 5, 2] , [ 11, 11] and [ 3, 2, 3, '
             '2, 3] are dominated ( by 2, 11 and 3 respectevitely) but arrays '
             '[ 3] , [ 1, 2] and [ 3, 3, 2, 2, 1] are not. Small remark: since '
             'any array can be dominated only by one number, we can not '
             'specify this number and just say that array is either dominated '
             'or not. You are given array a1, a2, . . . , an. Calculate its '
             'shortest dominated subarray or say that there are no such '
             'subarrays. The subarray of a is a contiguous part of the array '
             'a, i. e. the array ai, ai+ 1, . . . , aj for some 1≤i≤j≤n.',
  'input': 'The first line contains single integer T ( 1≤T≤1000) — the number '
           'of test cases. Each test case consists of two lines. The first '
           'line contains single integer n ( 1≤n≤2⋅105) — the length of the '
           'array a. The second line contains n integers a1, a2, . . . , an ( '
           "1≤ai≤n) — the corresponding values of the array a. It' s "
           "guaranteed that the total length of all arrays in one test doesn' "
           't exceed 2⋅105.',
  'note': 'In the first test case, there are no subarrays of length at least '
          '2, so the answer is −1. In the second test case, the whole array is '
          "dominated ( by 1) and it' s the only dominated subarray. In the "
          'third test case, the subarray a4, a5, a6 is the shortest dominated '
          'subarray. In the fourth test case, all subarrays of length more '
          'than one are dominated.',
  'output': 'Print T integers — one per test case. For each test case print '
            'the only integer — the length of the shortest dominated subarray, '
            'or −1 if there are no such subarrays.',
  'title': 'Dominated Subarray',
  'topics': ['greedy', 'implementation', 'sortings', 'strings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1257/C'},
 {'history': 'Lucy likes letters. She studied the definition of the '
             'lexicographical order at school and plays with it. At first, she '
             'tried to construct the lexicographically smallest word out of '
             'given letters. It was so easy! Then she tried to build multiple '
             'words and minimize one of them. This was much harder! Formally, '
             'Lucy wants to make n words of length l each out of the given n⋅l '
             'letters, so that the k- th of them in the lexicographic order is '
             'lexicographically as small as possible.',
  'input': 'The first line contains three integers n, l, and k ( 1≤k≤n≤1000; '
           '1≤l≤1000) — the total number of words, the length of each word, '
           'and the index of the word Lucy wants to minimize. The next line '
           'contains a string of n⋅l lowercase letters of the English '
           'alphabet.',
  'note': ' ',
  'output': 'Output n words of l letters each, one per line, using the letters '
            'from the input. Words must be sorted in the lexicographic order, '
            'and the k- th of them must be lexicographically as small as '
            'possible. If there are multiple answers with the smallest k- th '
            'word, output any of them.',
  'title': 'Lexicography',
  'topics': ['constructive algorithms', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1267/L'},
 {'history': 'You are given an integer x of n digits a1, a2, . . . , an, which '
             'make up its decimal notation in order from left to right. Also, '
             "you are given a positive integer k< n. Let' s call integer b1, "
             'b2, . . . , bm beautiful if bi= bi+ k for each i, such that '
             '1≤i≤m−k. You need to find the smallest beautiful integer y, such '
             'that y≥x.',
  'input': 'The first line of input contains two integers n, k ( 2≤n≤200000, '
           '1≤k< n) : the number of digits in x and k. The next line of input '
           'contains n digits a1, a2, . . . , an ( a1= ̸0, 0≤ai≤9) : digits of '
           'x.',
  'note': ' ',
  'output': 'In the first line print one integer m: the number of digits in y. '
            'In the next line print m digits b1, b2, . . . , bm ( b1= ̸0, '
            '0≤bi≤9) : digits of y.',
  'title': 'Long Beautiful Integer',
  'topics': ['constructive algorithms', 'greedy', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1268/A'},
 {'history': "Let' s call a binary string s awesome, if it has at least 1 "
             'symbol 1 and length of the string is divisible by the number of '
             '1 in it. In particular, 1, 1010, 111 are awesome, but 0, 110, '
             "01010 aren' t. You are given a binary string s. Count the number "
             'of its awesome substrings. A string a is a substring of a string '
             'b if a can be obtained from b by deletion of several ( possibly, '
             'zero or all) characters from the beginning and several ( '
             'possibly, zero or all) characters from the end.',
  'input': 'The first line contains the string s ( 1≤| s| ≤200000) consisting '
           'only of zeros and ones.',
  'note': 'In the first sample, all substrings of s are awesome. In the second '
          'sample, we have the following awesome substrings of s: 1 ( 2 times) '
          ', 01 ( 2 times) , 10 ( 2 times) , 010 ( 2 times) , 1010, 0101In the '
          'third sample, no substring is awesome.',
  'output': 'Output a single number — the number of awesome substrings of s.',
  'title': 'Awesome Substrings',
  'topics': ['math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1270/F'},
 {'history': 'You are given two bracket sequences ( not necessarily regular) s '
             "and t consisting only of characters ' ( ' and ' ) ' . You want "
             'to construct the shortest regular bracket sequence that contains '
             'both given bracket sequences as subsequences ( not necessarily '
             'contiguous) . Recall what is the regular bracket sequence: ( ) '
             'is the regular bracket sequence; if S is the regular bracket '
             'sequence, then ( S) is a regular bracket sequence; if S and T '
             'regular bracket sequences, then ST ( concatenation of S and T) '
             'is a regular bracket sequence. Recall that the subsequence of '
             'the string s is such string t that can be obtained from s by '
             'removing some ( possibly, zero) amount of characters. For '
             'example, " coder" , " force" , " cf" and " cores" are '
             'subsequences of " codeforces" , but " fed" and " z" are not.',
  'input': 'The first line of the input contains one bracket sequence s '
           "consisting of no more than 200 characters ' ( ' and ' ) ' . The "
           'second line of the input contains one bracket sequence t '
           "consisting of no more than 200 characters ' ( ' and ' ) ' .",
  'note': ' ',
  'output': 'Print one line — the shortest regular bracket sequence that '
            'contains both given bracket sequences as subsequences ( not '
            'necessarily contiguous) . If there are several answers, you can '
            'print any.',
  'title': 'Two Bracket Sequences',
  'topics': ['dp', 'strings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1272/F'},
 {'history': 'Polycarp has built his own web service. Being a modern web '
             'service it includes login feature. And that always implies '
             'password security problems. Polycarp decided to store the hash '
             'of the password, generated by the following algorithm: take the '
             'password p, consisting of lowercase Latin letters, and shuffle '
             'the letters randomly in it to obtain p′ ( p′ can still be equal '
             'to p) ; generate two random strings, consisting of lowercase '
             'Latin letters, s1 and s2 ( any of these strings can be empty) ; '
             'the resulting hash h= s1+ p′+ s2, where addition is string '
             'concatenation. For example, let the password p= " abacaba" . '
             'Then p′ can be equal to " aabcaab" . Random strings s1= " zyx" '
             'and s2= " kjh" . Then h= " zyxaabcaabkjh" . Note that no letters '
             'could be deleted or added to p to obtain p′, only the order '
             'could be changed. Now Polycarp asks you to help him to implement '
             'the password check module. Given the password p and the hash h, '
             'check that h can be the hash for the password p. Your program '
             'should answer t independent test cases.',
  'input': 'The first line contains one integer t ( 1≤t≤100) — the number of '
           'test cases. The first line of each test case contains a non- empty '
           'string p, consisting of lowercase Latin letters. The length of p '
           'does not exceed 100. The second line of each test case contains a '
           'non- empty string h, consisting of lowercase Latin letters. The '
           'length of h does not exceed 100.',
  'note': 'The first test case is explained in the statement. In the second '
          'test case both s1 and s2 are empty and p′= " threetwoone" is p '
          'shuffled. In the third test case the hash could not be obtained '
          'from the password. In the fourth test case s1= " n" , s2 is empty '
          'and p′= " one" is p shuffled ( even thought it stayed the same) . '
          'In the fifth test case the hash could not be obtained from the '
          'password.',
  'output': 'For each test case print the answer to it — " YES" if the given '
            'hash h could be obtained from the given password p or " NO" '
            'otherwise.',
  'title': 'Shuffle Hashing',
  'topics': ['brute force', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1278/A'},
 {'history': 'This is an interactive problem. After completing the last level '
             'of the enchanted temple, you received a powerful artifact of the '
             '255th level. Do not rush to celebrate, because this artifact has '
             'a powerful rune that can be destroyed with a single spell s, '
             'which you are going to find. We define the spell as some non- '
             'empty string consisting only of the letters a and b. At any '
             'time, you can cast an arbitrary non- empty spell t, and the rune '
             'on the artifact will begin to resist. Resistance of the rune is '
             'the edit distance between the strings that specify the casted '
             'spell t and the rune- destroying spell s. Edit distance of two '
             'strings s and t is a value equal to the minimum number of one- '
             'character operations of replacing, inserting and deleting '
             'characters in s to get t. For example, the distance between '
             'ababa and aaa is 2, the distance between aaa and aba is 1, the '
             'distance between bbaba and abb is 3. The edit distance is 0 if '
             'and only if the strings are equal. It is also worth considering '
             'that the artifact has a resistance limit — if you cast more than '
             'n+ 2 spells, where n is the length of spell s, the rune will be '
             'blocked. Thus, it takes n+ 2 or fewer spells to destroy the rune '
             'that is on your artifact. Keep in mind that the required '
             'destructive spell s must also be counted among these n+ 2 '
             'spells. Note that the length n of the rune- destroying spell s '
             'is not known to you in advance. It is only known that its length '
             'n does not exceed 300. InteractionInteraction is happening '
             'through queries. Each request consists of a single non- empty '
             'string t — the spell you want to cast. The length of string t '
             'should not exceed 300. Each string should consist only of the '
             'letters a and b. In response to the query, you will get '
             'resistance runes — the edit distance between the strings that '
             'specify the casted spell t and the secret rune- destroying spell '
             's. Remember that s contains only the letters a and b. After '
             'breaking the rune, your program should end immediately. A rune '
             'is destroyed when you get a response with resistance 0. After '
             'receiving the value 0, your program should terminate normally. '
             'In this problem interactor is not adaptive. This means that '
             'during any test the rune- destroying spell s does not change. If '
             'your query is invalid, - 1 will be returned. After receiving '
             'this your program should immediately terminate normally ( for '
             'example, by calling exit( 0) ) , otherwise, the testing system '
             'may issue an arbitrary verdict. If the number of spells exceeds '
             'limit ( n+ 2, where n is the length of the spell s, which is '
             'unknown to you) , you will get the Wrong Answer verdict. Your '
             'solution may receive the verdict Idleness Limit Exceeded if you '
             "don' t output anything or forget to flush the output buffer. To "
             'flush the output buffer, you need to do the following '
             'immediately after printing the query and the line end: fflush( '
             'stdout) or cout. flush( ) in C+ + ; System. out. flush( ) in '
             'Java; flush( output) in Pascal; stdout. flush( ) in Python; for '
             'other languages see documentation. HacksFor hacks, use the '
             'following format: In a single line print the string s ( 1≤| s| '
             '≤300) of letters a and b, which defines the rune- destroying '
             'spell. The hacked solution will not have direct access to the '
             'unknown spell.',
  'input': ' ',
  'note': ' ',
  'output': ' ',
  'title': 'Enchanted Artifact',
  'topics': ['constructive algorithms', 'interactive', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1282/D'},
 {'history': 'Happy new year! The year 2020 is also known as Year Gyeongja ( '
             '경자년, gyeongja- nyeon) in Korea. Where did the name come '
             "from? Let' s briefly look at the Gapja system, which is "
             'traditionally used in Korea to name the years. There are two '
             'sequences of nn strings s1, s2, s3, . . . , sns1, s2, s3, . . . '
             ', sn and mm strings t1, t2, t3, . . . , tmt1, t2, t3, . . . , '
             'tm. These strings contain only lowercase letters. There might be '
             "duplicates among these strings. Let' s call a concatenation of "
             'strings xx and yy as the string that is obtained by writing down '
             'strings xx and yy one right after another without changing the '
             'order. For example, the concatenation of the strings " code" and '
             '" forces" is the string " codeforces" . The year 1 has a name '
             'which is the concatenation of the two strings s1s1 and t1t1. '
             'When the year increases by one, we concatenate the next two '
             'strings in order from each of the respective sequences. If the '
             'string that is currently being used is at the end of its '
             'sequence, we go back to the first string in that sequence. For '
             'example, if n= 3, m= 4, s= n= 3, m= 4, s= " a" , " b" , " c" , '
             't= t= " d" , " e" , " f" , " g" , the following table denotes '
             'the resulting year names. Note that the names of the years may '
             'repeat. You are given two sequences of strings of size nn and mm '
             'and also qq queries. For each query, you will be given the '
             'current year. Could you find the name corresponding to the given '
             'year, according to the Gapja system?',
  'input': 'The first line contains two integers n, mn, m ( 1≤n, m≤201≤n, '
           'm≤20) . The next line contains nn strings s1, s2, . . . , sns1, '
           's2, . . . , sn. Each string contains only lowercase letters, and '
           'they are separated by spaces. The length of each string is at '
           'least 11 and at most 1010. The next line contains mm strings t1, '
           't2, . . . , tmt1, t2, . . . , tm. Each string contains only '
           'lowercase letters, and they are separated by spaces. The length of '
           'each string is at least 11 and at most 1010. Among the given n+ '
           'mn+ m strings may be duplicates ( that is, they are not '
           'necessarily all different) . The next line contains a single '
           'integer qq ( 1≤q≤20201≤q≤2020) . In the next qq lines, an integer '
           'yy ( 1≤y≤1091≤y≤109) is given, denoting the year we want to know '
           'the name for.',
  'note': 'The first example denotes the actual names used in the Gapja '
          'system. These strings usually are either a number or the name of '
          'some animal.',
  'output': 'Print qq lines. For each line, print the name of the year as per '
            'the rule described above.',
  'title': 'New Year and Naming',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1284/A'},
 {'history': 'Today, as a friendship gift, Bakry gave Badawy n integers a1, '
             'a2, . . . , an and challenged him to choose an integer X such '
             'that the value max is minimum possible, where ⊕denotes the '
             'bitwise XOR operation. As always, Badawy is too lazy, so you '
             'decided to help him and find the minimum possible value of 1 ≤i '
             '≤nmax ( a_ i ⊕X) .',
  'input': 'The first line contains integer n ( 1≤n ≤10^ 5) . The second line '
           'contains n integers a_ 1, a_ 2, . . . , a_ n ( 0 ≤a_ i ≤2^ 30- 1) '
           '.',
  'note': 'In the first sample, we can choose X = 3. In the second sample, we '
          'can choose X = 5.',
  'output': 'Print one integer — the minimum possible value of 1 ≤i ≤nmax ( a_ '
            'i ⊕X) .',
  'title': 'Dr. Evil Underscores',
  'topics': ['bitmasks',
             'brute force',
             'dfs and similar',
             'divide and conquer',
             'dp',
             'greedy',
             'strings',
             'trees'],
  'url': 'https://codeforces.com/problemset/problem/1285/D'},
 {'history': 'Fedya has a string S, initially empty, and an array W, also '
             'initially empty. There are n queries to process, one at a time. '
             'Query i consists of a lowercase English letter ci and a '
             'nonnegative integer wi. First, ci must be appended to S, and wi '
             'must be appended to W. The answer to the query is the sum of '
             'suspiciousnesses for all subsegments of W [ L, R] , ( 1≤L≤R≤i) . '
             'We define the suspiciousness of a subsegment as follows: if the '
             'substring of S corresponding to this subsegment ( that is, a '
             'string of consecutive characters from L- th to R- th, inclusive) '
             'matches the prefix of S of the same length ( that is, a '
             'substring corresponding to the subsegment [ 1, R−L+ 1] ) , then '
             'its suspiciousness is equal to the minimum in the array W on the '
             '[ L, R] subsegment. Otherwise, in case the substring does not '
             'match the corresponding prefix, the suspiciousness is 0. Help '
             'Fedya answer all the queries before the orderlies come for him!',
  'input': 'The first line contains an integer n ( 1≤n≤600000) — the number of '
           'queries. The i- th of the following n lines contains the query i: '
           'a lowercase letter of the Latin alphabet ci and an integer wi ( '
           '0≤wi≤230−1) . All queries are given in an encrypted form. Let ans '
           'be the answer to the previous query ( for the first query we set '
           'this value equal to 0) . Then, in order to get the real query, you '
           'need to do the following: perform a cyclic shift of ci in the '
           'alphabet forward by ans, and set wi equal to wi⊕( ans MASK) , '
           'where ⊕ is the bitwise exclusive " or" , is the bitwise " and" , '
           'and MASK= 230−1.',
  'note': 'For convenience, we will call " suspicious" those subsegments for '
          'which the corresponding lines are prefixes of S, that is, those '
          'whose suspiciousness may not be zero. As a result of decryption in '
          'the first example, after all requests, the string S is equal to " '
          'abacaba" , and all wi= 1, that is, the suspiciousness of all '
          "suspicious sub- segments is simply equal to 1. Let' s see how the "
          'answer is obtained after each request: 1. S = " a" , the array W '
          'has a single subsegment — [ 1, 1] , and the corresponding substring '
          'is " a" , that is, the entire string S, thus it is a prefix of S, '
          'and the suspiciousness of the subsegment is 1. 2. S = " ab" , '
          'suspicious subsegments: [ 1, 1] and [ 1, 2] , total 2. 3. S = " '
          'aba" , suspicious subsegments: [ 1, 1] , [ 1, 2] , [ 1, 3] and [ 3, '
          '3] , total 4. 4. S = " abac" , suspicious subsegments: [ 1, 1] , [ '
          '1, 2] , [ 1, 3] , [ 1, 4] and [ 3, 3] , total 5. 5. S = " abaca" , '
          'suspicious subsegments: [ 1, 1] , [ 1, 2] , [ 1, 3] , [ 1, 4] , [ '
          '1, 5] , [ 3, 3] and [ 5, 5] , total 7. 6. S = " abacab" , '
          'suspicious subsegments: [ 1, 1] , [ 1, 2] , [ 1, 3] , [ 1, 4] , [ '
          '1, 5] , [ 1, 6] , [ 3, 3] , [ 5, 5] and [ 5, 6] , total 9. 7. S = " '
          'abacaba" , suspicious subsegments: [ 1, 1] , [ 1, 2] , [ 1, 3] , [ '
          '1, 4] , [ 1, 5] , [ 1, 6] , [ 1, 7] , [ 3, 3] , [ 5, 5] , [ 5, 6] , '
          '[ 5, 7] and [ 7, 7] , total 12. In the second example, after all '
          'requests S = " aaba" , W= [ 2, 0, 2, 0] . 1. S = " a" , suspicious '
          'subsegments: [ 1, 1] ( suspiciousness 2) , totaling 2. 2. S = " aa" '
          ', suspicious subsegments: [ 1, 1] ( 2) , [ 1, 2] ( 0) , [ 2, 2] ( '
          '0) , totaling 2. 3. S = " aab" , suspicious subsegments: [ 1, 1] ( '
          '2) , [ 1, 2] ( 0) , [ 1, 3] ( 0) , [ 2, 2] ( 0) , totaling 2. 4. S '
          '= " aaba" , suspicious subsegments: [ 1, 1] ( 2) , [ 1, 2] ( 0) , [ '
          '1, 3] ( 0) , [ 1, 4] ( 0) , [ 2, 2] ( 0) , [ 4, 4] ( 0) , totaling '
          '2. In the third example, from the condition after all requests S = '
          '" abcde" , W= [ 7, 2, 10, 1, 7] . 1. S = " a" , suspicious '
          'subsegments: [ 1, 1] ( 7) , totaling 7. 2. S = " ab" , suspicious '
          'subsegments: [ 1, 1] ( 7) , [ 1, 2] ( 2) , totaling 9. 3. S = " '
          'abc" , suspicious subsegments: [ 1, 1] ( 7) , [ 1, 2] ( 2) , [ 1, '
          '3] ( 2) , totaling 11. 4. S = " abcd" , suspicious subsegments: [ '
          '1, 1] ( 7) , [ 1, 2] ( 2) , [ 1, 3] ( 2) , [ 1, 4] ( 1) , totaling '
          '12. 5. S = " abcde" , suspicious subsegments: [ 1, 1] ( 7) , [ 1, '
          '2] ( 2) , [ 1, 3] ( 2) , [ 1, 4] ( 1) , [ 1, 5] ( 1) , totaling 13.',
  'output': 'Print n lines, i- th line should contain a single integer — the '
            'answer to the i- th query.',
  'title': 'Fedya the Potter Strikes Back',
  'topics': ['data structures', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1286/E'},
 {'history': "Let' s call two strings ss and t anagrams of each other if it is "
             'possible to rearrange symbols in the string s to get a string, '
             "equal to t. Let' s consider two strings s and t which are "
             'anagrams of each other. We say that t is a reducible anagram of '
             's if there exists an integer k≥2 and 2k non- empty strings s1, '
             't1, s2, t2, . . . , sk, tk that satisfy the following '
             'conditions: If we write the strings s1, s2, . . . , sk in order, '
             'the resulting string will be equal to s; If we write the strings '
             't1, t2, . . . , tk in order, the resulting string will be equal '
             'to t; For all integers i between 1 and k inclusive, si and ti '
             "are anagrams of each other. If such strings don' t exist, then t "
             'is said to be an irreducible anagram of s. Note that these '
             'notions are only defined when s and t are anagrams of each '
             'other. For example, consider the string s= " gamegame" . Then '
             'the string t= " megamage" is a reducible anagram of s, we may '
             'choose for example s1= " game" , s2= " gam" , s3= " e" and t1= " '
             'mega" , t2= " mag" , t3= " e" : On the other hand, we can prove '
             'that t= " memegaga" is an irreducible anagram of s. You will be '
             'given a string s and q queries, represented by two integers '
             '1≤l≤r≤| s| ( where | s| is equal to the length of the string s) '
             '. For each query, you should find if the substring of s formed '
             'by characters from the l- th to the r- th has at least one '
             'irreducible anagram.',
  'input': 'The first line contains a string s, consisting of lowercase '
           'English characters ( 1≤| s| ≤2⋅105) . The second line contains a '
           'single integer q ( 1≤q≤105) — the number of queries. Each of the '
           'following q lines contain two integers l and r ( 1≤l≤r≤| s| ) , '
           'representing a query for the substring of s formed by characters '
           'from the l- th to the r- th.',
  'note': 'In the first sample, in the first and third queries, the substring '
          'is " a" , which has itself as an irreducible anagram since two or '
          'more non- empty strings cannot be put together to obtain " a" . On '
          'the other hand, in the second query, the substring is " aaa" , '
          'which has no irreducible anagrams: its only anagram is itself, and '
          'we may choose s1= " a" , s2= " aa" , t1= " a" , t2= " aa" to show '
          'that it is a reducible anagram. In the second query of the second '
          'sample, the substring is " abb" , which has, for example, " bba" as '
          'an irreducible anagram.',
  'output': 'For each query, print a single line containing " Yes" ( without '
            'quotes) if the corresponding substring has at least one '
            'irreducible anagram, and a single line containing " No" ( without '
            'quotes) otherwise.',
  'title': 'Irreducible Anagrams',
  'topics': ['binary search',
             'constructive algorithms',
             'data structures',
             'strings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1290/B'},
 {'history': "Let' s define a number ebne ( even but not even) if and only if "
             'its sum of digits is divisible by 2 but the number itself is not '
             'divisible by 2. For example, 13, 1227, 185217 are ebne numbers, '
             "while 12, 2, 177013, 265918 are not. If you' re still unsure "
             'what ebne numbers are, you can look at the sample notes for more '
             'clarification. You are given a non- negative integer s, '
             'consisting of n digits. You can delete some digits ( they are '
             'not necessary consecutive/ successive) to make the given number '
             'ebne. You cannot change the order of the digits, that is, after '
             'deleting the digits the remaining digits collapse. The resulting '
             "number shouldn' t contain leading zeros. You can delete any "
             'number of digits between 0 ( do not delete any digits at all) '
             'and n−1. For example, if you are given s= '
             '222373204424185217171912 then one of possible ways to make it '
             'ebne is: 222373204424185217171912 → 2237344218521717191. The sum '
             'of digits of 2237344218521717191 is equal to 70 and is divisible '
             'by 2, but number itself is not divisible by 2: it means that the '
             'resulting number is ebne. Find any resulting number that is '
             "ebne. If it' s impossible to create an ebne number from the "
             'given number report about it.',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤1000) — the number of test cases. The '
           'description of the test cases follows. The first line of each test '
           'case contains a single integer n ( 1≤n≤3000) — the number of '
           'digits in the original number. The second line of each test case '
           'contains a non- negative integer number s, consisting of n digits. '
           'It is guaranteed that s does not contain leading zeros and the sum '
           'of n over all test cases does not exceed 3000.',
  'note': 'In the first test case of the example, 1227 is already an ebne '
          'number ( as 1+ 2+ 2+ 7= 12, 12 is divisible by 2, while in the same '
          "time, 1227 is not divisible by 2) so we don' t need to delete any "
          'digits. Answers such as 127 and 17 will also be accepted. In the '
          'second test case of the example, it is clearly impossible to create '
          'an ebne number from the given number. In the third test case of the '
          'example, there are many ebne numbers we can obtain by deleting, for '
          'example, 1 digit such as 17703, 77013 or 17013. Answers such as '
          '1701 or 770 will not be accepted as they are not ebne numbers. '
          'Answer 013 will not be accepted as it contains leading zeroes. '
          'Explanation: 1+ 7+ 7+ 0+ 3= 18. As 18 is divisible by 2 while 17703 '
          'is not divisible by 2, we can see that 17703 is an ebne number. '
          'Same with 77013 and 17013; 1+ 7+ 0+ 1= 9. Because 9 is not '
          'divisible by 2, 1701 is not an ebne number; 7+ 7+ 0= 14. This time, '
          '14 is divisible by 2 but 770 is also divisible by 2, therefore, 770 '
          'is not an ebne number. In the last test case of the example, one of '
          'many other possible answers is given. Another possible answer is: '
          '222373204424185217171912 → 22237320442418521717191 ( delete the '
          'last digit) .',
  'output': 'For each test case given in the input print the answer in the '
            'following format: If it is impossible to create an ebne number, '
            'print " - 1" ( without quotes) ; Otherwise, print the resulting '
            'number after deleting some, possibly zero, but not all digits. '
            'This number should be ebne. If there are multiple answers, you '
            'can print any of them. Note that answers with leading zeros or '
            "empty strings are not accepted. It' s not necessary to minimize "
            'or maximize the number of deleted digits.',
  'title': 'Even But Not Even',
  'topics': ['greedy', 'math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1291/A'},
 {'history': 'You are given string s of length n consisting of 0- s and 1- s. '
             'You build an infinite string t as a concatenation of an infinite '
             'number of strings s, or t= ssss. . . For example, if s= 10010, '
             'then t= 100101001010010. . . Calculate the number of prefixes of '
             't with balance equal to x. The balance of some string q is equal '
             'to cnt0, q−cnt1, q, where cnt0, q is the number of occurrences '
             'of 0 in q, and cnt1, q is the number of occurrences of 1 in q. '
             'The number of such prefixes can be infinite; if it is so, you '
             'must say that. A prefix is a string consisting of several first '
             'letters of a given string, without any reorders. An empty prefix '
             'is also a valid prefix. For example, the string " abcd" has 5 '
             'prefixes: empty string, " a" , " ab" , " abc" and " abcd" .',
  'input': 'The first line contains the single integer T ( 1≤T≤100) — the '
           'number of test cases. Next 2T lines contain descriptions of test '
           'cases — two lines per test case. The first line contains two '
           'integers n and x ( 1≤n≤105, −109≤x≤109) — the length of string s '
           'and the desired balance, respectively. The second line contains '
           "the binary string s ( | s| = n, si∈0, 1) . It' s guaranteed that "
           "the total sum of n doesn' t exceed 105.",
  'note': 'In the first test case, there are 3 good prefixes of t: with length '
          '28, 30 and 32.',
  'output': 'Print T integers — one per test case. For each test case print '
            'the number of prefixes or −1 if there is an infinite number of '
            'such prefixes.',
  'title': 'Infinite Prefixes',
  'topics': ['math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1295/B'},
 {'history': 'You are given two strings s and t consisting of lowercase Latin '
             'letters. Also you have a string z which is initially empty. You '
             'want string z to be equal to string t. You can perform the '
             'following operation to achieve this: append any subsequence of s '
             'at the end of string z. A subsequence is a sequence that can be '
             'derived from the given sequence by deleting zero or more '
             'elements without changing the order of the remaining elements. '
             'For example, if z= ac, s= abcde, you may turn z into following '
             'strings in one operation: z= acace ( if we choose subsequence '
             'ace) ; z= acbcd ( if we choose subsequence bcd) ; z= acbce ( if '
             'we choose subsequence bce) . Note that after this operation '
             "string s doesn' t change. Calculate the minimum number of such "
             'operations to turn string z into string t.',
  'input': 'The first line contains the integer T ( 1≤T≤100) — the number of '
           'test cases. The first line of each testcase contains one string s '
           '( 1≤| s| ≤105) consisting of lowercase Latin letters. The second '
           'line of each testcase contains one string t ( 1≤| t| ≤105) '
           'consisting of lowercase Latin letters. It is guaranteed that the '
           'total length of all strings s and t in the input does not exceed '
           '2⋅105.',
  'note': ' ',
  'output': 'For each testcase, print one integer — the minimum number of '
            "operations to turn string z into string t. If it' s impossible "
            'print −1.',
  'title': 'Obtain The String',
  'topics': ['dp', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1295/C'},
 {'history': 'You are given a string s of lowercase Latin letters. It is '
             'required to paint each letter of the string in one of two colors '
             '( red or blue) so that if you write all the red letters from '
             'left to right and write all the blue letters from left to right, '
             'then the lexicographically maximum of the two written strings is '
             'lexicographically minimal. For each index, in the string s you '
             'can choose either of two colors. Formally, we write out: the '
             'string r ( can be empty) — all red letters in the order from '
             'left to right ( red subsequence) , the string b ( can be empty) '
             '— all blue letters in the order from left to right ( blue '
             'subsequence) . Your task is to paint the string such that max is '
             'minimal. Small reminder: the empty string is the '
             'lexicographically smallest string.',
  'input': 'The first line contains an integer t ( 1 ≤t ≤100) — the number of '
           'test cases in the test. Next, the test cases are given, one per '
           'line. Each test case is a non- empty string s of length between 2 '
           'to 100 characters, inclusive, which consists of lowercase Latin '
           'letters.',
  'note': ' ',
  'output': 'Print t lines, the i- th of them should contain the answer to the '
            'i- th test case of the input. Print a string of length n, where n '
            'is the length of the given string s: the j- th character of the '
            "string should be either ' R' or ' B' depending on the color of "
            'the j- th character in the answer ( painted in red or blue) . If '
            'there are several possible answers, print any of them.',
  'title': 'Paint the String',
  'topics': ['*special', 'dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1297/H'},
 {'history': 'You are given three strings a, b and c of the same length n. The '
             'strings consist of lowercase English letters only. The i- th '
             'letter of a is ai, the i- th letter of b is bi, the i- th letter '
             'of c is ci. For every i ( 1≤i≤n) you must swap ( i. e. exchange) '
             "ci with either ai or bi. So in total you' ll perform exactly n "
             'swap operations, each of them either ci↔ai or ci↔bi ( i iterates '
             'over all integers between 1 and n, inclusive) . For example, if '
             'a is " code" , b is " true" , and c is " help" , you can make c '
             'equal to " crue" taking the 1- st and the 4- th letters from a '
             'and the others from b. In this way a becomes " hodp" and b '
             'becomes " tele" . Is it possible that after these swaps the '
             'string a becomes exactly the same as the string b?',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤100) — the number of test cases. The '
           'description of the test cases follows. The first line of each test '
           'case contains a string of lowercase English letters a. The second '
           'line of each test case contains a string of lowercase English '
           'letters b. The third line of each test case contains a string of '
           'lowercase English letters c. It is guaranteed that in each test '
           'case these three strings are non- empty and have the same length, '
           'which is not exceeding 100.',
  'note': 'In the first test case, it is impossible to do the swaps so that '
          'string a becomes exactly the same as string b. In the second test '
          'case, you should swap ci with ai for all possible i. After the '
          'swaps a becomes " bca" , b becomes " bca" and c becomes " abc" . '
          'Here the strings a and b are equal. In the third test case, you '
          'should swap c1 with a1, c2 with b2, c3 with b3 and c4 with a4. Then '
          'string a becomes " baba" , string b becomes " baba" and string c '
          'becomes " abab" . Here the strings a and b are equal. In the fourth '
          'test case, it is impossible to do the swaps so that string a '
          'becomes exactly the same as string b.',
  'output': 'Print t lines with answers for all test cases. For each test '
            'case: If it is possible to make string a equal to string b print '
            '" YES" ( without quotes) , otherwise print " NO" ( without '
            'quotes) . You can print either lowercase or uppercase letters in '
            'the answers.',
  'title': 'Three Strings',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1301/A'},
 {'history': 'Ayoub thinks that he is a very smart person, so he created a '
             'function f( s) , where s is a binary string ( a string which '
             'contains only symbols " 0" and " 1" ) . The function f( s) is '
             'equal to the number of substrings in the string s that contains '
             'at least one symbol, that is equal to " 1" . More formally, f( '
             's) is equal to the number of pairs of integers ( l, r) , such '
             'that 1≤l≤r≤| s| ( where | s| is equal to the length of string s) '
             ', such that at least one of the symbols sl, sl+ 1, . . . , sr is '
             'equal to " 1" . For example, if s= " 01010" then f( s) = 12, '
             'because there are 12 such pairs ( l, r) : ( 1, 2) , ( 1, 3) , ( '
             '1, 4) , ( 1, 5) , ( 2, 2) , ( 2, 3) , ( 2, 4) , ( 2, 5) , ( 3, '
             '4) , ( 3, 5) , ( 4, 4) , ( 4, 5) . Ayoub also thinks that he is '
             'smarter than Mahmoud so he gave him two integers n and m and '
             'asked him this problem. For all binary strings s of length n '
             'which contains exactly m symbols equal to " 1" , find the '
             "maximum value of f( s) . Mahmoud couldn' t solve the problem so "
             'he asked you for help. Can you help him?',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤105) — the number of test cases. The '
           'description of the test cases follows. The only line for each test '
           'case contains two integers n, m ( 1≤n≤109, 0≤m≤n) — the length of '
           'the string and the number of symbols equal to " 1" in it.',
  'note': 'In the first test case, there exists only 3 strings of length 3, '
          'which has exactly 1 symbol, equal to " 1" . These strings are: s1= '
          '" 100" , s2= " 010" , s3= " 001" . The values of f for them are: f( '
          's1) = 3, f( s2) = 4, f( s3) = 3, so the maximum value is 4 and the '
          'answer is 4. In the second test case, the string s with the maximum '
          'value is " 101" . In the third test case, the string s with the '
          'maximum value is " 111" . In the fourth test case, the only string '
          's of length 4, which has exactly 0 symbols, equal to " 1" is " '
          '0000" and the value of f for that string is 0, so the answer is 0. '
          'In the fifth test case, the string s with the maximum value is " '
          '01010" and it is described as an example in the problem statement.',
  'output': 'For every test case print one integer number — the maximum value '
            'of f( s) over all strings s of length n, which has exactly m '
            'symbols, equal to " 1" .',
  'title': "Ayoub's function",
  'topics': ['binary search', 'combinatorics', 'greedy', 'math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1301/C'},
 {'history': 'You are given a string s. Each character is either 0 or 1. You '
             "want all 1' s in the string to form a contiguous subsegment. For "
             "example, if the string is 0, 1, 00111 or 01111100, then all 1' s "
             'form a contiguous subsegment, and if the string is 0101, 100001 '
             'or 11111111111101, then this condition is not met. You may erase '
             "some ( possibly none) 0' s from the string. What is the minimum "
             "number of 0' s that you have to erase?",
  'input': 'The first line contains one integer t ( 1≤t≤100) — the number of '
           'test cases. Then t lines follow, each representing a test case. '
           'Each line contains one string s ( 1≤| s| ≤100) ; each character of '
           's is either 0 or 1.',
  'note': 'In the first test case you have to delete the third and forth '
          'symbols from string 010011 ( it turns into 0111) .',
  'output': 'Print t integers, where the i- th integer is the answer to the i- '
            "th testcase ( the minimum number of 0' s that you have to erase "
            'from s) .',
  'title': 'Erasing Zeroes',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1303/A'},
 {'history': 'You are given a string s. You can build new string p from s '
             'using the following operation no more than two times: choose any '
             'subsequence si1, si2, . . . , sik where 1≤i1< i2< ⋯< ik≤| s| ; '
             'erase the chosen subsequence from s ( s can become empty) ; '
             'concatenate chosen subsequence to the right of the string p ( in '
             'other words, p= p+ si1si2. . . sik) . Of course, initially the '
             "string p is empty. For example, let s= ababcd. At first, let' s "
             'choose subsequence s1s4s5= abc — we will get s= bad and p= abc. '
             "At second, let' s choose s1s2= ba — we will get s= d and p= "
             'abcba. So we can build abcba from ababcd. Can you build a given '
             'string t using the algorithm above?',
  'input': 'The first line contains the single integer T ( 1≤T≤100) — the '
           'number of test cases. Next 2T lines contain test cases — two per '
           'test case. The first line contains string s consisting of '
           'lowercase Latin letters ( 1≤| s| ≤400) — the initial string. The '
           'second line contains string t consisting of lowercase Latin '
           "letters ( 1≤| t| ≤| s| ) — the string you' d like to build. It' s "
           "guaranteed that the total length of strings s doesn' t exceed 400.",
  'note': ' ',
  'output': 'Print T answers — one per test case. Print YES ( case '
            "insensitive) if it' s possible to build t and NO ( case "
            'insensitive) otherwise.',
  'title': 'Erase Subsequences',
  'topics': ['dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1303/E'},
 {'history': 'Returning back to problem solving, Gildong is now studying about '
             'palindromes. He learned that a palindrome is a string that is '
             'the same as its reverse. For example, strings " pop" , " noon" , '
             '" x" , and " kkkkkk" are palindromes, while strings " moon" , " '
             'tv" , and " abab" are not. An empty string is also a palindrome. '
             'Gildong loves this concept so much, so he wants to play with it. '
             'He has n distinct strings of equal length m. He wants to discard '
             'some of the strings ( possibly none or all) and reorder the '
             'remaining strings so that the concatenation becomes a '
             'palindrome. He also wants the palindrome to be as long as '
             'possible. Please help him find one.',
  'input': 'The first line contains two integers n and m ( 1≤n≤100, 1≤m≤50) — '
           'the number of strings and the length of each string. Next n lines '
           'contain a string of length m each, consisting of lowercase Latin '
           'letters only. All strings are distinct.',
  'note': 'In the first example, " battab" is also a valid answer. In the '
          'second example, there can be 4 different valid answers including '
          'the sample output. We are not going to provide any hints for what '
          'the others are. In the third example, the empty string is the only '
          'valid palindrome string.',
  'output': 'In the first line, print the length of the longest palindrome '
            'string you made. In the second line, print that palindrome. If '
            'there are multiple answers, print any one of them. If the '
            "palindrome is empty, print an empty line or don' t print this "
            'line at all.',
  'title': 'Longest Palindrome',
  'topics': ['brute force',
             'constructive algorithms',
             'greedy',
             'implementation',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1304/B'},
 {'history': 'Now that Kuroni has reached 10 years old, he is a big boy and '
             "doesn' t like arrays of integers as presents anymore. This year "
             'he wants a Bracket sequence as a Birthday present. More '
             'specifically, he wants a bracket sequence so complex that no '
             'matter how hard he tries, he will not be able to remove a simple '
             "subsequence! We say that a string formed by n characters ' ( ' "
             "or ' ) ' is simple if its length n is even and positive, its "
             "first n2 characters are ' ( ' , and its last n2 characters are ' "
             ") ' . For example, the strings ( ) and ( ( ) ) are simple, while "
             'the strings ) ( and ( ) ( ) are not simple. Kuroni will be given '
             "a string formed by characters ' ( ' and ' ) ' ( the given string "
             'is not necessarily simple) . An operation consists of choosing a '
             'subsequence of the characters of the string that forms a simple '
             'string and removing all the characters of this subsequence from '
             "the string. Note that this subsequence doesn' t have to be "
             'continuous. For example, he can apply the operation to the '
             "string ' ) ( ) ( ( ) ) ) ' , to choose a subsequence of bold "
             "characters, as it forms a simple string ' ( ( ) ) ' , delete "
             "these bold characters from the string and to get ' ) ) ( ) ' . "
             'Kuroni has to perform the minimum possible number of operations '
             'on the string, in such a way that no more operations can be '
             'performed on the remaining string. The resulting string does not '
             'have to be empty. Since the given string is too large, Kuroni is '
             'unable to figure out how to minimize the number of operations. '
             'Can you help him do it instead? A sequence of characters a is a '
             'subsequence of a string b if a can be obtained from b by '
             'deletion of several ( possibly, zero or all) characters.',
  'input': 'The only line of input contains a string s ( 1≤| s| ≤1000) formed '
           "by characters ' ( ' and ' ) ' , where | s| is the length of s.",
  'note': "In the first sample, the string is ' ( ( ) ( ( ' . The operation "
          'described corresponds to deleting the bolded subsequence. The '
          "resulting string is ' ( ( ( ' , and no more operations can be "
          'performed on it. Another valid answer is choosing indices 2 and 3, '
          'which results in the same final string. In the second sample, it is '
          'already impossible to perform any operations.',
  'output': 'In the first line, print an integer k — the minimum number of '
            'operations you have to apply. Then, print 2k lines describing the '
            'operations in the following format: For each operation, print a '
            'line containing an integer m — the number of characters in the '
            'subsequence you will remove. Then, print a line containing m '
            'integers 1≤a1< a2< ⋯< am — the indices of the characters you will '
            'remove. All integers must be less than or equal to the length of '
            'the current string, and the corresponding subsequence must form a '
            'simple string. If there are multiple valid sequences of '
            'operations with the smallest k, you may print any of them.',
  'title': 'Kuroni and Simple Strings',
  'topics': ['constructive algorithms', 'greedy', 'strings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1305/B'},
 {'history': 'Bessie the cow has just intercepted a text that Farmer John sent '
             'to Burger Queen! However, Bessie is sure that there is a secret '
             'message hidden inside. The text is a string s of lowercase Latin '
             'letters. She considers a string t as hidden in string s if t '
             'exists as a subsequence of s whose indices form an arithmetic '
             'progression. For example, the string aab is hidden in string '
             'aaabb because it occurs at indices 1, 3, and 5, which form an '
             'arithmetic progression with a common difference of 2. Bessie '
             'thinks that any hidden string that occurs the most times is the '
             'secret message. Two occurrences of a subsequence of S are '
             'distinct if the sets of indices are different. Help her find the '
             'number of occurrences of the secret message! For example, in the '
             'string aaabb, a is hidden 3 times, b is hidden 2 times, ab is '
             'hidden 6 times, aa is hidden 3 times, bb is hidden 1 time, aab '
             'is hidden 2 times, aaa is hidden 1 time, abb is hidden 1 time, '
             'aaab is hidden 1 time, aabb is hidden 1 time, and aaabb is '
             'hidden 1 time. The number of occurrences of the secret message '
             'is 6.',
  'input': 'The first line contains a string s of lowercase Latin letters ( '
           '1≤| s| ≤105) — the text that Bessie intercepted.',
  'note': 'In the first example, these are all the hidden strings and their '
          'indice sets: a occurs at ( 1) , ( 2) , ( 3) b occurs at ( 4) , ( 5) '
          'ab occurs at ( 1, 4) , ( 1, 5) , ( 2, 4) , ( 2, 5) , ( 3, 4) , ( 3, '
          '5) aa occurs at ( 1, 2) , ( 1, 3) , ( 2, 3) bb occurs at ( 4, 5) '
          'aab occurs at ( 1, 3, 5) , ( 2, 3, 4) aaa occurs at ( 1, 2, 3) abb '
          'occurs at ( 3, 4, 5) aaab occurs at ( 1, 2, 3, 4) aabb occurs at ( '
          '2, 3, 4, 5) aaabb occurs at ( 1, 2, 3, 4, 5) Note that all the sets '
          'of indices are arithmetic progressions. In the second example, no '
          'hidden string occurs more than once. In the third example, the '
          'hidden string is the letter l.',
  'output': 'Output a single integer — the number of occurrences of the secret '
            'message.',
  'title': 'Cow and Message',
  'topics': ['brute force', 'dp', 'math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1307/C'},
 {'history': 'VK just opened its second HQ in St. Petersburg! Side of its '
             'office building has a huge string ss written on its side. This '
             'part of the office is supposed to be split into mm meeting rooms '
             'in such way that meeting room walls are strictly between letters '
             'on the building. Obviously, meeting rooms should not be of size '
             '0, but can be as small as one letter wide. Each meeting room '
             'will be named after the substring of ss written on its side. For '
             'each possible arrangement of mm meeting rooms we ordered a test '
             'meeting room label for the meeting room with lexicographically '
             'minimal name. When delivered, those labels got sorted backward '
             'lexicographically. What is printed on kkth label of the '
             'delivery?',
  'input': 'In the first line, you are given three integer numbers n, m, kn, '
           'm, k — length of string ss, number of planned meeting rooms to '
           'split ss into and number of the interesting label ( 2≤n≤1000; '
           '1≤m≤1000; 1≤k≤10182≤n≤1000; 1≤m≤1000; 1≤k≤1018) . Second input '
           'line has string ss, consisting of nn lowercase english letters. '
           'For given n, m, kn, m, k there are at least kk ways to split ss '
           'into mm substrings.',
  'note': 'In the first example, delivery consists of the labels " aba" , " '
          'ab" , " a" . In the second example, delivery consists of 30603060 '
          'labels. The first label is " aupontrougevkof" and the last one is " '
          'a" .',
  'output': 'Output single string – name of meeting room printed on kk- th '
            'label of the delivery.',
  'title': 'Au Pont Rouge',
  'topics': ['binary search', 'dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1310/C'},
 {'history': 'Vasya had three strings a, b and s, which consist of lowercase '
             'English letters. The lengths of strings a and b are equal to n, '
             'the length of the string s is equal to m. Vasya decided to '
             'choose a substring of the string a, then choose a substring of '
             'the string b and concatenate them. Formally, he chooses a '
             'segment [ l1, r1] ( 1≤l1≤r1≤n) and a segment [ l2, r2] ( '
             '1≤l2≤r2≤n) , and after concatenation he obtains a string a[ l1, '
             'r1] + b[ l2, r2] = al1al1+ 1. . . ar1bl2bl2+ 1. . . br2. Now, '
             'Vasya is interested in counting number of ways to choose those '
             'segments adhering to the following conditions: segments [ l1, '
             'r1] and [ l2, r2] have non- empty intersection, i. e. there '
             'exists at least one integer x, such that l1≤x≤r1 and l2≤x≤r2; '
             'the string a[ l1, r1] + b[ l2, r2] is equal to the string s.',
  'input': 'The first line contains integers n and m ( 1≤n≤500000, 2≤m≤2⋅n) — '
           'the length of strings a and b and the length of the string s. The '
           'next three lines contain strings a, b and s, respectively. The '
           'length of the strings a and b is n, while the length of the string '
           's is m. All strings consist of lowercase English letters.',
  'note': "Let' s list all the pairs of segments that Vasya could choose in "
          'the first example: [ 2, 2] and [ 2, 5] ; [ 1, 2] and [ 2, 4] ; [ 5, '
          '5] and [ 2, 5] ; [ 5, 6] and [ 3, 5] ;',
  'output': 'Print one integer — the number of ways to choose a pair of '
            "segments, which satisfy Vasya' s conditions.",
  'title': 'Concatenation with intersection',
  'topics': ['data structures', 'hashing', 'strings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1313/E'},
 {'history': 'After a long party Petya decided to return home, but he turned '
             'out to be at the opposite end of the town from his home. There '
             'are nn crossroads in the line in the town, and there is either '
             'the bus or the tram station at each crossroad. The crossroads '
             'are represented as a string ss of length nn, where si= Asi= A, '
             'if there is a bus station at ii- th crossroad, and si= Bsi= B, '
             'if there is a tram station at ii- th crossroad. Currently Petya '
             'is at the first crossroad ( which corresponds to s1s1) and his '
             'goal is to get to the last crossroad ( which corresponds to '
             'snsn) . If for two crossroads ii and jj for all crossroads i, i+ '
             '1, . . . , j−1i, i+ 1, . . . , j−1 there is a bus station, one '
             'can pay aa roubles for the bus ticket, and go from ii- th '
             'crossroad to the jj- th crossroad by the bus ( it is not '
             'necessary to have a bus station at the jj- th crossroad) . '
             'Formally, paying aa roubles Petya can go from ii to jj if st= '
             'Ast= A for all i≤t< ji≤t< j. If for two crossroads ii and jj for '
             'all crossroads i, i+ 1, . . . , j−1i, i+ 1, . . . , j−1 there is '
             'a tram station, one can pay bb roubles for the tram ticket, and '
             'go from ii- th crossroad to the jj- th crossroad by the tram ( '
             'it is not necessary to have a tram station at the jj- th '
             'crossroad) . Formally, paying bb roubles Petya can go from ii to '
             'jj if st= Bst= B for all i≤t< ji≤t< j. For example, if ss= " '
             'AABBBAB" , a= 4a= 4 and b= 3b= 3 then Petya needs: buy one bus '
             'ticket to get from 11 to 33, buy one tram ticket to get from 33 '
             'to 66, buy one bus ticket to get from 66 to 77. Thus, in total '
             'he needs to spend 4+ 3+ 4= 114+ 3+ 4= 11 roubles. Please note '
             'that the type of the stop at the last crossroad ( i. e. the '
             'character snsn) does not affect the final expense. Now Petya is '
             'at the first crossroad, and he wants to get to the nn- th '
             "crossroad. After the party he has left with pp roubles. He' s "
             'decided to go to some station on foot, and then go to home using '
             'only public transport. Help him to choose the closest crossroad '
             'ii to go on foot the first, so he has enough money to get from '
             'the ii- th crossroad to the nn- th, using only tram and bus '
             'tickets.',
  'input': 'Each test contains one or more test cases. The first line contains '
           'the number of test cases tt ( 1≤t≤1041≤t≤104) . The first line of '
           'each test case consists of three integers a, b, pa, b, p ( 1≤a, b, '
           'p≤1051≤a, b, p≤105) — the cost of bus ticket, the cost of tram '
           'ticket and the amount of money Petya has. The second line of each '
           'test case consists of one string ss, where si= Asi= A, if there is '
           'a bus station at ii- th crossroad, and si= Bsi= B, if there is a '
           'tram station at ii- th crossroad ( 2≤| s| ≤1052≤| s| ≤105) . It is '
           'guaranteed, that the sum of the length of strings ss by all test '
           "cases in one test doesn' t exceed 105105.",
  'note': ' ',
  'output': 'For each test case print one number — the minimal index i of a '
            'crossroad Petya should go on foot. The rest of the path ( i. e. '
            'from i to n he should use public transport) .',
  'title': 'Homecoming',
  'topics': ['binary search', 'dp', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1315/B'},
 {'history': 'Vasya has a string s of length n. He decides to make the '
             'following modification to the string: Pick an integer k, ( '
             '1≤k≤n) . For i from 1 to n−k+ 1, reverse the substring s[ i: i+ '
             'k−1] of s. For example, if string s is qwer and k= 2, below is '
             'the series of transformations the string goes through: qwer ( '
             'original string) wqer ( after reversing the first substring of '
             'length 2) weqr ( after reversing the second substring of length '
             '2) werq ( after reversing the last substring of length 2) Hence, '
             'the resulting string after modifying s with k= 2 is werq. Vasya '
             'wants to choose a k such that the string obtained after the '
             'above- mentioned modification is lexicographically smallest '
             'possible among all choices of k. Among all such k, he wants to '
             'choose the smallest one. Since he is busy attending Felicity '
             '2020, he asks for your help. A string a is lexicographically '
             'smaller than a string b if and only if one of the following '
             'holds: a is a prefix of b, but a= ̸b; in the first position '
             'where a and b differ, the string a has a letter that appears '
             'earlier in the alphabet than the corresponding letter in b.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤5000) . The description of the '
           'test cases follows. The first line of each test case contains a '
           'single integer n ( 1≤n≤5000) — the length of the string s. The '
           'second line of each test case contains the string s of n lowercase '
           'latin letters. It is guaranteed that the sum of n over all test '
           'cases does not exceed 5000.',
  'note': 'In the first testcase of the first sample, the string modification '
          'results for the sample abab are as follows : for k= 1 : abab for k= '
          '2 : baba for k= 3 : abab for k= 4 : babaThe lexicographically '
          'smallest string achievable through modification is abab for k= 1 '
          'and 3. Smallest value of k needed to achieve is hence 1.',
  'output': 'For each testcase output two lines: In the first line output the '
            'lexicographically smallest string s′ achievable after the above- '
            'mentioned modification. In the second line output the appropriate '
            'value of k ( 1≤k≤n) that you chose for performing the '
            'modification. If there are multiple values of k that give the '
            'lexicographically smallest string, output the smallest value of k '
            'among them.',
  'title': 'String Modification',
  'topics': ['brute force',
             'constructive algorithms',
             'implementation',
             'sortings',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1316/B'},
 {'history': 'In this problem, we will deal with binary strings. Each '
             'character of a binary string is either a 0 or a 1. We will also '
             'deal with substrings; recall that a substring is a contiguous '
             'subsequence of a string. We denote the substring of string s '
             'starting from the l- th character and ending with the r- th '
             'character as s[ l. . . r] . The characters of each string are '
             'numbered from 1. We can perform several operations on the '
             'strings we consider. Each operation is to choose a substring of '
             'our string and replace it with another string. There are two '
             'possible types of operations: replace 011 with 110, or replace '
             '110 with 011. For example, if we apply exactly one operation to '
             'the string 110011110, it can be transformed into 011011110, '
             '110110110, or 110011011. Binary string a is considered reachable '
             'from binary string b if there exists a sequence s1, s2, . . . , '
             'sk such that s1= a, sk= b, and for every i∈[ 1, k−1] , si can be '
             'transformed into si+ 1 using exactly one operation. Note that k '
             'can be equal to 1, i. e. , every string is reachable from '
             'itself. You are given a string t and q queries to it. Each query '
             'consists of three integers l1, l2 and len. To answer each query, '
             'you have to determine whether t[ l1. . . l1+ len−1] is reachable '
             'from t[ l2. . . l2+ len−1] .',
  'input': 'The first line contains one integer n ( 1≤n≤2⋅105) — the length of '
           'string t. The second line contains one string t ( | t| = n) . Each '
           'character of t is either 0 or 1. The third line contains one '
           'integer q ( 1≤q≤2⋅105) — the number of queries. Then q lines '
           'follow, each line represents a query. The i- th line contains '
           'three integers l1, l2 and len ( 1≤l1, l2≤| t| , 1≤len≤| t| −max( '
           'l1, l2) + 1) for the i- th query.',
  'note': ' ',
  'output': 'For each query, print either YES if t[ l1. . . l1+ len−1] is '
            'reachable from t[ l2. . . l2+ len−1] , or NO otherwise. You may '
            'print each letter in any register.',
  'title': 'Reachable Strings',
  'topics': ['data structures', 'hashing', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1320/D'},
 {'history': 'You are given a string s consisting of lowercase Latin letters. '
             'Let the length of s be | s| . You may perform several operations '
             'on this string. In one operation, you can choose some index i '
             'and remove the i- th character of s ( si) if at least one of its '
             'adjacent characters is the previous letter in the Latin alphabet '
             'for si. For example, the previous letter for b is a, the '
             'previous letter for s is r, the letter a has no previous '
             'letters. Note that after each removal the length of the string '
             'decreases by one. So, the index i should satisfy the condition '
             '1≤i≤| s| during each operation. For the character si adjacent '
             'characters are si−1 and si+ 1. The first and the last characters '
             'of s both have only one adjacent character ( unless | s| = 1) . '
             'Consider the following example. Let s= bacabcab. During the '
             'first move, you can remove the first character s1= b because s2= '
             'a. Then the string becomes s= acabcab. During the second move, '
             'you can remove the fifth character s5= c because s4= b. Then the '
             'string becomes s= acabab. During the third move, you can remove '
             "the sixth character s6= ' b' because s5= a. Then the string "
             'becomes s= acaba. During the fourth move, the only character you '
             'can remove is s4= b, because s3= a ( or s5= a) . The string '
             'becomes s= acaa and you cannot do anything with it. Your task is '
             'to find the maximum possible number of characters you can remove '
             'if you choose the sequence of operations optimally.',
  'input': 'The first line of the input contains one integer | s| ( 1≤| s| '
           '≤100) — the length of s. The second line of the input contains one '
           'string s consisting of | s| lowercase Latin letters.',
  'note': 'The first example is described in the problem statement. Note that '
          'the sequence of moves provided in the statement is not the only, '
          'but it can be shown that the maximum possible answer to this test '
          'is 4. In the second example, you can remove all but one character '
          'of s. The only possible answer follows. During the first move, '
          'remove the third character s3= d, s becomes bca. During the second '
          'move, remove the second character s2= c, s becomes ba. And during '
          'the third move, remove the first character s1= b, s becomes a.',
  'output': 'Print one integer — the maximum possible number of characters you '
            'can remove if you choose the sequence of moves optimally.',
  'title': 'Remove Adjacent',
  'topics': ['brute force', 'constructive algorithms', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1321/C'},
 {'history': 'You are given an array a consisting of n integers. Your task is '
             'to determine if a has some subsequence of length at least 3 that '
             'is a palindrome. Recall that an array b is called a subsequence '
             'of the array a if b can be obtained by removing some ( possibly, '
             'zero) elements from a ( not necessarily consecutive) without '
             'changing the order of remaining elements. For example, [ 2] , [ '
             '1, 2, 1, 3] and [ 2, 3] are subsequences of [ 1, 2, 1, 3] , but '
             '[ 1, 1, 2] and [ 4] are not. Also, recall that a palindrome is '
             'an array that reads the same backward as forward. In other '
             'words, the array a of length n is the palindrome if ai= an−i−1 '
             'for all i from 1 to n. For example, arrays [ 1234] , [ 1, 2, 1] '
             ', [ 1, 3, 2, 2, 3, 1] and [ 10, 100, 10] are palindromes, but '
             'arrays [ 1, 2] and [ 1, 2, 3, 1] are not. You have to answer t '
             'independent test cases.',
  'input': 'The first line of the input contains one integer t ( 1≤t≤100) — '
           'the number of test cases. Next 2t lines describe test cases. The '
           'first line of the test case contains one integer n ( 3≤n≤5000) — '
           'the length of a. The second line of the test case contains n '
           'integers a1, a2, . . . , an ( 1≤ai≤n) , where ai is the i- th '
           'element of a. It is guaranteed that the sum of n over all test '
           'cases does not exceed 5000 ( ∑n≤5000) .',
  'note': 'In the first test case of the example, the array a has a '
          'subsequence [ 1, 2, 1] which is a palindrome. In the second test '
          'case of the example, the array a has two subsequences of length 3 '
          'which are palindromes: [ 2, 3, 2] and [ 2, 2, 2] . In the third '
          'test case of the example, the array a has no subsequences of length '
          'at least 3 which are palindromes. In the fourth test case of the '
          'example, the array a has one subsequence of length 4 which is a '
          'palindrome: [ 1, 2, 2, 1] ( and has two subsequences of length 3 '
          'which are palindromes: both are [ 1, 2, 1] ) . In the fifth test '
          'case of the example, the array a has no subsequences of length at '
          'least 3 which are palindromes.',
  'output': 'For each test case, print the answer — " YES" ( without quotes) '
            'if a has some subsequence of length at least 3 that is a '
            'palindrome and " NO" otherwise.',
  'title': 'Yet Another Palindrome Problem',
  'topics': ['brute force', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1324/B'},
 {'history': 'This is the easy version of the problem. The difference is the '
             'constraint on the sum of lengths of strings and the number of '
             'test cases. You can make hacks only if you solve all versions of '
             'this task. You are given a string s, consisting of lowercase '
             'English letters. Find the longest string, t, which satisfies the '
             'following conditions: The length of t does not exceed the length '
             'of s. t is a palindrome. There exists two strings a and b ( '
             'possibly empty) , such that t= a+ b ( " + " represents '
             'concatenation) , and a is prefix of s while b is suffix of s.',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤1000) , the number of test cases. The '
           'next t lines each describe a test case. Each test case is a non- '
           'empty string s, consisting of lowercase English letters. It is '
           'guaranteed that the sum of lengths of strings over all test cases '
           'does not exceed 5000.',
  'note': 'In the first test, the string s= " a" satisfies all conditions. In '
          'the second test, the string " abcdfdcba" satisfies all conditions, '
          'because: Its length is 9, which does not exceed the length of the '
          'string s, which equals 11. It is a palindrome. " abcdfdcba" = " '
          'abcdfdc" + " ba" , and " abcdfdc" is a prefix of s while " ba" is a '
          'suffix of s. It can be proven that there does not exist a longer '
          'string which satisfies the conditions. In the fourth test, the '
          'string " c" is correct, because " c" = " c" + " " and a or b can be '
          'empty. The other possible solution for this test is " s" .',
  'output': 'For each test case, print the longest string which satisfies the '
            'conditions described above. If there exists multiple possible '
            'solutions, print any of them.',
  'title': 'Prefix-Suffix Palindrome (Easy version)',
  'topics': ['hashing', 'string suffix structures', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1326/D1'},
 {'history': 'This is the hard version of the problem. The difference is the '
             'constraint on the sum of lengths of strings and the number of '
             'test cases. You can make hacks only if you solve all versions of '
             'this task. You are given a string s, consisting of lowercase '
             'English letters. Find the longest string, t, which satisfies the '
             'following conditions: The length of t does not exceed the length '
             'of s. t is a palindrome. There exists two strings a and b ( '
             'possibly empty) , such that t= a+ b ( " + " represents '
             'concatenation) , and a is prefix of s while b is suffix of s.',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤105) , the number of test cases. The next '
           't lines each describe a test case. Each test case is a non- empty '
           'string s, consisting of lowercase English letters. It is '
           'guaranteed that the sum of lengths of strings over all test cases '
           'does not exceed 106.',
  'note': 'In the first test, the string s= " a" satisfies all conditions. In '
          'the second test, the string " abcdfdcba" satisfies all conditions, '
          'because: Its length is 9, which does not exceed the length of the '
          'string s, which equals 11. It is a palindrome. " abcdfdcba" = " '
          'abcdfdc" + " ba" , and " abcdfdc" is a prefix of s while " ba" is a '
          'suffix of s. It can be proven that there does not exist a longer '
          'string which satisfies the conditions. In the fourth test, the '
          'string " c" is correct, because " c" = " c" + " " and a or b can be '
          'empty. The other possible solution for this test is " s" .',
  'output': 'For each test case, print the longest string which satisfies the '
            'conditions described above. If there exists multiple possible '
            'solutions, print any of them.',
  'title': 'Prefix-Suffix Palindrome (Hard version)',
  'topics': ['binary search',
             'greedy',
             'hashing',
             'string suffix structures',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1326/D2'},
 {'history': '',
  'input': 'The input consists of a single string of uppercase letters A- Z. '
           'The length of the string is between 1 and 10 characters, '
           'inclusive.',
  'note': ' ',
  'output': 'Output " YES" or " NO" .',
  'title': 'Elementary!',
  'topics': ['*special', 'brute force', 'dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1331/F'},
 {'history': 'Word s of length n is called k- complete if s is a palindrome, '
             'i. e. si= sn+ 1−i for all 1≤i≤n; s has a period of k, i. e. si= '
             'sk+ i for all 1≤i≤n−k. For example, " abaaba" is a 3- complete '
             'word, while " abccba" is not. Bob is given a word s of length n '
             'consisting of only lowercase Latin letters and an integer k, '
             'such that n is divisible by k. He wants to convert s to any k- '
             'complete word. To do this Bob can choose some i ( 1≤i≤n) and '
             'replace the letter at position i with some other lowercase Latin '
             'letter. So now Bob wants to know the minimum number of letters '
             'he has to replace to convert s to any k- complete word. Note '
             'that Bob can do zero changes if the word s is already k- '
             'complete. You are required to answer t test cases independently.',
  'input': 'The first line contains a single integer t ( 1≤t≤105) — the number '
           'of test cases. The first line of each test case contains two '
           'integers n and k ( 1≤k< n≤2⋅105, n is divisible by k) . The second '
           'line of each test case contains a word s of length n. It is '
           'guaranteed that word s only contains lowercase Latin letters. And '
           'it is guaranteed that the sum of n over all test cases will not '
           'exceed 2⋅105.',
  'note': 'In the first test case, one optimal solution is aaaaaa. In the '
          'second test case, the given word itself is k- complete.',
  'output': 'For each test case, output one integer, representing the minimum '
            'number of characters he has to replace to convert s to any k- '
            'complete word.',
  'title': 'K-Complete Word',
  'topics': ['dfs and similar', 'dsu', 'greedy', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1332/C'},
 {'history': "Kaavi, the mysterious fortune teller, deeply believes that one' "
             's fate is inevitable and unavoidable. Of course, she makes her '
             "living by predicting others' future. While doing divination, "
             'Kaavi believes that magic spells can provide great power for her '
             'to see the future. Kaavi has a string TT of length mm and all '
             'the strings with the prefix TT are magic spells. Kaavi also has '
             'a string SS of length nn and an empty string AA. During the '
             'divination, Kaavi needs to perform a sequence of operations. '
             'There are two different operations: Delete the first character '
             'of SS and add it at the front of AA. Delete the first character '
             'of SS and add it at the back of AA. Kaavi can perform no more '
             'than nn operations. To finish the divination, she wants to know '
             'the number of different operation sequences to make AA a magic '
             'spell ( i. e. with the prefix TT) . As her assistant, can you '
             'help her? The answer might be huge, so Kaavi only needs to know '
             'the answer modulo 998244353998244353. Two operation sequences '
             'are considered different if they are different in length or '
             'there exists an ii that their ii- th operation is different. A '
             'substring is a contiguous sequence of characters within a '
             'string. A prefix of a string SS is a substring of SS that occurs '
             'at the beginning of SS.',
  'input': 'The first line contains a string SS of length nn ( '
           '1≤n≤30001≤n≤3000) . The second line contains a string TT of length '
           'mm ( 1≤m≤n1≤m≤n) . Both strings contain only lowercase Latin '
           'letters.',
  'note': 'The first test: The red ones are the magic spells. In the first '
          'operation, Kaavi can either add the first character " a" at the '
          'front or the back of AA, although the results are the same, they '
          'are considered as different operations. So the answer is 6×2= '
          '126×2= 12.',
  'output': 'The output contains only one integer — the answer modulo '
            '998244353998244353.',
  'title': 'Kaavi and Magic Spell',
  'topics': ['dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1336/C'},
 {'history': "Let' s say string s has period k if si= si+ k for all i from 1 "
             'to | s| −k ( | s| means length of string s) and k is the minimum '
             'positive integer with this property. Some examples of a period: '
             'for s= " 0101" the period is k= 2, for s= " 0000" the period is '
             'k= 1, for s= " 010" the period is k= 2, for s= " 0011" the '
             "period is k= 4. You are given string t consisting only of 0' s "
             "and 1' s and you need to find such string s that: String s "
             "consists only of 0' s and 1' s; The length of s doesn' t exceed "
             '2⋅| t| ; String t is a subsequence of string s; String s has '
             'smallest possible period among all strings that meet conditions '
             '1—3. Let us recall that t is a subsequence of s if t can be '
             'derived from s by deleting zero or more elements ( any) without '
             'changing the order of the remaining elements. For example, t= " '
             '011" is a subsequence of s= " 10101" .',
  'input': 'The first line contains single integer T ( 1≤T≤100) — the number '
           'of test cases. Next T lines contain test cases — one per line. '
           "Each line contains string t ( 1≤| t| ≤100) consisting only of 0' s "
           "and 1' s.",
  'note': "In the first and second test cases, s= t since it' s already one of "
          'the optimal solutions. Answers have periods equal to 1 and 2, '
          'respectively. In the third test case, there are shorter optimal '
          "solutions, but it' s okay since we don' t need to minimize the "
          'string s. String s has period equal to 1.',
  'output': 'Print one string for each test case — string s you needed to '
            'find. If there are multiple solutions print any one of them.',
  'title': 'Binary Period',
  'topics': ['constructive algorithms', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1342/B'},
 {'history': 'Phoenix has a string s consisting of lowercase Latin letters. He '
             'wants to distribute all the letters of his string into k non- '
             'empty strings a1, a2, . . . , ak such that every letter of s '
             'goes to exactly one of the strings ai. The strings ai do not '
             'need to be substrings of s. Phoenix can distribute letters of s '
             'and rearrange the letters within each string ai however he '
             'wants. For example, if s= baba and k= 2, Phoenix may distribute '
             'the letters of his string in many ways, such as: ba and ba a and '
             'abb ab and ab aa and bb But these ways are invalid: baa and ba b '
             'and ba baba and empty string ( ai should be non- empty) Phoenix '
             'wants to distribute the letters of his string s into k strings '
             'a1, a2, . . . , ak to minimize the lexicographically maximum '
             'string among them, i. e. minimize max( a1, a2, . . . , ak) . '
             'Help him find the optimal distribution and print the minimal '
             'possible value of max( a1, a2, . . . , ak) . String x is '
             'lexicographically less than string y if either x is a prefix of '
             'y and x= ̸y, or there exists an index i ( 1≤i≤min( | x| , | y| ) '
             ') such that xi < yi and for every j ( 1≤j< i) xj= yj. Here | x| '
             'denotes the length of the string x.',
  'input': 'The input consists of multiple test cases. The first line contains '
           'an integer t ( 1≤t≤1000) — the number of test cases. Each test '
           'case consists of two lines. The first line of each test case '
           'consists of two integers n and k ( 1≤k≤n≤105) — the length of '
           'string s and the number of non- empty strings, into which Phoenix '
           'wants to distribute letters of s, respectively. The second line of '
           'each test case contains a string s of length n consisting only of '
           'lowercase Latin letters. It is guaranteed that the sum of n over '
           'all test cases is ≤105.',
  'note': 'In the first test case, one optimal solution is to distribute baba '
          'into ab and ab. In the second test case, one optimal solution is to '
          'distribute baacb into abbc and a. In the third test case, one '
          'optimal solution is to distribute baacb into ac, ab, and b. In the '
          'fourth test case, one optimal solution is to distribute aaaaa into '
          'aa, aa, and a. In the fifth test case, one optimal solution is to '
          'distribute aaxxzz into az, az, x, and x. In the sixth test case, '
          'one optimal solution is to distribute phoenix into ehinopx.',
  'output': 'Print t answers — one per test case. The i- th answer should be '
            'the minimal possible value of max( a1, a2, . . . , ak) in the i- '
            'th test case.',
  'title': 'Phoenix and Distribution',
  'topics': ['constructive algorithms', 'greedy', 'sortings', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1348/C'},
 {'history': 'You are given n strings a1, a2, . . . , an: all of them have the '
             'same length m. The strings consist of lowercase English letters. '
             'Find any string s of length m such that each of the given n '
             'strings differs from s in at most one position. Formally, for '
             'each given string ai, there is no more than one position j such '
             'that ai[ j] = ̸s[ j] . Note that the desired string s may be '
             'equal to one of the given strings ai, or it may differ from all '
             'the given strings. For example, if you have the strings abac and '
             'zbab, then the answer to the problem might be the string abab, '
             'which differs from the first only by the last character, and '
             'from the second only by the first.',
  'input': 'The first line contains an integer t ( 1≤t≤100) — the number of '
           'test cases. Then t test cases follow. Each test case starts with a '
           'line containing two positive integers n ( 1≤n≤10) and m ( 1≤m≤10) '
           '— the number of strings and their length. Then follow n strings '
           'ai, one per line. Each of them has length m and consists of '
           'lowercase English letters.',
  'note': 'The first test case was explained in the statement. In the second '
          'test case, the answer does not exist.',
  'output': 'Print t answers to the test cases. Each answer ( if it exists) is '
            'a string of length m consisting of lowercase English letters. If '
            'there are several answers, print any of them. If the answer does '
            'not exist, print " - 1" ( " minus one" , without quotes) .',
  'title': 'Spy-string',
  'topics': ['bitmasks',
             'brute force',
             'constructive algorithms',
             'dp',
             'hashing',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1360/F'},
 {'history': 'Shubham has a binary string s. A binary string is a string '
             'containing only characters " 0" and " 1" . He can perform the '
             'following operation on the string any amount of times: Select an '
             'index of the string, and flip the character at that index. This '
             'means, if the character was " 0" , it becomes " 1" , and vice '
             'versa. A string is called good if it does not contain " 010" or '
             '" 101" as a subsequence — for instance, " 1001" contains " 101" '
             'as a subsequence, hence it is not a good string, while " 1000" '
             'doesn\' t contain neither " 010" nor " 101" as subsequences, so '
             'it is a good string. What is the minimum number of operations he '
             'will have to perform, so that the string becomes good? It can be '
             'shown that with these operations we can make any string good. A '
             'string a is a subsequence of a string b if a can be obtained '
             'from b by deletion of several ( possibly, zero or all) '
             'characters.',
  'input': 'The first line of the input contains a single integer t ( 1≤t≤100) '
           '— the number of test cases. Each of the next t lines contains a '
           'binary string s ( 1≤| s| ≤1000) .',
  'note': 'In test cases 1, 2, 5, 6 no operations are required since they are '
          'already good strings. For the 3rd test case: " 001" can be achieved '
          'by flipping the first character — and is one of the possible ways '
          'to get a good string. For the 4th test case: " 000" can be achieved '
          'by flipping the second character — and is one of the possible ways '
          'to get a good string. For the 7th test case: " 000000" can be '
          'achieved by flipping the third and fourth characters — and is one '
          'of the possible ways to get a good string.',
  'output': 'For every string, output the minimum number of operations '
            'required to make it good.',
  'title': 'Subsequence Hate',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1363/B'},
 {'history': 'You are given two strings s and t, each of length n and '
             'consisting of lowercase Latin alphabets. You want to make s '
             'equal to t. You can perform the following operation on s any '
             'number of times to achieve it — Choose any substring of s and '
             'rotate it clockwise once, that is, if the selected substring is '
             's[ l, l+ 1. . . r] , then it becomes s[ r, l, l+ 1. . . r−1] . '
             'All the remaining characters of s stay in their position. For '
             'example, on rotating the substring [ 2, 4] , string " abcde" '
             'becomes " adbce" . A string a is a substring of a string b if a '
             'can be obtained from b by deletion of several ( possibly, zero '
             'or all) characters from the beginning and several ( possibly, '
             'zero or all) characters from the end. Find the minimum number of '
             "operations required to convert s to t, or determine that it' s "
             'impossible.',
  'input': 'The first line of the input contains a single integer t ( '
           '1≤t≤2000) — the number of test cases. The description of the test '
           'cases follows. The first line of each test case contains a single '
           'integer n ( 1≤n≤2000) — the length of the strings. The second and '
           'the third lines contain strings s and t respectively. The sum of n '
           'over all the test cases does not exceed 2000.',
  'note': "For the 1- st test case, since s and t are equal, you don' t need "
          'to apply any operation. For the 2- nd test case, you only need to '
          'apply one operation on the entire string ab to convert it to ba. '
          'For the 3- rd test case, you only need to apply one operation on '
          'the entire string abc to convert it to cab. For the 4- th test '
          'case, you need to apply the operation twice: first on the entire '
          'string abc to convert it to cab and then on the substring of length '
          '2 beginning at the second character to convert it to cba. For the '
          '5- th test case, you only need to apply one operation on the entire '
          'string abab to convert it to baba. For the 6- th test case, it is '
          'not possible to convert string s to t.',
  'output': 'For each test case, output the minimum number of operations to '
            'convert s to t. If it is not possible to convert s to t, output '
            '−1 instead.',
  'title': 'Rotating Substrings',
  'topics': ['dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1363/F'},
 {'history': "Let' s denote the function f( s) that takes a string s "
             'consisting of lowercase Latin letters and dots, and returns a '
             'string consisting of lowercase Latin letters as follows: let r '
             'be an empty string; process the characters of s from left to '
             'right. For each character c, do the following: if c is a '
             'lowercase Latin letter, append c at the end of the string r; '
             'otherwise, delete the last character from r ( if r is empty '
             'before deleting the last character — the function crashes) ; '
             'return r as the result of the function. You are given two '
             'strings s and t. You have to delete the minimum possible number '
             'of characters from s so that f( s) = t ( and the function does '
             "not crash) . Note that you aren' t allowed to insert new "
             'characters into s or reorder the existing ones.',
  'input': 'The input consists of two lines: the first one contains s — a '
           'string consisting of lowercase Latin letters and dots, the second '
           'one contains t — a string consisting of lowercase Latin letters ( '
           '1≤| t| ≤| s| ≤10000) . Additional constraint on the input: it is '
           'possible to remove some number of characters from s so that f( s) '
           '= t.',
  'note': ' ',
  'output': 'Print one integer — the minimum possible number of characters you '
            'have to delete from s so f( s) does not crash and returns t as '
            'the result of the function.',
  'title': 'Construct the String',
  'topics': ['data structures', 'dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1366/G'},
 {'history': 'Alice guesses the strings that Bob made for her. At first, Bob '
             'came up with the secret string a consisting of lowercase English '
             'letters. The string a has a length of 2 or more characters. '
             'Then, from string a he builds a new string b and offers Alice '
             'the string b so that she can guess the string a. Bob builds b '
             'from a as follows: he writes all the substrings of length 2 of '
             'the string a in the order from left to right, and then joins '
             'them in the same order into the string b. For example, if Bob '
             'came up with the string a= " abac" , then all the substrings of '
             'length 2 of the string a are: " ab" , " ba" , " ac" . Therefore, '
             'the string b= " abbaac" . You are given the string b. Help Alice '
             'to guess the string a that Bob came up with. It is guaranteed '
             'that b was built according to the algorithm given above. It can '
             'be proved that the answer to the problem is unique.',
  'input': 'The first line contains a single positive integer t ( 1≤t≤1000) — '
           'the number of test cases in the test. Then t test cases follow. '
           'Each test case consists of one line in which the string b is '
           'written, consisting of lowercase English letters ( 2≤| b| ≤100) — '
           'the string Bob came up with, where | b| is the length of the '
           'string b. It is guaranteed that b was built according to the '
           'algorithm given above.',
  'note': 'The first test case is explained in the statement. In the second '
          'test case, Bob came up with the string a= " ac" , the string a has '
          'a length 2, so the string b is equal to the string a. In the third '
          'test case, Bob came up with the string a= " bcdaf" , substrings of '
          'length 2 of string a are: " bc" , " cd" , " da" , " af" , so the '
          'string b= " bccddaaf" .',
  'output': 'Output t answers to test cases. Each answer is the secret string '
            'a, consisting of lowercase English letters, that Bob came up '
            'with.',
  'title': 'Short Substrings',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1367/A'},
 {'history': 'Karl likes Codeforces and subsequences. He wants to find a '
             'string of lowercase English letters that contains at least k '
             'subsequences codeforces. Out of all possible strings, Karl wants '
             'to find a shortest one. Formally, a codeforces subsequence of a '
             'string s is a subset of ten characters of s that read codeforces '
             'from left to right. For example, codeforces contains codeforces '
             'a single time, while codeforcesisawesome contains codeforces '
             'four times: codeforcesisawesome, codeforcesisawesome, '
             'codeforcesisawesome, codeforcesisawesome. Help Karl find any '
             'shortest string that contains at least k codeforces '
             'subsequences.',
  'input': 'The only line contains a single integer k ( 1≤k≤1016) .',
  'note': ' ',
  'output': 'Print a shortest string of lowercase English letters that '
            'contains at least k codeforces subsequences. If there are several '
            'such strings, print any of them.',
  'title': 'Codeforces Subsequences',
  'topics': ['brute force',
             'constructive algorithms',
             'greedy',
             'math',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1368/B'},
 {'history': 'Lee was cleaning his house for the party when he found a messy '
             "string under the carpets. Now he' d like to make it clean "
             'accurately and in a stylish way. . . The string s he found is a '
             'binary string of length n ( i. e. string consists only of 0- s '
             'and 1- s) . In one move he can choose two consecutive characters '
             'si and si+ 1, and if si is 1 and si+ 1 is 0, he can erase '
             'exactly one of them ( he can choose which one to erase but he '
             "can' t erase both characters simultaneously) . The string "
             'shrinks after erasing. Lee can make an arbitrary number of moves '
             "( possibly zero) and he' d like to make the string s as clean as "
             'possible. He thinks for two different strings x and y, the '
             'shorter string is cleaner, and if they are the same length, then '
             'the lexicographically smaller string is cleaner. Now you should '
             'answer t test cases: for the i- th test case, print the cleanest '
             'possible string that Lee can get by doing some number of moves. '
             'Small reminder: if we have two strings x and y of the same '
             'length then x is lexicographically smaller than y if there is a '
             'position i such that x1= y1, x2= y2, . . . , xi−1= yi−1 and xi< '
             'yi.',
  'input': 'The first line contains the integer t ( 1≤t≤104) — the number of '
           'test cases. Next 2t lines contain test cases — one per two lines. '
           'The first line of each test case contains the integer n ( 1≤n≤105) '
           '— the length of the string s. The second line contains the binary '
           'string s. The string s is a string of length n which consists only '
           "of zeroes and ones. It' s guaranteed that sum of n over test cases "
           "doesn' t exceed 105.",
  'note': "In the first test case, Lee can' t perform any moves. In the second "
          'test case, Lee should erase s2. In the third test case, Lee can '
          'make moves, for example, in the following order: 11001101 → 1100101 '
          '→ 110101 → 10101 → 1101 → 101 → 01.',
  'output': 'Print t answers — one per test case. The answer to the i- th test '
            'case is the cleanest string Lee can get after doing some number '
            'of moves ( possibly zero) .',
  'title': 'AccurateLee',
  'topics': ['greedy', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1369/B'},
 {'history': 'You are given a bracket sequence s of length n, where n is even '
             '( divisible by two) . The string s consists of n2 opening '
             "brackets ' ( ' and n2 closing brackets ' ) ' . In one move, you "
             'can choose exactly one bracket and move it to the beginning of '
             'the string or to the end of the string ( i. e. you choose some '
             'index i, remove the i- th character of s and insert it before or '
             'after all remaining characters of s) . Your task is to find the '
             'minimum number of moves required to obtain regular bracket '
             'sequence from s. It can be proved that the answer always exists '
             'under the given constraints. Recall what the regular bracket '
             'sequence is: " ( ) " is regular bracket sequence; if s is '
             'regular bracket sequence then " ( " + s + " ) " is regular '
             'bracket sequence; if s and t are regular bracket sequences then '
             's + t is regular bracket sequence. For example, " ( ) ( ) " , " '
             '( ( ) ) ( ) " , " ( ( ) ) " and " ( ) " are regular bracket '
             'sequences, but " ) ( " , " ( ) ( " and " ) ) ) " are not. You '
             'have to answer t independent test cases.',
  'input': 'The first line of the input contains one integer t ( 1≤t≤2000) — '
           'the number of test cases. Then t test cases follow. The first line '
           'of the test case contains one integer n ( 2≤n≤50) — the length of '
           's. It is guaranteed that n is even. The second line of the test '
           'case containg the string s consisting of n2 opening and n2 closing '
           'brackets.',
  'note': 'In the first test case of the example, it is sufficient to move the '
          'first bracket to the end of the string. In the third test case of '
          'the example, it is sufficient to move the last bracket to the '
          'beginning of the string. In the fourth test case of the example, we '
          'can choose last three openning brackets, move them to the beginning '
          'of the string and obtain " ( ( ( ) ) ) ( ( ) ) " .',
  'output': 'For each test case, print the answer — the minimum number of '
            'moves required to obtain regular bracket sequence from s. It can '
            'be proved that the answer always exists under the given '
            'constraints.',
  'title': 'Move Brackets',
  'topics': ['greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1374/C'},
 {'history': 'Acacius is studying strings theory. Today he came with the '
             'following problem. You are given a string s of length n '
             'consisting of lowercase English letters and question marks. It '
             'is possible to replace question marks with lowercase English '
             'letters in such a way that a string " abacaba" occurs as a '
             'substring in a resulting string exactly once? Each question mark '
             'should be replaced with exactly one lowercase English letter. '
             'For example, string " a? b? c" can be transformed into strings " '
             'aabbc" and " azbzc" , but can\' t be transformed into strings " '
             'aabc" , " a? bbc" and " babbc" . Occurrence of a string t of '
             'length m in the string s of length n as a substring is a index i '
             '( 1≤i≤n−m+ 1) such that string s[ i. . i+ m−1] consisting of m '
             'consecutive symbols of s starting from i- th equals to string t. '
             'For example string " ababa" has two occurrences of a string " '
             'aba" as a substring with i= 1 and i= 3, but there are no '
             'occurrences of a string " aba" in the string " acba" as a '
             'substring. Please help Acacius to check if it is possible to '
             'replace all question marks with lowercase English letters in '
             'such a way that a string " abacaba" occurs as a substring in a '
             'resulting string exactly once.',
  'input': 'First line of input contains an integer T ( 1≤T≤5000) , number of '
           'test cases. T pairs of lines with test case descriptions follow. '
           'The first line of a test case description contains a single '
           'integer n ( 7≤n≤50) , length of a string s. The second line of a '
           'test case description contains string s of length n consisting of '
           'lowercase English letters and question marks.',
  'note': 'In first example there is exactly one occurrence of a string " '
          'abacaba" in the string " abacaba" as a substring. In second example '
          'seven question marks can be replaced with any seven lowercase '
          'English letters and with " abacaba" in particular. In sixth example '
          'there are two occurrences of a string " abacaba" as a substring.',
  'output': 'For each test case output an answer for it. In case if there is '
            'no way to replace question marks in string s with a lowercase '
            'English letters in such a way that there is exactly one '
            'occurrence of a string " abacaba" in the resulting string as a '
            'substring output " No" . Otherwise output " Yes" and in the next '
            'line output a resulting string consisting of n lowercase English '
            'letters. If there are multiple possible strings, output any. You '
            'may print every letter in " Yes" and " No" in any case you want ( '
            'so, for example, the strings yEs, yes, Yes, and YES will all be '
            'recognized as positive answer) .',
  'title': 'Acacius and String',
  'topics': ['brute force', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1379/A'},
 {'history': 'This is the easy version of the problem. The difference between '
             'the versions is the constraint on n and the required number of '
             'operations. You can make hacks only if all versions of the '
             'problem are solved. There are two binary strings a and b of '
             'length n ( a binary string is a string consisting of symbols 0 '
             'and 1) . In an operation, you select a prefix of a, and '
             'simultaneously invert the bits in the prefix ( 0 changes to 1 '
             'and 1 changes to 0) and reverse the order of the bits in the '
             'prefix. For example, if a= 001011 and you select the prefix of '
             'length 3, it becomes 011011. Then if you select the entire '
             'string, it becomes 001001. Your task is to transform the string '
             'a into b in at most 3n operations. It can be proved that it is '
             'always possible.',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of test cases. Next 3t lines contain descriptions of test '
           'cases. The first line of each test case contains a single integer '
           'n ( 1≤n≤1000) — the length of the binary strings. The next two '
           'lines contain two binary strings a and b of length n. It is '
           'guaranteed that the sum of n across all test cases does not exceed '
           '1000.',
  'note': 'In the first test case, we have 01→11→00→10. In the second test '
          'case, we have 01011→00101→11101→01000→10100→00100→11100. In the '
          'third test case, the strings are already the same. Another solution '
          'is to flip the prefix of length 2, which will leave a unchanged.',
  'output': 'For each test case, output an integer k ( 0≤k≤3n) , followed by k '
            'integers p1, . . . , pk ( 1≤pi≤n) . Here k is the number of '
            'operations you use and pi is the length of the prefix you flip in '
            'the i- th operation.',
  'title': 'Prefix Flip (Easy Version)',
  'topics': ['constructive algorithms', 'data structures', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1381/A1'},
 {'history': 'This is the hard version of the problem. The difference between '
             'the versions is the constraint on n and the required number of '
             'operations. You can make hacks only if all versions of the '
             'problem are solved. There are two binary strings a and b of '
             'length n ( a binary string is a string consisting of symbols 0 '
             'and 1) . In an operation, you select a prefix of a, and '
             'simultaneously invert the bits in the prefix ( 0 changes to 1 '
             'and 1 changes to 0) and reverse the order of the bits in the '
             'prefix. For example, if a= 001011 and you select the prefix of '
             'length 3, it becomes 011011. Then if you select the entire '
             'string, it becomes 001001. Your task is to transform the string '
             'a into b in at most 2n operations. It can be proved that it is '
             'always possible.',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of test cases. Next 3t lines contain descriptions of test '
           'cases. The first line of each test case contains a single integer '
           'n ( 1≤n≤105) — the length of the binary strings. The next two '
           'lines contain two binary strings a and b of length n. It is '
           'guaranteed that the sum of n across all test cases does not exceed '
           '105.',
  'note': 'In the first test case, we have 01→11→00→10. In the second test '
          'case, we have 01011→00101→11101→01000→10100→00100→11100. In the '
          'third test case, the strings are already the same. Another solution '
          'is to flip the prefix of length 2, which will leave a unchanged.',
  'output': 'For each test case, output an integer k ( 0≤k≤2n) , followed by k '
            'integers p1, . . . , pk ( 1≤pi≤n) . Here k is the number of '
            'operations you use and pi is the length of the prefix you flip in '
            'the i- th operation.',
  'title': 'Prefix Flip (Hard Version)',
  'topics': ['constructive algorithms',
             'data structures',
             'implementation',
             'strings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1381/A2'},
 {'history': 'Note that the only difference between String Transformation 1 '
             'and String Transformation 2 is in the move Koa does. In this '
             'version the letter y Koa selects must be strictly greater '
             'alphabetically than x ( read statement for better understanding) '
             '. You can make hacks in these problems independently. Koa the '
             'Koala has two strings A and B of the same length n ( | A| = | B| '
             '= n) consisting of the first 20 lowercase English alphabet '
             'letters ( ie. from a to t) . In one move Koa: selects some '
             'subset of positions p1, p2, . . . , pk ( k≥1; 1≤pi≤n; pi= ̸pj if '
             'i= ̸j) of A such that Ap1= Ap2= . . . = Apk= x ( ie. all letters '
             'on this positions are equal to some letter x) . selects a letter '
             'y ( from the first 20 lowercase letters in English alphabet) '
             'such that y> x ( ie. letter y is strictly greater alphabetically '
             'than x) . sets each letter in positions p1, p2, . . . , pk to '
             'letter y. More formally: for each i ( 1≤i≤k) Koa sets Api= y. '
             'Note that you can only modify letters in string A. Koa wants to '
             'know the smallest number of moves she has to do to make strings '
             'equal to each other ( A= B) or to determine that there is no way '
             'to make them equal. Help her!',
  'input': 'Each test contains multiple test cases. The first line contains t '
           '( 1≤t≤10) — the number of test cases. Description of the test '
           'cases follows. The first line of each test case contains one '
           'integer n ( 1≤n≤105) — the length of strings A and B. The second '
           'line of each test case contains string A ( | A| = n) . The third '
           'line of each test case contains string B ( | B| = n) . Both '
           'strings consists of the first 20 lowercase English alphabet '
           'letters ( ie. from a to t) . It is guaranteed that the sum of n '
           'over all test cases does not exceed 105.',
  'note': 'In the 1- st test case Koa: selects positions 1 and 2 and sets A1= '
          'A2= b ( aab→bbb) . selects positions 2 and 3 and sets A2= A3= c ( '
          'bbb→bcc) . In the 2- nd test case Koa has no way to make string A '
          'equal B. In the 3- rd test case Koa: selects position 1 and sets '
          'A1= t ( abc→tbc) . selects position 2 and sets A2= s ( tbc→tsc) . '
          'selects position 3 and sets A3= r ( tsc→tsr) .',
  'output': 'For each test case: Print on a single line the smallest number of '
            'moves she has to do to make strings equal to each other ( A= B) '
            'or −1 if there is no way to make them equal.',
  'title': 'String Transformation 1',
  'topics': ['dsu',
             'graphs',
             'greedy',
             'sortings',
             'strings',
             'trees',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1383/A'},
 {'history': 'The length of the longest common prefix of two strings s= s1s2. '
             '. . sn and t= t1t2. . . tm is defined as the maximum integer k ( '
             '0≤k≤min( n, m) ) such that s1s2. . . sk equals t1t2. . . tk. Koa '
             'the Koala initially has n+ 1 strings s1, s2, . . . , sn+ 1. For '
             'each i ( 1≤i≤n) she calculated ai — the length of the longest '
             'common prefix of si and si+ 1. Several days later Koa found '
             "these numbers, but she couldn' t remember the strings. So Koa "
             'would like to find some strings s1, s2, . . . , sn+ 1 which '
             'would have generated numbers a1, a2, . . . , an. Can you help '
             'her? If there are many answers print any. We can show that '
             'answer always exists for the given constraints.',
  'input': 'Each test contains multiple test cases. The first line contains t '
           '( 1≤t≤100) — the number of test cases. Description of the test '
           'cases follows. The first line of each test case contains a single '
           'integer n ( 1≤n≤100) — the number of elements in the list a. The '
           'second line of each test case contains n integers a1, a2, . . . , '
           'an ( 0≤ai≤50) — the elements of a. It is guaranteed that the sum '
           'of n over all test cases does not exceed 100.',
  'note': 'In the 1- st test case one of the possible answers is s= [ aeren, '
          'ari, arousal, around, ari] . Lengths of longest common prefixes '
          'are: Between aeren and ari →1 Between ari and arousal →2 Between '
          'arousal and around →4 Between around and ari →2',
  'output': 'For each test case: Output n+ 1 lines. In the i- th line print '
            'string si ( 1≤| si| ≤200) , consisting of lowercase Latin '
            'letters. Length of the longest common prefix of strings si and '
            'si+ 1 has to be equal to ai. If there are many answers print any. '
            'We can show that answer always exists for the given constraints.',
  'title': 'Common Prefixes',
  'topics': ['constructive algorithms', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1384/A'},
 {'history': 'This is an easier version of the problem E with smaller '
             'constraints. Twilight Sparkle has received a new task from '
             'Princess Celestia. This time she asked to decipher the ancient '
             'scroll containing important knowledge of pony origin. To hide '
             'the crucial information from evil eyes, pony elders cast a spell '
             'on the scroll. That spell adds exactly one letter in any place '
             'to each word it is cast on. To make the path to the knowledge '
             'more tangled elders chose some of words in the scroll and cast a '
             'spell on them. Twilight Sparkle knows that the elders admired '
             'the order in all things so the scroll original scroll contained '
             'words in lexicographically non- decreasing order. She is asked '
             'to delete one letter from some of the words of the scroll ( to '
             'undo the spell) to get some version of the original scroll. '
             'Unfortunately, there may be more than one way to recover the '
             'ancient scroll. To not let the important knowledge slip by '
             'Twilight has to look through all variants of the original scroll '
             'and find the required one. To estimate the maximum time Twilight '
             'may spend on the work she needs to know the number of variants '
             'she has to look through. She asks you to find that number! Since '
             'that number can be very big, Twilight asks you to find it modulo '
             '109+ 7. It may occur that princess Celestia has sent a wrong '
             'scroll so the answer may not exist. A string a is '
             'lexicographically smaller than a string b if and only if one of '
             'the following holds: a is a prefix of b, but a= ̸b; in the first '
             'position where a and b differ, the string a has a letter that '
             'appears earlier in the alphabet than the corresponding letter in '
             'b.',
  'input': 'The first line contains a single integer n ( 1≤n≤1000) : the '
           'number of words in the scroll. The i- th of the next n lines '
           'contains a string consisting of lowercase English letters: the i- '
           'th word in the scroll. The length of each word is more or equal '
           'than 1. The sum of lengths of words does not exceed 20000.',
  'note': 'Notice that the elders could have written an empty word ( but they '
          'surely cast a spell on it so it holds a length 1 now) .',
  'output': 'Print one integer: the number of ways to get a version of the '
            'original from the scroll modulo 109+ 7.',
  'title': 'Twilight and Ancient Scroll (easier version)',
  'topics': ['dp',
             'hashing',
             'implementation',
             'string suffix structures',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1393/E1'},
 {'history': 'This is a harder version of the problem E with larger '
             'constraints. Twilight Sparkle has received a new task from '
             'Princess Celestia. This time she asked to decipher the ancient '
             'scroll containing important knowledge of pony origin. To hide '
             'the crucial information from evil eyes, pony elders cast a spell '
             'on the scroll. That spell adds exactly one letter in any place '
             'to each word it is cast on. To make the path to the knowledge '
             'more tangled elders chose some of words in the scroll and cast a '
             'spell on them. Twilight Sparkle knows that the elders admired '
             'the order in all things so the scroll original scroll contained '
             'words in lexicographically non- decreasing order. She is asked '
             'to delete one letter from some of the words of the scroll ( to '
             'undo the spell) to get some version of the original scroll. '
             'Unfortunately, there may be more than one way to recover the '
             'ancient scroll. To not let the important knowledge slip by '
             'Twilight has to look through all variants of the original scroll '
             'and find the required one. To estimate the maximum time Twilight '
             'may spend on the work she needs to know the number of variants '
             'she has to look through. She asks you to find that number! Since '
             'that number can be very big, Twilight asks you to find it modulo '
             '109+ 7. It may occur that princess Celestia has sent a wrong '
             'scroll so the answer may not exist. A string a is '
             'lexicographically smaller than a string b if and only if one of '
             'the following holds: a is a prefix of b, but a= ̸b; in the first '
             'position where a and b differ, the string a has a letter that '
             'appears earlier in the alphabet than the corresponding letter in '
             'b.',
  'input': 'The first line contains a single integer n ( 1≤n≤105) : the number '
           'of words in the scroll. The i- th of the next n lines contains a '
           'string consisting of lowercase English letters: the i- th word in '
           'the scroll. The length of each word is at least one. The sum of '
           'lengths of words does not exceed 106.',
  'note': 'Notice that the elders could have written an empty word ( but they '
          'surely cast a spell on it so it holds a length 1 now) .',
  'output': 'Print one integer: the number of ways to get a version of the '
            'original from the scroll modulo 109+ 7.',
  'title': 'Twilight and Ancient Scroll (harder version)',
  'topics': ['dp',
             'hashing',
             'implementation',
             'string suffix structures',
             'strings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1393/E2'},
 {'history': "No matter what trouble you' re in, don' t be afraid, but face it "
             "with a smile. I' ve made another billion dollars! — "
             'BoboniuBoboniu has issued his currencies, named Bobo Yuan. Bobo '
             'Yuan ( BBY) is a series of currencies. Boboniu gives each of '
             'them a positive integer identifier, such as BBY- 1, BBY- 2, etc. '
             'Boboniu has a BBY collection. His collection looks like a '
             'sequence. For example: We can use sequence a= [ 1, 2, 3, 3, 2, '
             '1, 4, 4, 1] a= [ 1, 2, 3, 3, 2, 1, 4, 4, 1] of length n= 9n= 9 '
             'to denote it. Now Boboniu wants to fold his collection. You can '
             'imagine that Boboniu stick his collection to a long piece of '
             'paper and fold it between currencies: Boboniu will only fold the '
             'same identifier of currencies together. In other words, if aiai '
             'is folded over ajaj ( 1≤i, j≤n1≤i, j≤n) , then ai= ajai= aj must '
             "hold. Boboniu doesn' t care if you follow this rule in the "
             'process of folding. But once it is finished, the rule should be '
             'obeyed. A formal definition of fold is described in notes. '
             'According to the picture above, you can fold aa two times. In '
             'fact, you can fold a= [ 1, 2, 3, 3, 2, 1, 4, 4, 1] a= [ 1, 2, 3, '
             '3, 2, 1, 4, 4, 1] at most two times. So the maximum number of '
             "folds of it is 22. As an international fan of Boboniu, you' re "
             "asked to calculate the maximum number of folds. You' re given a "
             'sequence aa of length nn, for each ii ( 1≤i≤n1≤i≤n) , you need '
             'to calculate the maximum number of folds of [ a1, a2, . . . , '
             'ai] [ a1, a2, . . . , ai] .',
  'input': 'The first line contains an integer nn ( 1≤n≤1051≤n≤105) . The '
           'second line contains nn integers a1, a2, . . . , ana1, a2, . . . , '
           'an ( 1≤ai≤n1≤ai≤n) .',
  'note': "Formally, for a sequence aa of length nn, let' s define the folding "
          'sequence as a sequence bb of length nn such that: bibi ( '
          '1≤i≤n1≤i≤n) is either 11 or −1−1. Let p( i) = [ bi= 1] + ∑i−1j= '
          '1bjp( i) = [ bi= 1] + ∑j= 1i−1bj. For all 1≤i< j≤n1≤i< j≤n, if p( '
          'i) = p( j) p( i) = p( j) , then aiai should be equal to ajaj. ( [ '
          'A] [ A] is the value of boolean expression AA. i. e. [ A] = 1[ A] = '
          '1 if AA is true, else [ A] = 0[ A] = 0) . Now we define the number '
          'of folds of bb as f( b) = ∑n−1i= 1[ bi= ̸bi+ 1] f( b) = ∑i= 1n−1[ '
          'bi= ̸bi+ 1] . The maximum number of folds of aa is F( a) = maxf( b) '
          '∣b is a folding sequence of aF( a) = maxf( b) ∣b is a folding '
          'sequence of a.',
  'output': 'Print nn integers. The ii- th of them should be equal to the '
            'maximum number of folds of [ a1, a2, . . . , ai] [ a1, a2, . . . '
            ', ai] .',
  'title': 'Boboniu and Banknote Collection',
  'topics': ['strings'],
  'url': 'https://codeforces.com/problemset/problem/1394/E'},
 {'history': 'You are given n strings s1, s2, . . . , sn consisting of '
             'lowercase Latin letters. In one operation you can remove a '
             'character from a string si and insert it to an arbitrary '
             'position in a string sj ( j may be equal to i) . You may perform '
             'this operation any number of times. Is it possible to make all n '
             'strings equal?',
  'input': 'The first line contains t ( 1≤t≤10) : the number of test cases. '
           'The first line of each test case contains a single integer n ( '
           '1≤n≤1000) : the number of strings. n lines follow, the i- th line '
           'contains si ( 1≤| si| ≤1000) . The sum of lengths of all strings '
           'in all test cases does not exceed 1000.',
  'note': 'In the first test case, you can do the following: Remove the third '
          'character of the first string and insert it after the second '
          'character of the second string, making the two strings " ca" and " '
          'cbab" respectively. Remove the second character of the second '
          'string and insert it after the second character of the first '
          'string, making both strings equal to " cab" . In the second test '
          'case, it is impossible to make all n strings equal.',
  'output': 'If it is possible to make the strings equal, print " YES" ( '
            'without quotes) . Otherwise, print " NO" ( without quotes) . You '
            'can output each character in either lowercase or uppercase.',
  'title': 'Juggling Letters',
  'topics': ['greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1397/A'},
 {'history': 'A binary string is a string where each character is either 0 or '
             '1. Two binary strings a and b of equal length are similar, if '
             'they have the same character in some position ( there exists an '
             'integer i such that ai= bi) . For example: 10010 and 01111 are '
             'similar ( they have the same character in position 4) ; 10010 '
             'and 11111 are similar; 111 and 111 are similar; 0110 and 1001 '
             'are not similar. You are given an integer n and a binary string '
             "s consisting of 2n−1 characters. Let' s denote s[ l. . r] as the "
             'contiguous substring of s starting with l- th character and '
             'ending with r- th character ( in other words, s[ l. . r] = slsl+ '
             '1sl+ 2. . . sr) . You have to construct a binary string w of '
             'length n which is similar to all of the following strings: s[ 1. '
             '. n] , s[ 2. . n+ 1] , s[ 3. . n+ 2] , . . . , s[ n. . 2n−1] .',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of test cases. The first line of each test case contains a '
           'single integer n ( 1≤n≤50) . The second line of each test case '
           'contains the binary string s of length 2n−1. Each character si is '
           'either 0 or 1.',
  'note': 'The explanation of the sample case ( equal characters in equal '
          'positions are bold) : The first test case: 1 is similar to s[ 1. . '
          '1] = 1. The second test case: 000 is similar to s[ 1. . 3] = 000; '
          '000 is similar to s[ 2. . 4] = 000; 000 is similar to s[ 3. . 5] = '
          '000. The third test case: 1010 is similar to s[ 1. . 4] = 1110; '
          '1010 is similar to s[ 2. . 5] = 1100; 1010 is similar to s[ 3. . 6] '
          '= 1000; 1010 is similar to s[ 4. . 7] = 0000. The fourth test case: '
          '00 is similar to s[ 1. . 2] = 10; 00 is similar to s[ 2. . 3] = 01.',
  'output': 'For each test case, print the corresponding binary string w of '
            'length n. If there are multiple such strings — print any of them. '
            'It can be shown that at least one string w meeting the '
            'constraints always exists.',
  'title': 'String Similarity',
  'topics': ['constructive algorithms', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1400/A'},
 {'history': 'You are given an integer value x and a string s consisting of '
             'digits from 1 to 9 inclusive. A substring of a string is a '
             'contiguous subsequence of that string. Let f( l, r) be the sum '
             "of digits of a substring s[ l. . r] . Let' s call substring s[ "
             'l1. . r1] x- prime if f( l1, r1) = x; there are no values l2, r2 '
             'such that l1≤l2≤r2≤r1; f( l2, r2) = ̸x; x is divisible by f( l2, '
             'r2) . You are allowed to erase some characters from the string. '
             'If you erase a character, the two resulting parts of the string '
             'are concatenated without changing their order. What is the '
             'minimum number of characters you should erase from the string so '
             'that there are no x- prime substrings in it? If there are no x- '
             'prime substrings in the given string s, then print 0.',
  'input': 'The first line contains a string s ( 1≤| s| ≤1000) . s contains '
           'only digits from 1 to 9 inclusive. The second line contains an '
           'integer x ( 1≤x≤20) .',
  'note': 'In the first example there are two 8- prime substrings " 8" and " '
          '53" . You can erase these characters to get rid of both: " '
          '116285317" . The resulting string " 1162317" contains no 8- prime '
          'substrings. Removing these characters is also a valid answer: " '
          '116285317" . In the second example you just have to erase both '
          'ones. In the third example there are no 13- prime substrings. There '
          'are no substrings with the sum of digits equal to 13 at all. In the '
          'fourth example you can have neither " 34" , nor " 43" in a string. '
          'Thus, you have to erase either all threes or all fours. There are 5 '
          "of each of them, so it doesn' t matter which.",
  'output': 'Print a single integer — the minimum number of characters you '
            'should erase from the string so that there are no x- prime '
            'substrings in it. If there are no x- prime substrings in the '
            'given string s, then print 0.',
  'title': 'x-prime Substrings',
  'topics': ['brute force',
             'dfs and similar',
             'dp',
             'string suffix structures',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1400/F'},
 {'history': 'Everybody knows that Balázs has the fanciest fence in the whole '
             "town. It' s built up from NN fancy sections. The sections are "
             'rectangles standing closely next to each other on the ground. '
             'The iith section has integer height hihi and integer width wiwi. '
             'We are looking for fancy rectangles on this fancy fence. A '
             'rectangle is fancy if: its sides are either horizontal or '
             'vertical and have integer lengths the distance between the '
             'rectangle and the ground is integer the distance between the '
             "rectangle and the left side of the first section is integer it' "
             's lying completely on sections What is the number of fancy '
             'rectangles? This number can be very big, so we are interested in '
             'it modulo 109+ 7109+ 7. Scoring '
             'Subtask1234567Points0121315151827ConstraintssampleN≤50andhi≤50andwi= '
             '1for allihi= 1orhi= 2for alliallhiare equalhi≤hi+ 1for '
             'alli≤N−1N≤1000no additional '
             'constraintsSubtaskPointsConstraints10sample212N≤50andhi≤50andwi= '
             '1for alli313hi= 1orhi= 2for alli415allhiare equal515hi≤hi+ 1for '
             'alli≤N−1618N≤1000727no additional constraints',
  'input': 'The first line contains NN ( 1≤N≤1051≤N≤105) – the number of '
           'sections. The second line contains NN space- separated integers, '
           'the iith number is hihi ( 1≤hi≤1091≤hi≤109) . The third line '
           'contains NN space- separated integers, the iith number is wiwi ( '
           '1≤wi≤1091≤wi≤109) .',
  'note': 'The fence looks like this: There are 5 fancy rectangles of shape: '
          'There are 3 fancy rectangles of shape: There is 1 fancy rectangle '
          'of shape: There are 2 fancy rectangles of shape: There is 1 fancy '
          'rectangle of shape:',
  'output': 'You should print a single integer, the number of fancy rectangles '
            'modulo 109+ 7109+ 7. So the output range is 0, 1, 2, . . . , 109+ '
            '60, 1, 2, . . . , 109+ 6.',
  'title': 'Fancy Fence',
  'topics': ['*special',
             'data structures',
             'dsu',
             'implementation',
             'math',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1402/A'},
 {'history': 'The government of Treeland wants to build a new road network. '
             'There are 2N2N cities in Treeland. The unfinished plan of the '
             'road network already contains N road segments, each of which '
             'connects two cities with a straight line. No two road segments '
             'have a common point ( including their endpoints) . Your task is '
             'to determine N−1 additional road segments satisfying the '
             'following conditions: Every new road segment must connect two '
             'cities with a straight line. If two segments ( new or old) have '
             'a common point, then this point must be an endpoint of both '
             'segments. The road network connects all cities: for each pair of '
             'cities there is a path consisting of segments that connects the '
             'two cities. Scoring SubtaskPointsConstraints10samples215all '
             'input segments are vertical. 315each pair of input segments are '
             'parallel. 415each input segment is either horizontal or '
             'vertical. 515N≤10000640no additional constraints',
  'input': 'The first line of the standard input contains N ( 2≤N≤105) – the '
           'number of existing road segments. Each of the following N lines '
           'contains four integers: x1, y1, x2, y2, where ( x1, y1) and ( x2, '
           'y2) are the coordinates of the endpoints of the segment ( −107≤xi, '
           'yi≤107) .',
  'note': '',
  'output': 'The standard output must contain N−1 lines, each of them '
            'containing four integers, x1, y1, x2, y2, where ( x1, y1) and ( '
            'x2, y2) are the coordinates of the cities that are the endpoints '
            'of a new road segment. If there are multiple solutions, your '
            'program may output any of them.',
  'title': 'Roads',
  'topics': ['*special', 'geometry', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1402/B'},
 {'history': 'Once upon a time, in the Land of the Shamans, everyone lived on '
             'the Sky- High Beanstalk. Each shaman had a unique identifying '
             'number ii between 00 and N−1N−1, and an altitude value HiHi, '
             'representing how high he lived above ground level. The distance '
             'between two altitudes is the absolute value of their difference. '
             'All shamans lived together in peace, until one of them stole the '
             'formula of the world- famous Potion of Great Power. To cover '
             'his/ her tracks, the Thief has put a Curse on the land: most '
             'inhabitants could no longer trust each other. . . Despite the '
             'very difficult circumstances, the Order of Good Investigators '
             'have gained the following information about the Curse: When the '
             'Curse first takes effect, everyone stops trusting each other. '
             'The Curse is unstable: at the end of each day ( exactly at '
             'midnight) , one pair of shamans will start or stop trusting each '
             'other. Unfortunately, each shaman will only ever trust at most '
             'DD others at any given time. They have also reconstructed a log '
             'of who trusted whom: for each night they know which pair of '
             'shamans started/ stopped trusting each other. They believe the '
             'Thief has whispered the formula to an Evil Shaman. To avoid '
             'detection, both of them visited the home of one of their ( '
             'respective) trusted friends. During the visit, the Thief '
             'whispered the formula to the Evil Shaman through the window. ( '
             'Note: this trusted friend did not have to be home at the time. '
             "In fact, it' s even possible that they visited each other' s "
             'houses – shamans are weird. ) Fortunately, whispers only travel '
             'short distances, so the Order knows the two trusted friends '
             'visited ( by the Thief and the Evil Shaman) must live very close '
             'to each other. They ask you to help with their investigation. '
             'They would like to test their suspicions: what if the Thief was '
             'xx, the Evil Shaman was yy, and the formula was whispered on day '
             'vv? What is the smallest distance the whispered formula had to '
             'travel? That is, what is the minimum distance between the '
             'apartments of some shamans x′x′ and y′y′ ( i. e. min( '
             '∣∣Hx′−Hy′∣∣) min( | Hx′−Hy′| ) ) , such that x′x′ was a trusted '
             'friend of xx and y′y′ was a trusted friend of yy on day vv? They '
             'will share all their information with you, then ask you a number '
             'of questions. You need to answer each question immediately, '
             'before receiving the next one. InteractionThe interaction will '
             'begin with a line containing NN, DD, UU and QQ ( 2≤N≤100000( '
             '2≤N≤100000, 1≤D≤5001≤D≤500, 0≤U≤2000000≤U≤200000, 1≤Q≤50000) '
             '1≤Q≤50000) – the number of shamans, the maximum number of '
             'trusted friends a shaman can have at any given point, the number '
             'of days, and the number of questions. On the next line NN space '
             'separated integers will follow, the iith ( 1≤i≤N) ( 1≤i≤N) of '
             'which being Hi−1Hi−1 ( 0≤Hi−1≤109) ( 0≤Hi−1≤109) , the altitude '
             'of shaman i−1i−1. On the next UU lines there will be two '
             'integers each, on the iith ( 1≤i≤U1≤i≤U) AiAi and BiBi ( 0≤Ai, '
             'Bi< N( 0≤Ai, Bi< N and Ai= ̸Bi) Ai= ̸Bi) , which represents a '
             'pair of shamans who started or stopped trusting each other at '
             'the end of day i−1i−1. That is, if AiAi and BiBi trusted each '
             'other on day i−1i−1, they did not trust each other on day ii, or '
             'vice versa. Read all of these integers. The interactor now will '
             'ask you QQ question, so the following interaction should happen '
             'QQ times: Read 33 integers describing the current query: x, yx, '
             'y and vv ( x= ̸yx= ̸y, 0≤x, y< N0≤x, y< N and 0≤v≤U0≤v≤U) , '
             'where xx is the suspected Thief, yy is the suspected Evil '
             'Shaman, and vv is the suspected day. . Then print the answer to '
             'this query on a single line, i. e. you should print the minimum '
             'distance the whispered formula had to travel from some trusted '
             'friend x′x′ of xx to a trusted friend y′y′ of yy. In case '
             'someone trusted both xx and yy ( i. e. x′= y′x′= y′) , you '
             'should print 00. If xx or yy had no trusted friends, print '
             '109109. After printing each line do not forget to output end of '
             'line and flush the output. Otherwise, you will get Idleness '
             'limit exceeded. To do this, use: fflush( stdout) or cout. flush( '
             ') in C+ + ; System. out. flush( ) in Java; flush( output) in '
             'Pascal; stdout. flush( ) in Python; see documentation for other '
             'languages. Scoring '
             'Subtask123456Points01714182130ConstraintssamplesQ, U≤1000v= Ufor '
             'all questionsHi∈0, 1for all shamansiU, N≤10000no additional '
             'constraintsSubtaskPointsConstraints10samples217Q, U≤1000314v= '
             'Ufor all questions418Hi∈0, 1for all shamansi521U, N≤10000630no '
             'additional constraints',
  'input': ' ',
  'note': 'Example queries: Evolution of friendships:',
  'output': ' ',
  'title': 'The Potion of Great Power',
  'topics': ['*special',
             '2-sat',
             'binary search',
             'data structures',
             'graphs',
             'interactive',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1403/A'},
 {'history': 'A bitstring is a string consisting only of the characters 0 and '
             '1. A bitstring is called k- balanced if every substring of size '
             'k of this bitstring has an equal amount of 0 and 1 characters ( '
             'k2 of each) . You are given an integer k and a string s which is '
             'composed only of characters 0, 1, and ? . You need to determine '
             'whether you can make a k- balanced bitstring by replacing every '
             '? characters in s with either 0 or 1. A string a is a substring '
             'of a string b if a can be obtained from b by deletion of several '
             '( possibly, zero or all) characters from the beginning and '
             'several ( possibly, zero or all) characters from the end.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤104) . Description of the test '
           'cases follows. The first line of each test case contains two '
           'integers n and k ( 2≤k≤n≤3⋅105, k is even) — the length of the '
           'string and the parameter for a balanced bitstring. The next line '
           'contains the string s ( | s| = n) . It is given that s consists of '
           'only 0, 1, and ? . It is guaranteed that the sum of n over all '
           'test cases does not exceed 3⋅105.',
  'note': 'For the first test case, the string is already a 4- balanced '
          'bitstring. For the second test case, the string can be transformed '
          'into 101. For the fourth test case, the string can be transformed '
          'into 0110. For the fifth test case, the string can be transformed '
          'into 1100110.',
  'output': 'For each test case, print YES if we can replace every ? in s with '
            '0 or 1 such that the resulting bitstring is k- balanced, or NO if '
            'it is not possible.',
  'title': 'Balanced Bitstring',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1404/A'},
 {'history': 'You are given an array of integers a1, a2, . . . , an. Find the '
             'maximum possible value of aiajakalat among all five indices ( i, '
             'j, k, l, t) ( i< j< k< l< t) .',
  'input': 'The input consists of multiple test cases. The first line contains '
           'an integer t ( 1≤t≤2⋅104) — the number of test cases. The '
           'description of the test cases follows. The first line of each test '
           'case contains a single integer n ( 5≤n≤105) — the size of the '
           'array. The second line of each test case contains n integers a1, '
           "a2, . . . , an ( −3×103≤ai≤3×103) — given array. It' s guaranteed "
           'that the sum of n over all test cases does not exceed 2⋅105.',
  'note': 'In the first test case, choosing a1, a2, a3, a4, a5 is a best '
          'choice: ( −1) ⋅( −2) ⋅( −3) ⋅( −4) ⋅( −5) = −120. In the second '
          'test case, choosing a1, a2, a3, a5, a6 is a best choice: ( −1) ⋅( '
          '−2) ⋅( −3) ⋅2⋅( −1) = 12. In the third test case, choosing a1, a2, '
          'a3, a4, a5 is a best choice: ( −1) ⋅0⋅0⋅0⋅( −1) = 0. In the fourth '
          'test case, choosing a1, a2, a3, a4, a6 is a best choice: ( −9) ⋅( '
          '−7) ⋅( −5) ⋅( −3) ⋅1= 945.',
  'output': 'For each test case, print one integer — the answer to the '
            'problem.',
  'title': 'Maximum Product',
  'topics': ['brute force', 'dp', 'greedy', 'implementation', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1406/B'},
 {'history': 'There are n robbers at coordinates ( a1, b1) , ( a2, b2) , . . . '
             ', ( an, bn) and m searchlight at coordinates ( c1, d1) , ( c2, '
             'd2) , . . . , ( cm, dm) . In one move you can move each robber '
             'to the right ( increase ai of each robber by one) or move each '
             'robber up ( increase bi of each robber by one) . Note that you '
             "should either increase all ai or all bi, you can' t increase ai "
             'for some points and bi for some other points. Searchlight j can '
             'see a robber i if ai≤cj and bi≤dj. A configuration of robbers is '
             'safe if no searchlight can see a robber ( i. e. if there is no '
             'pair i, j such that searchlight j can see a robber i) . What is '
             'the minimum number of moves you need to perform to reach a safe '
             'configuration?',
  'input': 'The first line of input contains two integers n and m ( 1≤n, '
           'm≤2000) : the number of robbers and the number of searchlight. '
           'Each of the next n lines contains two integers ai, bi ( 0≤ai, '
           'bi≤106) , coordinates of robbers. Each of the next m lines '
           'contains two integers ci, di ( 0≤ci, di≤106) , coordinates of '
           'searchlights.',
  'note': 'In the first test, you can move each robber to the right three '
          'times. After that there will be one robber in the coordinates ( 3, '
          '0) . The configuration of the robbers is safe, because the only '
          "searchlight can' t see the robber, because it is in the coordinates "
          '( 2, 3) and 3> 2. In the second test, you can move each robber to '
          'the right two times and two times up. After that robbers will be in '
          "the coordinates ( 3, 8) , ( 8, 3) . It' s easy the see that the "
          'configuration of the robbers is safe. It can be proved that you '
          "can' t reach a safe configuration using no more than 3 moves.",
  'output': 'Print one integer: the minimum number of moves you need to '
            'perform to reach a safe configuration.',
  'title': 'Searchlights',
  'topics': ['binary search',
             'brute force',
             'data structures',
             'dp',
             'implementation',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1408/D'},
 {'history': 'You are given mm sets of integers A1, A2, . . . , AmA1, A2, . . '
             '. , Am; elements of these sets are integers between 11 and nn, '
             'inclusive. There are two arrays of positive integers a1, a2, . . '
             '. , ama1, a2, . . . , am and b1, b2, . . . , bnb1, b2, . . . , '
             'bn. In one operation you can delete an element jj from the set '
             'AiAi and pay ai+ bjai+ bj coins for that. You can make several ( '
             'maybe none) operations ( some sets can become empty) . After '
             'that, you will make an edge- colored undirected graph consisting '
             'of nn vertices. For each set AiAi you will add an edge ( x, y) ( '
             'x, y) with color ii for all x, y∈Aix, y∈Ai and x< yx< y. Some '
             'pairs of vertices can be connected with more than one edge, but '
             'such edges have different colors. You call a cycle i1→e1→i2→e2→. '
             '. . →ik→ek→i1i1→e1→i2→e2→. . . →ik→ek→i1 ( ejej is some edge '
             'connecting vertices ijij and ij+ 1ij+ 1 in this graph) rainbow '
             'if all edges on it have different colors. Find the minimum '
             'number of coins you should pay to get a graph without rainbow '
             'cycles.',
  'input': 'The first line contains two integers mm and nn ( 1≤m, n≤1051≤m, '
           'n≤105) , the number of sets and the number of vertices in the '
           'graph. The second line contains mm integers a1, a2, . . . , ama1, '
           'a2, . . . , am ( 1≤ai≤1091≤ai≤109) . The third line contains nn '
           'integers b1, b2, . . . , bnb1, b2, . . . , bn ( 1≤bi≤1091≤bi≤109) '
           '. In the each of the next of mm lines there are descriptions of '
           'sets. In the ii- th line the first integer sisi ( 1≤si≤n1≤si≤n) is '
           'equal to the size of AiAi. Then sisi integers follow: the elements '
           'of the set AiAi. These integers are from 11 to nn and distinct. It '
           'is guaranteed that the sum of sisi for all 1≤i≤m1≤i≤m does not '
           'exceed 2⋅1052⋅105.',
  'note': 'In the first test, you can make such operations: Delete element 11 '
          'from set 11. You should pay a1+ b1= 5a1+ b1= 5 coins for that. '
          'Delete element 11 from set 22. You should pay a2+ b1= 6a2+ b1= 6 '
          'coins for that. You pay 1111 coins in total. After these '
          'operations, the first and the second sets will be equal to 22 and '
          'the third set will be equal to 1, 21, 2. So, the graph will consist '
          'of one edge ( 1, 2) ( 1, 2) of color 33. In the second test, you '
          'can make such operations: Delete element 11 from set 11. You should '
          'pay a1+ b1= 11a1+ b1= 11 coins for that. Delete element 44 from set '
          '22. You should pay a2+ b4= 13a2+ b4= 13 coins for that. Delete '
          'element 77 from set 33. You should pay a3+ b7= 13a3+ b7= 13 coins '
          'for that. Delete element 44 from set 44. You should pay a4+ b4= '
          '16a4+ b4= 16 coins for that. Delete element 77 from set 66. You '
          'should pay a6+ b7= 13a6+ b7= 13 coins for that. You pay 6666 coins '
          'in total. After these operations, the sets will be: 2, 32, 3; 11; '
          '1, 31, 3; 33; 3, 4, 5, 6, 73, 4, 5, 6, 7; 55; 88. We will get the '
          'graph: There are no rainbow cycles in it.',
  'output': 'Print one integer: the minimum number of coins you should pay for '
            'operations to avoid rainbow cycles in the obtained graph.',
  'title': 'Avoid Rainbow Cycles',
  'topics': ['data structures', 'dsu', 'graphs', 'greedy', 'sortings', 'trees'],
  'url': 'https://codeforces.com/problemset/problem/1408/E'},
 {'history': 'There are nn points on a plane. The ii- th point has coordinates '
             '( xi, yi) ( xi, yi) . You have two horizontal platforms, both of '
             'length kk. Each platform can be placed anywhere on a plane but '
             'it should be placed horizontally ( on the same yy- coordinate) '
             'and have integer borders. If the left border of the platform is '
             '( x, y) ( x, y) then the right border is ( x+ k, y) ( x+ k, y) '
             'and all points between borders ( including borders) belong to '
             'the platform. Note that platforms can share common points ( '
             'overlap) and it is not necessary to place both platforms on the '
             'same yy- coordinate. When you place both platforms on a plane, '
             'all points start falling down decreasing their yy- coordinate. '
             'If a point collides with some platform at some moment, the point '
             'stops and is saved. Points which never collide with any platform '
             'are lost. Your task is to find the maximum number of points you '
             'can save if you place both platforms optimally. You have to '
             'answer tt independent test cases. For better understanding, '
             'please read the Note section below to see a picture for the '
             'first test case.',
  'input': 'The first line of the input contains one integer tt ( '
           '1≤t≤2⋅1041≤t≤2⋅104) — the number of test cases. Then tt test cases '
           'follow. The first line of the test case contains two integers nn '
           'and kk ( 1≤n≤2⋅1051≤n≤2⋅105; 1≤k≤1091≤k≤109) — the number of '
           'points and the length of each platform, respectively. The second '
           'line of the test case contains nn integers x1, x2, . . . , xnx1, '
           'x2, . . . , xn ( 1≤xi≤1091≤xi≤109) , where xixi is xx- coordinate '
           'of the ii- th point. The third line of the input contains nn '
           'integers y1, y2, . . . , yny1, y2, . . . , yn ( 1≤yi≤1091≤yi≤109) '
           ', where yiyi is yy- coordinate of the ii- th point. All points are '
           'distinct ( there is no pair 1≤i< j≤n1≤i< j≤n such that xi= xjxi= '
           'xj and yi= yjyi= yj) . It is guaranteed that the sum of nn does '
           'not exceed 2⋅1052⋅105 ( ∑n≤2⋅105∑n≤2⋅105) .',
  'note': 'The picture corresponding to the first test case of the example: '
          'Blue dots represent the points, red segments represent the '
          'platforms. One of the possible ways is to place the first platform '
          'between points ( 1, −1) ( 1, −1) and ( 2, −1) ( 2, −1) and the '
          'second one between points ( 4, 3) ( 4, 3) and ( 5, 3) ( 5, 3) . '
          'Vectors represent how the points will fall down. As you can see, '
          "the only point we can' t save is the point ( 3, 7) ( 3, 7) so it "
          'falls down infinitely and will be lost. It can be proven that we '
          "can' t achieve better answer here. Also note that the point ( 5, 3) "
          "( 5, 3) doesn' t fall at all because it is already on the platform.",
  'output': 'For each test case, print the answer: the maximum number of '
            'points you can save if you place both platforms optimally.',
  'title': 'Two Platforms',
  'topics': ['binary search', 'dp', 'sortings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1409/E'},
 {'history': 'You are given two strings s and t consisting of lowercase Latin '
             'letters. The length of t is 2 ( i. e. this string consists only '
             'of two characters) . In one move, you can choose any character '
             'of s and replace it with any lowercase Latin letter. More '
             'formally, you choose some i and replace si ( the character at '
             "the position i) with some character from ' a' to ' z' . You want "
             'to do no more than k replacements in such a way that maximizes '
             'the number of occurrences of t in s as a subsequence. Recall '
             'that a subsequence is a sequence that can be derived from the '
             'given sequence by deleting zero or more elements without '
             'changing the order of the remaining elements.',
  'input': 'The first line of the input contains two integers n and k ( '
           '2≤n≤200; 0≤k≤n) — the length of s and the maximum number of moves '
           'you can make. The second line of the input contains the string s '
           'consisting of n lowercase Latin letters. The third line of the '
           'input contains the string t consisting of two lowercase Latin '
           'letters.',
  'note': 'In the first example, you can obtain the string " abab" replacing '
          "s1 with ' a' and s4 with ' b' . Then the answer is 3. In the second "
          'example, you can obtain the string " ssddsdd" and get the answer '
          '10. In the fourth example, you can obtain the string " aaacaaa" and '
          'get the answer 15.',
  'output': 'Print one integer — the maximum possible number of occurrences of '
            't in s as a subsequence if you replace no more than k characters '
            'in s optimally.',
  'title': 'Subsequences of Length Two',
  'topics': ['dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1409/F'},
 {'history': "Currently, XXOC' s rap is a string consisting of zeroes, ones, "
             'and question marks. Unfortunately, haters gonna hate. They will '
             'write x angry comments for every occurrence of subsequence 01 '
             'and y angry comments for every occurrence of subsequence 10. You '
             'should replace all the question marks with 0 or 1 in such a way '
             'that the number of angry comments would be as small as possible. '
             'String b is a subsequence of string a, if it can be obtained by '
             'removing some characters from a. Two occurrences of a '
             'subsequence are considered distinct if sets of positions of '
             'remaining characters are distinct.',
  'input': "The first line contains string s — XXOC' s rap ( 1≤| s| ≤105) . "
           'The second line contains two integers x and y — the number of '
           'angry comments XXOC will recieve for every occurrence of 01 and 10 '
           'accordingly ( 0≤x, y≤106) .',
  'note': 'In the first example one of the optimum ways to replace is 001. '
          'Then there will be 2 subsequences 01 and 0 subsequences 10. Total '
          'number of angry comments will be equal to 2⋅2+ 0⋅3= 4. In the '
          'second example one of the optimum ways to replace is 11111. Then '
          'there will be 0 subsequences 01 and 0 subsequences 10. Total number '
          'of angry comments will be equal to 0⋅13+ 0⋅37= 0. In the third '
          'example one of the optimum ways to replace is 1100. Then there will '
          'be 0 subsequences 01 and 4 subsequences 10. Total number of angry '
          'comments will be equal to 0⋅239+ 4⋅7= 28. In the fourth example one '
          'of the optimum ways to replace is 01101001. Then there will be 8 '
          'subsequences 01 and 8 subsequences 10. Total number of angry '
          'comments will be equal to 8⋅5+ 8⋅7= 96.',
  'output': 'Output a single integer — the minimum number of angry comments.',
  'title': 'Grime Zoo',
  'topics': ['brute force', 'greedy', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1411/D'},
 {'history': "You' ve got a string S consisting of n lowercase English letters "
             'from your friend. It turned out that this is a number written in '
             'poman numerals. The poman numeral system is long forgotten. All '
             "that' s left is the algorithm to transform number from poman "
             'numerals to the numeral system familiar to us. Characters of S '
             "are numbered from 1 to n from left to right. Let' s denote the "
             'value of S as f( S) , it is defined as follows: If | S| > 1, an '
             'arbitrary integer m ( 1≤m< | S| ) is chosen, and it is defined '
             'that f( S) = −f( S[ 1, m] ) + f( S[ m+ 1, | S| ] ) , where S[ l, '
             'r] denotes the substring of S from the l- th to the r- th '
             'position, inclusively. Otherwise S= c, where c is some English '
             'letter. Then f( S) = 2pos( c) , where pos( c) is the position of '
             'letter c in the alphabet ( pos( a) = 0, pos( z) = 25) . Note '
             'that m is chosen independently on each step. Your friend thinks '
             'it is possible to get f( S) = T by choosing the right m on every '
             'step. Is he right?',
  'input': 'The first line contains two integers n and T ( 2≤n≤105, '
           '−1015≤T≤1015) . The second line contains a string S consisting of '
           'n lowercase English letters.',
  'note': 'In the second example, you cannot get −7. But you can get 1, for '
          'example, as follows: First choose m= 1, then f( abc) = −f( a) + f( '
          'bc) f( a) = 20= 1 f( bc) = −f( b) + f( c) = −21+ 22= 2 In the end '
          'f( abc) = −1+ 2= 1',
  'output': 'Print " Yes" if it is possible to get the desired value. '
            'Otherwise, print " No" . You can print each letter in any case ( '
            'upper or lower) .',
  'title': 'Poman Numbers',
  'topics': ['bitmasks', 'greedy', 'math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1411/E'},
 {'history': 'After battling Shikamaru, Tayuya decided that her flute is too '
             'predictable, and replaced it with a guitar. The guitar has 66 '
             'strings and an infinite number of frets numbered from 11. '
             'Fretting the fret number jj on the ii- th string produces the '
             'note ai+ jai+ j. Tayuya wants to play a melody of nn notes. Each '
             'note can be played on different string- fret combination. The '
             'easiness of performance depends on the difference between the '
             'maximal and the minimal indices of used frets. The less this '
             'difference is, the easier it is to perform the technique. Please '
             'determine the minimal possible difference. For example, if a= [ '
             '1, 1, 2, 2, 3, 3] a= [ 1, 1, 2, 2, 3, 3] , and the sequence of '
             'notes is 4, 11, 11, 12, 12, 13, 134, 11, 11, 12, 12, 13, 13 ( '
             'corresponding to the second example) , we can play the first '
             'note on the first string, and all the other notes on the sixth '
             'string. Then the maximal fret will be 1010, the minimal one will '
             'be 33, and the answer is 10−3= 710−3= 7, as shown on the '
             'picture.',
  'input': 'The first line contains 66 space- separated numbers a1a1, a2a2, . '
           ". . , a6a6 ( 1≤ai≤1091≤ai≤109) which describe the Tayuya' s "
           'strings. The second line contains the only integer nn ( '
           '1≤n≤1000001≤n≤100000) standing for the number of notes in the '
           'melody. The third line consists of nn integers b1b1, b2b2, . . . , '
           'bnbn ( 1≤bi≤1091≤bi≤109) , separated by space. They describe the '
           "notes to be played. It' s guaranteed that bi> ajbi> aj for all "
           '1≤i≤n1≤i≤n and 1≤j≤61≤j≤6, in other words, you can play each note '
           'on any string.',
  'note': 'In the first sample test it is optimal to play the first note on '
          'the first string, the second note on the second string, the third '
          'note on the sixth string, the fourth note on the fourth string, the '
          'fifth note on the fifth string, and the sixth note on the third '
          'string. In this case the 100100- th fret is used each time, so the '
          "difference is 100−100= 0100−100= 0. In the second test it' s "
          'optimal, for example, to play the second note on the first string, '
          'and all the other notes on the sixth string. Then the maximal fret '
          'will be 1010, the minimal one will be 33, and the answer is 10−3= '
          '710−3= 7.',
  'output': 'Print the minimal possible difference of the maximal and the '
            'minimal indices of used frets.',
  'title': 'Perform Easily',
  'topics': ['binary search',
             'brute force',
             'dp',
             'implementation',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1413/C'},
 {'history': 'You are given an array a consisting of n non- negative integers. '
             'You have to choose a non- negative integer x and form a new '
             'array b of size n according to the following rule: for all i '
             'from 1 to n, bi= ai⊕x ( ⊕ denotes the operation bitwise XOR) . '
             'An inversion in the b array is a pair of integers i and j such '
             'that 1≤i< j≤n and bi> bj. You should choose x in such a way that '
             'the number of inversions in b is minimized. If there are several '
             'options for x — output the smallest one.',
  'input': 'First line contains a single integer n ( 1≤n≤3⋅105) — the number '
           'of elements in a. Second line contains n space- separated integers '
           'a1, a2, . . . , an ( 0≤ai≤109) , where ai is the i- th element of '
           'a.',
  'note': 'In the first sample it is optimal to leave the array as it is by '
          'choosing x= 0. In the second sample the selection of x= 14 results '
          'in b: [ 4, 9, 7, 4, 9, 11, 11, 13, 11] . It has 4 inversions: i= 2, '
          'j= 3; i= 2, j= 4; i= 3, j= 4; i= 8, j= 9. In the third sample the '
          'selection of x= 8 results in b: [ 0, 2, 11] . It has no inversions.',
  'output': 'Output two integers: the minimum possible number of inversions in '
            'b, and the minimum possible value of x, which achieves those '
            'number of inversions.',
  'title': 'XOR Inverse',
  'topics': ['bitmasks',
             'data structures',
             'divide and conquer',
             'dp',
             'greedy',
             'math',
             'sortings',
             'strings',
             'trees'],
  'url': 'https://codeforces.com/problemset/problem/1416/C'},
 {'history': 'RedDreamer has an array a consisting of n non- negative '
             "integers, and an unlucky integer T. Let' s denote the misfortune "
             'of array b having length m as f( b) — the number of pairs of '
             'integers ( i, j) such that 1≤i< j≤m and bi+ bj= T. RedDreamer '
             'has to paint each element of a into one of two colors, white and '
             'black ( for each element, the color is chosen independently) , '
             'and then create two arrays c and d so that all white elements '
             'belong to c, and all black elements belong to d ( it is possible '
             'that one of these two arrays becomes empty) . RedDreamer wants '
             'to paint the elements in such a way that f( c) + f( d) is '
             'minimum possible. For example: if n= 6, T= 7 and a= [ 1, 2, 3, '
             '4, 5, 6] , it is possible to paint the 1- st, the 4- th and the '
             '5- th elements white, and all other elements black. So c= [ 1, '
             '4, 5] , d= [ 2, 3, 6] , and f( c) + f( d) = 0+ 0= 0; if n= 3, T= '
             '6 and a= [ 3, 3, 3] , it is possible to paint the 1- st element '
             'white, and all other elements black. So c= [ 3] , d= [ 3, 3] , '
             'and f( c) + f( d) = 0+ 1= 1. Help RedDreamer to paint the array '
             'optimally!',
  'input': 'The first line contains one integer t ( 1≤t≤1000) — the number of '
           'test cases. Then t test cases follow. The first line of each test '
           'case contains two integers n and T ( 1≤n≤105, 0≤T≤109) — the '
           'number of elements in the array and the unlucky integer, '
           'respectively. The second line contains n integers a1, a2, . . . , '
           'an ( 0≤ai≤109) — the elements of the array. The sum of n over all '
           'test cases does not exceed 105.',
  'note': ' ',
  'output': 'For each test case print n integers: p1, p2, . . . , pn ( each pi '
            'is either 0 or 1) denoting the colors. If pi is 0, then ai is '
            'white and belongs to the array c, otherwise it is black and '
            'belongs to the array d. If there are multiple answers that '
            'minimize the value of f( c) + f( d) , print any of them.',
  'title': 'Two Arrays',
  'topics': ['greedy', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1417/B'},
 {'history': 'You are given an array a, consisting of n integers. Each '
             'position i ( 1≤i≤n) of the array is either locked or unlocked. '
             'You can take the values on the unlocked positions, rearrange '
             'them in any order and place them back into the unlocked '
             'positions. You are not allowed to remove any values, add the new '
             'ones or rearrange the values on the locked positions. You are '
             'allowed to leave the values in the same order as they were. For '
             'example, let a= [ −1, 1, 3_ , 2, −2_ , 1, −4, 0_ ] , the '
             'underlined positions are locked. You can obtain the following '
             'arrays: [ −1, 1, 3_ , 2, −2_ , 1, −4, 0_ ] ; [ −4, −1, 3_ , 2, '
             '−2_ , 1, 1, 0_ ] ; [ 1, −1, 3_ , 2, −2_ , 1, −4, 0_ ] ; [ 1, 2, '
             '3_ , −1, −2_ , −4, 1, 0_ ] ; and some others. Let p be a '
             'sequence of prefix sums of the array a after the rearrangement. '
             'So p1= a1, p2= a1+ a2, p3= a1+ a2+ a3, . . . , pn= a1+ a2+ ⋯+ '
             'an. Let k be the maximum j ( 1≤j≤n) such that pj< 0. If there '
             'are no j such that pj< 0, then k= 0. Your goal is to rearrange '
             'the values in such a way that k is minimum possible. Output the '
             'array a after the rearrangement such that the value k for it is '
             'minimum possible. If there are multiple answers then print any '
             'of them.',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of testcases. Then t testcases follow. The first line of '
           'each testcase contains a single integer n ( 1≤n≤100) — the number '
           'of elements in the array a. The second line of each testcase '
           'contains n integers a1, a2, . . . , an ( −105≤ai≤105) — the '
           'initial array a. The third line of each testcase contains n '
           'integers l1, l2, . . . , ln ( 0≤li≤1) , where li= 0 means that the '
           'position i is unlocked and li= 1 means that the position i is '
           'locked.',
  'note': 'In the first testcase you can rearrange all values however you want '
          'but any arrangement will result in k= 0. For example, for an '
          'arrangement [ 1, 2, 3] , p= [ 1, 3, 6] , so there are no j such '
          'that pj< 0. Thus, k= 0. In the second testcase you are not allowed '
          'to rearrange any elements. Thus, the printed array should be '
          'exactly the same as the initial one. In the third testcase the '
          'prefix sums for the printed array are p= [ −8, −14, −13, −9, −5, 2, '
          '0] . The maximum j is 5, thus k= 5. There are no arrangements such '
          'that k< 5. In the fourth testcase p= [ −4, −4, −3, 3, 6] . In the '
          'fifth testcase p= [ −1, 3, 10, 2, 12, 11] .',
  'output': 'Print n integers — the array a after the rearrangement. Value k ( '
            'the maximum j such that pj< 0 ( or 0 if there are no such j) ) '
            'should be minimum possible. For each locked position the printed '
            'value should be equal to the initial one. The values on the '
            'unlocked positions should be an arrangement of the initial ones. '
            'If there are multiple answers then print any of them.',
  'title': 'Negative Prefixes',
  'topics': ['greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1418/B'},
 {'history': 'This is the easy version of the problem. The difference between '
             'the versions is that in the easy version all prices ai are '
             'different. You can make hacks if and only if you solved both '
             "versions of the problem. Today is Sage' s birthday, and she will "
             'go shopping to buy ice spheres. All n ice spheres are placed in '
             'a row and they are numbered from 1 to n from left to right. Each '
             'ice sphere has a positive integer price. In this version all '
             'prices are different. An ice sphere is cheap if it costs '
             'strictly less than two neighboring ice spheres: the nearest to '
             'the left and the nearest to the right. The leftmost and the '
             'rightmost ice spheres are not cheap. Sage will choose all cheap '
             'ice spheres and then buy only them. You can visit the shop '
             'before Sage and reorder the ice spheres as you wish. Find out '
             'the maximum number of ice spheres that Sage can buy, and show '
             'how the ice spheres should be reordered.',
  'input': 'The first line contains a single integer n ( 1≤n≤105) — the number '
           'of ice spheres in the shop. The second line contains n different '
           'integers a1, a2, . . . , an ( 1≤ai≤109) — the prices of ice '
           'spheres.',
  'note': "In the example it' s not possible to place ice spheres in any order "
          'so that Sage would buy 3 of them. If the ice spheres are placed '
          'like this ( 3, 1, 4, 2, 5) , then Sage will buy two spheres: one '
          'for 1 and one for 2, because they are cheap.',
  'output': 'In the first line print the maximum number of ice spheres that '
            'Sage can buy. In the second line print the prices of ice spheres '
            'in the optimal order. If there are several correct answers, you '
            'can print any of them.',
  'title': "Sage's Birthday (easy version)",
  'topics': ['binary search', 'constructive algorithms', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1419/D1'},
 {'history': 'This is the hard version of the problem. The difference between '
             'the versions is that in the easy version all prices ai are '
             'different. You can make hacks if and only if you solved both '
             "versions of the problem. Today is Sage' s birthday, and she will "
             'go shopping to buy ice spheres. All n ice spheres are placed in '
             'a row and they are numbered from 1 to n from left to right. Each '
             'ice sphere has a positive integer price. In this version, some '
             'prices can be equal. An ice sphere is cheap if it costs strictly '
             'less than two neighboring ice spheres: the nearest to the left '
             'and the nearest to the right. The leftmost and the rightmost ice '
             'spheres are not cheap. Sage will choose all cheap ice spheres '
             'and then buy only them. You can visit the shop before Sage and '
             'reorder the ice spheres as you wish. Find out the maximum number '
             'of ice spheres that Sage can buy, and show how the ice spheres '
             'should be reordered.',
  'input': 'The first line contains a single integer n ( 1≤n≤105) — the number '
           'of ice spheres in the shop. The second line contains n integers '
           'a1, a2, . . . , an ( 1≤ai≤109) — the prices of ice spheres.',
  'note': "In the sample it' s not possible to place the ice spheres in any "
          'order so that Sage would buy 4 of them. If the spheres are placed '
          'in the order ( 3, 1, 4, 2, 4, 2, 5) , then Sage will buy one sphere '
          'for 1 and two spheres for 2 each.',
  'output': 'In the first line print the maximum number of ice spheres that '
            'Sage can buy. In the second line print the prices of ice spheres '
            'in the optimal order. If there are several correct answers, you '
            'can print any of them.',
  'title': "Sage's Birthday (hard version)",
  'topics': ['binary search',
             'brute force',
             'constructive algorithms',
             'greedy',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1419/D2'},
 {'history': "For god' s sake, you' re boxes with legs! It is literally your "
             'only purpose! Walking onto buttons! How can you not do the one '
             "thing you were designed for? Oh, that' s funny, is it? Oh it' s "
             "funny? Because we' ve been at this for twelve hours and you "
             "haven' t solved it either, so I don' t know why you' re "
             "laughing. You' ve got one hour! Solve it! Wheatley decided to "
             'try to make a test chamber. He made a nice test chamber, but '
             'there was only one detail absent — cubes. For completing the '
             'chamber Wheatley needs n cubes. i- th cube has a volume ai. '
             'Wheatley has to place cubes in such a way that they would be '
             'sorted in a non- decreasing order by their volume. Formally, for '
             'each i> 1, ai−1≤ai must hold. To achieve his goal, Wheatley can '
             'exchange two neighbouring cubes. It means that for any i> 1 you '
             'can exchange cubes on positions i−1 and i. But there is a '
             'problem: Wheatley is very impatient. If Wheatley needs more than '
             "n⋅( n−1) 2−1 exchange operations, he won' t do this boring work. "
             'Wheatly wants to know: can cubes be sorted under this '
             'conditions?',
  'input': 'Each test contains multiple test cases. The first line contains '
           'one positive integer t ( 1≤t≤1000) , denoting the number of test '
           'cases. Description of the test cases follows. The first line of '
           'each test case contains one positive integer n ( 2≤n≤5⋅104) — '
           'number of cubes. The second line contains n positive integers ai ( '
           '1≤ai≤109) — volumes of cubes. It is guaranteed that the sum of n '
           'over all test cases does not exceed 105.',
  'note': 'In the first test case it is possible to sort all the cubes in 7 '
          'exchanges. In the second test case the cubes are already sorted. In '
          'the third test case we can make 0 exchanges, but the cubes are not '
          'sorted yet, so the answer is " NO" .',
  'output': 'For each test case, print a word in a single line: " YES" ( '
            'without quotation marks) if the cubes can be sorted and " NO" ( '
            'without quotation marks) otherwise.',
  'title': 'Cubes Sorting',
  'topics': ['math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1420/A'},
 {'history': 'Ori and Sein have overcome many difficult challenges. They '
             'finally lit the Shrouded Lantern and found Gumon Seal, the key '
             'to the Forlorn Ruins. When they tried to open the door to the '
             'ruins. . . nothing happened. Ori was very surprised, but Sein '
             'gave the explanation quickly: clever Gumon decided to make an '
             'additional defence for the door. There are n lamps with Spirit '
             "Tree' s light. Sein knows the time of turning on and off for the "
             'i- th lamp — li and ri respectively. To open the door you have '
             'to choose k lamps in such a way that there will be a moment of '
             'time when they all will be turned on. While Sein decides which '
             'of the k lamps to pick, Ori is interested: how many ways there '
             'are to pick such k lamps that the door will open? It may happen '
             'that Sein may be wrong and there are no such k lamps. The answer '
             'might be large, so print it modulo 998244353.',
  'input': 'First line contains two integers n and k ( 1≤n≤3⋅105, 1≤k≤n) — '
           'total number of lamps and the number of lamps that must be turned '
           'on simultaneously. Next n lines contain two integers li ans ri ( '
           '1≤li≤ri≤109) — period of time when i- th lamp is turned on.',
  'note': 'In first test case there are nine sets of k lamps: ( 1, 2, 3) , ( '
          '1, 2, 4) , ( 1, 2, 5) , ( 1, 2, 6) , ( 1, 3, 6) , ( 1, 4, 6) , ( 2, '
          '3, 6) , ( 2, 4, 6) , ( 2, 6, 7) . In second test case k= 1, so the '
          'answer is 3. In third test case there are no such pairs of lamps. '
          'In forth test case all lamps are turned on in a time 3, so the '
          'answer is 1. In fifth test case there are seven sets of k lamps: ( '
          '1, 2) , ( 1, 3) , ( 2, 3) , ( 2, 4) , ( 3, 4) , ( 3, 5) , ( 4, 5) .',
  'output': 'Print one integer — the answer to the task modulo 998244353.',
  'title': 'Rescue Nibel!',
  'topics': ['combinatorics', 'data structures', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1420/D'},
 {'history': 'Ringo found a string s of length n in his yellow submarine. The '
             'string contains only lowercase letters from the English '
             'alphabet. As Ringo and his friends love palindromes, he would '
             'like to turn the string s into a palindrome by applying two '
             'types of operations to the string. The first operation allows '
             'him to choose i ( 2≤i≤n−1) and to append the substring s2s3. . . '
             'si ( i−1 characters) reversed to the front of s. The second '
             'operation allows him to choose i ( 2≤i≤n−1) and to append the '
             'substring sisi+ 1. . . sn−1 ( n−i characters) reversed to the '
             'end of s. Note that characters in the string in this problem are '
             'indexed from 1. For example suppose s= abcdef. If he performs '
             'the first operation with i= 3 then he appends cb to the front of '
             's and the result will be cbabcdef. Performing the second '
             'operation on the resulted string with i= 5 will yield '
             'cbabcdefedc. Your task is to help Ringo make the entire string a '
             'palindrome by applying any of the two operations ( in total) at '
             'most 30 times. The length of the resulting palindrome must not '
             'exceed 106It is guaranteed that under these constraints there '
             'always is a solution. Also note you do not have to minimize '
             'neither the number of operations applied, nor the length of the '
             'resulting string, but they have to fit into the constraints.',
  'input': 'The only line contains the string S ( 3≤| s| ≤105) of lowercase '
           'letters from the English alphabet.',
  'note': 'For the first example the following operations are performed: abac '
          '→ abacab → abacabaThe second sample performs the following '
          'operations: acccc → cccacccc → ccccaccccThe third example is '
          'already a palindrome so no operations are required.',
  'output': 'The first line should contain k ( 0≤k≤30) — the number of '
            'operations performed. Each of the following k lines should '
            'describe an operation in form L i or R i. L represents the first '
            'operation, R represents the second operation, i represents the '
            'index chosen. The length of the resulting palindrome must not '
            'exceed 106.',
  'title': 'Palindromifier',
  'topics': ['constructive algorithms', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1421/C'},
 {'history': 'Yura has been walking for some time already and is planning to '
             'return home. He needs to get home as fast as possible. To do '
             'this, Yura can use the instant- movement locations around the '
             "city. Let' s represent the city as an area of n×n square blocks. "
             'Yura needs to move from the block with coordinates ( sx, sy) to '
             'the block with coordinates ( fx, fy) . In one minute Yura can '
             'move to any neighboring by side block; in other words, he can '
             'move in four directions. Also, there are m instant- movement '
             'locations in the city. Their coordinates are known to you and '
             'Yura. Yura can move to an instant- movement location in no time '
             'if he is located in a block with the same coordinate x or with '
             'the same coordinate y as the location. Help Yura to find the '
             'smallest time needed to get home.',
  'input': 'The first line contains two integers n and m — the size of the '
           'city and the number of instant- movement locations ( 1≤n≤109, '
           '0≤m≤105) . The next line contains four integers sx sy fx fy — the '
           "coordinates of Yura' s initial position and the coordinates of his "
           'home ( 1≤sx, sy, fx, fy≤n) . Each of the next m lines contains two '
           'integers xi yi — coordinates of the i- th instant- movement '
           'location ( 1≤xi, yi≤n) .',
  'note': 'In the first example Yura needs to reach ( 5, 5) from ( 1, 1) . He '
          'can do that in 5 minutes by first using the second instant- '
          "movement location ( because its y coordinate is equal to Yura' s y "
          'coordinate) , and then walking ( 4, 1) →( 4, 2) →( 4, 3) →( 5, 3) '
          '→( 5, 4) →( 5, 5) .',
  'output': 'In the only line print the minimum time required to get home.',
  'title': 'Returning Home',
  'topics': ['graphs', 'shortest paths', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1422/D'},
 {'history': 'Some time ago Lesha found an entertaining string s consisting of '
             'lowercase English letters. Lesha immediately developed an unique '
             'algorithm for this string and shared it with you. The algorithm '
             'is as follows. Lesha chooses an arbitrary ( possibly zero) '
             'number of pairs on positions ( i, i+ 1) in such a way that the '
             'following conditions are satisfied: for each pair ( i, i+ 1) the '
             'inequality 0≤i< | s| −1 holds; for each pair ( i, i+ 1) the '
             'equality si= si+ 1 holds; there is no index that is contained in '
             'more than one pair. After that Lesha removes all characters on '
             'indexes contained in these pairs and the algorithm is over. '
             'Lesha is interested in the lexicographically smallest strings he '
             'can obtain by applying the algorithm to the suffixes of the '
             'given string.',
  'input': 'The only line contains the string s ( 1≤| s| ≤105) — the initial '
           'string consisting of lowercase English letters only.',
  'note': 'Consider the first example. The longest suffix is the whole string '
          '" abcdd" . Choosing one pair ( 4, 5) , Lesha obtains " abc" . The '
          'next longest suffix is " bcdd" . Choosing one pair ( 3, 4) , we '
          'obtain " bc" . The next longest suffix is " cdd" . Choosing one '
          'pair ( 2, 3) , we obtain " c" . The next longest suffix is " dd" . '
          'Choosing one pair ( 1, 2) , we obtain " " ( an empty string) . The '
          'last suffix is the string " d" . No pair can be chosen, so the '
          'answer is " d" . In the second example, for the longest suffix " '
          'abbcdddeaaffdfouurtytwoo" choose three pairs ( 11, 12) , ( 16, 17) '
          ', ( 23, 24) and we obtain " abbcdddeaadfortytw"',
  'output': 'In | s| lines print the lengths of the answers and the answers '
            'themselves, starting with the answer for the longest suffix. The '
            'output can be large, so, when some answer is longer than 10 '
            'characters, instead print the first 5 characters, then " . . . " '
            ', then the last 2 characters of the answer.',
  'title': 'Minlexes',
  'topics': ['dp', 'greedy', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1422/E'},
 {'history': 'During one of the space missions, humans have found an evidence '
             'of previous life at one of the planets. They were lucky enough '
             'to find a book with birth and death years of each individual '
             "that had been living at this planet. What' s interesting is that "
             'these years are in the range ( 1, 109) ! Therefore, the planet '
             "was named Longlifer. In order to learn more about Longlifer' s "
             'previous population, scientists need to determine the year with '
             'maximum number of individuals that were alive, as well as the '
             'number of alive individuals in that year. Your task is to help '
             'scientists solve this problem!',
  'input': 'The first line contains an integer n ( 1≤n≤105) — the number of '
           'people. Each of the following n lines contain two integers b and d '
           '( 1≤b< d≤109) representing birth and death year ( respectively) of '
           'each individual.',
  'note': 'You can assume that an individual living from b to d has been born '
          'at the beginning of b and died at the beginning of d, and therefore '
          'living for d - b years.',
  'output': 'Print two integer numbers separated by blank character, y — the '
            'year with a maximum number of people alive and k — the number of '
            'people alive in year y. In the case of multiple possible '
            'solutions, print the solution with minimum year.',
  'title': 'Years',
  'topics': ['data structures', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1424/G'},
 {'history': 'While exploring the old caves, researchers found a book, or more '
             'precisely, a stash of mixed pages from a book. Luckily, all of '
             'the original pages are present and each page contains its '
             'number. Therefore, the researchers can reconstruct the book. '
             'After taking a deeper look into the contents of these pages, '
             "linguists think that this may be some kind of dictionary. What' "
             's interesting is that this ancient civilization used an alphabet '
             'which is a subset of the English alphabet, however, the order of '
             'these letters in the alphabet is not like the one in the English '
             'language. Given the contents of pages that researchers have '
             'found, your task is to reconstruct the alphabet of this ancient '
             'civilization using the provided pages from the dictionary.',
  'input': 'First- line contains two integers: n and k ( 1≤n, k≤103) — the '
           'number of pages that scientists have found and the number of words '
           'present at each page. Following n groups contain a line with a '
           'single integer pi ( 0≤n< 103) — the number of i- th page, as well '
           'as k lines, each line containing one of the strings ( up to 100 '
           'characters) written on the page numbered pi.',
  'note': ' ',
  'output': 'Output a string representing the reconstructed alphabet of this '
            'ancient civilization. If the book found is not a dictionary, '
            'output " IMPOSSIBLE" without quotes. In case there are multiple '
            'solutions, output any of them.',
  'title': 'Ancient Language',
  'topics': ['graphs', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1424/M'},
 {'history': 'Kolya got an integer array a1, a2, . . . , an. The array can '
             "contain both positive and negative integers, but Kolya doesn' t "
             "like 0, so the array doesn' t contain any zeros. Kolya doesn' t "
             'like that the sum of some subsegments of his array can be 0. The '
             'subsegment is some consecutive segment of elements of the array. '
             'You have to help Kolya and change his array in such a way that '
             "it doesn' t contain any subsegments with the sum 0. To reach "
             'this goal, you can insert any integers between any pair of '
             'adjacent elements of the array ( integers can be really any: '
             'positive, negative, 0, any by absolute value, even such a huge '
             "that they can' t be represented in most standard programming "
             'languages) . Your task is to find the minimum number of integers '
             "you have to insert into Kolya' s array in such a way that the "
             "resulting array doesn' t contain any subsegments with the sum 0.",
  'input': 'The first line of the input contains one integer n ( 2≤n≤200000) — '
           "the number of elements in Kolya' s array. The second line of the "
           'input contains n integers a1, a2, . . . , an ( −109≤ai≤109, ai= '
           "̸0) — the description of Kolya' s array.",
  'note': 'Consider the first example. There is only one subsegment with the '
          'sum 0. It starts in the second element and ends in the fourth '
          "element. It' s enough to insert one element so the array doesn' t "
          'contain any subsegments with the sum equal to zero. For example, it '
          'is possible to insert the integer 1 between second and third '
          'elements of the array. There are no subsegments having sum 0 in the '
          "second example so you don' t need to do anything.",
  'output': 'Print the minimum number of integers you have to insert into '
            "Kolya' s array in such a way that the resulting array doesn' t "
            'contain any subsegments with the sum 0.',
  'title': 'Non-zero Segments',
  'topics': ['constructive algorithms',
             'data structures',
             'greedy',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1426/D'},
 {'history': 'You are given a string s consisting of lowercase Latin letters " '
             'a" , " b" and " c" and question marks " ? " . Let the number of '
             "question marks in the string s be k. Let' s replace each "
             'question mark with one of the letters " a" , " b" and " c" . '
             'Here we can obtain all 3k possible strings consisting only of '
             'letters " a" , " b" and " c" . For example, if s= " ac? b? c" '
             'then we can obtain the following strings: [ " acabac" , " '
             'acabbc" , " acabcc" , " acbbac" , " acbbbc" , " acbbcc" , " '
             'accbac" , " accbbc" , " accbcc" ] . Your task is to count the '
             'total number of subsequences " abc" in all resulting strings. '
             'Since the answer can be very large, print it modulo 109+ 7. A '
             'subsequence of the string t is such a sequence that can be '
             'derived from the string t after removing some ( possibly, zero) '
             'number of letters without changing the order of remaining '
             'letters. For example, the string " baacbc" contains two '
             'subsequences " abc" — a subsequence consisting of letters at '
             'positions ( 2, 5, 6) and a subsequence consisting of letters at '
             'positions ( 3, 5, 6) .',
  'input': 'The first line of the input contains one integer n ( 3≤n≤200000) — '
           'the length of s. The second line of the input contains the string '
           's of length n consisting of lowercase Latin letters " a" , " b" '
           'and " c" and question marks" ? " .',
  'note': 'In the first example, we can obtain 9 strings: " acabac" — there '
          'are 2 subsequences " abc" , " acabbc" — there are 4 subsequences " '
          'abc" , " acabcc" — there are 4 subsequences " abc" , " acbbac" — '
          'there are 2 subsequences " abc" , " acbbbc" — there are 3 '
          'subsequences " abc" , " acbbcc" — there are 4 subsequences " abc" , '
          '" accbac" — there is 1 subsequence " abc" , " accbbc" — there are 2 '
          'subsequences " abc" , " accbcc" — there are 2 subsequences " abc" . '
          'So, there are 2+ 4+ 4+ 2+ 3+ 4+ 1+ 2+ 2= 24 subsequences " abc" in '
          'total.',
  'output': 'Print the total number of subsequences " abc" in all strings you '
            'can obtain if you replace all question marks with letters " a" , '
            '" b" and " c" , modulo 109+ 7.',
  'title': 'Number of Subsequences',
  'topics': ['combinatorics', 'dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1426/F'},
 {'history': 'You are given an array of n integers a1, a2, . . . , an. You '
             'have to create an array of n integers b1, b2, . . . , bn such '
             'that: The array b is a rearrangement of the array a, that is, it '
             'contains the same values and each value appears the same number '
             'of times in the two arrays. In other words, the multisets a1, '
             'a2, . . . , an and b1, b2, . . . , bn are equal. For example, if '
             'a= [ 1, −1, 0, 1] , then b= [ −1, 1, 1, 0] and b= [ 0, 1, −1, 1] '
             'are rearrangements of a, but b= [ 1, −1, −1, 0] and b= [ 1, 0, '
             '2, −3] are not rearrangements of a. For all k= 1, 2, . . . , n '
             'the sum of the first k elements of b is nonzero. Formally, for '
             'all k= 1, 2, . . . , n, it must hold b1+ b2+ ⋯+ bk= ̸0. If an '
             'array b1, b2, . . . , bn with the required properties does not '
             'exist, you have to print NO.',
  'input': 'Each test contains multiple test cases. The first line contains an '
           'integer t ( 1≤t≤1000) — the number of test cases. The description '
           'of the test cases follows. The first line of each testcase '
           'contains one integer n ( 1≤n≤50) — the length of the array a. The '
           'second line of each testcase contains n integers a1, a2, . . . , '
           'an ( −50≤ai≤50) — the elements of a.',
  'note': 'Explanation of the first testcase: An array with the desired '
          'properties is b= [ 1, −2, 3, −4] . For this array, it holds: The '
          'first element of b is 1. The sum of the first two elements of b is '
          '−1. The sum of the first three elements of b is 2. The sum of the '
          'first four elements of b is −2. Explanation of the second testcase: '
          'Since all values in a are 0, any rearrangement b of a will have all '
          'elements equal to 0 and therefore it clearly cannot satisfy the '
          'second property described in the statement ( for example because '
          'b1= 0) . Hence in this case the answer is NO. Explanation of the '
          'third testcase: An array with the desired properties is b= [ 1, 1, '
          '−1, 1, −1] . For this array, it holds: The first element of b is 1. '
          'The sum of the first two elements of b is 2. The sum of the first '
          'three elements of b is 1. The sum of the first four elements of b '
          'is 2. The sum of the first five elements of b is 1. Explanation of '
          'the fourth testcase: An array with the desired properties is b= [ '
          '−40, 13, 40, 0, −9, −31] . For this array, it holds: The first '
          'element of b is −40. The sum of the first two elements of b is −27. '
          'The sum of the first three elements of b is 13. The sum of the '
          'first four elements of b is 13. The sum of the first five elements '
          'of b is 4. The sum of the first six elements of b is −27.',
  'output': 'For each testcase, if there is not an array b1, b2, . . . , bn '
            'with the required properties, print a single line with the word '
            'NO. Otherwise print a line with the word YES, followed by a line '
            'with the n integers b1, b2, . . . , bn. If there is more than one '
            'array b1, b2, . . . , bn satisfying the required properties, you '
            'can print any of them.',
  'title': 'Avoiding Zero',
  'topics': ['math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1427/A'},
 {'history': 'You like playing chess tournaments online. In your last '
             'tournament you played n games. For the sake of this problem, '
             'each chess game is either won or lost ( no draws) . When you '
             'lose a game you get 0 points. When you win you get 1 or 2 '
             'points: if you have won also the previous game you get 2 points, '
             'otherwise you get 1 point. If you win the very first game of the '
             'tournament you get 1 point ( since there is not a " previous '
             'game" ) . The outcomes of the n games are represented by a '
             'string s of length n: the i- th character of s is W if you have '
             'won the i- th game, while it is L if you have lost the i- th '
             'game. After the tournament, you notice a bug on the website that '
             'allows you to change the outcome of at most k of your games ( '
             'meaning that at most k times you can change some symbol L to W, '
             'or W to L) . Since your only goal is to improve your chess '
             'rating, you decide to cheat and use the bug. Compute the maximum '
             'score you can get by cheating in the optimal way.',
  'input': 'Each test contains multiple test cases. The first line contains an '
           'integer t ( 1≤t≤20, 000) — the number of test cases. The '
           'description of the test cases follows. The first line of each '
           'testcase contains two integers n, k ( 1≤n≤100, 000, 0≤k≤n) – the '
           'number of games played and the number of outcomes that you can '
           'change. The second line contains a string s of length n containing '
           'only the characters W and L. If you have won the i- th game then '
           'si= W, if you have lost the i- th game then si= L. It is '
           'guaranteed that the sum of n over all testcases does not exceed '
           '200, 000.',
  'note': 'Explanation of the first testcase. Before changing any outcome, the '
          'score is 2. Indeed, you won the first game, so you got 1 point, and '
          'you won also the third, so you got another 1 point ( and not 2 '
          'because you lost the second game) . An optimal way to cheat is to '
          'change the outcomes of the second and fourth game. Doing so, you '
          'end up winning the first four games ( the string of the outcomes '
          'becomes WWWWL) . Hence, the new score is 7= 1+ 2+ 2+ 2: 1 point for '
          'the first game and 2 points for the second, third and fourth game. '
          'Explanation of the second testcase. Before changing any outcome, '
          'the score is 3. Indeed, you won the fourth game, so you got 1 '
          'point, and you won also the fifth game, so you got 2 more points ( '
          'since you won also the previous game) . An optimal way to cheat is '
          'to change the outcomes of the first, second, third and sixth game. '
          'Doing so, you end up winning all games ( the string of the outcomes '
          'becomes WWWWWW) . Hence, the new score is 11= 1+ 2+ 2+ 2+ 2+ 2: 1 '
          'point for the first game and 2 points for all the other games.',
  'output': 'For each testcase, print a single integer – the maximum score you '
            'can get by cheating in the optimal way.',
  'title': 'Chess Cheater',
  'topics': ['greedy', 'implementation', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1427/B'},
 {'history': 'Zookeeper is playing a game. In this game, Zookeeper must use '
             "bombs to bomb a string that consists of letters ' A' and ' B' . "
             'He can use bombs to bomb a substring which is either " AB" or " '
             'BB" . When he bombs such a substring, the substring gets deleted '
             'from the string and the remaining parts of the string get '
             'concatenated. For example, Zookeeper can use two such '
             'operations: AABABBA → AABBA → AAA. Zookeeper wonders what the '
             'shortest string he can make is. Can you help him find the length '
             'of the shortest string?',
  'input': 'Each test contains multiple test cases. The first line contains a '
           'single integer t ( 1≤t≤20000) — the number of test cases. The '
           'description of the test cases follows. Each of the next t lines '
           'contains a single test case each, consisting of a non- empty '
           'string s: the string that Zookeeper needs to bomb. It is '
           "guaranteed that all symbols of s are either ' A' or ' B' . It is "
           'guaranteed that the sum of | s| ( length of s) among all test '
           'cases does not exceed 2⋅105.',
  'note': "For the first test case, you can' t make any moves, so the answer "
          'is 3. For the second test case, one optimal sequence of moves is '
          'BABA → BA. So, the answer is 2. For the third test case, one '
          'optimal sequence of moves is AABBBABBBB → AABBBABB → AABBBB → ABBB '
          '→ AB → ( empty string) . So, the answer is 0.',
  'output': 'For each test case, print a single integer: the length of the '
            'shortest string that Zookeeper can make.',
  'title': 'ABBB',
  'topics': ['brute force', 'data structures', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1428/C'},
 {'history': 'There are some rabbits in Singapore Zoo. To feed them, Zookeeper '
             'bought nn carrots with lengths a1, a2, a3, . . . , ana1, a2, a3, '
             '. . . , an. However, rabbits are very fertile and multiply very '
             'quickly. Zookeeper now has kk rabbits and does not have enough '
             'carrots to feed all of them. To solve this problem, Zookeeper '
             'decided to cut the carrots into kk pieces. For some reason, all '
             'resulting carrot lengths must be positive integers. Big carrots '
             'are very difficult for rabbits to handle and eat, so the time '
             'needed to eat a carrot of size xx is x2x2. Help Zookeeper split '
             'his carrots while minimizing the sum of time taken for rabbits '
             'to eat the carrots.',
  'input': 'The first line contains two integers nn and kk ( 1≤n≤k≤105) ( '
           '1≤n≤k≤105) : the initial number of carrots and the number of '
           'rabbits. The next line contains nn integers a1, a2, . . . , ana1, '
           'a2, . . . , an ( 1≤ai≤106) ( 1≤ai≤106) : lengths of carrots. It is '
           'guaranteed that the sum of aiai is at least kk.',
  'note': 'For the first test, the optimal sizes of carrots are 1, 1, 1, 2, 2, '
          '21, 1, 1, 2, 2, 2. The time taken is 12+ 12+ 12+ 22+ 22+ 22= 1512+ '
          '12+ 12+ 22+ 22+ 22= 15For the second test, the optimal sizes of '
          'carrots are 4, 5, 5, 54, 5, 5, 5. The time taken is 42+ 52+ 52+ 52= '
          '9142+ 52+ 52+ 52= 91.',
  'output': 'Output one integer: the minimum sum of time taken for rabbits to '
            'eat carrots.',
  'title': 'Carrots for Rabbits',
  'topics': ['binary search', 'data structures', 'greedy', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1428/E'},
 {'history': 'You have n barrels lined up in a row, numbered from left to '
             'right from one. Initially, the i- th barrel contains ai liters '
             'of water. You can pour water from one barrel to another. In one '
             'act of pouring, you can choose two different barrels x and y ( '
             "the x- th barrel shouldn' t be empty) and pour any possible "
             'amount of water from barrel x to barrel y ( possibly, all water) '
             '. You may assume that barrels have infinite capacity, so you can '
             'pour any amount of water in each of them. Calculate the maximum '
             'possible difference between the maximum and the minimum amount '
             'of water in the barrels, if you can pour water at most k times. '
             'Some examples: if you have four barrels, each containing 5 '
             'liters of water, and k= 1, you may pour 5 liters from the second '
             'barrel into the fourth, so the amounts of water in the barrels '
             'are [ 5, 0, 5, 10] , and the difference between the maximum and '
             "the minimum is 10; if all barrels are empty, you can' t make any "
             'operation, so the difference between the maximum and the minimum '
             'amount is still 0.',
  'input': 'The first line contains one integer t ( 1≤t≤1000) — the number of '
           'test cases. The first line of each test case contains two integers '
           'n and k ( 1≤k< n≤2⋅105) — the number of barrels and the number of '
           'pourings you can make. The second line contains n integers a1, a2, '
           '. . . , an ( 0≤ai≤109) , where ai is the initial amount of water '
           "the i- th barrel has. It' s guaranteed that the total sum of n "
           "over test cases doesn' t exceed 2⋅105.",
  'note': ' ',
  'output': 'For each test case, print the maximum possible difference between '
            'the maximum and the minimum amount of water in the barrels, if '
            'you can pour water at most k times.',
  'title': 'Barrels',
  'topics': ['greedy', 'implementation', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1430/B'},
 {'history': 'You are given a string s. You have to reverse it — that is, the '
             'first letter should become equal to the last letter before the '
             'reversal, the second letter should become equal to the second- '
             'to- last letter before the reversal — and so on. For example, if '
             'your goal is to reverse the string " abddea" , you should get '
             'the string " aeddba" . To accomplish your goal, you can swap the '
             'neighboring elements of the string. Your task is to calculate '
             'the minimum number of swaps you have to perform to reverse the '
             'given string.',
  'input': 'The first line contains one integer n ( 2≤n≤200000) — the length '
           'of s. The second line contains s — a string consisting of n '
           'lowercase Latin letters.',
  'note': 'In the first example, you have to swap the third and the fourth '
          'elements, so the string becomes " aazaa" . Then you have to swap '
          'the second and the third elements, so the string becomes " azaaa" . '
          'So, it is possible to reverse the string in two swaps. Since the '
          "string in the second example is a palindrome, you don' t have to do "
          'anything to reverse it.',
  'output': 'Print one integer — the minimum number of swaps of neighboring '
            'elements you have to perform to reverse the string.',
  'title': 'String Reversal',
  'topics': ['data structures', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1430/E'},
 {'history': 'You are given a matrix consisting of n rows and m columns. The '
             'matrix contains lowercase letters of the Latin alphabet. You can '
             'perform the following operation any number of times you want to: '
             'choose two integers i ( 1≤i≤m) and k ( 0< k< n) , and shift '
             'every column j such that i≤j≤m cyclically by k. The shift is '
             'performed upwards. For example, if you have a matrix ( '
             'abcdefghi) and perform an operation with i= 2, k= 1, then it '
             'becomes: ( aefdhigbc) You have to process q queries. Each of the '
             'queries is a string of length m consisting of lowercase letters '
             'of the Latin alphabet. For each query, you have to calculate the '
             'minimum number of operations described above you have to perform '
             'so that at least one row of the matrix is equal to the string '
             'from the query. Note that all queries are independent, that is, '
             "the operations you perform in a query don' t affect the initial "
             'matrix in other queries.',
  'input': 'The first line contains three integers n, m, q ( 2≤n, m, q≤2. '
           '5⋅105; n⋅m≤5⋅105; q⋅m≤5⋅105) — the number of rows and columns in '
           'the matrix and the number of queries, respectively. The next n '
           'lines contains m lowercase Latin letters each — elements of the '
           'matrix. The following q lines contains a description of queries — '
           'strings of length m consisting of lowercase letters of the Latin '
           'alphabet.',
  'note': ' ',
  'output': 'Print q integers. The i- th integer should be equal to the '
            'minimum number of operations you have to perform so that the '
            'matrix contains a string from the i- th query or −1 if the '
            'specified string cannot be obtained.',
  'title': 'Cyclic Shifts',
  'topics': ['*special', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1431/I'},
 {'history': 'Chef Monocarp has just put n dishes into an oven. He knows that '
             'the i- th dish has its optimal cooking time equal to ti minutes. '
             'At any positive integer minute T Monocarp can put no more than '
             'one dish out of the oven. If the i- th dish is put out at some '
             'minute T, then its unpleasant value is | T−ti| — the absolute '
             'difference between T and ti. Once the dish is out of the oven, '
             "it can' t go back in. Monocarp should put all the dishes out of "
             'the oven. What is the minimum total unpleasant value Monocarp '
             'can obtain?',
  'input': 'The first line contains a single integer q ( 1≤q≤200) — the number '
           'of testcases. Then q testcases follow. The first line of the '
           'testcase contains a single integer n ( 1≤n≤200) — the number of '
           'dishes in the oven. The second line of the testcase contains n '
           'integers t1, t2, . . . , tn ( 1≤ti≤n) — the optimal cooking time '
           "for each dish. The sum of n over all q testcases doesn' t exceed "
           '200.',
  'note': 'In the first example Monocarp can put out the dishes at minutes 3, '
          '1, 5, 4, 6, 2. That way the total unpleasant value will be | 4−3| + '
          '| 2−1| + | 4−5| + | 4−4| + | 6−5| + | 2−2| = 4. In the second '
          'example Monocarp can put out the dishes at minutes 4, 5, 6, 7, 8, '
          '9, 10. In the third example Monocarp can put out the dish at minute '
          '1. In the fourth example Monocarp can put out the dishes at minutes '
          '5, 1, 2, 4, 3. In the fifth example Monocarp can put out the dishes '
          'at minutes 1, 3, 4, 5.',
  'output': 'Print a single integer for each testcase — the minimum total '
            'unpleasant value Monocarp can obtain when he puts out all the '
            'dishes out of the oven. Remember that Monocarp can only put the '
            'dishes out at positive integer minutes and no more than one dish '
            'at any minute.',
  'title': 'Chef Monocarp',
  'topics': ['dp', 'flows', 'graph matchings', 'greedy', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1437/C'},
 {'history': 'For the simplicity, let\' s say that the " Death Note" is a '
             'notebook that kills a person when their name is written in it. '
             "It' s easy to kill with it, but it' s pretty hard to keep track "
             "of people you haven' t killed and still plan to. You decided to "
             'make a " Death Database Management System" — a computer program '
             'that provides the easy access to the database of possible '
             "victims. Let me describe its specifications to you. Let' s "
             'define a victim entity: a victim has a name ( not necessarily '
             'unique) that consists only of lowercase Latin letters and an '
             'integer suspicion value. At the start of the program the user '
             'enters a list of n victim names into a database, each suspicion '
             'value is set to 0. Then the user makes queries of two types: 1 i '
             'x — set the suspicion value of the i- th victim to x; 2 q — '
             'given a string q find the maximum suspicion value of a victim '
             'whose name is a contiguous substring of q. Just to remind you, '
             "this program doesn' t kill people, it only helps to search for "
             'the names to write down in an actual notebook. Thus, the list of '
             "the victims in the database doesn' t change throughout the "
             'queries. What are you waiting for? Write that program now!',
  'input': 'The first line contains two integers n and m ( 1≤n, m≤3⋅105) — the '
           'number of victims and the number of queries, respectively. Each of '
           'the next n lines contains a single string si — the name of the i- '
           'th victim. Each name consists only of lowercase Latin letters. '
           'Each of the next m lines contains a query of one of two types: 1 i '
           'x ( 1≤i≤n, 0≤x≤109) — change the suspicion value of the i- th '
           'victim to x; 2 q — given a string q consisting only of lowercase '
           'Latin letters find the maximum suspicion value of a victim whose '
           'name is a contiguous substring of q. There is at least one query '
           "of the second type. The total length of the strings si doesn' t "
           "exceed 3⋅105. The total length of the strings q doesn' t exceed "
           '3⋅105.',
  'note': ' ',
  'output': 'For each query of the second type print an integer value. If '
            'there is no victim name that is a contiguous substring of q, then '
            'print −1. Otherwise, print the maximum suspicion value of a '
            'victim whose name is a contiguous substring of q.',
  'title': 'Death DBMS',
  'topics': ['data structures', 'string suffix structures', 'strings', 'trees'],
  'url': 'https://codeforces.com/problemset/problem/1437/G'},
 {'history': "You' re given an array b of length n. Let' s define another "
             'array a, also of length n, for which ai= 2bi ( 1≤i≤n) . Valerii '
             'says that every two non- intersecting subarrays of a have '
             'different sums of elements. You want to determine if he is '
             'wrong. More formally, you need to determine if there exist four '
             'integers l1, r1, l2, r2 that satisfy the following conditions: '
             '1≤l1≤r1< l2≤r2≤n; al1+ al1+ 1+ . . . + ar1−1+ ar1= al2+ al2+ 1+ '
             '. . . + ar2−1+ ar2. If such four integers exist, you will prove '
             'Valerii wrong. Do they exist? An array c is a subarray of an '
             'array d if c can be obtained from d by deletion of several ( '
             'possibly, zero or all) elements from the beginning and several ( '
             'possibly, zero or all) elements from the end.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤100) . Description of the test '
           'cases follows. The first line of every test case contains a single '
           'integer n ( 2≤n≤1000) . The second line of every test case '
           'contains n integers b1, b2, . . . , bn ( 0≤bi≤109) .',
  'note': 'In the first case, a= [ 16, 8, 1, 2, 4, 1] . Choosing l1= 1, r1= 1, '
          'l2= 2 and r2= 6 works because 16= ( 8+ 1+ 2+ 4+ 1) . In the second '
          'case, you can verify that there is no way to select to such '
          'subarrays.',
  'output': 'For every test case, if there exist two non- intersecting '
            'subarrays in a that have the same sum, output YES on a separate '
            'line. Otherwise, output NO on a separate line. Also, note that '
            'each letter can be in any case.',
  'title': 'Valerii Against Everyone',
  'topics': ['constructive algorithms',
             'data structures',
             'greedy',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1438/B'},
 {'history': "Bertown is a city with n buildings in a straight line. The city' "
             's security service discovered that some buildings were mined. A '
             'map was compiled, which is a string of length n, where the i- th '
             'character is " 1" if there is a mine under the building number i '
             'and " 0" otherwise. Bertown\' s best sapper knows how to '
             'activate mines so that the buildings above them are not damaged. '
             'When a mine under the building numbered x is activated, it '
             'explodes and activates two adjacent mines under the buildings '
             'numbered x−1 and x+ 1 ( if there were no mines under the '
             'building, then nothing happens) . Thus, it is enough to activate '
             'any one mine on a continuous segment of mines to activate all '
             'the mines of this segment. For manual activation of one mine, '
             'the sapper takes a coins. He can repeat this operation as many '
             'times as you want. Also, a sapper can place a mine under a '
             "building if it wasn' t there. For such an operation, he takes b "
             'coins. He can also repeat this operation as many times as you '
             'want. The sapper can carry out operations in any order. You want '
             'to blow up all the mines in the city to make it safe. Find the '
             'minimum number of coins that the sapper will have to pay so that '
             'after his actions there are no mines left in the city.',
  'input': 'The first line contains one positive integer t ( 1≤t≤105) — the '
           'number of test cases. Then t test cases follow. Each test case '
           'begins with a line containing two integers a and b ( 1≤a, b≤1000) '
           '— the cost of activating and placing one mine, respectively. The '
           'next line contains a map of mines in the city — a string '
           'consisting of zeros and ones. The sum of the string lengths for '
           'all test cases does not exceed 105.',
  'note': 'In the second test case, if we place a mine under the fourth '
          'building and then activate it, then all mines on the field are '
          'activated. The cost of such operations is six, b= 1 coin for '
          'placing a mine and a= 5 coins for activating.',
  'output': 'For each test case, output one integer — the minimum number of '
            'coins that the sapper will have to pay.',
  'title': 'Saving the City',
  'topics': ['dp', 'greedy', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1443/B'},
 {'history': 'Petya is preparing for his birthday. He decided that there would '
             'be n different dishes on the dinner table, numbered from 1 to n. '
             "Since Petya doesn' t like to cook, he wants to order these "
             'dishes in restaurants. Unfortunately, all dishes are prepared in '
             'different restaurants and therefore Petya needs to pick up his '
             'orders from n different places. To speed up this process, he '
             'wants to order courier delivery at some restaurants. Thus, for '
             'each dish, there are two options for Petya how he can get it: '
             'the dish will be delivered by a courier from the restaurant i, '
             'in this case the courier will arrive in ai minutes, Petya goes '
             'to the restaurant i on his own and picks up the dish, he will '
             'spend bi minutes on this. Each restaurant has its own couriers '
             'and they start delivering the order at the moment Petya leaves '
             'the house. In other words, all couriers work in parallel. Petya '
             'must visit all restaurants in which he has not chosen delivery, '
             'he does this consistently. For example, if Petya wants to order '
             'n= 4 dishes and a= [ 3, 7, 4, 5] , and b= [ 2, 1, 2, 4] , then '
             'he can order delivery from the first and the fourth restaurant, '
             'and go to the second and third on your own. Then the courier of '
             'the first restaurant will bring the order in 3 minutes, the '
             'courier of the fourth restaurant will bring the order in 5 '
             'minutes, and Petya will pick up the remaining dishes in 1+ 2= 3 '
             "minutes. Thus, in 5 minutes all the dishes will be at Petya' s "
             'house. Find the minimum time after which all the dishes can be '
             "at Petya' s home.",
  'input': 'The first line contains one positive integer t ( 1≤t≤2⋅105) — the '
           'number of test cases. Then t test cases follow. Each test case '
           'begins with a line containing one integer n ( 1≤n≤2⋅105) — the '
           'number of dishes that Petya wants to order. The second line of '
           'each test case contains n integers a1. . . an ( 1≤ai≤109) — the '
           'time of courier delivery of the dish with the number i. The third '
           'line of each test case contains n integers b1. . . bn ( 1≤bi≤109) '
           '— the time during which Petya will pick up the dish with the '
           'number i. The sum of n over all test cases does not exceed 2⋅105.',
  'note': ' ',
  'output': 'For each test case output one integer — the minimum time after '
            "which all dishes can be at Petya' s home.",
  'title': 'The Delivery Dilemma',
  'topics': ['binary search', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1443/C'},
 {'history': 'You are given an array a of length 2n. Consider a partition of '
             'array a into two subsequences p and q of length n each ( each '
             'element of array a should be in exactly one subsequence: either '
             "in p or in q) . Let' s sort p in non- decreasing order, and q in "
             'non- increasing order, we can denote the sorted versions by x '
             'and y, respectively. Then the cost of a partition is defined as '
             'f( p, q) = ∑ni= 1| xi−yi| . Find the sum of f( p, q) over all '
             'correct partitions of array a. Since the answer might be too '
             'big, print its remainder modulo 998244353.',
  'input': 'The first line contains a single integer n ( 1≤n≤150000) . The '
           'second line contains 2n integers a1, a2, . . . , a2n ( 1≤ai≤109) — '
           'elements of array a.',
  'note': 'Two partitions of an array are considered different if the sets of '
          'indices of elements included in the subsequence p are different. In '
          'the first example, there are two correct partitions of the array a: '
          'p= [ 1] , q= [ 4] , then x= [ 1] , y= [ 4] , f( p, q) = | 1−4| = 3; '
          'p= [ 4] , q= [ 1] , then x= [ 4] , y= [ 1] , f( p, q) = | 4−1| = 3. '
          'In the second example, there are six valid partitions of the array '
          'a: p= [ 2, 1] , q= [ 2, 1] ( elements with indices 1 and 2 in the '
          'original array are selected in the subsequence p) ; p= [ 2, 2] , q= '
          '[ 1, 1] ; p= [ 2, 1] , q= [ 1, 2] ( elements with indices 1 and 4 '
          'are selected in the subsequence p) ; p= [ 1, 2] , q= [ 2, 1] ; p= [ '
          '1, 1] , q= [ 2, 2] ; p= [ 2, 1] , q= [ 2, 1] ( elements with '
          'indices 3 and 4 are selected in the subsequence p) .',
  'output': 'Print one integer — the answer to the problem, modulo 998244353.',
  'title': 'Divide and Sum',
  'topics': ['combinatorics', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1444/B'},
 {'history': 'You are given two arrays a and b, each consisting of n positive '
             'integers, and an integer x. Please determine if one can '
             'rearrange the elements of b so that ai+ bi≤x holds for each i ( '
             '1≤i≤n) .',
  'input': 'The first line of input contains one integer t ( 1≤t≤100) — the '
           'number of test cases. t blocks follow, each describing an '
           'individual test case. The first line of each test case contains '
           'two integers n and x ( 1≤n≤50; 1≤x≤1000) — the length of arrays a '
           'and b, and the parameter x, described in the problem statement. '
           'The second line of each test case contains n integers a1, a2, . . '
           '. , an ( 1≤a1≤a2≤⋯≤an≤x) — the elements of array a in non- '
           'descending order. The third line of each test case contains n '
           'integers b1, b2, . . . , bn ( 1≤b1≤b2≤⋯≤bn≤x) — the elements of '
           'array b in non- descending order. Test cases are separated by a '
           'blank line.',
  'note': "In the first test case, one can rearrange b so it' ll look like [ "
          '1, 2, 1] . In this case, 1+ 1≤4; 2+ 2≤4; 3+ 1≤4. In the second test '
          'case, one can set b to [ 5, 2] , then 1+ 5≤6; 4+ 2≤6. In the third '
          'test case, no matter how one shuffles array b, a4+ b4= 4+ b4> 4. In '
          'the fourth test case, there is only one rearrangement of array b '
          "and it doesn' t satisfy the condition since 5+ 5> 5.",
  'output': 'For each test case print Yes if one can rearrange the '
            'corresponding array b so that ai+ bi≤x holds for each i ( 1≤i≤n) '
            'or No otherwise. Each character can be printed in any case.',
  'title': 'Array Rearrangment',
  'topics': ['greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1445/A'},
 {'history': 'You have a knapsack with the capacity of W. There are also n '
             'items, the i- th one has weight wi. You want to put some of '
             'these items into the knapsack in such a way that their total '
             'weight C is at least half of its size, but ( obviously) does not '
             'exceed it. Formally, C should satisfy: ⌈W2⌉≤C≤W. Output the list '
             'of items you will put into the knapsack or determine that '
             'fulfilling the conditions is impossible. If there are several '
             'possible lists of items satisfying the conditions, you can '
             "output any. Note that you don' t have to maximize the sum of "
             'weights of items in the knapsack.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤104) . Description of the test '
           'cases follows. The first line of each test case contains integers '
           'n and W ( 1≤n≤200000, 1≤W≤1018) . The second line of each test '
           'case contains n integers w1, w2, . . . , wn ( 1≤wi≤109) — weights '
           'of the items. The sum of n over all test cases does not exceed '
           '200000.',
  'note': 'In the first test case, you can take the item of weight 3 and fill '
          'the knapsack just right. In the second test case, all the items are '
          "larger than the knapsack' s capacity. Therefore, the answer is −1. "
          'In the third test case, you fill the knapsack exactly in half.',
  'output': 'For each test case, if there is no solution, print a single '
            'integer −1. If there exists a solution consisting of m items, '
            'print m in the first line of the output and m integers j1, j2, . '
            '. . , jm ( 1≤ji≤n, all ji are distinct) in the second line of the '
            'output — indices of the items you would like to pack into the '
            'knapsack. If there are several possible lists of items satisfying '
            "the conditions, you can output any. Note that you don' t have to "
            'maximize the sum of weights items in the knapsack.',
  'title': 'Knapsack',
  'topics': ['constructive algorithms', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1446/A'},
 {'history': 'You are given two strings A and B representing essays of two '
             'students who are suspected cheaters. For any two strings C, D we '
             'define their similarity score S( C, D) as 4⋅LCS( C, D) −| C| −| '
             'D| , where LCS( C, D) denotes the length of the Longest Common '
             'Subsequence of strings C and D. You believe that only some part '
             "of the essays could have been copied, therefore you' re "
             'interested in their substrings. Calculate the maximal similarity '
             'score over all pairs of substrings. More formally, output '
             'maximal S( C, D) over all pairs ( C, D) , where C is some '
             'substring of A, and D is some substring of B. If X is a string, '
             '| X| denotes its length. A string a is a substring of a string b '
             'if a can be obtained from b by deletion of several ( possibly, '
             'zero or all) characters from the beginning and several ( '
             'possibly, zero or all) characters from the end. A string a is a '
             'subsequence of a string b if a can be obtained from b by '
             'deletion of several ( possibly, zero or all) characters. Pay '
             'attention to the difference between the substring and '
             'subsequence, as they both appear in the problem statement. You '
             'may wish to read the Wikipedia page about the Longest Common '
             'Subsequence problem.',
  'input': 'The first line contains two positive integers n and m ( 1≤n, '
           'm≤5000) — lengths of the two strings A and B. The second line '
           'contains a string consisting of n lowercase Latin letters — string '
           'A. The third line contains a string consisting of m lowercase '
           'Latin letters — string B.',
  'note': 'For the first case: abb from the first string and abab from the '
          'second string have LCS equal to abb. The result is S( abb, abab) = '
          '( 4⋅| abb| ) - | abb| - | abab| = 4⋅3−3−4= 5.',
  'output': 'Output maximal S( C, D) over all pairs ( C, D) , where C is some '
            'substring of A, and D is some substring of B.',
  'title': 'Catching Cheaters',
  'topics': ['dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1446/B'},
 {'history': 'A string b is a subsequence of a string a if b can be obtained '
             'from a by deletion of several ( possibly, zero or all) '
             'characters. For example, " xy" is a subsequence of " xzyw" and " '
             'xy" , but not " yx" . You are given a string a. Your task is to '
             'reorder the characters of a so that " trygub" is not a '
             'subsequence of the resulting string. In other words, you should '
             'find a string b which is a permutation of symbols of the string '
             'a and " trygub" is not a subsequence of b. We have a truly '
             'marvelous proof that any string can be arranged not to contain " '
             'trygub" as a subsequence, but this problem statement is too '
             'short to contain it.',
  'input': 'The first line contains a single integer t ( 1≤t≤100) — the number '
           'of test cases. The first line of each test case contains a single '
           'integer n ( 1≤n≤200) — the length of a. The next line contains the '
           'string a of length n, consisting of lowercase English letters.',
  'note': 'In the first test case, " bugyrtnotna" does not contain " trygub" '
          'as a subsequence. It does contain the letters of " trygub" , but '
          'not in the correct order, so it is not a subsequence. In the second '
          'test case, we did not change the order of characters because it is '
          'not needed. In the third test case, " bruhtrywatchinggura" does '
          'contain " trygu" as a subsequence, but not " trygub" .',
  'output': 'For each test case, output a string b of length n which is a '
            'permutation of characters of the string a, and such that " '
            'trygub" is not a subsequence of it. If there exist multiple '
            'possible strings b, you can print any.',
  'title': 'Avoid Trygub',
  'topics': ['constructive algorithms', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1450/A'},
 {'history': 'Hr0d1y has q queries on a binary string s of length n. A binary '
             "string is a string containing only characters ' 0' and ' 1' . A "
             'query is described by a pair of integers li, ri ( 1≤li< ri≤n) . '
             'For each query, he has to determine whether there exists a good '
             'subsequence in s that is equal to the substring s[ li. . . ri] . '
             'A substring s[ i. . . j] of a string s is the string formed by '
             'characters sisi+ 1. . . sj. String a is said to be a subsequence '
             'of string b if a can be obtained from b by deleting some '
             'characters without changing the order of the remaining '
             'characters. A subsequence is said to be good if it is not '
             'contiguous and has length ≥2. For example, if s is " 1100110" , '
             'then the subsequences s1s2s4 ( " 1100110" ) and s1s5s7 ( " '
             '1100110" ) are good, while s1s2s3 ( " 1100110" ) is not good. '
             'Can you help Hr0d1y answer each query?',
  'input': 'The first line of the input contains a single integer t ( 1≤t≤100) '
           '— the number of test cases. The description of each test case is '
           'as follows. The first line contains two integers n ( 2≤n≤100) and '
           'q ( 1≤q≤100) — the length of the string and the number of queries. '
           'The second line contains the string s. The i- th of the next q '
           'lines contains two integers li and ri ( 1≤li< ri≤n) .',
  'note': 'In the first test case, s[ 2. . . 4] = " 010" . In this case s1s3s5 '
          '( " 001000" ) and s2s3s6 ( " 001000" ) are good suitable '
          'subsequences, while s2s3s4 ( " 001000" ) is not good. s[ 1. . . 3] '
          '= " 001" . No suitable good subsequence exists. s[ 3. . . 5] = " '
          '100" . Here s3s5s6 ( " 001000" ) is a suitable good subsequence.',
  'output': 'For each test case, output q lines. The i- th line of the output '
            'of each test case should contain " YES" if there exists a good '
            'subsequence equal to the substring s[ li. . . ri] , and " NO" '
            'otherwise. You may print each letter in any case ( upper or '
            'lower) .',
  'title': 'Non-Substring Subsequence',
  'topics': ['dp', 'greedy', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1451/B'},
 {'history': 'Ashish has two strings a and b, each of length n, and an integer '
             'k. The strings only contain lowercase English letters. He wants '
             'to convert string a into string b by performing some ( possibly '
             'zero) operations on a. In one move, he can either choose an '
             'index i ( 1≤i≤n−1) and swap ai and ai+ 1, or choose an index i ( '
             '1≤i≤n−k+ 1) and if ai, ai+ 1, . . . , ai+ k−1 are all equal to '
             "some character c ( c= ̸ ' z' ) , replace each one with the next "
             "character ( c+ 1) , that is, ' a' is replaced by ' b' , ' b' is "
             "replaced by ' c' and so on. Note that he can perform any number "
             'of operations, and the operations can only be performed on '
             'string a. Help Ashish determine if it is possible to convert '
             'string a into b after performing some ( possibly zero) '
             'operations on it.',
  'input': 'The first line contains a single integer t ( 1≤t≤105) — the number '
           'of test cases. The description of each test case is as follows. '
           'The first line of each test case contains two integers n ( '
           '2≤n≤106) and k ( 1≤k≤n) . The second line of each test case '
           'contains the string a of length n consisting of lowercase English '
           'letters. The third line of each test case contains the string b of '
           'length n consisting of lowercase English letters. It is guaranteed '
           'that the sum of values n among all test cases does not exceed 106.',
  'note': 'In the first test case it can be shown that it is impossible to '
          'convert a into b. In the second test case, " abba" inc→ " acca" '
          'inc→ . . . inc→ " azza" . Here " swap" denotes an operation of the '
          'first type, and " inc" denotes an operation of the second type. In '
          'the fourth test case, " aaabba" swap→ " aaabab" swap→ " aaaabb" '
          'inc→ . . . inc→ " ddaabb" inc→ . . . inc→ " ddddbb" inc→ . . . inc→ '
          '" ddddcc" .',
  'output': 'For each test case, print " Yes" if Ashish can convert a into b '
            'after some moves, else print " No" . You may print the letters of '
            'the answer in any case ( upper or lower) .',
  'title': 'String Equality',
  'topics': ['dp', 'greedy', 'hashing', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1451/C'},
 {'history': 'You are asked to watch your nephew who likes to play with toy '
             'blocks in a strange way. He has n boxes and the i- th box has ai '
             'blocks. His game consists of two steps: he chooses an arbitrary '
             'box i; he tries to move all blocks from the i- th box to other '
             'boxes. If he can make the same number of blocks in each of n−1 '
             'other boxes then he will be happy, otherwise, will be sad. Note '
             'that your nephew can only move the blocks from the chosen box to '
             'the other boxes; he cannot move blocks from the other boxes. You '
             "don' t want to make your nephew sad, so you decided to put "
             'several extra blocks into some boxes in such a way that no '
             "matter which box i he chooses he won' t be sad. What is the "
             'minimum number of extra blocks you need to put?',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of test cases. The first line of each test case contains '
           'the integer n ( 2≤n≤105) — the number of boxes. The second line of '
           'each test case contains n integers a1, a2, . . . , an ( 0≤ai≤109) '
           "— the number of blocks in each box. It' s guaranteed that the sum "
           "of n over test cases doesn' t exceed 105.",
  'note': 'In the first test case, you can, for example, put one extra block '
          'into the first box and make a= [ 4, 2, 2] . If your nephew chooses '
          'the box with 4 blocks, then we will move two blocks to the second '
          'box and two blocks to the third box. If he chooses the box with 2 '
          'blocks then he will move these two blocks to the other box with 2 '
          "blocks. In the second test case, you don' t need to put any extra "
          'blocks, since no matter which box your nephew chooses, he can '
          'always make other boxes equal. In the third test case, you should '
          'put 3 extra blocks. For example, you can put 2 blocks in the first '
          "box and 1 block in the third box. You' ll get array a= [ 2, 3, 1] .",
  'output': 'For each test case, print a single integer — the minimum number '
            'of blocks you need to put. It can be proved that the answer '
            'always exists, i. e. the number of blocks is finite.',
  'title': 'Toy Blocks',
  'topics': ['binary search', 'greedy', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1452/B'},
 {'history': 'Berland regional ICPC contest has just ended. There were m '
             'participants numbered from 1 to m, who competed on a problemset '
             'of n problems numbered from 1 to n. Now the editorial is about '
             'to take place. There are two problem authors, each of them is '
             'going to tell the tutorial to exactly k consecutive tasks of the '
             'problemset. The authors choose the segment of k consecutive '
             'tasks for themselves independently of each other. The segments '
             'can coincide, intersect or not intersect at all. The i- th '
             'participant is interested in listening to the tutorial of all '
             'consecutive tasks from li to ri. Each participant always chooses '
             'to listen to only the problem author that tells the tutorials to '
             'the maximum number of tasks he is interested in. Let this '
             'maximum number be ai. No participant can listen to both of the '
             "authors, even if their segments don' t intersect. The authors "
             'want to choose the segments of k consecutive tasks for '
             'themselves in such a way that the sum of ai over all '
             'participants is maximized.',
  'input': 'The first line contains three integers n, m and k ( 1≤n, m≤2000, '
           '1≤k≤n) — the number of problems, the number of participants and '
           'the length of the segment of tasks each of the problem authors '
           'plans to tell the tutorial to. The i- th of the next m lines '
           'contains two integers li and ri ( 1≤li≤ri≤n) — the segment of '
           'tasks the i- th participant is interested in listening to the '
           'tutorial to.',
  'note': 'In the first example the first author can tell the tutorial to '
          'problems from 1 to 3 and the second one — from 6 to 8. That way the '
          'sequence of ai will be [ 3, 2, 3, 3, 3] . Notice that the last '
          "participant can' t listen to both author, he only chooses the one "
          "that tells the maximum number of problems he' s interested in. In "
          'the second example the first one can tell problems 2 to 4, the '
          'second one — 4 to 6. In the third example the first one can tell '
          'problems 1 to 1, the second one — 2 to 2. Or 4 to 4 and 3 to 3. '
          'Every pair of different problems will get the same sum of 2. In the '
          'fourth example the first one can tell problems 1 to 5, the second '
          'one — 1 to 5 as well.',
  'output': 'Print a single integer — the maximum sum of ai over all '
            'participants.',
  'title': 'Two Editorials',
  'topics': ['brute force', 'dp', 'greedy', 'sortings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1452/E'},
 {'history': 'You are given a sequence a consisting of n integers a1, a2, . . '
             '. , an, and an integer x. Your task is to make the sequence a '
             'sorted ( it is considered sorted if the condition a1≤a2≤a3≤⋯≤an '
             'holds) . To make the sequence sorted, you may perform the '
             'following operation any number of times you want ( possibly '
             'zero) : choose an integer i such that 1≤i≤n and ai> x, and swap '
             'the values of ai and x. For example, if a= [ 0, 2, 3, 5, 4] , x= '
             '1, the following sequence of operations is possible: choose i= 2 '
             '( it is possible since a2> x) , then a= [ 0, 1, 3, 5, 4] , x= 2; '
             'choose i= 3 ( it is possible since a3> x) , then a= [ 0, 1, 2, '
             '5, 4] , x= 3; choose i= 4 ( it is possible since a4> x) , then '
             'a= [ 0, 1, 2, 3, 4] , x= 5. Calculate the minimum number of '
             'operations you have to perform so that a becomes sorted, or '
             'report that it is impossible.',
  'input': 'The first line contains one integer t ( 1≤t≤500) — the number of '
           'test cases. Each test case consists of two lines. The first line '
           'contains two integers n and x ( 1≤n≤500, 0≤x≤500) — the number of '
           'elements in the sequence and the initial value of x. The second '
           'line contains n integers a1, a2, . . . , an ( 0≤ai≤500) . The sum '
           'of values of n over all test cases in the input does not exceed '
           '500.',
  'note': ' ',
  'output': 'For each test case, print one integer — the minimum number of '
            'operations you have to perform to make a sorted, or −1, if it is '
            'impossible.',
  'title': 'Sequence and Swaps',
  'topics': ['dp', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1455/D'},
 {'history': 'Mike received an array aa of length nn as a birthday present and '
             'decided to test how pretty it is. An array would pass the ii- th '
             'prettiness test if there is a way to get an array with a sum of '
             'elements totaling sisi, using some number ( possibly zero) of '
             'slicing operations. An array slicing operation is conducted in '
             'the following way: assume mid= ⌊max( array) + min( array) 2⌋mid= '
             '⌊max( array) + min( array) 2⌋, where maxmax and minmin — are '
             'functions that find the maximum and the minimum array elements. '
             'In other words, midmid is the sum of the maximum and the minimum '
             'element of arrayarray divided by 22 rounded down. Then the array '
             'is split into two parts leftleft and rightright. The leftleft '
             'array contains all elements which are less than or equal midmid, '
             'and the rightright array contains all elements which are greater '
             'than midmid. Elements in leftleft and rightright keep their '
             'relative order from arrayarray. During the third step we choose '
             'which of the leftleft and rightright arrays we want to keep. The '
             'chosen array replaces the current one and the other is '
             'permanently discarded. You need to help Mike find out the '
             'results of qq prettiness tests. Note that you test the '
             'prettiness of the array aa, so you start each prettiness test '
             'with the primordial ( initial) array aa. Thus, the first slice ( '
             'if required) is always performed on the array aa.',
  'input': 'Each test contains one or more test cases. The first line contains '
           'the number of test cases tt ( 1≤t≤1001≤t≤100) . The first line of '
           'each test case contains two integers nn and qq ( 1≤n, q≤105) ( '
           '1≤n, q≤105) — the length of the array aa and the total number of '
           'prettiness tests. The second line of each test case contains nn '
           'integers a1, a2, . . . , ana1, a2, . . . , an ( 1≤ai≤106) ( '
           '1≤ai≤106) — the contents of the array aa. Next qq lines of each '
           'test case contain a single integer sisi ( 1≤si≤109) ( 1≤si≤109) — '
           'the sum of elements which Mike wants to get in the ii- th test. It '
           'is guaranteed that the sum of nn and the sum of qq does not exceed '
           '105105 ( ∑n, ∑q≤105∑n, ∑q≤105) .',
  'note': 'Explanation of the first test case: We can get an array with the '
          'sum s1= 1s1= 1 in the following way: 1. 1 a= [ 1, 2, 3, 4, 5] a= [ '
          '1, 2, 3, 4, 5] , mid= 1+ 52= 3mid= 1+ 52= 3, left= [ 1, 2, 3] left= '
          '[ 1, 2, 3] , right= [ 4, 5] right= [ 4, 5] . We choose to keep the '
          'leftleft array. 1. 2 a= [ 1, 2, 3] a= [ 1, 2, 3] , mid= 1+ 32= '
          '2mid= 1+ 32= 2, left= [ 1, 2] left= [ 1, 2] , right= [ 3] right= [ '
          '3] . We choose to keep the leftleft array. 1. 3 a= [ 1, 2] a= [ 1, '
          '2] , mid= 1+ 22= 1mid= 1+ 22= 1, left= [ 1] left= [ 1] , right= [ '
          '2] right= [ 2] . We choose to keep the leftleft array with the sum '
          'equalling 11. It can be demonstrated that an array with the sum s2= '
          '8s2= 8 is impossible to generate. An array with the sum s3= 9s3= 9 '
          'can be generated in the following way: 3. 1 a= [ 1, 2, 3, 4, 5] a= '
          '[ 1, 2, 3, 4, 5] , mid= 1+ 52= 3mid= 1+ 52= 3, left= [ 1, 2, 3] '
          'left= [ 1, 2, 3] , right= [ 4, 5] right= [ 4, 5] . We choose to '
          'keep the rightright array with the sum equalling 99. It can be '
          'demonstrated that an array with the sum s4= 12s4= 12 is impossible '
          'to generate. We can get an array with the sum s5= 6s5= 6 in the '
          'following way: 5. 1 a= [ 1, 2, 3, 4, 5] a= [ 1, 2, 3, 4, 5] , mid= '
          '1+ 52= 3mid= 1+ 52= 3, left= [ 1, 2, 3] left= [ 1, 2, 3] , right= [ '
          '4, 5] right= [ 4, 5] . We choose to keep the leftleft with the sum '
          'equalling 66. Explanation of the second test case: It can be '
          'demonstrated that an array with the sum s1= 1s1= 1 is imposssible '
          'to generate. We can get an array with the sum s2= 2s2= 2 in the '
          'following way: 2. 1 a= [ 3, 1, 3, 1, 3] a= [ 3, 1, 3, 1, 3] , mid= '
          '1+ 32= 2mid= 1+ 32= 2, left= [ 1, 1] left= [ 1, 1] , right= [ 3, 3, '
          '3] right= [ 3, 3, 3] . We choose to keep the leftleft array with '
          'the sum equalling 22. It can be demonstrated that an array with the '
          'sum s3= 3s3= 3 is imposssible to generate. We can get an array with '
          'the sum s4= 9s4= 9 in the following way: 4. 1 a= [ 3, 1, 3, 1, 3] '
          'a= [ 3, 1, 3, 1, 3] , mid= 1+ 32= 2mid= 1+ 32= 2, left= [ 1, 1] '
          'left= [ 1, 1] , right= [ 3, 3, 3] right= [ 3, 3, 3] . We choose to '
          'keep the rightright array with the sum equalling 99. We can get an '
          'array with the sum s5= 11s5= 11 with zero slicing operations, '
          'because array sum is equal to 1111.',
  'output': 'Print qq lines, each containing either a " Yes" if the '
            'corresponding prettiness test is passed and " No" in the opposite '
            'case.',
  'title': 'Divide and Summarize',
  'topics': ['binary search',
             'brute force',
             'data structures',
             'divide and conquer',
             'implementation',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1461/D'},
 {'history': 'Polycarp has a string s[ 1. . . n] of length n consisting of '
             'decimal digits. Polycarp performs the following operation with '
             'the string s no more than once ( i. e. he can perform operation '
             '0 or 1 time) : Polycarp selects two numbers i and j ( 1≤i≤j≤n) '
             'and removes characters from the s string at the positions i, i+ '
             '1, i+ 2, . . . , j ( i. e. removes substring s[ i. . . j] ) . '
             'More formally, Polycarp turns the string s into the string s1s2. '
             '. . si−1sj+ 1sj+ 2. . . sn. For example, the string s= " '
             '20192020" Polycarp can turn into strings: " 2020" ( in this case '
             '( i, j) = ( 3, 6) or ( i, j) = ( 1, 4) ) ; " 2019220" ( in this '
             'case ( i, j) = ( 6, 6) ) ; " 020" ( in this case ( i, j) = ( 1, '
             '5) ) ; other operations are also possible, only a few of them '
             'are listed above. Polycarp likes the string " 2020" very much, '
             'so he is wondering if it is possible to turn the string s into a '
             'string " 2020" in no more than one operation? Note that you can '
             'perform zero operations.',
  'input': 'The first line contains a positive integer t ( 1≤t≤1000) — number '
           'of test cases in the test. Then t test cases follow. The first '
           'line of each test case contains an integer n ( 4≤n≤200) — length '
           'of the string s. The next line contains a string s of length n '
           'consisting of decimal digits. It is allowed that the string s '
           'starts with digit 0.',
  'note': 'In the first test case, Polycarp could choose i= 3 and j= 6. In the '
          'second test case, Polycarp could choose i= 2 and j= 5. In the third '
          'test case, Polycarp did not perform any operations with the string.',
  'output': 'For each test case, output on a separate line: " YES" if Polycarp '
            'can turn the string s into a string " 2020" in no more than one '
            'operation ( i. e. he can perform 0 or 1 operation) ; " NO" '
            'otherwise. You may print every letter of " YES" and " NO" in any '
            'case you want ( so, for example, the strings yEs, yes, Yes and '
            'YES will all be recognized as positive answer) .',
  'title': "Last Year's Substring",
  'topics': ['dp', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1462/B'},
 {'history': 'This is the easy version of this problem. The only difference '
             'between easy and hard versions is the constraints on k and m ( '
             'in this version k= 2 and m= 3) . Also, in this version of the '
             "problem, you DON' T NEED to output the answer by modulo. You are "
             'given a sequence a of length n consisting of integers from 1 to '
             'n. The sequence may contain duplicates ( i. e. some elements can '
             'be equal) . Find the number of tuples of m= 3 elements such that '
             'the maximum number in the tuple differs from the minimum by no '
             'more than k= 2. Formally, you need to find the number of triples '
             'of indices i< j< z such thatmax( ai, aj, az) −min( ai, aj, az) '
             '≤2. For example, if n= 4 and a= [ 1, 2, 4, 3] , then there are '
             'two such triples ( i= 1, j= 2, z= 4 and i= 2, j= 3, z= 4) . If '
             'n= 4 and a= [ 1, 1, 1, 1] , then all four possible triples are '
             'suitable.',
  'input': 'The first line contains a single integer t ( 1≤t≤2⋅105) — the '
           'number of test cases. Then t test cases follow. The first line of '
           'each test case contains an integer n ( 1≤n≤2⋅105) — the length of '
           'the sequence a. The next line contains n integers a1, a2, . . . , '
           'an ( 1≤ai≤n) — the sequence a. It is guaranteed that the sum of n '
           'for all test cases does not exceed 2⋅105.',
  'note': ' ',
  'output': 'Output t answers to the given test cases. Each answer is the '
            'required number of triples of elements, such that the maximum '
            'value in the triple differs from the minimum by no more than 2. '
            'Note that in difference to the hard version of the problem, you '
            "don' t need to output the answer by modulo. You must output the "
            'exact value of the answer.',
  'title': 'Close Tuples (easy version)',
  'topics': ['binary search',
             'combinatorics',
             'math',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1462/E1'},
 {'history': 'This is the hard version of this problem. The only difference '
             'between the easy and hard versions is the constraints on k and '
             'm. In this version of the problem, you need to output the answer '
             'by modulo 109+ 7. You are given a sequence a of length n '
             'consisting of integers from 1 to n. The sequence may contain '
             'duplicates ( i. e. some elements can be equal) . Find the number '
             'of tuples of m elements such that the maximum number in the '
             'tuple differs from the minimum by no more than k. Formally, you '
             'need to find the number of tuples of m indices i1< i2< . . . < '
             'im, such thatmax( ai1, ai2, . . . , aim) −min( ai1, ai2, . . . , '
             'aim) ≤k. For example, if n= 4, m= 3, k= 2, a= [ 1, 2, 4, 3] , '
             'then there are two such triples ( i= 1, j= 2, z= 4 and i= 2, j= '
             '3, z= 4) . If n= 4, m= 2, k= 1, a= [ 1, 1, 1, 1] , then all six '
             'possible pairs are suitable. As the result can be very large, '
             'you should print the value modulo 109+ 7 ( the remainder when '
             'divided by 109+ 7) .',
  'input': 'The first line contains a single integer t ( 1≤t≤2⋅105) — the '
           'number of test cases. Then t test cases follow. The first line of '
           'each test case contains three integers n, m, k ( 1≤n≤2⋅105, '
           '1≤m≤100, 1≤k≤n) — the length of the sequence a, number of elements '
           'in the tuples and the maximum difference of elements in the tuple. '
           'The next line contains n integers a1, a2, . . . , an ( 1≤ai≤n) — '
           'the sequence a. It is guaranteed that the sum of n for all test '
           'cases does not exceed 2⋅105.',
  'note': ' ',
  'output': 'Output t answers to the given test cases. Each answer is the '
            'required number of tuples of m elements modulo 109+ 7, such that '
            'the maximum value in the tuple differs from the minimum by no '
            'more than k.',
  'title': 'Close Tuples (hard version)',
  'topics': ['binary search',
             'combinatorics',
             'implementation',
             'math',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1462/E2'},
 {'history': 'Ivan is a programming teacher. During the academic year, he '
             'plans to give n lectures on n different topics. Each topic '
             'should be used in exactly one lecture. Ivan wants to choose '
             'which topic will he explain during the 1- st, 2- nd, . . . , n- '
             'th lecture — formally, he wants to choose some permutation of '
             "integers from 1 to n ( let' s call this permutation q) . qi is "
             'the index of the topic Ivan will explain during the i- th '
             'lecture. For each topic ( except exactly one) , there exists a '
             'prerequisite topic ( for the topic i, the prerequisite topic is '
             'pi) . Ivan cannot give a lecture on a topic before giving a '
             'lecture on its prerequisite topic. There exists at least one '
             'valid ordering of topics according to these prerequisite '
             'constraints. Ordering the topics correctly can help students '
             'understand the lectures better. Ivan has k special pairs of '
             'topics ( xi, yi) such that he knows that the students will '
             'understand the yi- th topic better if the lecture on it is '
             'conducted right after the lecture on the xi- th topic. Ivan '
             'wants to satisfy the constraints on every such pair, that is, '
             'for every i∈[ 1, k] , there should exist some j∈[ 1, n−1] such '
             'that qj= xi and qj+ 1= yi. Now Ivan wants to know if there '
             'exists an ordering of topics that satisfies all these '
             'constraints, and if at least one exists, find any of them.',
  'input': 'The first line contains two integers n and k ( 2≤n≤3⋅105, 1≤k≤n−1) '
           '— the number of topics and the number of special pairs of topics, '
           'respectively. The second line contains n integers p1, p2, . . . , '
           'pn ( 0≤pi≤n) , where pi is the prerequisite topic for the topic i '
           '( or pi= 0 if the i- th topic has no prerequisite topics) . '
           'Exactly one of these integers is 0. At least one ordering of '
           'topics such that for every i the pi- th topic is placed before the '
           'i- th topic exists. Then k lines follow, the i- th line contains '
           'two integers xi and yi ( 1≤xi, yi≤n; xi= ̸yi) — the topics from '
           'the i- th special pair. All values of xi are pairwise distinct; '
           'similarly, all valus of yi are pairwise distinct.',
  'note': ' ',
  'output': 'If there is no ordering of topics meeting all the constraints, '
            'print 0. Otherwise, print n pairwise distinct integers q1, q2, . '
            '. . , qn ( 1≤qi≤n) — the ordering of topics meeting all of the '
            'constraints. If there are multiple answers, print any of them.',
  'title': 'Plan of Lectures',
  'topics': ['constructive algorithms',
             'dfs and similar',
             'dsu',
             'graphs',
             'implementation',
             'sortings',
             'trees'],
  'url': 'https://codeforces.com/problemset/problem/1463/E'},
 {'history': "After his wife' s tragic death, Eurydice, Orpheus descended to "
             'the realm of death to see her. Reaching its gates was uneasy, '
             'but passing through them proved to be even more challenging. '
             'Mostly because of Cerberus, the three- headed hound of Hades. '
             'Orpheus, a famous poet, and musician plans to calm Cerberus with '
             'his poetry and safely walk past him. He created a very peculiar '
             'poem for Cerberus. It consists only of lowercase English '
             "letters. We call a poem' s substring a palindrome if and only if "
             'it reads the same backwards and forwards. A string a is a '
             'substring of a string b if a can be obtained from b by deleting '
             'several ( possibly zero or all) characters from the beginning '
             'and several ( possibly zero or all) characters from the end. '
             'Unfortunately, Cerberus dislikes palindromes of length greater '
             "than 1. For example in the poem abaa the hound of Hades wouldn' "
             't like substrings aba and aa. Orpheus can only calm Cerberus if '
             "the hound likes his poetry. That' s why he wants to change his "
             'poem so that it does not contain any palindrome substrings of '
             'length greater than 1. Orpheus can modify the poem by replacing '
             'a letter at any position with any lowercase English letter. He '
             'can use this operation arbitrarily many times ( possibly zero) . '
             'Since there can be many palindromes in his poem, he may have to '
             'make some corrections. But how many, exactly? Given the poem, '
             'determine the minimal number of letters that have to be changed '
             'so that the poem does not contain any palindromes of length '
             'greater than 1.',
  'input': 'The first line of the input contains a single integer t ( 1≤t≤105) '
           'denoting the number of test cases, then t test cases follow. The '
           'first and only line of each test case contains a non- empty string '
           "of lowercase English letters, Orpheus' poem. The sum of the length "
           "of Orpheus' poems in all test cases will not exceed 105.",
  'note': 'In the first test case, we can replace the third character with c '
          'and obtain a palindrome- less poem bacba. In the second test case, '
          'we can replace the third character with d and obtain a palindrome- '
          'less poem abdac. In the third test case, the initial poem already '
          "doesn' t contain any palindromes, so Orpheus doesn' t need to "
          'change anything there.',
  'output': 'You should output t lines, i- th line should contain a single '
            'integer, answer to the i- th test case.',
  'title': 'Canine poetry',
  'topics': ['dp', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1466/C'},
 {'history': "You' ve probably heard about the twelve labors of Heracles, but "
             'do you have any idea about the thirteenth? It is commonly '
             'assumed it took him a dozen years to complete the twelve feats, '
             'so on average, a year to accomplish every one of them. As time '
             'flows faster these days, you have minutes rather than months to '
             'solve this task. But will you manage? In this problem, you are '
             'given a tree with nn weighted vertices. A tree is a connected '
             'graph with n−1n−1 edges. Let us define its kk- coloring as an '
             'assignment of kk colors to the edges so that each edge has '
             "exactly one color assigned to it. Note that you don' t have to "
             'use all kk colors. A subgraph of color xx consists of these '
             'edges from the original tree, which are assigned color xx, and '
             'only those vertices that are adjacent to at least one such edge. '
             'So there are no vertices of degree 00 in such a subgraph. The '
             'value of a connected component is the sum of weights of its '
             'vertices. Let us define the value of a subgraph as a maximum of '
             'values of its connected components. We will assume that the '
             'value of an empty subgraph equals 00. There is also a value of a '
             'kk- coloring, which equals the sum of values of subgraphs of all '
             'kk colors. Given a tree, for each kk from 11 to n−1n−1 calculate '
             'the maximal value of a kk- coloring.',
  'input': 'In the first line of input, there is a single integer tt ( '
           '1≤t≤1051≤t≤105) denoting the number of test cases. Then tt test '
           'cases follow. First line of each test case contains a single '
           'integer nn ( 2≤n≤1052≤n≤105) . The second line consists of nn '
           'integers w1, w2, . . . , wnw1, w2, . . . , wn ( 0≤wi≤1090≤wi≤109) '
           ', wiwi equals the weight of ii- th vertex. In each of the '
           'following n−1n−1 lines, there are two integers uu, vv ( 1≤u, '
           'v≤n1≤u, v≤n) describing an edge between vertices uu and vv. It is '
           'guaranteed that these edges form a tree. The sum of nn in all test '
           'cases will not exceed 2⋅1052⋅105.',
  'note': 'The optimal kk- colorings from the first test case are the '
          'following: In the 11- coloring all edges are given the same color. '
          'The subgraph of color 11 contains all the edges and vertices from '
          'the original graph. Hence, its value equals 3+ 5+ 4+ 6= 183+ 5+ 4+ '
          '6= 18. In an optimal 22- coloring edges ( 2, 1) ( 2, 1) and ( 3, 1) '
          '( 3, 1) are assigned color 11. Edge ( 4, 3) ( 4, 3) is of color 22. '
          'Hence the subgraph of color 11 consists of a single connected '
          'component ( vertices 1, 2, 31, 2, 3) and its value equals 3+ 5+ 4= '
          '123+ 5+ 4= 12. The subgraph of color 22 contains two vertices and '
          'one edge. Its value equals 4+ 6= 104+ 6= 10. In an optimal 33- '
          'coloring all edges are assigned distinct colors. Hence subgraphs of '
          'each color consist of a single edge. They values are as follows: 3+ '
          '4= 73+ 4= 7, 4+ 6= 104+ 6= 10, 3+ 5= 83+ 5= 8.',
  'output': 'For every test case, your program should print one line '
            'containing n−1n−1 integers separated with a single space. The ii- '
            'th number in a line should be the maximal value of a ii- coloring '
            'of the tree.',
  'title': '13th Labour of Heracles',
  'topics': ['data structures', 'greedy', 'sortings', 'trees'],
  'url': 'https://codeforces.com/problemset/problem/1466/D'},
 {'history': 'You may know that Euclid was a mathematician. Well, as it turns '
             'out, Morpheus knew it too. So when he wanted to play a mean '
             'trick on Euclid, he sent him an appropriate nightmare. In his '
             'bad dream Euclid has a set S of n m- dimensional vectors over '
             'the Z2 field and can perform vector addition on them. In other '
             'words he has vectors with m coordinates, each one equal either 0 '
             'or 1. Vector addition is defined as follows: let u+ v= w, then '
             'wi= ( ui+ vi) mod2. Euclid can sum any subset of S and archive '
             'another m- dimensional vector over Z2. In particular, he can sum '
             'together an empty subset; in such a case, the resulting vector '
             'has all coordinates equal 0. Let T be the set of all the vectors '
             'that can be written as a sum of some vectors from S. Now Euclid '
             'wonders the size of T and whether he can use only a subset S′ of '
             'S to obtain all the vectors from T. As it is usually the case in '
             'such scenarios, he will not wake up until he figures this out. '
             'So far, things are looking rather grim for the philosopher. But '
             'there is hope, as he noticed that all vectors in S have at most '
             '2 coordinates equal 1. Help Euclid and calculate | T| , the '
             'number of m- dimensional vectors over Z2 that can be written as '
             'a sum of some vectors from S. As it can be quite large, '
             'calculate it modulo 109+ 7. You should also find S′, the '
             'smallest such subset of S, that all vectors in T can be written '
             'as a sum of vectors from S′. In case there are multiple such '
             'sets with a minimal number of elements, output the '
             'lexicographically smallest one with respect to the order in '
             'which their elements are given in the input. Consider sets A and '
             'B such that | A| = | B| . Let a1, a2, . . . a| A| and b1, b2, . '
             '. . b| B| be increasing arrays of indices elements of A and B '
             'correspondingly. A is lexicographically smaller than B iff there '
             'exists such i that aj= bj for all j< i and ai< bi.',
  'input': 'In the first line of input, there are two integers n, m ( 1≤n, '
           'm≤5⋅105) denoting the number of vectors in S and the number of '
           'dimensions. Next n lines contain the description of the vectors in '
           'S. In each of them there is an integer k ( 1≤k≤2) and then follow '
           'k distinct integers x1, . . . xk ( 1≤xi≤m) . This encodes an m- '
           'dimensional vector having 1s on coordinates x1, . . . xk and 0s on '
           'the rest of them. Among the n vectors, no two are the same.',
  'note': 'In the first example we are given three vectors: 10 01 11 It turns '
          'out that we can represent all vectors from our 2- dimensional space '
          'using these vectors: 00 is a sum of the empty subset of above '
          'vectors; 01= 11+ 10, is a sum of the first and third vector; 10= '
          '10, is just the first vector; 11= 10+ 01, is a sum of the first and '
          'the second vector. Hence, T= 00, 01, 10, 11. We can choose any two '
          'of the three vectors from S and still be able to obtain all the '
          'vectors in T. In such a case, we choose the two vectors which '
          'appear first in the input. Since we cannot obtain all vectors in T '
          'using only a single vector from S, | S′| = 2 and S′= 10, 01 ( '
          'indices 1 and 2) , as set 1, 2 is lexicographically the smallest. '
          'We can represent all vectors from T, using only vectors from S′, as '
          'shown below: 00 is a sum of the empty subset; 01= 01 is just the '
          'second vector; 10= 10 is just the first vector; 11= 10+ 01 is a sum '
          'of the first and the second vector.',
  'output': 'In the first line, output two integers: remainder modulo 109+ 7 '
            'of | T| and | S′| . In the second line, output | S′| numbers, '
            'indices of the elements of S′ in ascending order. The elements of '
            'S are numbered from 1 in the order they are given in the input.',
  'title': "Euclid's nightmare",
  'topics': ['bitmasks',
             'dfs and similar',
             'dsu',
             'graphs',
             'greedy',
             'math',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1466/F'},
 {'history': "Whoso in ignorance draws near to them and hears the Sirens' "
             'voice, he nevermore returns. Homer, OdysseyIn the times of Jason '
             'and the Argonauts, it was well known that sirens use the sound '
             'of their songs to lure sailors into their demise. Yet only a few '
             'knew that every time sirens call a sailor by his name, his will '
             'weakens, making him more vulnerable. For the purpose of this '
             'problem, both siren songs and names of the sailors will be '
             'represented as strings of lowercase English letters. The more '
             "times the sailor' s name occurs as a contiguous substring of the "
             'song, the greater danger he is in. Jason found out that sirens '
             'can sing one of the n+ 1 songs, which have the following '
             'structure: let si ( 0≤i≤n) be the i- th song and t be a string '
             'of length n, then for every i< n: si+ 1= sitisi. In other words '
             'i+ 1- st song is the concatenation of i- th song, i- th letter ( '
             '0- indexed) of t and the i- th song. Fortunately, he also knows '
             "s0 and t. Jason wonders how many times a sailor' s name is "
             'mentioned in a particular song. Answer q queries: given the '
             "sailor' s name ( w) and the index of a song ( i) output the "
             'number of occurrences of w in si as a substring. As this number '
             'can be quite large, output its remainder modulo 109+ 7.',
  'input': 'In the first line of input there are two integers n, q ( 1≤n, '
           'q≤105) meaning that there are n+ 1 songs and q queries. In the '
           'next two lines strings s0 and t follow ( 1≤| s0| ≤100, | t| = n) . '
           'Next q lines describe the queries; each one contains an integer k '
           '( 0≤k≤n) , the index of the song sung by the sirens, and a non- '
           'empty string w, which is the name of a sailor. All strings in this '
           'problem consist only of lowercase English letters, and the sum of '
           "lengths of sailors' names does not exceed 106.",
  'note': 'In the first example songs of the sirens are as follows: Song 0: aa '
          'Song 1: aabaa Song 2: aabaacaabaa Song 3: aabaacaabaadaabaacaabaa',
  'output': 'Output q lines, i- th of them should contain the remainder modulo '
            '109+ 7 of the number of occurrences of w in sk.',
  'title': 'Song of the Sirens',
  'topics': ['combinatorics',
             'divide and conquer',
             'hashing',
             'math',
             'string suffix structures',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1466/G'},
 {'history': 'Consider a long corridor which can be divided into n square '
             'cells of size 1×1. These cells are numbered from 1 to n from '
             'left to right. There are two people in this corridor, a hooligan '
             'and a security guard. Initially, the hooligan is in the a- th '
             'cell, the guard is in the b- th cell ( a= ̸b) . One of the '
             'possible situations. The corridor consists of 7 cells, the '
             'hooligan is in the 3- rd cell, the guard is in the 6- th ( n= 7, '
             "a= 3, b= 6) . There are m firecrackers in the hooligan' s "
             'pocket, the i- th firecracker explodes in si seconds after being '
             'lit. The following events happen each second ( sequentially, '
             'exactly in the following order) : firstly, the hooligan either '
             'moves into an adjacent cell ( from the cell i, he can move to '
             'the cell ( i+ 1) or to the cell ( i−1) , and he cannot leave the '
             'corridor) or stays in the cell he is currently. If the hooligan '
             "doesn' t move, he can light one of his firecrackers and drop it. "
             "The hooligan can' t move into the cell where the guard is; "
             'secondly, some firecrackers that were already dropped may '
             'explode. Formally, if the firecracker j is dropped on the T- th '
             'second, then it will explode on the ( T+ sj) - th second ( for '
             'example, if a firecracker with sj= 2 is dropped on the 4- th '
             'second, it explodes on the 6- th second) ; finally, the guard '
             'moves one cell closer to the hooligan. If the guard moves to the '
             'cell where the hooligan is, the hooligan is caught. Obviously, '
             'the hooligan will be caught sooner or later, since the corridor '
             'is finite. His goal is to see the maximum number of firecrackers '
             'explode before he is caught; that is, he will act in order to '
             'maximize the number of firecrackers that explodes before he is '
             'caught. Your task is to calculate the number of such '
             'firecrackers, if the hooligan acts optimally.',
  'input': 'The first line contains one integer t ( 1≤t≤1000) — the number of '
           'test cases. Each test case consists of two lines. The first line '
           'contains four integers n, m, a and b ( 2≤n≤109; 1≤m≤2⋅105; 1≤a, '
           'b≤n; a= ̸b) — the size of the corridor, the number of '
           'firecrackers, the initial location of the hooligan and the initial '
           'location of the guard, respectively. The second line contains m '
           'integers s1, s2, . . . , sm ( 1≤si≤109) , where si is the time it '
           'takes the i- th firecracker to explode after it is lit. It is '
           'guaranteed that the sum of m over all test cases does not exceed '
           '2⋅105.',
  'note': 'In the first test case, the hooligan should act, for example, as '
          'follows: second 1: drop the second firecracker, so it will explode '
          'on the 5- th second. The guard moves to the cell 5; second 2: move '
          'to the cell 2. The guard moves to the cell 4; second 3: drop the '
          'first firecracker, so it will explode on the 4- th second. The '
          'guard moves to the cell 3; second 4: move to the cell 1. The first '
          'firecracker explodes. The guard moves to the cell 2; second 5: stay '
          'in the cell 1. The second firecracker explodes. The guard moves to '
          'the cell 1 and catches the hooligan.',
  'output': 'For each test case, print one integer — the maximum number of '
            'firecrackers that the hooligan can explode before he is caught.',
  'title': 'Firecrackers',
  'topics': ['binary search', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1468/D'},
 {'history': "Let' s call two strings a and b ( both of length k) a bit "
             'similar if they have the same character in some position, i. e. '
             'there exists at least one i∈[ 1, k] such that ai= bi. You are '
             'given a binary string s of length n ( a string of n characters 0 '
             "and/ or 1) and an integer k. Let' s denote the string s[ i. . j] "
             'as the substring of s starting from the i- th character and '
             'ending with the j- th character ( that is, s[ i. . j] = sisi+ '
             "1si+ 2. . . sj−1sj) . Let' s call a binary string t of length k "
             'beautiful if it is a bit similar to all substrings of s having '
             'length exactly k; that is, it is a bit similar to s[ 1. . k] , '
             's[ 2. . k+ 1] , . . . , s[ n−k+ 1. . n] . Your goal is to find '
             'the lexicographically smallest string t that is beautiful, or '
             'report that no such string exists. String x is lexicographically '
             'less than string y if either x is a prefix of y ( and x= ̸y) , '
             'or there exists such i ( 1≤i≤min( | x| , | y| ) ) , that xi< yi, '
             'and for any j ( 1≤j< i) xj= yj.',
  'input': 'The first line contains one integer q ( 1≤q≤10000) — the number of '
           'test cases. Each test case consists of two lines. The first line '
           'of each test case contains two integers n and k ( 1≤k≤n≤106) . The '
           'second line contains the string s, consisting of n characters ( '
           'each character is either 0 or 1) . It is guaranteed that the sum '
           'of n over all test cases does not exceed 106.',
  'note': ' ',
  'output': 'For each test case, print the answer as follows: if it is '
            'impossible to construct a beautiful string, print one line '
            "containing the string NO ( note: exactly in upper case, you can' "
            't print No, for example) ; otherwise, print two lines. The first '
            'line should contain the string YES ( exactly in upper case as '
            'well) ; the second line — the lexicographically smallest '
            'beautiful string, consisting of k characters 0 and/ or 1.',
  'title': 'A Bit Similar',
  'topics': ['bitmasks',
             'brute force',
             'hashing',
             'string suffix structures',
             'strings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1469/E'},
 {'history': 'Petya organized a strange birthday party. He invited n friends '
             'and assigned an integer ki to the i- th of them. Now Petya would '
             'like to give a present to each of them. In the nearby shop there '
             'are m unique presents available, the j- th present costs cj '
             "dollars ( 1≤c1≤c2≤. . . ≤cm) . It' s not allowed to buy a single "
             'present more than once. For the i- th friend Petya can either '
             'buy them a present j≤ki, which costs cj dollars, or just give '
             'them cki dollars directly. Help Petya determine the minimum '
             'total cost of hosting his party.',
  'input': 'The first input line contains a single integer t ( 1≤t≤103) — the '
           'number of test cases. The first line of each test case contains '
           'two integers n and m ( 1≤n, m≤3⋅105) — the number of friends, and '
           'the number of unique presents available. The following line '
           'contains n integers k1, k2, . . . , kn ( 1≤ki≤m) , assigned by '
           'Petya to his friends. The next line contains m integers c1, c2, . '
           '. . , cm ( 1≤c1≤c2≤. . . ≤cm≤109) — the prices of the presents. It '
           'is guaranteed that sum of values n over all test cases does not '
           'exceed 3⋅105, and the sum of values m over all test cases does not '
           'exceed 3⋅105.',
  'note': 'In the first example, there are two test cases. In the first one, '
          'Petya has 5 friends and 4 available presents. Petya can spend only '
          '30 dollars if he gives 5 dollars to the first friend. A present '
          'that costs 12 dollars to the second friend. A present that costs 5 '
          'dollars to the third friend. A present that costs 3 dollars to the '
          'fourth friend. 5 dollars to the fifth friend. In the second one, '
          'Petya has 5 and 5 available presents. Petya can spend only 190 '
          'dollars if he gives A present that costs 10 dollars to the first '
          'friend. A present that costs 40 dollars to the second friend. 90 '
          'dollars to the third friend. 40 dollars to the fourth friend. 10 '
          'dollars to the fifth friend.',
  'output': 'For each test case output a single integer — the minimum cost of '
            'the party.',
  'title': 'Strange Birthday Party',
  'topics': ['binary search', 'dp', 'greedy', 'sortings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1470/A'},
 {'history': 'During their New Year holidays, Alice and Bob play the following '
             'game using an array a of n integers: Players take turns, Alice '
             'moves first. Each turn a player chooses any element and removes '
             'it from the array. If Alice chooses even value, then she adds it '
             "to her score. If the chosen value is odd, Alice' s score does "
             'not change. Similarly, if Bob chooses odd value, then he adds it '
             "to his score. If the chosen value is even, then Bob' s score "
             'does not change. If there are no numbers left in the array, then '
             'the game ends. The player with the highest score wins. If the '
             'scores of the players are equal, then a draw is declared. For '
             'example, if n= 4 and a= [ 5, 2, 7, 3] , then the game could go '
             'as follows ( there are other options) : On the first move, Alice '
             'chooses 2 and get two points. Her score is now 2. The array a is '
             'now [ 5, 7, 3] . On the second move, Bob chooses 5 and get five '
             'points. His score is now 5. The array a is now [ 7, 3] . On the '
             'third move, Alice chooses 7 and get no points. Her score is now '
             '2. The array a is now [ 3] . On the last move, Bob chooses 3 and '
             'get three points. His score is now 8. The array a is empty now. '
             'Since Bob has more points at the end of the game, he is the '
             'winner. You want to find out who will win if both players play '
             'optimally. Note that there may be duplicate numbers in the '
             'array.',
  'input': 'The first line contains an integer t ( 1≤t≤104) — the number of '
           'test cases. Then t test cases follow. The first line of each test '
           'case contains an integer n ( 1≤n≤2⋅105) — the number of elements '
           'in the array a. The next line contains n integers a1, a2, . . . , '
           'an ( 1≤ai≤109) — the array a used to play the game. It is '
           'guaranteed that the sum of n over all test cases does not exceed '
           '2⋅105.',
  'note': ' ',
  'output': 'For each test case, output on a separate line: " Alice" if Alice '
            'wins with the optimal play; " Bob" if Bob wins with the optimal '
            'play; " Tie" , if a tie is declared during the optimal play.',
  'title': 'Even-Odd Game',
  'topics': ['dp', 'games', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1472/D'},
 {'history': 'Polycarp has invited n friends to celebrate the New Year. During '
             'the celebration, he decided to take a group photo of all his '
             'friends. Each friend can stand or lie on the side. Each friend '
             'is characterized by two values hi ( their height) and wi ( their '
             'width) . On the photo the i- th friend will occupy a rectangle '
             'hi×wi ( if they are standing) or wi×hi ( if they are lying on '
             'the side) . The j- th friend can be placed in front of the i- th '
             'friend on the photo if his rectangle is lower and narrower than '
             'the rectangle of the i- th friend. Formally, at least one of the '
             'following conditions must be fulfilled: hj< hi and wj< wi ( both '
             'friends are standing or both are lying) ; wj< hi and hj< wi ( '
             'one of the friends is standing and the other is lying) . For '
             'example, if n= 3, h= [ 3, 5, 3] and w= [ 4, 4, 3] , then: the '
             'first friend can be placed in front of the second: w1< h2 and '
             'h1< w2 ( one of the them is standing and the other one is lying) '
             '; the third friend can be placed in front of the second: h3< h2 '
             'and w3< w2 ( both friends are standing or both are lying) . In '
             'other cases, the person in the foreground will overlap the '
             'person in the background. Help Polycarp for each i find any j, '
             'such that the j- th friend can be located in front of the i- th '
             'friend ( i. e. at least one of the conditions above is '
             'fulfilled) . Please note that you do not need to find the '
             'arrangement of all people for a group photo. You just need to '
             'find for each friend i any other friend j who can be located in '
             'front of him. Think about it as you need to solve n separate '
             'independent subproblems.',
  'input': 'The first line contains one integer t ( 1≤t≤104) — the number of '
           'test cases. Then t test cases follow. The first line of each test '
           'case contains one integer n ( 1≤n≤2⋅105) — the number of friends. '
           'This is followed by n lines, each of which contains a description '
           'of the corresponding friend. Each friend is described by two '
           'integers hi and wi ( 1≤hi, wi≤109) — height and width of the i- th '
           'friend, respectively. It is guaranteed that the sum of n over all '
           'test cases does not exceed 2⋅105.',
  'note': 'The first test case is described in the statement. In the third '
          'test case, the following answers are also correct: [ −1, −1, 1, 2] '
          '; [ −1, −1, 1, 1] ; [ −1, −1, 2, 1] .',
  'output': 'For each test case output n integers on a separate line, where '
            'the i- th number is the index of a friend that can be placed in '
            'front of the i- th. If there is no such friend, then output - 1. '
            'If there are several answers, output any.',
  'title': 'Correct Placement',
  'topics': ['binary search',
             'data structures',
             'dp',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1472/E'},
 {'history': 'Every year Santa Claus gives gifts to all children. However, '
             'each country has its own traditions, and this process takes '
             'place in different ways. For example, in Berland you need to '
             "solve the New Year' s puzzle. Polycarp got the following "
             'problem: given a grid strip of size 2×n2×n, some cells of it are '
             'blocked. You need to check if it is possible to tile all free '
             'cells using the 2×12×1 and 1×21×2 tiles ( dominoes) . For '
             'example, if n= 5n= 5 and the strip looks like this ( black cells '
             'are blocked) : Then it can be tiled, for example, using two '
             'vertical and two horizontal tiles, as in the picture below ( '
             'different tiles are marked by different colors) . And if n= 3n= '
             '3 and the strip looks like this: It is impossible to tile free '
             'cells. Polycarp easily solved this task and received his New '
             "Year' s gift. Can you solve it?",
  'input': 'The first line contains an integer tt ( 1≤t≤1041≤t≤104) — the '
           'number of test cases. Then tt test cases follow. Each test case is '
           'preceded by an empty line. The first line of each test case '
           'contains two integers nn and mm ( 1≤n≤1091≤n≤109, '
           '1≤m≤2⋅1051≤m≤2⋅105) — the length of the strip and the number of '
           'blocked cells on it. Each of the next mm lines contains two '
           'integers ri, ciri, ci ( 1≤ri≤2, 1≤ci≤n1≤ri≤2, 1≤ci≤n) — numbers of '
           'rows and columns of blocked cells. It is guaranteed that all '
           'blocked cells are different, i. e. ( ri, ci) = ̸( rj, cj) , i= ̸j( '
           'ri, ci) = ̸( rj, cj) , i= ̸j. It is guaranteed that the sum of mm '
           'over all test cases does not exceed 2⋅1052⋅105.',
  'note': 'The first two test cases are explained in the statement. In the '
          'third test case the strip looks like this: It is easy to check that '
          'the unblocked squares on it can not be tiled.',
  'output': 'For each test case, print on a separate line: " YES" , if it is '
            'possible to tile all unblocked squares with the 2×12×1 and 1×21×2 '
            'tiles; " NO" otherwise. You can output " YES" and " NO" in any '
            'case ( for example, the strings yEs, yes, Yes and YES will be '
            'recognized as positive) .',
  'title': "New Year's Puzzle",
  'topics': ['brute force', 'dp', 'graph matchings', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1472/F'},
 {'history': 'You have an array a1, a2, . . . , an. All ai are positive '
             'integers. In one step you can choose three distinct indices i, '
             'j, and k ( i= ̸j; i= ̸k; j= ̸k) and assign the sum of aj and ak '
             'to ai, i. e. make ai= aj+ ak. Can you make all ai lower or equal '
             'to d using the operation above any number of times ( possibly, '
             'zero) ?',
  'input': 'The first line contains a single integer t ( 1≤t≤2000) — the '
           'number of test cases. The first line of each test case contains '
           'two integers n and d ( 3≤n≤100; 1≤d≤100) — the number of elements '
           'in the array a and the value d. The second line contains n '
           'integers a1, a2, . . . , an ( 1≤ai≤100) — the array a.',
  'note': "In the first test case, we can prove that we can' t make all ai≤3. "
          'In the second test case, all ai are already less or equal than d= '
          '4. In the third test case, we can, for example, choose i= 5, j= 1, '
          'k= 2 and make a5= a1+ a2= 2+ 1= 3. Array a will become [ 2, 1, 5, '
          '3, 3] . After that we can make a3= a5+ a2= 3+ 1= 4. Array will '
          'become [ 2, 1, 4, 3, 3] and all elements are less or equal than d= '
          '4.',
  'output': "For each test case, print YES, if it' s possible to make all "
            'elements ai less or equal than d using the operation above. '
            'Otherwise, print NO. You may print each letter in any case ( for '
            'example, YES, Yes, yes, yEs will all be recognized as positive '
            'answer) .',
  'title': 'Replacing Elements',
  'topics': ['greedy', 'implementation', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1473/A'},
 {'history': "Let' s define a multiplication operation between a string a and "
             'a positive integer x: a⋅x is the string that is a result of '
             'writing x copies of a one after another. For example, " abc" ⋅ 2 '
             '= " abcabc" , " a" ⋅ 5 = " aaaaa" . A string a is divisible by '
             'another string b if there exists an integer x such that b⋅x= a. '
             'For example, " abababab" is divisible by " ab" , but is not '
             'divisible by " ababab" or " aa" . LCM of two strings s and t ( '
             'defined as LCM( s, t) ) is the shortest non- empty string that '
             'is divisible by both s and t. You are given two strings s and t. '
             'Find LCM( s, t) or report that it does not exist. It can be '
             'shown that if LCM( s, t) exists, it is unique.',
  'input': 'The first line contains one integer q ( 1≤q≤2000) — the number of '
           'test cases. Each test case consists of two lines, containing '
           'strings s and t ( 1≤| s| , | t| ≤20) . Each character in each of '
           "these strings is either ' a' or ' b' .",
  'note': 'In the first test case, " baba" = " baba" ⋅ 1 = " ba" ⋅ 2. In the '
          'second test case, " aaaaaa" = " aa" ⋅ 3 = " aaa" ⋅ 2.',
  'output': 'For each test case, print LCM( s, t) if it exists; otherwise, '
            'print - 1. It can be shown that if LCM( s, t) exists, it is '
            'unique.',
  'title': 'String LCM',
  'topics': ['brute force', 'math', 'number theory', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1473/B'},
 {'history': 'You are given a program that consists of n instructions. '
             'Initially a single variable x is assigned to 0. Afterwards, the '
             'instructions are of two types: increase x by 1; decrease x by 1. '
             'You are given m queries of the following format: query l r — how '
             'many distinct values is x assigned to if all the instructions '
             'between the l- th one and the r- th one inclusive are ignored '
             'and the rest are executed without changing the order?',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of testcases. Then the description of t testcases follows. '
           'The first line of each testcase contains two integers n and m ( '
           '1≤n, m≤2⋅105) — the number of instructions in the program and the '
           'number of queries. The second line of each testcase contains a '
           "program — a string of n characters: each character is either ' + ' "
           "or ' - ' — increment and decrement instruction, respectively. Each "
           'of the next m lines contains two integers l and r ( 1≤l≤r≤n) — the '
           "description of the query. The sum of n over all testcases doesn' t "
           "exceed 2⋅105. The sum of m over all testcases doesn' t exceed "
           '2⋅105.',
  'note': 'The instructions that remain for each query of the first testcase '
          'are: empty program — x was only equal to 0; " - " — x had values 0 '
          'and −1; " —+ " — x had values 0, −1, −2, −3, −2 — there are 4 '
          'distinct values among them; " + –+ –+ " — the distinct values are '
          '1, 0, −1, −2.',
  'output': 'For each testcase print m integers — for each query l, r print '
            'the number of distinct values variable x is assigned to if all '
            'the instructions between the l- th one and the r- th one '
            'inclusive are ignored and the rest are executed without changing '
            'the order.',
  'title': 'Program',
  'topics': ['data structures', 'dp', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1473/D'},
 {'history': 'You found a useless array a of 2n positive integers. You have '
             "realized that you actually don' t need this array, so you "
             'decided to throw out all elements of a. It could have been an '
             'easy task, but it turned out that you should follow some rules: '
             'In the beginning, you select any positive integer x. Then you do '
             'the following operation n times: select two elements of array '
             'with sum equals x; remove them from a and replace x with maximum '
             'of that two numbers. For example, if initially a= [ 3, 5, 1, 2] '
             ', you can select x= 6. Then you can select the second and the '
             'third elements of a with sum 5+ 1= 6 and throw them out. After '
             'this operation, x equals 5 and there are two elements in array: '
             '3 and 2. You can throw them out on the next operation. Note, '
             "that you choose x before the start and can' t change it as you "
             'want between the operations. Determine how should you behave to '
             'throw out all elements of a.',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of test cases. The first line of each test case contains '
           'the single integer n ( 1≤n≤1000) . The second line of each test '
           'case contains 2n integers a1, a2, . . . , a2n ( 1≤ai≤106) — the '
           'initial array a. It is guaranteed that the total sum of n over all '
           "test cases doesn' t exceed 1000.",
  'note': 'The first test case was described in the statement. In the second '
          'and third test cases, we can show that it is impossible to throw '
          'out all elements of array a.',
  'output': 'For each test case in the first line print YES if it is possible '
            'to throw out all elements of the array and NO otherwise. If it is '
            'possible to throw out all elements, print the initial value of x '
            "you' ve chosen. Print description of n operations next. For each "
            'operation, print the pair of integers you remove.',
  'title': 'Array Destruction',
  'topics': ['brute force',
             'constructive algorithms',
             'data structures',
             'greedy',
             'implementation',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1474/C'},
 {'history': 'Polycarp often uses his smartphone. He has already installed n '
             'applications on it. Application with number i takes up ai units '
             'of memory. Polycarp wants to free at least m units of memory ( '
             'by removing some applications) . Of course, some applications '
             'are more important to Polycarp than others. He came up with the '
             'following scoring system — he assigned an integer bi to each '
             'application: bi= 1 — regular application; bi= 2 — important '
             'application. According to this rating system, his phone has b1+ '
             'b2+ . . . + bn convenience points. Polycarp believes that if he '
             'removes applications with numbers i1, i2, . . . , ik, then he '
             'will free ai1+ ai2+ . . . + aik units of memory and lose bi1+ '
             'bi2+ . . . + bik convenience points. For example, if n= 5, m= 7, '
             'a= [ 5, 3, 2, 1, 4] , b= [ 2, 1, 1, 2, 1] , then Polycarp can '
             'uninstall the following application sets ( not all options are '
             'listed below) : applications with numbers 1, 4 and 5. In this '
             'case, it will free a1+ a4+ a5= 10 units of memory and lose b1+ '
             'b4+ b5= 5 convenience points; applications with numbers 1 and 3. '
             'In this case, it will free a1+ a3= 7 units of memory and lose '
             'b1+ b3= 3 convenience points. applications with numbers 2 and 5. '
             'In this case, it will free a2+ a5= 7 memory units and lose b2+ '
             'b5= 2 convenience points. Help Polycarp, choose a set of '
             'applications, such that if removing them will free at least m '
             'units of memory and lose the minimum number of convenience '
             'points, or indicate that such a set does not exist.',
  'input': 'The first line contains one integer t ( 1≤t≤104) — the number of '
           'test cases. Then t test cases follow. The first line of each test '
           'case contains two integers n and m ( 1≤n≤2⋅105, 1≤m≤109) — the '
           "number of applications on Polycarp' s phone and the number of "
           'memory units to be freed. The second line of each test case '
           'contains n integers a1, a2, . . . , an ( 1≤ai≤109) — the number of '
           'memory units used by applications. The third line of each test '
           'case contains n integers b1, b2, . . . , bn ( 1≤bi≤2) — the '
           'convenience points of each application. It is guaranteed that the '
           'sum of n over all test cases does not exceed 2⋅105.',
  'note': 'In the first test case, it is optimal to remove applications with '
          'numbers 2 and 5, freeing 7 units of memory. b2+ b5= 2. In the '
          'second test case, by removing the only application, Polycarp will '
          'be able to clear only 2 of memory units out of the 3 needed. In the '
          'third test case, it is optimal to remove applications with numbers '
          '1, 2, 3 and 4, freeing 10 units of memory. b1+ b2+ b3+ b4= 6. In '
          'the fourth test case, it is optimal to remove applications with '
          'numbers 1, 3 and 4, freeing 12 units of memory. b1+ b3+ b4= 4. In '
          'the fifth test case, it is optimal to remove applications with '
          'numbers 1 and 2, freeing 5 units of memory. b1+ b2= 3.',
  'output': 'For each test case, output on a separate line: - 1, if there is '
            'no set of applications, removing which will free at least m units '
            'of memory; the minimum number of convenience points that Polycarp '
            'will lose if such a set exists.',
  'title': 'Cleaning the Phone',
  'topics': ['binary search', 'dp', 'sortings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1475/D'},
 {'history': 'Masha works in an advertising agency. In order to promote the '
             'new brand, she wants to conclude contracts with some bloggers. '
             'In total, Masha has connections of n different bloggers. Blogger '
             'numbered i has ai followers. Since Masha has a limited budget, '
             'she can only sign a contract with k different bloggers. Of '
             'course, Masha wants her ad to be seen by as many people as '
             'possible. Therefore, she must hire bloggers with the maximum '
             'total number of followers. Help her, find the number of ways to '
             'select k bloggers so that the total number of their followers is '
             'maximum possible. Two ways are considered different if there is '
             'at least one blogger in the first way, which is not in the '
             'second way. Masha believes that all bloggers have different '
             'followers ( that is, there is no follower who would follow two '
             'different bloggers) . For example, if n= 4, k= 3, a= [ 1, 3, 1, '
             '2] , then Masha has two ways to select 3 bloggers with the '
             'maximum total number of followers: conclude contracts with '
             'bloggers with numbers 1, 2 and 4. In this case, the number of '
             'followers will be equal to a1+ a2+ a4= 6. conclude contracts '
             'with bloggers with numbers 2, 3 and 4. In this case, the number '
             'of followers will be equal to a2+ a3+ a4= 6. Since the answer '
             'can be quite large, output it modulo 109+ 7.',
  'input': 'The first line contains one integer t ( 1≤t≤1000) — the number of '
           'test cases. Then t test cases follow. The first line of each test '
           'case contains two integers n and k ( 1≤k≤n≤1000) — the number of '
           'bloggers and how many of them you can sign a contract with. The '
           'second line of each test case contains n integers a1, a2, . . . an '
           '( 1≤ai≤n) — the number of followers of each blogger. It is '
           'guaranteed that the sum of n over all test cases does not exceed '
           '1000.',
  'note': 'The test case is explained in the statements. In the second test '
          'case, the following ways are valid: conclude contracts with '
          'bloggers with numbers 1 and 2. In this case, the number of '
          'followers will be equal to a1+ a2= 2; conclude contracts with '
          'bloggers with numbers 1 and 3. In this case, the number of '
          'followers will be equal to a1+ a3= 2; conclude contracts with '
          'bloggers with numbers 1 and 4. In this case, the number of '
          'followers will be equal to a1+ a4= 2; conclude contracts with '
          'bloggers with numbers 2 and 3. In this case, the number of '
          'followers will be equal to a2+ a3= 2; conclude contracts with '
          'bloggers with numbers 2 and 4. In this case, the number of '
          'followers will be equal to a2+ a4= 2; conclude contracts with '
          'bloggers with numbers 3 and 4. In this case, the number of '
          'followers will be equal to a3+ a4= 2. In the third test case, the '
          'following ways are valid: concludes a contract with a blogger with '
          'the number 2. In this case, the number of followers will be equal '
          'to a2= 2.',
  'output': 'For each test case, on a separate line output one integer — the '
            'number of ways to select k bloggers so that the total number of '
            'their followers is maximum possible.',
  'title': 'Advertising Agency',
  'topics': ['combinatorics', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1475/E'},
 {'history': 'Polycarp found on the street an array a of n elements. Polycarp '
             'invented his criterion for the beauty of an array. He calls an '
             'array a beautiful if at least one of the following conditions '
             'must be met for each different pair of indices i= ̸j: ai is '
             'divisible by aj; or aj is divisible by ai. For example, if: n= 5 '
             'and a= [ 7, 9, 3, 14, 63] , then the a array is not beautiful ( '
             'for i= 4 and j= 2, none of the conditions above is met) ; n= 3 '
             'and a= [ 2, 14, 42] , then the a array is beautiful; n= 4 and a= '
             '[ 45, 9, 3, 18] , then the a array is not beautiful ( for i= 1 '
             'and j= 4 none of the conditions above is met) ; Ugly arrays '
             'upset Polycarp, so he wants to remove some elements from the '
             'array a so that it becomes beautiful. Help Polycarp determine '
             'the smallest number of elements to remove to make the array a '
             'beautiful.',
  'input': 'The first line contains one integer t ( 1≤t≤10) — the number of '
           'test cases. Then t test cases follow. The first line of each test '
           'case contains one integer n ( 1≤n≤2⋅105) — the length of the array '
           'a. The second line of each test case contains n numbers a1, a2, . '
           '. . , an ( 1≤ai≤2⋅105) — elements of the array a.',
  'note': 'In the first test case, removing 7 and 14 will make array a '
          'beautiful. In the second test case, the array a is already '
          'beautiful. In the third test case, removing one of the elements 45 '
          'or 18 will make the array a beautiful. In the fourth test case, the '
          'array a is beautiful.',
  'output': 'For each test case output one integer — the minimum number of '
            'elements that must be removed to make the array a beautiful.',
  'title': 'Strange Beauty',
  'topics': ['dp', 'math', 'number theory', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1475/G'},
 {'history': 'You are given n patterns p1, p2, . . . , pn and m strings s1, '
             's2, . . . , sm. Each pattern pi consists of k characters that '
             'are either lowercase Latin letters or wildcard characters ( '
             'denoted by underscores) . All patterns are pairwise distinct. '
             'Each string sj consists of k lowercase Latin letters. A string a '
             'matches a pattern b if for each i from 1 to k either bi is a '
             'wildcard character or bi= ai. You are asked to rearrange the '
             'patterns in such a way that the first pattern the j- th string '
             'matches is p[ mtj] . You are allowed to leave the order of the '
             'patterns unchanged. Can you perform such a rearrangement? If you '
             'can, then print any valid order.',
  'input': 'The first line contains three integers n, m and k ( 1≤n, m≤105, '
           '1≤k≤4) — the number of patterns, the number of strings and the '
           'length of each pattern and string. Each of the next n lines '
           'contains a pattern — k characters that are either lowercase Latin '
           'letters or underscores. All patterns are pairwise distinct. Each '
           'of the next m lines contains a string — k lowercase Latin letters, '
           'and an integer mt ( 1≤mt≤n) — the index of the first pattern the '
           'corresponding string should match.',
  'note': 'The order of patterns after the rearrangement in the first example '
          'is the following: aaaa _ _ b_ ab_ _ _ bcd _ b_ d Thus, the first '
          'string matches patterns ab_ _ , _ bcd, _ b_ d in that order, the '
          'first of them is ab_ _ , that is indeed p[ 4] . The second string '
          'matches _ _ b_ and ab_ _ , the first of them is _ _ b_ , that is p[ '
          '2] . The last string matches _ bcd and _ b_ d, the first of them is '
          '_ bcd, that is p[ 5] . The answer to that test is not unique, other '
          "valid orders also exist. In the second example cba doesn' t match _ "
          '_ c, thus, no valid order exists. In the third example the order ( '
          'a_ , _ b) makes both strings match pattern 1 first and the order ( '
          '_ b, a_ ) makes both strings match pattern 2 first. Thus, there is '
          'no order that produces the result 1 and 2.',
  'output': 'Print " NO" if there is no way to rearrange the patterns in such '
            'a way that the first pattern that the j- th string matches is p[ '
            'mtj] . Otherwise, print " YES" in the first line. The second line '
            'should contain n distinct integers from 1 to n — the order of the '
            'patterns. If there are multiple answers, print any of them.',
  'title': 'Pattern Matching',
  'topics': ['bitmasks',
             'data structures',
             'dfs and similar',
             'graphs',
             'hashing',
             'sortings',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1476/E'},
 {'history': 'You are given an integer array a of size n. You have to perform '
             'm queries. Each query has one of two types: " 1 l r k" — '
             'calculate the minimum value dif such that there are exist k '
             'distinct integers x1, x2, . . . , xk such that cnti> 0 ( for '
             'every i∈[ 1, k] ) and | cnti−cntj| ≤dif ( for every i∈[ 1, k] , '
             'j∈[ 1, k] ) , where cnti is the number of occurrences of xi in '
             'the subarray a[ l. . r] . If it is impossible to choose k '
             'integers, report it; " 2 p x" — assign ap: = x.',
  'input': 'The first line contains two integers n and m ( 1≤n, m≤105) — the '
           'size of the array a and the number of queries. The second line '
           'contains n integers a1, a2, . . . , an ( 1≤ai≤105) . Next m lines '
           'contain queries ( one per line) . Each query has one of two types: '
           '" 1 l r k" ( 1≤l≤r≤n; 1≤k≤105) " 2 p x" ( 1≤p≤n; 1≤x≤105) . It\' s '
           'guaranteed that there is at least one query of the first type.',
  'note': ' ',
  'output': 'For each query of the first type, print the minimum value of dif '
            'that satisfies all required conditions, or −1 if it is impossible '
            'to choose k distinct integers.',
  'title': 'Minimum Difference',
  'topics': ['data structures', 'hashing', 'sortings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1476/G'},
 {'history': 'Nezzar loves the game osu! . osu! is played on beatmaps, which '
             'can be seen as an array consisting of distinct points on a '
             'plane. A beatmap is called nice if for any three consecutive '
             'points A, B, CA, B, C listed in order, the angle between these '
             'three points, centered at BB, is strictly less than 9090 '
             'degrees. Points A, B, CA, B, C on the left have angle less than '
             '9090 degrees, so they can be three consecutive points of a nice '
             'beatmap; Points A′, B′, C′A′, B′, C′ on the right have angle '
             'greater or equal to 9090 degrees, so they cannot be three '
             'consecutive points of a nice beatmap. Now Nezzar has a beatmap '
             'of nn distinct points A1, A2, . . . , AnA1, A2, . . . , An. '
             'Nezzar would like to reorder these nn points so that the '
             'resulting beatmap is nice. Formally, you are required to find a '
             'permutation p1, p2, . . . , pnp1, p2, . . . , pn of integers '
             'from 11 to nn, such that beatmap Ap1, Ap2, . . . , ApnAp1, Ap2, '
             '. . . , Apn is nice. If it is impossible, you should determine '
             'it.',
  'input': 'The first line contains a single integer nn ( 3≤n≤50003≤n≤5000) . '
           'Then nn lines follow, ii- th of them contains two integers xixi, '
           'yiyi ( −109≤xi, yi≤109−109≤xi, yi≤109) — coordinates of point '
           'AiAi. It is guaranteed that all points are distinct.',
  'note': 'Here is the illustration for the first test: Please note that the '
          'angle between A1A1, A2A2 and A5A5, centered at A2A2, is treated as '
          '00 degrees. However, angle between A1A1, A5A5 and A2A2, centered at '
          'A5A5, is treated as 180180 degrees.',
  'output': 'If there is no solution, print −1−1. Otherwise, print nn '
            'integers, representing a valid permutation pp. If there are '
            'multiple possible answers, you can print any.',
  'title': 'Nezzar and Nice Beatmap',
  'topics': ['constructive algorithms',
             'geometry',
             'greedy',
             'math',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1477/C'},
 {'history': 'Long time ago there was a symmetric array a1, a2, . . . , a2n '
             'consisting of 2n distinct integers. Array a1, a2, . . . , a2n is '
             'called symmetric if for each integer 1≤i≤2n, there exists an '
             'integer 1≤j≤2n such that ai= −aj. For each integer 1≤i≤2n, '
             'Nezzar wrote down an integer di equal to the sum of absolute '
             'differences from ai to all integers in a, i. e. di= ∑2nj= 1| '
             'ai−aj| . Now a million years has passed and Nezzar can barely '
             'remember the array d and totally forget a. Nezzar wonders if '
             'there exists any symmetric array a consisting of 2n distinct '
             'integers that generates the array d.',
  'input': 'The first line contains a single integer t ( 1≤t≤105) — the number '
           'of test cases. The first line of each test case contains a single '
           'integer n ( 1≤n≤105) . The second line of each test case contains '
           '2n integers d1, d2, . . . , d2n ( 0≤di≤1012) . It is guaranteed '
           'that the sum of n over all test cases does not exceed 105.',
  'note': 'In the first test case, a= [ 1, −3, −1, 3] is one possible '
          'symmetric array that generates the array d= [ 8, 12, 8, 12] . In '
          'the second test case, it can be shown that there is no symmetric '
          'array consisting of distinct integers that can generate array d.',
  'output': 'For each test case, print " YES" in a single line if there exists '
            'a possible array a. Otherwise, print " NO" . You can print '
            'letters in any case ( upper or lower) .',
  'title': 'Nezzar and Symmetric Array',
  'topics': ['implementation', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1478/C'},
 {'history': 'Homer has two friends Alice and Bob. Both of them are string '
             'fans. One day, Alice and Bob decide to play a game on a string '
             's= s1s2. . . sn of length n consisting of lowercase English '
             'letters. They move in turns alternatively and Alice makes the '
             'first move. In a move, a player must choose an index i ( 1≤i≤n) '
             'that has not been chosen before, and change si to any other '
             'lowercase English letter c that c= ̸si. When all indices have '
             'been chosen, the game ends. The goal of Alice is to make the '
             'final string lexicographically as small as possible, while the '
             'goal of Bob is to make the final string lexicographically as '
             'large as possible. Both of them are game experts, so they always '
             'play games optimally. Homer is not a game expert, so he wonders '
             'what the final string will be. A string a is lexicographically '
             'smaller than a string b if and only if one of the following '
             'holds: a is a prefix of b, but a= ̸b; in the first position '
             'where a and b differ, the string a has a letter that appears '
             'earlier in the alphabet than the corresponding letter in b.',
  'input': 'Each test contains multiple test cases. The first line contains t '
           '( 1≤t≤1000) — the number of test cases. Description of the test '
           'cases follows. The only line of each test case contains a single '
           'string s ( 1≤| s| ≤50) consisting of lowercase English letters.',
  'note': 'In the first test case: Alice makes the first move and must change '
          "the only letter to a different one, so she changes it to ' b' . In "
          "the second test case: Alice changes the first letter to ' a' , then "
          "Bob changes the second letter to ' z' , Alice changes the third "
          "letter to ' a' and then Bob changes the fourth letter to ' z' . In "
          "the third test case: Alice changes the first letter to ' b' , and "
          "then Bob changes the second letter to ' y' .",
  'output': 'For each test case, print the final string in a single line.',
  'title': 'Yet Another String Game',
  'topics': ['games', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1480/A'},
 {'history': 'The great hero guards the country where Homer lives. The hero '
             'has attack power A and initial health value B. There are n '
             'monsters in front of the hero. The i- th monster has attack '
             'power ai and initial health value bi. The hero or a monster is '
             'said to be living, if his or its health value is positive ( '
             'greater than or equal to 1) ; and he or it is said to be dead, '
             'if his or its health value is non- positive ( less than or equal '
             'to 0) . In order to protect people in the country, the hero will '
             'fight with monsters until either the hero is dead or all the '
             'monsters are dead. In each fight, the hero can select an '
             'arbitrary living monster and fight with it. Suppose the i- th '
             'monster is selected, and the health values of the hero and the '
             'i- th monster are x and y before the fight, respectively. After '
             'the fight, the health values of the hero and the i- th monster '
             'become x−ai and y−A, respectively. Note that the hero can fight '
             'the same monster more than once. For the safety of the people in '
             'the country, please tell them whether the great hero can kill '
             'all the monsters ( even if the great hero himself is dead after '
             'killing the last monster) .',
  'input': 'Each test contains multiple test cases. The first line contains t '
           '( 1≤t≤105) — the number of test cases. Description of the test '
           'cases follows. The first line of each test case contains three '
           'integers A ( 1≤A≤106) , B ( 1≤B≤106) and n ( 1≤n≤105) — the attack '
           'power of the great hero, the initial health value of the great '
           'hero, and the number of monsters. The second line of each test '
           'case contains n integers a1, a2, . . . , an ( 1≤ai≤106) , where ai '
           'denotes the attack power of the i- th monster. The third line of '
           'each test case contains n integers b1, b2, . . . , bn ( 1≤bi≤106) '
           ', where bi denotes the initial health value of the i- th monster. '
           'It is guaranteed that the sum of n over all test cases does not '
           'exceed 105.',
  'note': 'In the first example: There will be 6 fights between the hero and '
          'the only monster. After that, the monster is dead and the health '
          'value of the hero becomes 17−6×2= 5> 0. So the answer is " YES" , '
          'and moreover, the hero is still living. In the second example: '
          'After all monsters are dead, the health value of the hero will '
          'become 709, regardless of the order of all fights. So the answer is '
          '" YES" . In the third example: A possible order is to fight with '
          'the 1- st, 2- nd, 3- rd and 4- th monsters. After all fights, the '
          'health value of the hero becomes −400. Unfortunately, the hero is '
          'dead, but all monsters are also dead. So the answer is " YES" . In '
          'the fourth example: The hero becomes dead but the monster is still '
          'living with health value 1000−999= 1. So the answer is " NO" .',
  'output': 'For each test case print the answer: " YES" ( without quotes) if '
            'the great hero can kill all the monsters. Otherwise, print " NO" '
            '( without quotes) .',
  'title': 'The Great Hero',
  'topics': ['greedy', 'implementation', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1480/B'},
 {'history': 'You were dreaming that you are traveling to a planet named '
             'Planetforces on your personal spaceship. Unfortunately, its '
             'piloting system was corrupted and now you need to fix it in '
             'order to reach Planetforces. Space can be represented as the '
             'XYXY plane. You are starting at point ( 0, 0) ( 0, 0) , and '
             'Planetforces is located in point ( px, py) ( px, py) . The '
             'piloting system of your spaceship follows its list of orders '
             'which can be represented as a string ss. The system reads ss '
             'from left to right. Suppose you are at point ( x, y) ( x, y) and '
             'current order is sisi: if si= Usi= U, you move to ( x, y+ 1) ( '
             'x, y+ 1) ; if si= Dsi= D, you move to ( x, y−1) ( x, y−1) ; if '
             'si= Rsi= R, you move to ( x+ 1, y) ( x+ 1, y) ; if si= Lsi= L, '
             'you move to ( x−1, y) ( x−1, y) . Since string ss could be '
             "corrupted, there is a possibility that you won' t reach "
             'Planetforces in the end. Fortunately, you can delete some orders '
             "from ss but you can' t change their positions. Can you delete "
             'several orders ( possibly, zero) from ss in such a way, that '
             "you' ll reach Planetforces after the system processes all "
             'orders?',
  'input': 'The first line contains a single integer tt ( 1≤t≤10001≤t≤1000) — '
           'the number of test cases. Each test case consists of two lines. '
           'The first line in each test case contains two integers pxpx and '
           'pypy ( −105≤px, py≤105−105≤px, py≤105; ( px, py) = ̸( 0, 0) ( px, '
           'py) = ̸( 0, 0) ) — the coordinates of Planetforces ( px, py) ( px, '
           'py) . The second line contains the string ss ( 1≤| s| ≤1051≤| s| '
           '≤105: | s| | s| is the length of string ss) — the list of orders. '
           'It is guaranteed that the sum of | s| | s| over all test cases '
           'does not exceed 105105.',
  'note': "In the first case, you don' t need to modify ss, since the given ss "
          'will bring you to Planetforces. In the second case, you can delete '
          'orders s2s2, s3s3, s4s4, s6s6, s7s7 and s8s8, so ss becomes equal '
          'to " UR" . In the third test case, you have to delete order s9s9, '
          "otherwise, you won' t finish in the position of Planetforces.",
  'output': 'For each test case, print " YES" if you can delete several orders '
            "( possibly, zero) from ss in such a way, that you' ll reach "
            'Planetforces. Otherwise, print " NO" . You can print each letter '
            'in any case ( upper or lower) .',
  'title': 'Space Navigation ',
  'topics': ['greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1481/A'},
 {'history': 'You are given an array of integers b1, b2, . . . , bn. An array '
             'a1, a2, . . . , an of integers is hybrid if for each i ( 1≤i≤n) '
             'at least one of these conditions is true: bi= ai, or bi= ∑ij= '
             '1aj. Find the number of hybrid arrays a1, a2, . . . , an. As the '
             'result can be very large, you should print the answer modulo '
             '109+ 7.',
  'input': 'The first line contains a single integer t ( 1≤t≤104) — the number '
           'of test cases. The first line of each test case contains a single '
           'integer n ( 1≤n≤2⋅105) . The second line of each test case '
           'contains n integers b1, b2, . . . , bn ( −109≤bi≤109) . It is '
           'guaranteed that the sum of n for all test cases does not exceed '
           '2⋅105.',
  'note': 'In the first test case, the hybrid arrays are [ 1, −2, 1] , [ 1, '
          '−2, 2] , [ 1, −1, 1] . In the second test case, the hybrid arrays '
          'are [ 1, 1, 1, 1] , [ 1, 1, 1, 4] , [ 1, 1, 3, −1] , [ 1, 1, 3, 4] '
          ', [ 1, 2, 0, 1] , [ 1, 2, 0, 4] , [ 1, 2, 3, −2] , [ 1, 2, 3, 4] . '
          'In the fourth test case, the only hybrid array is [ 0, 0, 0, 1] .',
  'output': 'For each test case, print a single integer: the number of hybrid '
            'arrays a1, a2, . . . , an modulo 109+ 7.',
  'title': 'Copy or Prefix Sum',
  'topics': ['combinatorics', 'data structures', 'dp', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1485/F'},
 {'history': 'You and your friends live in nn houses. Each house is located on '
             'a 2D plane, in a point with integer coordinates. There might be '
             'different houses located in the same point. The mayor of the '
             'city is asking you for places for the building of the Eastern '
             'exhibition. You have to find the number of places ( points with '
             'integer coordinates) , so that the summary distance from all the '
             'houses to the exhibition is minimal. The exhibition can be built '
             'in the same point as some house. The distance between two points '
             '( x1, y1) ( x1, y1) and ( x2, y2) ( x2, y2) is | x1−x2| + | '
             'y1−y2| | x1−x2| + | y1−y2| , where | x| | x| is the absolute '
             'value of xx.',
  'input': 'First line contains a single integer tt ( 1≤t≤1000) ( 1≤t≤1000) — '
           'the number of test cases. The first line of each test case '
           'contains a single integer nn ( 1≤n≤1000) ( 1≤n≤1000) . Next nn '
           'lines describe the positions of the houses ( xi, yi) ( xi, yi) ( '
           "0≤xi, yi≤109) ( 0≤xi, yi≤109) . It' s guaranteed that the sum of "
           'all nn does not exceed 10001000.',
  'note': 'Here are the images for the example test cases. Blue dots stand for '
          'the houses, green — possible positions for the exhibition. First '
          'test case. Second test case. Third test case. Fourth test case. '
          'Fifth test case. Sixth test case. Here both houses are located at ( '
          '0, 0) ( 0, 0) .',
  'output': 'For each test case output a single integer - the number of '
            'different positions for the exhibition. The exhibition can be '
            'built in the same point as some house.',
  'title': 'Eastern Exhibition',
  'topics': ['binary search', 'geometry', 'shortest paths', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1486/B'},
 {'history': 'n heroes fight against each other in the Arena. Initially, the '
             'i- th hero has level ai. Each minute, a fight between two '
             'different heroes occurs. These heroes can be chosen arbitrarily '
             "( it' s even possible that it is the same two heroes that were "
             'fighting during the last minute) . When two heroes of equal '
             'levels fight, nobody wins the fight. When two heroes of '
             'different levels fight, the one with the higher level wins, and '
             'his level increases by 1. The winner of the tournament is the '
             "first hero that wins in at least 100500 fights ( note that it' s "
             'possible that the tournament lasts forever if no hero wins this '
             'number of fights, then there is no winner) . A possible winner '
             'is a hero such that there exists a sequence of fights that this '
             'hero becomes the winner of the tournament. Calculate the number '
             'of possible winners among n heroes.',
  'input': 'The first line contains one integer t ( 1≤t≤500) — the number of '
           'test cases. Each test case consists of two lines. The first line '
           'contains one integer n ( 2≤n≤100) — the number of heroes. The '
           'second line contains n integers a1, a2, . . . , an ( 1≤ai≤100) , '
           'where ai is the initial level of the i- th hero.',
  'note': 'In the first test case of the example, the only possible winner is '
          'the first hero. In the second test case of the example, each fight '
          'between the heroes results in nobody winning it, so the tournament '
          'lasts forever and there is no winner.',
  'output': 'For each test case, print one integer — the number of possible '
            'winners among the given n heroes.',
  'title': 'Arena',
  'topics': ['implementation', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1487/A'},
 {'history': 'Ivan wants to have a good dinner. A good dinner should consist '
             'of a first course, a second course, a drink, and a dessert. '
             'There are n1 different types of first courses Ivan can buy ( the '
             'i- th of them costs ai coins) , n2 different types of second '
             'courses ( the i- th of them costs bi coins) , n3 different types '
             'of drinks ( the i- th of them costs ci coins) and n4 different '
             'types of desserts ( the i- th of them costs di coins) . Some '
             "dishes don' t go well with each other. There are m1 pairs of "
             "first courses and second courses that don' t go well with each "
             'other, m2 pairs of second courses and drinks, and m3 pairs of '
             "drinks and desserts that don' t go well with each other. Ivan "
             'wants to buy exactly one first course, one second course, one '
             'drink, and one dessert so that they go well with each other, and '
             'the total cost of the dinner is the minimum possible. Help him '
             'to find the cheapest dinner option!',
  'input': 'The first line contains four integers n1, n2, n3 and n4 ( '
           '1≤ni≤150000) — the number of types of first courses, second '
           'courses, drinks and desserts, respectively. Then four lines '
           'follow. The first line contains n1 integers a1, a2, . . . , an1 ( '
           '1≤ai≤108) , where ai is the cost of the i- th type of first '
           'course. Three next lines denote the costs of second courses, '
           'drinks, and desserts in the same way ( 1≤bi, ci, di≤108) . The '
           'next line contains one integer m1 ( 0≤m1≤200000) — the number of '
           "pairs of first and second courses that don' t go well with each "
           'other. Each of the next m1 lines contains two integers xi and yi ( '
           "1≤xi≤n1; 1≤yi≤n2) denoting that the first course number xi doesn' "
           't go well with the second course number yi. All these pairs are '
           'different. The block of pairs of second dishes and drinks that '
           "don' t go well with each other is given in the same format. The "
           "same for pairs of drinks and desserts that don' t go well with "
           'each other ( 0≤m2, m3≤200000) .',
  'note': 'The best option in the first example is to take the first course 2, '
          'the second course 1, the drink 2 and the dessert 1. In the second '
          'example, the only pair of the first course and the second course is '
          "bad, so it' s impossible to have dinner.",
  'output': "If it' s impossible to choose a first course, a second course, a "
            'drink, and a dessert so that they go well with each other, print '
            '−1. Otherwise, print one integer — the minimum total cost of the '
            'dinner.',
  'title': 'Cheap Dinner',
  'topics': ['brute force',
             'data structures',
             'graphs',
             'greedy',
             'implementation',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1487/E'},
 {'history': 'Polycarp was gifted an array a of length n. Polycarp considers '
             'an array beautiful if there exists a number C, such that each '
             'number in the array occurs either zero or C times. Polycarp '
             'wants to remove some elements from the array a to make it '
             'beautiful. For example, if n= 6 and a= [ 1, 3, 2, 1, 4, 2] , '
             'then the following options are possible to make the array a '
             'array beautiful: Polycarp removes elements at positions 2 and 5, '
             'array a becomes equal to [ 1, 2, 1, 2] ; Polycarp removes '
             'elements at positions 1 and 6, array a becomes equal to [ 3, 2, '
             '1, 4] ; Polycarp removes elements at positions 1, 2 and 6, array '
             'a becomes equal to [ 2, 1, 4] ; Help Polycarp determine the '
             'minimum number of elements to remove from the array a to make it '
             'beautiful.',
  'input': 'The first line contains one integer t ( 1≤t≤104) — the number of '
           'test cases. Then t test cases follow. The first line of each test '
           'case consists of one integer n ( 1≤n≤2⋅105) — the length of the '
           'array a. The second line of each test case contains n integers a1, '
           'a2, . . . , an ( 1≤ai≤109) — array a. It is guaranteed that the '
           'sum of n over all test cases does not exceed 2⋅105.',
  'note': ' ',
  'output': 'For each test case, output one integer — the minimum number of '
            'elements that Polycarp has to remove from the array a to make it '
            'beautiful.',
  'title': 'Equalize the Array',
  'topics': ['binary search', 'data structures', 'greedy', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1490/F'},
 {'history': 'You are given a string s consisting of lowercase English letters '
             "and a number k. Let' s call a string consisting of lowercase "
             'English letters beautiful if the number of occurrences of each '
             'letter in that string is divisible by k. You are asked to find '
             'the lexicographically smallest beautiful string of length n, '
             'which is lexicographically greater or equal to string s. If such '
             'a string does not exist, output −1. A string a is '
             'lexicographically smaller than a string b if and only if one of '
             'the following holds: a is a prefix of b, but a= ̸b; in the first '
             'position where a and b differ, the string a has a letter that '
             'appears earlier in the alphabet than the corresponding letter in '
             'b.',
  'input': 'The first line contains a single integer T ( 1≤T≤10000) — the '
           'number of test cases. The next 2⋅T lines contain the description '
           'of test cases. The description of each test case consists of two '
           'lines. The first line of the description contains two integers n '
           'and k ( 1≤k≤n≤105) — the length of string s and number k '
           'respectively. The second line contains string s consisting of '
           'lowercase English letters. It is guaranteed that the sum of n over '
           'all test cases does not exceed 105.',
  'note': 'In the first test case " acac" is greater than or equal to s, and '
          'each letter appears 2 or 0 times in it, so it is beautiful. In the '
          'second test case each letter appears 0 or 1 times in s, so s itself '
          'is the answer. We can show that there is no suitable string in the '
          'third test case. In the fourth test case each letter appears 0, 3, '
          'or 6 times in " abaabaaab" . All these integers are divisible by 3.',
  'output': 'For each test case output in a separate line lexicographically '
            'smallest beautiful string of length n, which is greater or equal '
            'to string s, or −1 if such a string does not exist.',
  'title': 'K-beautiful Strings',
  'topics': ['binary search',
             'brute force',
             'constructive algorithms',
             'greedy',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1493/C'},
 {'history': 'You are given an array a of length n. You are asked to process q '
             'queries of the following format: given integers i and x, '
             'multiply ai by x. After processing each query you need to output '
             'the greatest common divisor ( GCD) of all elements of the array '
             'a. Since the answer can be too large, you are asked to output it '
             'modulo 109+ 7.',
  'input': 'The first line contains two integers — n and q ( 1≤n, q≤2⋅105) . '
           'The second line contains n integers a1, a2, . . . , an ( '
           '1≤ai≤2⋅105) — the elements of the array a before the changes. The '
           'next q lines contain queries in the following format: each line '
           'contains two integers i and x ( 1≤i≤n, 1≤x≤2⋅105) .',
  'note': 'After the first query the array is [ 12, 6, 8, 12] , gcd( 12, 6, 8, '
          '12) = 2. After the second query — [ 12, 18, 8, 12] , gcd( 12, 18, '
          '8, 12) = 2. After the third query — [ 12, 18, 24, 12] , gcd( 12, '
          '18, 24, 12) = 6. Here the gcd function denotes the greatest common '
          'divisor.',
  'output': 'Print q lines: after processing each query output the GCD of all '
            'elements modulo 109+ 7 on a separate line.',
  'title': 'GCD of an Array',
  'topics': ['brute force',
             'data structures',
             'hashing',
             'implementation',
             'math',
             'number theory',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1493/D'},
 {'history': 'You are given two integers l and r in binary representation. Let '
             'g( x, y) be equal to the bitwise XOR of all integers from x to y '
             "inclusive ( that is x⊕( x+ 1) ⊕⋯⊕( y−1) ⊕y) . Let' s define f( "
             'l, r) as the maximum of all values of g( x, y) satisfying '
             'l≤x≤y≤r. Output f( l, r) .',
  'input': 'The first line contains a single integer n ( 1≤n≤106) — the length '
           'of the binary representation of r. The second line contains the '
           'binary representation of l — a string of length n consisting of '
           'digits 0 and 1 ( 0≤l< 2n) . The third line contains the binary '
           'representation of r — a string of length n consisting of digits 0 '
           'and 1 ( 0≤r< 2n) . It is guaranteed that l≤r. The binary '
           'representation of r does not contain any extra leading zeros ( if '
           'r= 0, the binary representation of it consists of a single zero) . '
           'The binary representation of l is preceded with leading zeros so '
           'that its length is equal to n.',
  'note': 'In sample test case l= 19, r= 122. f( x, y) is maximal and is equal '
          'to 127, with x= 27, y= 100, for example.',
  'output': 'In a single line output the value of f( l, r) for the given pair '
            'of l and r in binary representation without extra leading zeros.',
  'title': 'Enormous XOR',
  'topics': ['bitmasks',
             'constructive algorithms',
             'greedy',
             'math',
             'strings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1493/E'},
 {'history': 'The Dogeforces company has kk employees. Each employee, except '
             'for lower- level employees, has at least 22 subordinates. Lower- '
             'level employees have no subordinates. Each employee, except for '
             'the head of the company, has exactly one direct supervisor. The '
             'head of the company is a direct or indirect supervisor of all '
             'employees. It is known that in Dogeforces, each supervisor '
             'receives a salary strictly more than all his subordinates. The '
             'full structure of the company is a secret, but you know the '
             'number of lower- level employees and for each pair of lower- '
             'level employees, the salary of their common supervisor is known '
             '( if there are several such supervisors, then the supervisor '
             'with the minimum salary) . You have to restore the structure of '
             'the company.',
  'input': 'The first line contains a single integer nn ( 2≤n≤5002≤n≤500) — '
           'the number of lower- level employees. This is followed by nn '
           'lines, where ii- th line contains nn integers ai, 1, ai, 2, . . . '
           ', ai, nai, 1, ai, 2, . . . , ai, n ( 1≤ai, j≤50001≤ai, j≤5000) — '
           'salary of the common supervisor of employees with numbers ii and '
           'jj. It is guaranteed that ai, j= aj, iai, j= aj, i. Note that ai, '
           'iai, i is equal to the salary of the ii- th employee.',
  'note': 'One of the possible structures in the first example:',
  'output': 'In the first line, print a single integer kk — the number of '
            'employees in the company. In the second line, print kk integers '
            'c1, c2, . . . , ckc1, c2, . . . , ck, where cici is the salary of '
            'the employee with the number ii. In the third line, print a '
            'single integer rr — the number of the employee who is the head of '
            'the company. In the following k−1k−1 lines, print two integers vv '
            'and uu ( 1≤v, u≤k1≤v, u≤k) — the number of the employee and his '
            'direct supervisor. Note that the lower- level employees have '
            'numbers from 11 to nn, and for the rest of the employees, you '
            'have to assign numbers from n+ 1n+ 1 to kk. If there are several '
            'correct company structures, you can print any of them.',
  'title': 'Dogeforces',
  'topics': ['constructive algorithms',
             'data structures',
             'dfs and similar',
             'divide and conquer',
             'dsu',
             'greedy',
             'sortings',
             'trees'],
  'url': 'https://codeforces.com/problemset/problem/1494/D'},
 {'history': 'Diamond Miner is a game that is similar to Gold Miner, but there '
             'are n miners instead of 1 in this game. The mining area can be '
             'described as a plane. The n miners can be regarded as n points '
             'on the y- axis. There are n diamond mines in the mining area. We '
             'can regard them as n points on the x- axis. For some reason, no '
             'miners or diamond mines can be at the origin ( point ( 0, 0) ) . '
             'Every miner should mine exactly one diamond mine. Every miner '
             'has a hook, which can be used to mine a diamond mine. If a miner '
             'at the point ( a, b) uses his hook to mine a diamond mine at the '
             'point ( c, d) , he will spend √( a−c) 2+ ( b−d) 2 energy to mine '
             "it ( the distance between these points) . The miners can' t move "
             'or help each other. The object of this game is to minimize the '
             'sum of the energy that miners spend. Can you find this minimum?',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤10) — the number of test cases. The '
           'description of the test cases follows. The first line of each test '
           'case contains a single integer n ( 1≤n≤105) — the number of miners '
           'and mines. Each of the next 2n lines contains two space- separated '
           'integers x ( −108≤x≤108) and y ( −108≤y≤108) , which represent the '
           "point ( x, y) to describe a miner' s or a diamond mine' s "
           'position. Either x= 0, meaning there is a miner at the point ( 0, '
           'y) , or y= 0, meaning there is a diamond mine at the point ( x, 0) '
           '. There can be multiple miners or diamond mines at the same point. '
           'It is guaranteed that no point is at the origin. It is guaranteed '
           'that the number of points on the x- axis is equal to n and the '
           "number of points on the y- axis is equal to n. It' s guaranteed "
           'that the sum of n for all test cases does not exceed 105.',
  'note': 'In the first test case, the miners are at ( 0, 1) and ( 0, −1) , '
          'while the diamond mines are at ( 1, 0) and ( −2, 0) . If you '
          'arrange the miners to get the diamond mines in the way, shown in '
          'the picture, you can get the sum of the energy √2+ √5.',
  'output': 'For each test case, print a single real number — the minimal sum '
            'of energy that should be spent. Your answer is considered correct '
            'if its absolute or relative error does not exceed 10−9. Formally, '
            "let your answer be a, and the jury' s answer be b. Your answer is "
            'accepted if and only if | a−b| max( 1, | b| ) ≤10−9.',
  'title': 'Diamond Miner',
  'topics': ['geometry', 'greedy', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1495/A'},
 {'history': 'Kawashiro Nitori is a girl who loves competitive programming. '
             'One day she found a string and an integer. As an advanced '
             'problem setter, she quickly thought of a problem. Given a string '
             's and a parameter k, you need to check if there exist k+ 1 non- '
             'empty strings a1, a2. . . , ak+ 1, such that s= a1+ a2+ . . . + '
             'ak+ ak+ 1+ R( ak) + R( ak−1) + . . . + R( a1) . Here + '
             'represents concatenation. We define R( x) as a reversed string '
             'x. For example R( abcd) = dcba. Note that in the formula above '
             'the part R( ak+ 1) is intentionally skipped.',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤100) — the number of test cases. The '
           'description of the test cases follows. The first line of each test '
           'case description contains two integers n, k ( 1≤n≤100, 0≤k≤⌊n2⌋) — '
           'the length of the string s and the parameter k. The second line of '
           'each test case description contains a single string s of length n, '
           'consisting of lowercase English letters.',
  'note': 'In the first test case, one possible solution is a1= qw and a2= q. '
          'In the third test case, one possible solution is a1= i and a2= o. '
          'In the fifth test case, one possible solution is a1= '
          'dokidokiliteratureclub.',
  'output': 'For each test case, print " YES" ( without quotes) , if it is '
            'possible to find a1, a2, . . . , ak+ 1, and " NO" ( without '
            'quotes) otherwise. You can print letters in any case ( upper or '
            'lower) .',
  'title': 'Split it!',
  'topics': ['brute force', 'constructive algorithms', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1496/A'},
 {'history': 'You are given an integer n and an array a1, a2, . . . , an. You '
             'should reorder the elements of the array a in such way that the '
             'sum of MEX on prefixes ( i- th prefix is a1, a2, . . . , ai) is '
             'maximized. Formally, you should find an array b1, b2, . . . , '
             'bn, such that the sets of elements of arrays a and b are equal ( '
             'it is equivalent to array b can be found as an array a with some '
             'reordering of its elements) and n∑i= 1MEX( b1, b2, . . . , bi) '
             'is maximized. MEX of a set of nonnegative integers is the '
             'minimal nonnegative integer such that it is not in the set. For '
             'example, MEX( 1, 2, 3) = 0, MEX( 0, 1, 2, 4, 5) = 3.',
  'input': 'The first line contains a single integer t ( 1≤t≤100) — the number '
           'of test cases. The first line of each test case contains a single '
           'integer n ( 1≤n≤100) . The second line of each test case contains '
           'n integers a1, a2, . . . , an ( 0≤ai≤100) .',
  'note': 'In the first test case in the answer MEX for prefixes will be: MEX( '
          '0) = 1 MEX( 0, 1) = 2 MEX( 0, 1, 2) = 3 MEX( 0, 1, 2, 3) = 4 MEX( '
          '0, 1, 2, 3, 4) = 5 MEX( 0, 1, 2, 3, 4, 7) = 5 MEX( 0, 1, 2, 3, 4, '
          '7, 3) = 5 The sum of MEX= 1+ 2+ 3+ 4+ 5+ 5+ 5= 25. It can be '
          'proven, that it is a maximum possible sum of MEX on prefixes.',
  'output': 'For each test case print an array b1, b2, . . . , bn — the '
            'optimal reordering of a1, a2, . . . , an, so the sum of MEX on '
            'its prefixes is maximized. If there exist multiple optimal '
            'answers you can find any.',
  'title': 'Meximization',
  'topics': ['brute force', 'data structures', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1497/A'},
 {'history': 'This is an interactive problem. Remember to flush your output '
             'while communicating with the testing program. You may use '
             'fflush( stdout) in C+ + , system. out. flush( ) in Java, stdout. '
             'flush( ) in Python or flush( output) in Pascal to flush the '
             'output. If you use some other programming language, consult its '
             'documentation. You may also refer to the guide on interactive '
             'problems: https: / / codeforces. com/ blog/ entry/ 45307. There '
             'is a city in which Dixit lives. In the city, there are n houses. '
             'There is exactly one directed road between every pair of houses. '
             'For example, consider two houses A and B, then there is a '
             'directed road either from A to B or from B to A but not both. '
             'The number of roads leading to the i- th house is ki. Two houses '
             'A and B are bi- reachable if A is reachable from B and B is '
             'reachable from A. We say that house B is reachable from house A '
             'when there is a path from house A to house B. Dixit wants to buy '
             'two houses in the city, that is, one for living and one for '
             'studying. Of course, he would like to travel from one house to '
             'another. So, he wants to find a pair of bi- reachable houses A '
             'and B. Among all such pairs, he wants to choose one with the '
             'maximum value of | kA−kB| , where ki is the number of roads '
             'leading to the house i. If more than one optimal pair exists, '
             'any of them is suitable. Since Dixit is busy preparing '
             'CodeCraft, can you help him find the desired pair of houses, or '
             'tell him that no such houses exist? In the problem input, you '
             'are not given the direction of each road. You are given — for '
             'each house — only the number of incoming roads to that house ( '
             'ki) . You are allowed to ask only one type of query from the '
             'judge: give two houses A and B, and the judge answers whether B '
             'is reachable from A. There is no upper limit on the number of '
             'queries. But, you cannot ask more queries after the judge '
             'answers " Yes" to any of your queries. Also, you cannot ask the '
             'same query twice. Once you have exhausted all your queries ( or '
             'the judge responds " Yes" to any of your queries) , your program '
             'must output its guess for the two houses and quit. See the '
             'Interaction section below for more details. InteractionTo ask a '
             'query, print " ? A B" ( 1≤A, B≤N, A= ̸B) . The judge will '
             'respond " Yes" if house B is reachable from house A, or " No" '
             'otherwise. To output the final answer, print " ! A B" , where A '
             'and B are bi- reachable with the maximum possible value of | '
             'kA−kB| . If there does not exist such pair of houses A and B, '
             'output " ! 0 0" . After outputting the final answer, your '
             'program must terminate immediately, otherwise you will receive '
             'Wrong Answer verdict. You cannot ask the same query twice. There '
             'is no upper limit to the number of queries you ask, but, you '
             'cannot ask more queries after the judge answers " Yes" to any of '
             'your queries. Your program must now output the final answer ( " '
             '! A B" or " ! 0 0" ) and terminate. If you ask a query in '
             'incorrect format or repeat a previous query, you will get Wrong '
             'Answer verdict. After printing a query do not forget to output '
             'the end of the line and flush the output. Otherwise, you will '
             'get the Idleness limit exceeded error. To do this, use: fflush( '
             'stdout) or cout. flush( ) in C+ + ; System. out. flush( ) in '
             'Java; flush( output) in Pascal; stdout. flush( ) in Python; see '
             'documentation for other languages.',
  'input': 'The first line contains a single integer n ( 3≤n≤500) denoting the '
           'number of houses in the city. The next line contains n space- '
           'separated integers k1, k2, . . . , kn ( 0≤ki≤n−1) , the i- th of '
           'them represents the number of incoming roads to the i- th house.',
  'note': 'In the first sample input, we are given a city of three houses with '
          'one incoming road each. The user program asks one query: " ? 1 2" : '
          'asking whether we can reach from house 1 to house 2. The judge '
          'responds with " Yes" . The user program now concludes that this is '
          'sufficient information to determine the correct answer. So, it '
          'outputs " ! 1 2" and quits. In the second sample input, the user '
          'program queries for six different pairs of houses, and finally '
          'answers " ! 0 0" as it is convinced that no two houses as desired '
          'in the question exist in this city.',
  'output': ' ',
  'title': 'Two Houses',
  'topics': ['brute force', 'graphs', 'greedy', 'interactive', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1498/E'},
 {'history': 'You are given two strings x and y, both consist only of '
             'lowercase Latin letters. Let | s| be the length of string s. '
             "Let' s call a sequence a a merging sequence if it consists of "
             'exactly | x| zeros and exactly | y| ones in some order. A merge '
             'z is produced from a sequence a by the following rules: if ai= '
             '0, then remove a letter from the beginning of x and append it to '
             'the end of z; if ai= 1, then remove a letter from the beginning '
             'of y and append it to the end of z. Two merging sequences a and '
             'b are different if there is some position i such that ai= ̸bi. '
             "Let' s call a string z chaotic if for all i from 2 to | z| zi−1= "
             '̸zi. Let s[ l, r] for some 1≤l≤r≤| s| be a substring of '
             'consecutive letters of s, starting from position l and ending at '
             'position r inclusive. Let f( l1, r1, l2, r2) be the number of '
             'different merging sequences of x[ l1, r1] and y[ l2, r2] that '
             'produce chaotic merges. Note that only non- empty substrings of '
             'x and y are considered. Calculate ∑1≤l1≤r1≤| x| 1≤l2≤r2≤| y| f( '
             'l1, r1, l2, r2) . Output the answer modulo 998244353.',
  'input': 'The first line contains a string x ( 1≤| x| ≤1000) . The second '
           'line contains a string y ( 1≤| y| ≤1000) . Both strings consist '
           'only of lowercase Latin letters.',
  'note': 'In the first example there are: 6 pairs of substrings " a" and " b" '
          ', each with valid merging sequences " 01" and " 10" ; 3 pairs of '
          'substrings " a" and " bb" , each with a valid merging sequence " '
          '101" ; 4 pairs of substrings " aa" and " b" , each with a valid '
          'merging sequence " 010" ; 2 pairs of substrings " aa" and " bb" , '
          'each with valid merging sequences " 0101" and " 1010" ; 2 pairs of '
          'substrings " aaa" and " b" , each with no valid merging sequences; '
          '1 pair of substrings " aaa" and " bb" with a valid merging sequence '
          '" 01010" ; Thus, the answer is 6⋅2+ 3⋅1+ 4⋅1+ 2⋅2+ 2⋅0+ 1⋅1= 24.',
  'output': 'Print a single integer — the sum of f( l1, r1, l2, r2) over '
            '1≤l1≤r1≤| x| and 1≤l2≤r2≤| y| modulo 998244353.',
  'title': 'Chaotic Merge',
  'topics': ['combinatorics', 'dp', 'math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1499/E'},
 {'history': 'Kostya is extremely busy: he is renovating his house! He needs '
             'to hand wallpaper, assemble furniture throw away trash. Kostya '
             'is buying tiles for bathroom today. He is standing in front of a '
             'large square stand with tiles in a shop. The stand is a square '
             'of n×n cells, each cell of which contains a small tile with '
             'color ci, j. The shop sells tiles in packs: more specifically, '
             'you can only buy a subsquare of the initial square. A subsquare '
             'is any square part of the stand, i. e. any set S( i0, j0, k) = '
             'ci, j | i0≤i< i0+ k, j0≤j< j0+ k with 1≤i0, j0≤n−k+ 1. Kostya '
             'still does not know how many tiles he needs, so he considers the '
             "subsquares of all possible sizes. He doesn' t want his bathroom "
             'to be too colorful. Help Kostya to count for each k≤n the number '
             'of subsquares of size k×k that have at most q different colors '
             'of tiles. Two subsquares are considered different if their '
             'location on the stand is different.',
  'input': 'The first line contains two integers n and q ( 1≤n≤1500, 1≤q≤10) — '
           'the size of the stand and the limit on the number of distinct '
           'colors in a subsquare. Each of the next n lines contains n '
           'integers ci, j ( 1≤ci, j≤n2) : the j- th integer in the i- th line '
           'is the color of the tile in the cell ( i, j) .',
  'note': "In the first example all colors are distinct. Kostya doesn' t want "
          'the subsquare have more than 4 colors, so he can buy any subsquare '
          "of size 1×1 or 2×2, but he can' t buy a subsquare of size 3×3. In "
          'the second example there are colors that appear multiple times. '
          'Because q= 8, Kostya can buy any subsquare of size 1×1 and 2×2, and '
          'any subsquare 3×3, because of such subsquare has 7 different '
          "colors. He can' t buy the whole stand 4×4, because there are 9 "
          'colors.',
  'output': 'For each k from 1 to n print a single integer — the number of '
            'subsquares of size k×k with no more than q different colors.',
  'title': 'Tiles for Bathroom',
  'topics': ['data structures', 'sortings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1500/D'},
 {'history': 'This week Arkady wanted to cook some pancakes ( to follow '
             'ancient traditions) and make a problem about that. But then he '
             "remembered that one can' t make a problem about stacking "
             'pancakes without working at a specific IT company, so he decided '
             'to bake the Napoleon cake instead. To bake a Napoleon cake, one '
             'has to bake n dry layers first, and then put them on each other '
             'in one stack, adding some cream. Arkady started with an empty '
             'plate, and performed the following steps n times: place a new '
             'cake layer on the top of the stack; after the i- th layer is '
             'placed, pour ai units of cream on top of the stack. When x units '
             'of cream are poured on the top of the stack, top x layers of the '
             'cake get drenched in the cream. If there are less than x layers, '
             'all layers get drenched and the rest of the cream is wasted. If '
             'x= 0, no layer gets drenched. The picture represents the first '
             'test case of the example. Help Arkady determine which layers of '
             'the cake eventually get drenched when the process is over, and '
             "which don' t.",
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤20000) . Description of the test '
           'cases follows. The first line of each test case contains a single '
           'integer n ( 1≤n≤2⋅105) — the number of layers in the cake. The '
           'second line of each test case contains n integers a1, a2, . . . , '
           'an ( 0≤ai≤n) — the amount of cream poured on the cake after adding '
           'each layer. It is guaranteed that the sum of n over all test cases '
           'does not exceed 2⋅105.',
  'note': ' ',
  'output': 'For each test case, print a single line with n integers. The i- '
            'th of the integers should be equal to 1 if the i- th layer from '
            'the bottom gets drenched, and 0 otherwise.',
  'title': 'Napoleon Cake',
  'topics': ['dp', 'implementation', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1501/B'},
 {'history': 'There are n cities numbered from 1 to n, and city i has beauty '
             'ai. A salesman wants to start at city 1, visit every city '
             'exactly once, and return to city 1. For all i= ̸j, a flight from '
             'city i to city j costs max( ci, aj−ai) dollars, where ci is the '
             'price floor enforced by city i. Note that there is no absolute '
             'value. Find the minimum total cost for the salesman to complete '
             'his trip.',
  'input': 'The first line contains a single integer n ( 2≤n≤105) — the number '
           'of cities. The i- th of the next n lines contains two integers ai, '
           'ci ( 0≤ai, ci≤109) — the beauty and price floor of the i- th city.',
  'note': 'In the first test case, we can travel in order 1→3→2→1. The flight '
          '1→3 costs max( c1, a3−a1) = max( 9, 4−1) = 9. The flight 3→2 costs '
          'max( c3, a2−a3) = max( 1, 2−4) = 1. The flight 2→1 costs max( c2, '
          'a1−a2) = max( 1, 1−2) = 1. The total cost is 11, and we cannot do '
          'better.',
  'output': 'Output a single integer — the minimum total cost.',
  'title': 'Travelling Salesman Problem',
  'topics': ['binary search',
             'data structures',
             'dp',
             'greedy',
             'shortest paths',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1503/C'},
 {'history': 'There is a deck of n cards. The i- th card has a number ai on '
             'the front and a number bi on the back. Every integer between 1 '
             'and 2n appears exactly once on the cards. A deck is called '
             'sorted if the front values are in increasing order and the back '
             'values are in decreasing order. That is, if ai< ai+ 1 and bi> '
             'bi+ 1 for all 1≤i< n. To flip a card i means swapping the values '
             'of ai and bi. You must flip some subset of cards ( possibly, '
             'none) , then put all the cards in any order you like. What is '
             'the minimum number of cards you must flip in order to sort the '
             'deck?',
  'input': 'The first line contains a single integer n ( 1≤n≤2⋅105) — the '
           'number of cards. The next n lines describe the cards. The i- th of '
           'these lines contains two integers ai, bi ( 1≤ai, bi≤2n) . Every '
           'integer between 1 and 2n appears exactly once.',
  'note': 'In the first test case, we flip the cards ( 1, 9) and ( 2, 7) . The '
          'deck is then ordered ( 3, 10) , ( 5, 8) , ( 6, 4) , ( 7, 2) , ( 9, '
          '1) . It is sorted because 3< 5< 6< 7< 9 and 10> 8> 4> 2> 1. In the '
          'second test case, it is impossible to sort the deck.',
  'output': 'If it is impossible to sort the deck, output " - 1" . Otherwise, '
            'output the minimum number of flips required to sort the deck.',
  'title': 'Flip the Cards',
  'topics': ['2-sat',
             'constructive algorithms',
             'data structures',
             'greedy',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1503/D'},
 {'history': 'A palindrome is a string that reads the same backward as '
             'forward. For example, the strings " z" , " aaa" , " aba" , and " '
             'abccba" are palindromes, but " codeforces" and " ab" are not. '
             'You hate palindromes because they give you déjà vu. There is a '
             "string s. You must insert exactly one character ' a' somewhere "
             'in s. If it is possible to create a string that is not a '
             'palindrome, you should find one example. Otherwise, you should '
             'report that it is impossible. For example, suppose s= " cbabc" . '
             'By inserting an \' a\' , you can create " acbabc" , " cababc" , '
             '" cbaabc" , " cbabac" , or " cbabca" . However " cbaabc" is a '
             'palindrome, so you must output one of the other options.',
  'input': 'The first line contains a single integer t ( 1≤t≤104) — the number '
           'of test cases. The only line of each test case contains a string s '
           'consisting of lowercase English letters. The total length of all '
           'strings does not exceed 3⋅105.',
  'note': 'The first test case is described in the statement. In the second '
          'test case, we can make either " aab" or " aba" . But " aba" is a '
          'palindrome, so " aab" is the only correct answer. In the third test '
          'case, " zaza" and " zzaa" are correct answers, but not " azza" . In '
          'the fourth test case, " baa" is the only correct answer. In the '
          'fifth test case, we can only make " aa" , which is a palindrome. So '
          'the answer is " NO" . In the sixth test case, " anutforajaroftuna" '
          "is a palindrome, but inserting ' a' elsewhere is valid.",
  'output': 'For each test case, if there is no solution, output " NO" . '
            'Otherwise, output " YES" followed by your constructed string of '
            'length | s| + 1 on the next line. If there are multiple '
            'solutions, you may print any. You can print each letter of " YES" '
            'and " NO" in any case ( upper or lower) .',
  'title': ' Déjà Vu',
  'topics': ['constructive algorithms', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1504/A'},
 {'history': 'You are given the strings a and b, consisting of lowercase Latin '
             'letters. You can do any number of the following operations in '
             'any order: if | a| > 0 ( the length of the string a is greater '
             'than zero) , delete the first character of the string a, that '
             'is, replace a with a2a3. . . an; if | a| > 0, delete the last '
             'character of the string a, that is, replace a with a1a2. . . '
             'an−1; if | b| > 0 ( the length of the string b is greater than '
             'zero) , delete the first character of the string b, that is, '
             'replace b with b2b3. . . bn; if | b| > 0, delete the last '
             'character of the string b, that is, replace b with b1b2. . . '
             'bn−1. Note that after each of the operations, the string a or b '
             'may become empty. For example, if a= " hello" and b= " icpc" , '
             'then you can apply the following sequence of operations: delete '
             'the first character of the string a ⇒ a= " ello" and b= " icpc" '
             '; delete the first character of the string b ⇒ a= " ello" and b= '
             '" cpc" ; delete the first character of the string b ⇒ a= " ello" '
             'and b= " pc" ; delete the last character of the string a ⇒ a= " '
             'ell" and b= " pc" ; delete the last character of the string b ⇒ '
             'a= " ell" and b= " p" . For the given strings a and b, find the '
             'minimum number of operations for which you can make the strings '
             'a and b equal. Note that empty strings are also equal.',
  'input': 'The first line contains a single integer t ( 1≤t≤100) . Then t '
           'test cases follow. The first line of each test case contains the '
           'string a ( 1≤| a| ≤20) , consisting of lowercase Latin letters. '
           'The second line of each test case contains the string b ( 1≤| b| '
           '≤20) , consisting of lowercase Latin letters.',
  'note': ' ',
  'output': 'For each test case, output the minimum number of operations that '
            'can make the strings a and b equal.',
  'title': 'Double-ended Strings',
  'topics': ['brute force', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1506/C'},
 {'history': "Consider an infinite triangle made up of layers. Let' s number "
             'the layers, starting from one, from the top of the triangle ( '
             'from top to bottom) . The kk- th layer of the triangle contains '
             'k points, numbered from left to right. Each point of an infinite '
             'triangle is described by a pair of numbers ( r, c) ( 1≤c≤r) , '
             'where r is the number of the layer, and c is the number of the '
             'point in the layer. From each point ( r, c) there are two '
             'directed edges to the points ( r+ 1, c) and ( r+ 1, c+ 1) , but '
             'only one of the edges is activated. If r+ c is even, then the '
             'edge to the point ( r+ 1, c) is activated, otherwise the edge to '
             'the point ( r+ 1, c+ 1) is activated. Look at the picture for a '
             'better understanding. Activated edges are colored in black. Non- '
             'activated edges are colored in gray. From the point ( r1, c1) it '
             'is possible to reach the point ( r2, c2) , if there is a path '
             'between them only from activated edges. For example, in the '
             'picture above, there is a path from ( 1, 1) to ( 3, 2) , but '
             'there is no path from ( 2, 1) to ( 1, 1) . Initially, you are at '
             'the point ( 1, 1) . For each turn, you can: Replace activated '
             'edge for point ( r, c) . That is if the edge to the point ( r+ '
             '1, c) is activated, then instead of it, the edge to the point ( '
             'r+ 1, c+ 1) becomes activated, otherwise if the edge to the '
             'point ( r+ 1, c+ 1) , then instead if it, the edge to the point '
             '( r+ 1, c) becomes activated. This action increases the cost of '
             'the path by 1; Move from the current point to another by '
             'following the activated edge. This action does not increase the '
             'cost of the path. You are given a sequence of n points of an '
             'infinite triangle ( r1, c1) , ( r2, c2) , . . . , ( rn, cn) . '
             'Find the minimum cost path from ( 1, 1) , passing through all n '
             'points in arbitrary order.',
  'input': 'The first line contains one integer t ( 1≤t≤104) is the number of '
           'test cases. Then t test cases follow. Each test case begins with a '
           'line containing one integer n ( 1≤n≤2⋅105) is the number of points '
           'to visit. The second line contains n numbers r1, r2, . . . , rn ( '
           '1≤ri≤109) , where ri is the number of the layer in which i- th '
           'point is located. The third line contains n numbers c1, c2, . . . '
           ', cn ( 1≤ci≤ri) , where ci is the number of the i- th point in the '
           'ri layer. It is guaranteed that all n points are distinct. It is '
           'guaranteed that there is always at least one way to traverse all n '
           'points. It is guaranteed that the sum of n over all test cases '
           'does not exceed 2⋅105.',
  'note': ' ',
  'output': 'For each test case, output the minimum cost of a path passing '
            'through all points in the corresponding test case.',
  'title': 'Triangular Paths',
  'topics': ['constructive algorithms',
             'graphs',
             'math',
             'shortest paths',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1506/F'},
 {'history': 'You are given a string s, consisting of lowercase Latin letters. '
             'While there is at least one character in the string s that is '
             'repeated at least twice, you perform the following operation: '
             'you choose the index i ( 1≤i≤| s| ) such that the character at '
             'position i occurs at least two times in the string s, and delete '
             'the character at position i, that is, replace s with s1s2. . . '
             'si−1si+ 1si+ 2. . . sn. For example, if s= " codeforces" , then '
             'you can apply the following sequence of operations: i= 6⇒s= " '
             'codefrces" ; i= 1⇒s= " odefrces" ; i= 7⇒s= " odefrcs" ; Given a '
             'given string s, find the lexicographically maximum string that '
             'can be obtained after applying a certain sequence of operations '
             'after which all characters in the string become unique. A string '
             'a of length n is lexicographically less than a string b of '
             'length m, if: there is an index i ( 1≤i≤min( n, m) ) such that '
             'the first i−1 characters of the strings a and b are the same, '
             'and the i- th character of the string a is less than i- th '
             'character of string b; or the first min( n, m) characters in the '
             'strings a and b are the same and n< m. For example, the string '
             'a= " aezakmi" is lexicographically less than the string b= " '
             'aezus" .',
  'input': 'The first line contains one integer t ( 1≤t≤104) . Then t test '
           'cases follow. Each test case is characterized by a string s, '
           'consisting of lowercase Latin letters ( 1≤| s| ≤2⋅105) . It is '
           'guaranteed that the sum of the lengths of the strings in all test '
           'cases does not exceed 2⋅105.',
  'note': ' ',
  'output': 'For each test case, output the lexicographically maximum string '
            'that can be obtained after applying a certain sequence of '
            'operations after which all characters in the string become '
            'unique.',
  'title': 'Maximize the Remaining String',
  'topics': ['brute force', 'data structures', 'dp', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1506/G'},
 {'history': 'A bitstring is a string that contains only the characters 0 and '
             '1. Koyomi Kanou is working hard towards her dream of becoming a '
             'writer. To practice, she decided to participate in the Binary '
             'Novel Writing Contest. The writing prompt for the contest '
             'consists of three bitstrings of length 2n. A valid novel for the '
             'contest is a bitstring of length at most 3n that contains at '
             'least two of the three given strings as subsequences. Koyomi has '
             'just received the three prompt strings from the contest '
             'organizers. Help her write a valid novel for the contest. A '
             'string a is a subsequence of a string b if a can be obtained '
             'from b by deletion of several ( possibly, zero) characters.',
  'input': 'The first line contains a single integer t ( 1≤t≤104) — the number '
           'of test cases. The first line of each test case contains a single '
           'integer n ( 1≤n≤105) . Each of the following three lines contains '
           'a bitstring of length 2n. It is guaranteed that these three '
           'strings are pairwise distinct. It is guaranteed that the sum of n '
           'across all test cases does not exceed 105.',
  'note': 'In the first test case, the bitstrings 00 and 01 are subsequences '
          'of the output string: 010 and 010. Note that 11 is not a '
          'subsequence of the output string, but this is not required. In the '
          'second test case all three input strings are subsequences of the '
          'output string: 011001010, 011001010 and 011001010.',
  'output': 'For each test case, print a single line containing a bitstring of '
            'length at most 3n that has at least two of the given bitstrings '
            'as subsequences. It can be proven that under the constraints of '
            'the problem, such a bitstring always exists. If there are '
            'multiple possible answers, you may output any of them.',
  'title': 'Binary Literature',
  'topics': ['constructive algorithms',
             'greedy',
             'implementation',
             'strings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1508/A'},
 {'history': 'Based on a peculiar incident at basketball practice, Akari came '
             'up with the following competitive programming problem! You are '
             'given nn points on the plane, no three of which are collinear. '
             'The ii- th point initially has a label aiai, in such a way that '
             'the labels a1, a2, . . . , ana1, a2, . . . , an form a '
             'permutation of 1, 2, . . . , n1, 2, . . . , n. You are allowed '
             'to modify the labels through the following operation: Choose two '
             'distinct integers ii and jj between 11 and nn. Swap the labels '
             'of points ii and jj, and finally Draw the segment between points '
             'ii and jj. A sequence of operations is valid if after applying '
             'all of the operations in the sequence in order, the kk- th point '
             'ends up having the label kk for all kk between 11 and nn '
             "inclusive, and the drawn segments don' t intersect each other "
             'internally. Formally, if two of the segments intersect, then '
             'they must do so at a common endpoint of both segments. In '
             'particular, all drawn segments must be distinct. Find any valid '
             'sequence of operations, or say that none exist.',
  'input': 'The first line contains an integer nn ( 3≤n≤20003≤n≤2000) — the '
           'number of points. The ii- th of the following nn lines contains '
           'three integers xixi, yiyi, aiai ( −106≤xi, yi≤106−106≤xi, yi≤106, '
           '1≤ai≤n1≤ai≤n) , representing that the ii- th point has coordinates '
           '( xi, yi) ( xi, yi) and initially has label aiai. It is guaranteed '
           'that all points are distinct, no three points are collinear, and '
           'the labels a1, a2, . . . , ana1, a2, . . . , an form a permutation '
           'of 1, 2, . . . , n1, 2, . . . , n.',
  'note': 'The following animation showcases the first sample test case. The '
          'black numbers represent the indices of the points, while the boxed '
          'orange numbers represent their labels. In the second test case, all '
          'labels are already in their correct positions, so no operations are '
          'necessary.',
  'output': 'If it is impossible to perform a valid sequence of operations, '
            'print −1−1. Otherwise, print an integer kk ( 0≤k≤n( n−1) 20≤k≤n( '
            'n−1) 2) — the number of operations to perform, followed by kk '
            'lines, each containing two integers ii and jj ( 1≤i, j≤n1≤i, j≤n, '
            'i= ̸ji= ̸j) — the indices of the points chosen for the operation. '
            'Note that you are not required to minimize or maximize the value '
            'of kk. If there are multiple possible answers, you may print any '
            'of them.',
  'title': 'Swap Pass',
  'topics': ['constructive algorithms', 'geometry', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1508/D'},
 {'history': 'Yuu Koito and Touko Nanami are newlyweds! On the wedding day, '
             'Yuu gifted Touko a directed tree with nn nodes and rooted at 11, '
             'and a labeling aa which is some DFS order of the tree. Every '
             'edge in this tree is directed away from the root. After calling '
             'dfs( 1) the following algorithm returns aa as a DFS order of a '
             'tree rooted at 11 : order : = 0a : = array of length n function '
             'dfs( u) : order : = order + 1 a[ u] : = order for all v such '
             'that there is a directed edge ( u - > v) : dfs( v) Note that '
             'there may be different DFS orders for a given tree. Touko likes '
             'the present so much she decided to play with it! On each day '
             'following the wedding day, Touko performs this procedure once: '
             'Among all directed edges u→vu→v such that au< avau< av, select '
             'the edge u′→v′u′→v′ with the lexicographically smallest pair ( '
             'au′, av′) ( au′, av′) . Swap au′au′ and av′av′. Days have passed '
             'since their wedding, and Touko has somehow forgotten which date '
             'the wedding was and what was the original labeling aa! Fearing '
             'that Yuu might get angry, Touko decided to ask you to derive '
             'these two pieces of information using the current labeling. '
             'Being her good friend, you need to find the number of days that '
             'have passed since the wedding, and the original labeling of the '
             'tree. However, there is a chance that Touko might have messed up '
             'her procedures, which result in the current labeling being '
             'impossible to obtain from some original labeling; in that case, '
             'please inform Touko as well.',
  'input': 'The first line of the input contains an integer nn ( '
           '2≤n≤3⋅1052≤n≤3⋅105) — the number of nodes on the tree. The second '
           'line contains nn integers a1a1, a2a2, . . . , anan ( 1≤ai≤n1≤ai≤n, '
           'all aiai are distinct) — the current labeling of the tree. Each of '
           'the next n−1n−1 lines contains two integers uiui and vivi ( 1≤u, '
           'v≤n1≤u, v≤n, u= ̸vu= ̸v) , describing an directed edge from uiui '
           'to vivi. The edges form a directed tree rooted at 11.',
  'note': 'The following animation showcases the first sample test case. The '
          'white label inside the node represents the index of the node ii, '
          'while the boxed orange label represents the value aiai.',
  'output': 'If the current labeling is impossible to arrive at from any DFS '
            'order, print NO. Else, on the first line, print YES. On the '
            'second line, print a single integer denoting the number of days '
            'since the wedding. On the third line, print nn numbers space- '
            'separated denoting the original labeling of the tree. If there '
            'are multiple correct outputs, print any. This means: you are '
            'allowed to output any pair ( DFS order, number of days) , such '
            'that we get the current configuration from the DFS order you '
            'provided in exactly the number of days you provided.',
  'title': 'Tree Calendar',
  'topics': ['brute force',
             'constructive algorithms',
             'data structures',
             'dfs and similar',
             'sortings',
             'trees'],
  'url': 'https://codeforces.com/problemset/problem/1508/E'},
 {'history': "Let' s define the cost of a string s as the number of index "
             'pairs i and j ( 1≤i< j< | s| ) such that si= sj and si+ 1= sj+ '
             '1. You are given two positive integers n and k. Among all '
             'strings with length n that contain only the first k characters '
             'of the Latin alphabet, find a string with minimum possible cost. '
             'If there are multiple such strings with minimum cost — find any '
             'of them.',
  'input': 'The only line contains two integers n and k ( 1≤n≤2⋅105; 1≤k≤26) .',
  'note': ' ',
  'output': 'Print the string s such that it consists of n characters, each '
            'its character is one of the k first Latin letters, and it has the '
            'minimum possible cost among all these strings. If there are '
            'multiple such strings — print any of them.',
  'title': 'Min Cost String',
  'topics': ['brute force',
             'constructive algorithms',
             'graphs',
             'greedy',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1511/D'},
 {'history': 'A chainword is a special type of crossword. As most of the '
             'crosswords do, it has cells that you put the letters in and some '
             'sort of hints to what these letters should be. The letter cells '
             'in a chainword are put in a single row. We will consider '
             'chainwords of length mm in this task. A hint to a chainword is a '
             "sequence of segments such that the segments don' t intersect "
             'with each other and cover all mm letter cells. Each segment '
             'contains a description of the word in the corresponding cells. '
             'The twist is that there are actually two hints: one sequence is '
             'the row above the letter cells and the other sequence is the row '
             'below the letter cells. When the sequences are different, they '
             'provide a way to resolve the ambiguity in the answers. You are '
             'provided with a dictionary of nn words, each word consists of '
             'lowercase Latin letters. All words are pairwise distinct. An '
             'instance of a chainword is the following triple: a string of mm '
             'lowercase Latin letters; the first hint: a sequence of segments '
             'such that the letters that correspond to each segment spell a '
             'word from the dictionary; the second hint: another sequence of '
             'segments such that the letters that correspond to each segment '
             'spell a word from the dictionary. Note that the sequences of '
             "segments don' t necessarily have to be distinct. Two instances "
             'of chainwords are considered different if they have different '
             'strings, different first hints or different second hints. Count '
             'the number of different instances of chainwords. Since the '
             'number might be pretty large, output it modulo '
             '998244353998244353.',
  'input': 'The first line contains two integers nn and mm ( 1≤n≤81≤n≤8, '
           '1≤m≤1091≤m≤109) — the number of words in the dictionary and the '
           'number of letter cells. Each of the next nn lines contains a word '
           '— a non- empty string of no more than 55 lowercase Latin letters. '
           'All words are pairwise distinct.',
  'note': 'Here are all the instances of the valid chainwords for the first '
          'example: The red lines above the letters denote the segments of the '
          'first hint, the blue lines below the letters denote the segments of '
          'the second hint. In the second example the possible strings are: " '
          'abab" , " abcd" , " cdab" and " cdcd" . All the hints are segments '
          'that cover the first two letters and the last two letters.',
  'output': 'Print a single integer — the number of different instances of '
            'chainwords of length mm for the given dictionary modulo '
            '998244353998244353.',
  'title': 'Chainword',
  'topics': ['brute force',
             'data structures',
             'dp',
             'matrices',
             'string suffix structures',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1511/F'},
 {'history': "You are given a string s consisting of the characters ' 0' , ' "
             "1' , and ' ? ' . You need to replace all the characters with ' ? "
             "' in the string s by ' 0' or ' 1' so that the string becomes a "
             "palindrome and has exactly a characters ' 0' and exactly b "
             "characters ' 1' . Note that each of the characters ' ? ' is "
             'replaced independently from the others. A string t of length n '
             'is called a palindrome if the equality t[ i] = t[ n−i+ 1] is '
             'true for all i ( 1≤i≤n) . For example, if s= " 01? ? ? ? ? 0" , '
             "a= 4 and b= 4, then you can replace the characters ' ? ' in the "
             'following ways: " 01011010" ; " 01100110" . For the given string '
             "s and the numbers a and b, replace all the characters with ' ? ' "
             "in the string s by ' 0' or ' 1' so that the string becomes a "
             "palindrome and has exactly a characters ' 0' and exactly b "
             "characters ' 1' .",
  'input': 'The first line contains a single integer t ( 1≤t≤104) . Then t '
           'test cases follow. The first line of each test case contains two '
           'integers a and b ( 0≤a, b≤2⋅105, a+ b≥1) . The second line of each '
           'test case contains the string s of length a+ b, consisting of the '
           "characters ' 0' , ' 1' , and ' ? ' . It is guaranteed that the sum "
           'of the string lengths of s over all test cases does not exceed '
           '2⋅105.',
  'note': ' ',
  'output': 'For each test case, output: " - 1" , if you can\' t replace all '
            "the characters ' ? ' in the string s by ' 0' or ' 1' so that the "
            'string becomes a palindrome and that it contains exactly a '
            "characters ' 0' and exactly b characters ' 1' ; the string that "
            'is obtained as a result of the replacement, otherwise. If there '
            'are several suitable ways to replace characters, you can output '
            'any.',
  'title': 'A-B Palindrome',
  'topics': ['constructive algorithms', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1512/C'},
 {'history': 'You are given an array aa of nn ( n≥2n≥2) positive integers and '
             'an integer pp. Consider an undirected weighted graph of nn '
             'vertices numbered from 11 to nn for which the edges between the '
             'vertices ii and jj ( i< ji< j) are added in the following '
             'manner: If gcd( ai, ai+ 1, ai+ 2, . . . , aj) = min( ai, ai+ 1, '
             'ai+ 2, . . . , aj) gcd( ai, ai+ 1, ai+ 2, . . . , aj) = min( ai, '
             'ai+ 1, ai+ 2, . . . , aj) , then there is an edge of weight min( '
             'ai, ai+ 1, ai+ 2, . . . , aj) min( ai, ai+ 1, ai+ 2, . . . , aj) '
             'between ii and jj. If i+ 1= ji+ 1= j, then there is an edge of '
             'weight pp between ii and jj. Here gcd( x, y, . . . ) gcd( x, y, '
             '. . . ) denotes the greatest common divisor ( GCD) of integers '
             'xx, yy, . . . . Note that there could be multiple edges between '
             'ii and jj if both of the above conditions are true, and if both '
             'the conditions fail for ii and jj, then there is no edge between '
             'these vertices. The goal is to find the weight of the minimum '
             'spanning tree of this graph.',
  'input': 'The first line contains a single integer tt ( 1≤t≤1041≤t≤104) — '
           'the number of test cases. The first line of each test case '
           'contains two integers nn ( 2≤n≤2⋅1052≤n≤2⋅105) and pp ( '
           '1≤p≤1091≤p≤109) — the number of nodes and the parameter pp. The '
           'second line contains nn integers a1, a2, a3, . . . , ana1, a2, a3, '
           '. . . , an ( 1≤ai≤1091≤ai≤109) . It is guaranteed that the sum of '
           'nn over all test cases does not exceed 2⋅1052⋅105.',
  'note': 'Here are the graphs for the four test cases of the example ( the '
          'edges of a possible MST of the graphs are marked pink) : For test '
          'case 1 For test case 2 For test case 3 For test case 4',
  'output': 'Output tt lines. For each test case print the weight of the '
            'corresponding graph.',
  'title': 'GCD and MST',
  'topics': ['constructive algorithms',
             'dsu',
             'graphs',
             'greedy',
             'number theory',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1513/D'},
 {'history': 'An array is called beautiful if all the elements in the array '
             'are equal. You can transform an array using the following steps '
             'any number of times: Choose two indices i and j ( 1≤i, j≤n) , '
             'and an integer x ( 1≤x≤ai) . Let i be the source index and j be '
             'the sink index. Decrease the i- th element by x, and increase '
             'the j- th element by x. The resulting values at i- th and j- th '
             'index are ai−x and aj+ x respectively. The cost of this '
             'operation is x⋅| j−i| . Now the i- th index can no longer be the '
             'sink and the j- th index can no longer be the source. The total '
             'cost of a transformation is the sum of all the costs in step 3. '
             'For example, array [ 0, 2, 3, 3] can be transformed into a '
             'beautiful array [ 2, 2, 2, 2] with total cost 1⋅| 1−3| + 1⋅| '
             '1−4| = 5. An array is called balanced, if it can be transformed '
             'into a beautiful array, and the cost of such transformation is '
             'uniquely defined. In other words, the minimum cost of '
             'transformation into a beautiful array equals the maximum cost. '
             'You are given an array a1, a2, . . . , an of length n, '
             'consisting of non- negative integers. Your task is to find the '
             'number of balanced arrays which are permutations of the given '
             'array. Two arrays are considered different, if elements at some '
             'position differ. Since the answer can be large, output it modulo '
             '109+ 7.',
  'input': 'The first line contains a single integer n ( 1≤n≤105) — the size '
           'of the array. The second line contains n integers a1, a2, . . . , '
           'an ( 0≤ai≤109) .',
  'note': 'In the first example, [ 1, 2, 3] is a valid permutation as we can '
          'consider the index with value 3 as the source and index with value '
          '1 as the sink. Thus, after conversion we get a beautiful array [ 2, '
          '2, 2] , and the total cost would be 2. We can show that this is the '
          'only transformation of this array that leads to a beautiful array. '
          'Similarly, we can check for other permutations too. In the second '
          'example, [ 0, 0, 4, 4] and [ 4, 4, 0, 0] are balanced permutations. '
          'In the third example, all permutations are balanced.',
  'output': 'Output a single integer — the number of balanced permutations '
            'modulo 109+ 7.',
  'title': 'Cost Equilibrium',
  'topics': ['combinatorics', 'constructive algorithms', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1513/E'},
 {'history': 'You are given 2 arrays a and b, both of size n. You can swap two '
             'elements in b at most once ( or leave it as it is) , and you are '
             'required to minimize the value ∑i| ai−bi| . Find the minimum '
             'possible value of this sum.',
  'input': 'The first line contains a single integer n ( 1≤n≤2⋅105) . The '
           'second line contains n integers a1, a2, . . . , an ( 1≤ai≤109) . '
           'The third line contains n integers b1, b2, . . . , bn ( 1≤bi≤109) '
           '.',
  'note': 'In the first example, we can swap the first and fifth element in '
          'array b, so that it becomes [ 5, 2, 3, 4, 1] . Therefore, the '
          'minimum possible value of this sum would be | 5−5| + | 4−2| + | '
          '3−3| + | 2−4| + | 1−1| = 4. In the second example, we can swap the '
          'first and second elements. So, our answer would be 2.',
  'output': 'Output the minimum value of ∑i| ai−bi| .',
  'title': 'Swapping Problem',
  'topics': ['brute force',
             'constructive algorithms',
             'data structures',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1513/F'},
 {'history': 'Baby Ehab has a piece of Cut and Stick with an array a of length '
             'n written on it. He plans to grab a pair of scissors and do the '
             'following to it: pick a range ( l, r) and cut out every element '
             'al, al+ 1, . . . , ar in this range; stick some of the elements '
             'together in the same order they were in the array; end up with '
             'multiple pieces, where every piece contains some of the elements '
             'and every element belongs to some piece. More formally, he '
             'partitions the sequence al, al+ 1, . . . , ar into subsequences. '
             'He thinks a partitioning is beautiful if for every piece ( '
             'subsequence) it holds that, if it has length x, then no value '
             "occurs strictly more than ⌈x2⌉ times in it. He didn' t pick a "
             "range yet, so he' s wondering: for q ranges ( l, r) , what is "
             'the minimum number of pieces he needs to partition the elements '
             'al, al+ 1, . . . , ar into so that the partitioning is '
             'beautiful. A sequence b is a subsequence of an array a if b can '
             'be obtained from a by deleting some ( possibly zero) elements. '
             'Note that it does not have to be contiguous.',
  'input': 'The first line contains two integers n and q ( 1≤n, q≤3⋅105) — the '
           'length of the array a and the number of queries. The second line '
           'contains n integers a1, a2, . . . , an ( 1≤ai≤n) — the elements of '
           'the array a. Each of the next q lines contains two integers l and '
           'r ( 1≤l≤r≤n) — the range of this query.',
  'note': 'In the first query, you can just put the whole array in one '
          'subsequence, since its length is 6, and no value occurs more than 3 '
          'times in it. In the second query, the elements of the query range '
          "are [ 3, 2, 3, 3] . You can' t put them all in one subsequence, "
          'since its length is 4, and 3 occurs more than 2 times. However, you '
          'can partition it into two subsequences: [ 3] and [ 2, 3, 3] .',
  'output': 'For each query, print the minimum number of subsequences you need '
            'to partition this range into so that the partitioning is '
            'beautiful. We can prove such partitioning always exists.',
  'title': 'Cut and Stick',
  'topics': ['binary search',
             'data structures',
             'greedy',
             'implementation',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1514/D'},
 {'history': 'This is an interactive problem. Baby Ehab loves crawling around '
             'his apartment. It has n rooms numbered from 0 to n−1. For every '
             "pair of rooms, a and b, there' s either a direct passage from "
             'room a to room b, or from room b to room a, but never both. Baby '
             'Ehab wants to go play with Baby Badawy. He wants to know if he '
             "could get to him. However, he doesn' t know anything about his "
             'apartment except the number of rooms. He can ask the baby sitter '
             'two types of questions: is the passage between room a and room b '
             'directed from a to b or the other way around? does room x have a '
             'passage towards any of the rooms s1, s2, . . . , sk? He can ask '
             'at most 9n queries of the first type and at most 2n queries of '
             'the second type. After asking some questions, he wants to know '
             "for every pair of rooms a and b whether there' s a path from a "
             'to b or not. A path from a to b is a sequence of passages that '
             'starts from room a and ends at room b. InteractionTo ask a '
             'question of the first type, use the format: 1 a b ( 0≤a, b≤n−1, '
             'a= ̸b) . we will answer with 1 if the passage is from a to b, '
             'and 0 if it is from b to a. you can ask at most 9n questions of '
             'this type in each test case. To ask a question of the second '
             'type, use the format: 2 x k s1 s2 . . . sk ( 0≤x, si≤n−1, 0≤k< '
             'n, x= ̸si, elements of s are pairwise distinct) . we will answer '
             "with 1 if there' s a passage from x to any of the rooms in s, "
             'and 0 otherwise. you can ask at most 2n questions of this type '
             'in each test case. If we answer with −1 instead of a valid '
             'answer, that means you exceeded the number of queries or made an '
             'invalid query. Exit immediately after receiving −1 and you will '
             'see Wrong answer verdict. Otherwise, you can get an arbitrary '
             'verdict because your solution will continue to read from a '
             'closed stream. After printing a query, do not forget to output '
             'end of line and flush the output. Otherwise, you will get '
             'Idleness limit exceeded. To do this, use: fflush( stdout) or '
             'cout. flush( ) in C+ + ; System. out. flush( ) in Java; flush( '
             'output) in Pascal; stdout. flush( ) in Python; see the '
             'documentation for other languages. Hacks: The first line should '
             'contain an integer t — the number of test cases. The first line '
             'of each test case should contain an integer n ( 4≤n≤100) — the '
             'number of rooms. Each of the next n lines should contain a '
             'binary string of length n. The j- th character of the i- th '
             "string should be 1 if there' s a passage from room i to room j, "
             '0 otherwise. The i- th character of the i- th string should be '
             '0.',
  'input': 'The first line contains an integer t ( 1≤t≤30) — the number of '
           'test cases you need to solve. Then each test case starts with an '
           'integer n ( 4≤n≤100) — the number of rooms. The sum of n across '
           "the test cases doesn' t exceed 500.",
  'note': "In the given example: The first query asks whether there' s a "
          'passage from room 3 to any of the other rooms. The second query '
          'asks about the direction of the passage between rooms 0 and 1. '
          'After a couple other queries, we concluded that you can go from any '
          "room to any other room except if you start at room 3, and you can' "
          't get out of this room, so we printed the matrix: '
          '1111111111110001The interactor answered with 1, telling us the '
          'answer is correct.',
  'output': 'To print the answer for a test case, print a line containing " 3" '
            ', followed by n lines, each containing a binary string of length '
            "n. The j- th character of the i- th string should be 1 if there' "
            "s a path from room i to room j, and 0 if there isn' t. The i- th "
            'character of the i- th string should be 1 for each valid i. After '
            'printing the answer, we will respond with a single integer. If '
            "it' s 1, you printed a correct answer and should keep solving the "
            "test cases ( or exit if it is the last one) . If it' s −1, you "
            'printed a wrong answer and should terminate to get Wrong answer '
            'verdict. Otherwise, you can get an arbitrary verdict because your '
            'solution will continue to read from a closed stream.',
  'title': "Baby Ehab's Hyper Apartment",
  'topics': ['binary search',
             'graphs',
             'interactive',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1514/E'},
 {'history': 'To satisfy his love of matching socks, Phoenix has brought his n '
             'socks ( n is even) to the sock store. Each of his socks has a '
             'color ci and is either a left sock or right sock. Phoenix can '
             'pay one dollar to the sock store to either: recolor a sock to '
             'any color c′ ( 1≤c′≤n) turn a left sock into a right sock turn a '
             'right sock into a left sock The sock store may perform each of '
             'these changes any number of times. Note that the color of a left '
             "sock doesn' t change when it turns into a right sock, and vice "
             'versa. A matching pair of socks is a left and right sock with '
             'the same color. What is the minimum cost for Phoenix to make n/ '
             '2 matching pairs? Each sock must be included in exactly one '
             'matching pair.',
  'input': 'The input consists of multiple test cases. The first line contains '
           'an integer t ( 1≤t≤1000) — the number of test cases. The first '
           'line of each test case contains three integers n, l, and r ( '
           '2≤n≤2⋅105; n is even; 0≤l, r≤n; l+ r= n) — the total number of '
           'socks, and the number of left and right socks, respectively. The '
           'next line contains n integers ci ( 1≤ci≤n) — the colors of the '
           'socks. The first l socks are left socks, while the next r socks '
           'are right socks. It is guaranteed that the sum of n across all the '
           'test cases will not exceed 2⋅105.',
  'note': 'In the first test case, Phoenix can pay 2 dollars to: recolor sock '
          '1 to color 2 recolor sock 3 to color 2 There are now 3 matching '
          'pairs. For example, pairs ( 1, 4) , ( 2, 5) , and ( 3, 6) are '
          'matching. In the second test case, Phoenix can pay 3 dollars to: '
          'turn sock 6 from a right sock to a left sock recolor sock 3 to '
          'color 1 recolor sock 4 to color 1 There are now 3 matching pairs. '
          'For example, pairs ( 1, 3) , ( 2, 4) , and ( 5, 6) are matching.',
  'output': 'For each test case, print one integer — the minimum cost for '
            'Phoenix to make n/ 2 matching pairs. Each sock must be included '
            'in exactly one matching pair.',
  'title': 'Phoenix and Socks',
  'topics': ['greedy', 'sortings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1515/D'},
 {'history': 'Phoenix loves playing with bits — specifically, by using the '
             'bitwise operations AND, OR, and XOR. He has n integers a1, a2, . '
             '. . , an, and will perform q of the following queries: replace '
             'all numbers ai where l≤ai≤r with ai AND x; replace all numbers '
             'ai where l≤ai≤r with ai OR x; replace all numbers ai where '
             'l≤ai≤r with ai XOR x; output how many distinct integers ai where '
             'l≤ai≤r. For each query, Phoenix is given l, r, and x. Note that '
             'he is considering the values of the numbers, not their indices.',
  'input': 'The first line contains two integers n and q ( 1≤n≤2⋅105; 1≤q≤105) '
           '— the number of integers and the number of queries, respectively. '
           'The second line contains n integers a1, a2, . . . , an ( 0≤ai< '
           '220) — the integers that Phoenix starts with. The next q lines '
           'contain the queries. For each query, the first integer of each '
           'line is t ( 1≤t≤4) — the type of query. If t∈1, 2, 3, then three '
           'integers li, ri, and xi will follow ( 0≤li, ri, xi< 220; li≤ri) . '
           'Otherwise, if t= 4, two integers li and ri will follow ( 0≤li≤ri< '
           '220) . It is guaranteed that there is at least one query where t= '
           '4.',
  'note': 'In the first example: For the first query, 2 is replaced by 2 AND '
          '2= 2 and 3 is replaced with 3 AND 2= 2. The set of numbers is 1, 2, '
          '4, 5. For the second query, there are 3 distinct numbers between 2 '
          'and 5: 2, 4, and 5. For the third query, 2 is replaced by 2 XOR 3= '
          '1, 4 is replaced by 4 XOR 3= 7, and 5 is replaced by 5 XOR 3= 6. '
          'The set of numbers is 1, 6, 7. For the fourth query, there are 2 '
          'distinct numbers between 1 and 6: 1 and 6. For the fifth query, 1 '
          'is replaced by 1 OR 8= 9. The set of numbers is 6, 7, 9. For the '
          'sixth query, there is one distinct number between 8 and 10: 9.',
  'output': 'Print the answer for each query where t= 4.',
  'title': 'Phoenix and Bits',
  'topics': ['bitmasks', 'brute force', 'data structures', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1515/H'},
 {'history': 'Phoenix wonders what it is like to rob diamonds from a jewelry '
             'store! There are n types of diamonds. The i- th type has weight '
             'wi and value vi. The store initially has ai diamonds of the i- '
             'th type. Each day, for q days, one of the following will happen: '
             'A new shipment of ki diamonds of type di arrive. The store sells '
             'ki diamonds of type di. Phoenix wonders what will happen if he '
             'robs the store using a bag that can fit diamonds with total '
             'weight not exceeding ci. If he greedily takes diamonds of the '
             'largest value that fit, how much value would be taken? If there '
             'are multiple diamonds with the largest value, he will take the '
             'one with minimum weight. If, of the diamonds with the largest '
             'value, there are multiple with the same minimum weight, he will '
             'take any of them. Of course, since Phoenix is a law- abiding '
             'citizen, this is all a thought experiment and he never actually '
             'robs any diamonds from the store. This means that queries of '
             'type 3 do not affect the diamonds in the store.',
  'input': 'The first line contains two integers n and q ( 1≤n≤2⋅105; 1≤q≤105) '
           '— the number of types of diamonds and number of days, '
           'respectively. The next n lines describe each type of diamond. The '
           'i- th line will contain three integers ai, wi, and vi ( 0≤ai≤105; '
           '1≤wi, vi≤105) — the initial number of diamonds of the i- th type, '
           'the weight of diamonds of the i- th type, and the value of '
           'diamonds of the i- th type, respectively. The next q lines contain '
           'the queries. For each query, the first integer of each line is t ( '
           '1≤t≤3) — the type of query. If t= 1, then two integers ki, di '
           'follow ( 1≤ki≤105; 1≤di≤n) . This means that a new shipment of ki '
           'diamonds arrived, each of type di. If t= 2, then two integers ki, '
           'di follow ( 1≤ki≤105; 1≤di≤n) . This means that the store has sold '
           'ki diamonds, each of type di. It is guaranteed that the store had '
           'the diamonds before they sold them. If t= 3, an integer ci will '
           "follow ( 1≤ci≤1018) — the weight capacity of Phoenix' s bag. It is "
           'guaranteed that there is at least one query where t= 3.',
  'note': 'For the first query where t= 3, Phoenix can fit 2 diamonds of type '
          '1, with total weight 6 and value 8. For the second query where t= '
          '3, Phoenix will first fit in 3 diamonds of type 3, then one diamond '
          'of type 1 for a total weight of 9 and a value of 16. Note that '
          'diamonds of type 3 are prioritized over type 1 because type 3 has '
          'equal value but less weight. For the final query where t= 3, '
          'Phoenix can fit every diamond for a total value of 13.',
  'output': 'Print the answer for each query of the third type ( t= 3) .',
  'title': 'Phoenix and Diamonds',
  'topics': ['binary search', 'data structures', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1515/I'},
 {'history': 'The 2050 volunteers are organizing the " Run! Chase the Rising '
             'Sun" activity. Starting on Apr 25 at 7: 30 am, runners will '
             'complete the 6km trail around the Yunqi town. There are n+ 1 '
             'checkpoints on the trail. They are numbered by 0, 1, . . . , n. '
             'A runner must start at checkpoint 0 and finish at checkpoint n. '
             'No checkpoint is skippable — he must run from checkpoint 0 to '
             'checkpoint 1, then from checkpoint 1 to checkpoint 2 and so on. '
             'Look at the picture in notes section for clarification. Between '
             'any two adjacent checkpoints, there are m different paths to '
             'choose. For any 1≤i≤n, to run from checkpoint i−1 to checkpoint '
             'i, a runner can choose exactly one from the m possible paths. '
             'The length of the j- th path between checkpoint i−1 and i is bi, '
             'j for any 1≤j≤m and 1≤i≤n. To test the trail, we have m runners. '
             'Each runner must run from the checkpoint 0 to the checkpoint n '
             'once, visiting all the checkpoints. Every path between every '
             'pair of adjacent checkpoints needs to be ran by exactly one '
             'runner. If a runner chooses the path of length li between '
             'checkpoint i−1 and i ( 1≤i≤n) , his tiredness is nmini= 1li, i. '
             'e. the minimum length of the paths he takes. Please arrange the '
             'paths of the m runners to minimize the sum of tiredness of them.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤10000) . Description of the test '
           'cases follows. The first line of each test case contains two '
           'integers n and m ( 1≤n, m≤100) . The i- th of the next n lines '
           'contains m integers bi, 1, bi, 2, . . . , bi, m ( 1≤bi, j≤109) . '
           'It is guaranteed that the sum of n⋅m over all test cases does not '
           'exceed 104.',
  'note': 'In the first case, the sum of tiredness is min( 2, 5) + min( 3, 3) '
          '+ min( 4, 1) = 6. In the second case, the sum of tiredness is min( '
          '2, 4, 3) + min( 3, 1, 5) = 3.',
  'output': 'For each test case, output n lines. The j- th number in the i- th '
            'line should contain the length of the path that runner j chooses '
            'to run from checkpoint i−1 to checkpoint i. There should be '
            'exactly m integers in the i- th line and these integers should '
            'form a permuatation of bi, 1, . . . , bi, m for all 1≤i≤n. If '
            'there are multiple answers, print any.',
  'title': 'Morning Jogging',
  'topics': ['constructive algorithms', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1517/B'},
 {'history': 'Polycarp is an organizer of a Berland ICPC regional event. There '
             'are n universities in Berland numbered from 1 to n. Polycarp '
             'knows all competitive programmers in the region. There are n '
             'students: the i- th student is enrolled at a university ui and '
             'has a programming skill si. Polycarp has to decide on the rules '
             'now. In particular, the number of members in the team. Polycarp '
             'knows that if he chooses the size of the team to be some integer '
             'k, each university will send their k strongest ( with the '
             'highest programming skill s) students in the first team, the '
             'next k strongest students in the second team and so on. If there '
             "are fewer than k students left, then the team can' t be formed. "
             'Note that there might be universities that send zero teams. The '
             'strength of the region is the total skill of the members of all '
             'present teams. If there are no teams present, then the strength '
             'is 0. Help Polycarp to find the strength of the region for each '
             'choice of k from 1 to n.',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of testcases. The first line of each testcase contains a '
           'single integer n ( 1≤n≤2⋅105) — the number of universities and the '
           'number of students. The second line of each testcase contains n '
           'integers u1, u2, . . . , un ( 1≤ui≤n) — the university the i- th '
           'student is enrolled at. The third line of each testcase contains n '
           'integers s1, s2, . . . , sn ( 1≤si≤109) — the programming skill of '
           "the i- th student. The sum of n over all testcases doesn' t exceed "
           '2⋅105.',
  'note': 'In the first testcase the teams from each university for each k '
          'are: k= 1: university 1: [ 6] , [ 5] , [ 5] , [ 3] ; university 2: '
          '[ 8] , [ 1] , [ 1] ; k= 2: university 1: [ 6, 5] , [ 5, 3] ; '
          'university 2: [ 8, 1] ; k= 3: university 1: [ 6, 5, 5] ; university '
          '2: [ 8, 1, 1] ; k= 4: university 1: [ 6, 5, 5, 3] ;',
  'output': 'For each testcase print n integers: the strength of the region — '
            'the total skill of the members of the present teams — for each '
            'choice of team size k.',
  'title': 'Berland Regional',
  'topics': ['brute force',
             'data structures',
             'greedy',
             'number theory',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1519/C'},
 {'history': 'There are nn points on an infinite plane. The ii- th point has '
             'coordinates ( xi, yi) ( xi, yi) such that xi> 0xi> 0 and yi> '
             '0yi> 0. The coordinates are not necessarily integer. In one move '
             'you perform the following operations: choose two points aa and '
             'bb ( a= ̸ba= ̸b) ; move point aa from ( xa, ya) ( xa, ya) to '
             'either ( xa+ 1, ya) ( xa+ 1, ya) or ( xa, ya+ 1) ( xa, ya+ 1) ; '
             'move point bb from ( xb, yb) ( xb, yb) to either ( xb+ 1, yb) ( '
             'xb+ 1, yb) or ( xb, yb+ 1) ( xb, yb+ 1) ; remove points aa and '
             'bb. However, the move can only be performed if there exists a '
             'line that passes through the new coordinates of aa, new '
             "coordinates of bb and ( 0, 0) ( 0, 0) . Otherwise, the move can' "
             't be performed and the points stay at their original coordinates '
             '( xa, ya) ( xa, ya) and ( xb, yb) ( xb, yb) , respectively. The '
             'numeration of points does not change after some points are '
             "removed. Once the points are removed, they can' t be chosen in "
             'any later moves. Note that you have to move both points during '
             "the move, you can' t leave them at their original coordinates. "
             'What is the maximum number of moves you can perform? What are '
             'these moves? If there are multiple answers, you can print any of '
             'them.',
  'input': 'The first line contains a single integer nn ( 1≤n≤2⋅1051≤n≤2⋅105) '
           '— the number of points. The ii- th of the next nn lines contains '
           'four integers ai, bi, ci, diai, bi, ci, di ( 1≤ai, bi, ci, '
           'di≤1091≤ai, bi, ci, di≤109) . The coordinates of the ii- th point '
           'are xi= aibixi= aibi and yi= cidiyi= cidi.',
  'note': 'Here are the points and the moves for the ones that get chosen for '
          'the moves from the first example:',
  'output': 'In the first line print a single integer cc — the maximum number '
            'of moves you can perform. Each of the next cc lines should '
            'contain a description of a move: two integers aa and bb ( 1≤a, '
            'b≤n1≤a, b≤n, a= ̸ba= ̸b) — the points that are removed during the '
            'current move. There should be a way to move points aa and bb '
            "according to the statement so that there' s a line that passes "
            'through the new coordinates of aa, the new coordinates of bb and '
            '( 0, 0) ( 0, 0) . No removed point can be chosen in a later move. '
            'If there are multiple answers, you can print any of them. You can '
            'print the moves and the points in the move in the arbitrary '
            'order.',
  'title': 'Off by One',
  'topics': ['constructive algorithms',
             'dfs and similar',
             'geometry',
             'graphs',
             'sortings',
             'trees'],
  'url': 'https://codeforces.com/problemset/problem/1519/E'},
 {'history': 'There are nn robots driving along an OX axis. There are also two '
             'walls: one is at coordinate 00 and one is at coordinate mm. The '
             'ii- th robot starts at an integer coordinate xi ( 0< xi< m) xi ( '
             '0< xi< m) and moves either left ( towards the 00) or right with '
             'the speed of 11 unit per second. No two robots start at the same '
             'coordinate. Whenever a robot reaches a wall, it turns around '
             'instantly and continues his ride in the opposite direction with '
             'the same speed. Whenever several robots meet at the same integer '
             'coordinate, they collide and explode into dust. Once a robot has '
             "exploded, it doesn' t collide with any other robot. Note that if "
             'several robots meet at a non- integer coordinate, nothing '
             'happens. For each robot find out if it ever explodes and print '
             'the time of explosion if it happens and −1−1 otherwise.',
  'input': 'The first line contains a single integer tt ( 1≤t≤10001≤t≤1000) — '
           'the number of testcases. Then the descriptions of tt testcases '
           'follow. The first line of each testcase contains two integers nn '
           'and mm ( 1≤n≤3⋅1051≤n≤3⋅105; 2≤m≤1082≤m≤108) — the number of '
           'robots and the coordinate of the right wall. The second line of '
           'each testcase contains nn integers x1, x2, . . . , xnx1, x2, . . . '
           ', xn ( 0< xi< m0< xi< m) — the starting coordinates of the robots. '
           'The third line of each testcase contains nn space- separated '
           "characters ' L' or ' R' — the starting directions of the robots ( "
           "' L' stands for left and ' R' stands for right) . All coordinates "
           'xixi in the testcase are distinct. The sum of nn over all '
           "testcases doesn' t exceed 3⋅1053⋅105.",
  'note': 'Here is the picture for the seconds 0, 1, 20, 1, 2 and 33 of the '
          "first testcase: Notice that robots 22 and 33 don' t collide because "
          'they meet at the same point 2. 52. 5, which is not integer. After '
          "second 33 robot 66 just drive infinitely because there' s no robot "
          'to collide with.',
  'output': 'For each testcase print nn integers — for the ii- th robot output '
            'the time it explodes at if it does and −1−1 otherwise.',
  'title': 'Robot Collisions',
  'topics': ['data structures', 'greedy', 'implementation', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1525/C'},
 {'history': 'You are given an array a of 2n distinct integers. You want to '
             'arrange the elements of the array in a circle such that no '
             'element is equal to the the arithmetic mean of its 2 neighbours. '
             'More formally, find an array b, such that: b is a permutation of '
             'a. For every i from 1 to 2n, bi= ̸bi−1+ bi+ 12, where b0= b2n '
             'and b2n+ 1= b1. It can be proved that under the constraints of '
             'this problem, such array b always exists.',
  'input': 'The first line of input contains a single integer t ( 1≤t≤1000) — '
           'the number of testcases. The description of testcases follows. The '
           'first line of each testcase contains a single integer n ( 1≤n≤25) '
           '. The second line of each testcase contains 2n integers a1, a2, . '
           '. . , a2n ( 1≤ai≤109) — elements of the array. Note that there is '
           'no limit to the sum of n over all testcases.',
  'note': "In the first testcase, array [ 3, 1, 4, 2, 5, 6] works, as it' s a "
          'permutation of [ 1, 2, 3, 4, 5, 6] , and 3+ 42= ̸1, 1+ 22= ̸4, 4+ '
          '52= ̸2, 2+ 62= ̸5, 5+ 32= ̸6, 6+ 12= ̸3.',
  'output': 'For each testcase, you should output 2n integers, b1, b2, . . . '
            'b2n, for which the conditions from the statement are satisfied.',
  'title': 'Mean Inequality',
  'topics': ['constructive algorithms', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1526/A'},
 {'history': 'After rejecting 10100 data structure problems, Errorgorn is very '
             "angry at Anton and decided to kill him. Anton' s DNA can be "
             'represented as a string a which only contains the characters " '
             'ANTON" ( there are only 4 distinct characters) . Errorgorn can '
             "change Anton' s DNA into string b which must be a permutation of "
             "a. However, Anton' s body can defend against this attack. In 1 "
             'second, his body can swap 2 adjacent characters of his DNA to '
             "transform it back to a. Anton' s body is smart and will use the "
             'minimum number of moves. To maximize the chance of Anton dying, '
             "Errorgorn wants to change Anton' s DNA the string that maximizes "
             "the time for Anton' s body to revert his DNA. But since "
             'Errorgorn is busy making more data structure problems, he needs '
             'your help to find the best string B. Can you help him?',
  'input': 'The first line of input contains a single integer t ( 1≤t≤100000) '
           '— the number of testcases. The first and only line of each '
           'testcase contains 1 string a ( 1≤| a| ≤100000) . a consists of '
           'only the characters " A" , " N" , " O" and " T" . It is guaranteed '
           'that the sum of | a| over all testcases does not exceed 100000.',
  'note': "For the first testcase, it takes 7 seconds for Anton' s body to "
          'transform NNOTA to ANTON: NNOTA → NNOAT → NNAOT → NANOT → NANTO → '
          'ANNTO → ANTNO → ANTON. Note that you cannot output strings such as '
          'AANTON, ANTONTRYGUB, AAAAA and anton as it is not a permutation of '
          "ANTON. For the second testcase, it takes 2 seconds for Anton' s "
          'body to transform AANN to NAAN. Note that other strings such as '
          'NNAA and ANNA will also be accepted.',
  'output': 'For each testcase, print a single string, b. If there are '
            'multiple answers, you can output any one of them. b must be a '
            'permutation of the string a.',
  'title': 'Kill Anton',
  'topics': ['brute force',
             'constructive algorithms',
             'data structures',
             'math',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1526/D'},
 {'history': 'A sequence ( b1, b2, . . . , bk) is called strange, if the '
             'absolute difference between any pair of its elements is greater '
             'than or equal to the maximum element in the sequence. Formally '
             "speaking, it' s strange if for every pair ( i, j) with 1≤i< j≤k, "
             'we have | ai−aj| ≥MAX, where MAX is the largest element of the '
             'sequence. In particular, any sequence of length at most 1 is '
             'strange. For example, the sequences ( −2021, −1, −1, −1) and ( '
             '−1, 0, 1) are strange, but ( 3, 0, 1) is not, because | 0−1| < '
             '3. Sifid has an array a of n integers. Sifid likes everything '
             'big, so among all the strange subsequences of a, he wants to '
             'find the length of the longest one. Can you help him? A sequence '
             'c is a subsequence of an array d if c can be obtained from d by '
             'deletion of several ( possibly, zero or all) elements.',
  'input': 'The first line contains an integer t ( 1≤t≤104) — the number of '
           'test cases. The description of the test cases follows. The first '
           'line of each test case contains an integer n ( 1≤n≤105) — the '
           'length of the array a. The second line of each test case contains '
           'n integers a1, a2, . . . , an ( −109≤ai≤109) — the elements of the '
           'array a. It is guaranteed that the sum of n over all test cases '
           "doesn' t exceed 105.",
  'note': 'In the first test case, one of the longest strange subsequences is '
          '( a1, a2, a3, a4) In the second test case, one of the longest '
          'strange subsequences is ( a1, a3, a4, a5, a7) . In the third test '
          'case, one of the longest strange subsequences is ( a1, a3, a4, a5) '
          '. In the fourth test case, one of the longest strange subsequences '
          'is ( a2) . In the fifth test case, one of the longest strange '
          'subsequences is ( a1, a2, a4) .',
  'output': 'For each test case output a single integer — the length of the '
            'longest strange subsequence of a.',
  'title': 'Sifid and Strange Subsequences',
  'topics': ['greedy', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1529/B'},
 {'history': 'You and your friend Ilya are participating in an individual '
             'programming contest consisting of multiple stages. A contestant '
             'can get between 0 and 100 points, inclusive, for each stage, '
             'independently of other contestants. Points received by '
             'contestants in different stages are used for forming overall '
             'contest results. Suppose that k stages of the contest are '
             'completed. For each contestant, k−⌊k4⌋ stages with the highest '
             'scores are selected, and these scores are added up. This sum is '
             'the overall result of the contestant. ( Here ⌊t⌋ denotes '
             'rounding t down. ) For example, suppose 9 stages are completed, '
             'and your scores are 50, 30, 50, 50, 100, 10, 30, 100, 50. First, '
             '7 stages with the highest scores are chosen — for example, all '
             'stages except for the 2- nd and the 6- th can be chosen. Then '
             'your overall result is equal to 50+ 50+ 50+ 100+ 30+ 100+ 50= '
             '430. As of now, n stages are completed, and you know the points '
             'you and Ilya got for these stages. However, it is unknown how '
             'many more stages will be held. You wonder what the smallest '
             'number of additional stages is, after which your result might '
             "become greater than or equal to Ilya' s result, at least in "
             'theory. Find this number!',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤1000) . Description of the test '
           'cases follows. The first line of each test case contains a single '
           'integer n ( 1≤n≤105) — the number of completed stages. The second '
           'line contains n integers a1, a2, . . . , an ( 0≤ai≤100) — your '
           'points for the completed stages. The third line contains n '
           "integers b1, b2, . . . , bn ( 0≤bi≤100) — Ilya' s points for the "
           'completed stages. It is guaranteed that the sum of n over all test '
           'cases does not exceed 105.',
  'note': 'In the first test case, you have scored 100 points for the first '
          'stage, while Ilya has scored 0. Thus, your overall result ( 100) is '
          "already not less than Ilya' s result ( 0) . In the second test "
          'case, you have scored 0 points for the first stage, while Ilya has '
          'scored 100. A single stage with an opposite result is enough for '
          "both your and Ilya' s overall scores to become equal to 100. In the "
          'third test case, your overall result is 30+ 40+ 50= 120, while '
          "Ilya' s result is 100+ 100+ 100= 300. After three additional stages "
          "your result might become equal to 420, while Ilya' s result might "
          'become equal to 400. In the fourth test case, your overall result '
          "after four additional stages might become equal to 470, while Ilya' "
          's result might become equal to 400. Three stages are not enough.',
  'output': 'For each test case print a single integer — the smallest number '
            'of additional stages required for your result to be able to '
            "become greater than or equal to Ilya' s result. If your result is "
            "already not less than Ilya' s result, print 0.",
  'title': 'Pursuit',
  'topics': ['binary search', 'brute force', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1530/C'},
 {'history': 'Prefix function of string t= t1t2. . . tn and position i in it '
             'is defined as the length k of the longest proper ( not equal to '
             'the whole substring) prefix of substring t1t2. . . ti which is '
             'also a suffix of the same substring. For example, for string t= '
             'abacaba the values of the prefix function in positions 1, 2, . . '
             '. , 7 are equal to [ 0, 0, 1, 0, 1, 2, 3] . Let f( t) be equal '
             'to the maximum value of the prefix function of string t over all '
             'its positions. For example, f( abacaba) = 3. You are given a '
             'string s. Reorder its characters arbitrarily to get a string t ( '
             'the number of occurrences of any character in strings s and t '
             'must be equal) . The value of f( t) must be minimized. Out of '
             'all options to minimize f( t) , choose the one where string t is '
             'the lexicographically smallest.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤105) . Description of the test '
           'cases follows. The only line of each test case contains string s ( '
           '1≤| s| ≤105) consisting of lowercase English letters. It is '
           'guaranteed that the sum of lengths of s over all test cases does '
           'not exceed 105.',
  'note': 'A string a is lexicographically smaller than a string b if and only '
          'if one of the following holds: a is a prefix of b, but a= ̸b; in '
          'the first position where a and b differ, the string a has a letter '
          'that appears earlier in the alphabet than the corresponding letter '
          'in b. In the first test case, f( t) = 0 and the values of prefix '
          'function are [ 0, 0, 0, 0, 0] for any permutation of letters. '
          'String ckpuv is the lexicographically smallest permutation of '
          'letters of string vkcup. In the second test case, f( t) = 1 and the '
          'values of prefix function are [ 0, 1, 0, 1, 0, 1, 0] . In the third '
          'test case, f( t) = 5 and the values of prefix function are [ 0, 1, '
          '2, 3, 4, 5] .',
  'output': 'For each test case print a single string t. The multisets of '
            'letters in strings s and t must be equal. The value of f( t) , '
            'the maximum of prefix functions in string t, must be as small as '
            'possible. String t must be the lexicographically smallest string '
            'out of all strings satisfying the previous conditions.',
  'title': 'Minimax',
  'topics': ['constructive algorithms', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1530/E'},
 {'history': 'There are n students in a university. The number of students is '
             'even. The i- th student has programming skill equal to ai. The '
             'coach wants to form n2 teams. Each team should consist of '
             'exactly two students, and each student should belong to exactly '
             'one team. Two students can form a team only if their skills are '
             'equal ( otherwise they cannot understand each other and cannot '
             'form a team) . Students can solve problems to increase their '
             'skill. One solved problem increases the skill by one. The coach '
             'wants to know the minimum total number of problems students '
             'should solve to form exactly n2 teams ( i. e. each pair of '
             'students should form a team) . Your task is to find this number.',
  'input': 'The first line of the input contains one integer n ( 2≤n≤100) — '
           'the number of students. It is guaranteed that n is even. The '
           'second line of the input contains n integers a1, a2, . . . , an ( '
           '1≤ai≤100) , where ai is the skill of the i- th student.',
  'note': 'In the first example the optimal teams will be: ( 3, 4) , ( 1, 6) '
          'and ( 2, 5) , where numbers in brackets are indices of students. '
          'Then, to form the first team the third student should solve 1 '
          'problem, to form the second team nobody needs to solve problems and '
          'to form the third team the second student should solve 4 problems '
          'so the answer is 1+ 4= 5. In the second example the first student '
          'should solve 99 problems to form a team with the second one.',
  'output': 'Print one number — the minimum total number of problems students '
            'should solve to form exactly n2 teams.',
  'title': 'Teams Forming',
  'topics': ['*special', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1532/D'},
 {'history': 'Ivan wants to play a game with you. He picked some string s of '
             "length n consisting only of lowercase Latin letters. You don' t "
             'know this string. Ivan has informed you about all its improper '
             'prefixes and suffixes ( i. e. prefixes and suffixes of lengths '
             "from 1 to n−1) , but he didn' t tell you which strings are "
             'prefixes and which are suffixes. Ivan wants you to guess which '
             'of the given 2n−2 strings are prefixes of the given string and '
             'which are suffixes. It may be impossible to guess the string '
             'Ivan picked ( since multiple strings may give the same set of '
             'suffixes and prefixes) , but Ivan will accept your answer if '
             'there is at least one string that is consistent with it. Let the '
             'game begin!',
  'input': 'The first line of the input contains one integer number n ( '
           '2≤n≤100) — the length of the guessed string s. The next 2n−2 lines '
           'are contain prefixes and suffixes, one per line. Each of them is '
           'the string of length from 1 to n−1 consisting only of lowercase '
           'Latin letters. They can be given in arbitrary order. It is '
           'guaranteed that there are exactly 2 strings of each length from 1 '
           'to n−1. It is also guaranteed that these strings are prefixes and '
           'suffixes of some existing string of length n.',
  'note': 'The only string which Ivan can guess in the first example is " '
          'ababa" . The only string which Ivan can guess in the second example '
          'is " aaa" . Answers " SPSP" , " SSPP" and " PSPS" are also '
          'acceptable. In the third example Ivan can guess the string " ac" or '
          'the string " ca" . The answer " SP" is also acceptable.',
  'output': 'Print one string of length 2n−2 — the string consisting only of '
            "characters ' P' and ' S' . The number of characters ' P' should "
            "be equal to the number of characters ' S' . The i- th character "
            "of this string should be ' P' if the i- th of the input strings "
            "is the prefix and ' S' otherwise. If there are several possible "
            'answers, you can print any.',
  'title': 'Prefixes and Suffixes',
  'topics': ['*special', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1532/F'},
 {'history': 'Annie has gotten bored of winning every coding contest and '
             'farming unlimited rating. Today, she is going to farm potatoes '
             "instead. Annie' s garden is an infinite 2D plane. She has nn "
             'potatoes to plant, and the ii- th potato must be planted at ( '
             'xi, yi) ( xi, yi) . Starting at the point ( 0, 0) ( 0, 0) , '
             'Annie begins walking, in one step she can travel one unit right '
             'or up ( increasing her xx or yy coordinate by 11 respectively) . '
             'At any point ( X, Y) ( X, Y) during her walk she can plant some '
             'potatoes at arbitrary points using her potato gun, consuming '
             'max( | X−x| , | Y−y| ) max( | X−x| , | Y−y| ) units of energy in '
             'order to plant a potato at ( x, y) ( x, y) . Find the minimum '
             'total energy required to plant every potato. Note that Annie may '
             'plant any number of potatoes from any point.',
  'input': 'The first line contains the integer nn ( 1≤n≤8000001≤n≤800000) . '
           'The next nn lines contain two integers xixi and yiyi ( 0≤xi, '
           'yi≤1090≤xi, yi≤109) , representing the location of the ii- th '
           'potato. It is possible that some potatoes should be planted in the '
           'same location.',
  'note': 'In example 11, Annie can travel to each spot directly and plant a '
          'potato with no energy required. In example 22, moving to ( 1, 0) ( '
          '1, 0) , Annie plants the second potato using 11 energy. Next, she '
          'travels to ( 1, 1) ( 1, 1) and plants the first potato with 00 '
          'energy.',
  'output': 'Print the minimum total energy to plant all potatoes.',
  'title': 'A New Beginning',
  'topics': ['data structures', 'dp', 'geometry', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1534/G'},
 {'history': 'This is an interactive problem. As he qualified for IOI this '
             'year, Little Ericyi was given a gift from all his friends: a '
             'tree of nn nodes! On the flight to IOI Little Ericyi was very '
             'bored, so he decided to play a game with Little Yvonne with his '
             'new tree. First, Little Yvonne selects two ( not necessarily '
             'different) nodes aa and bb on the tree ( without telling Ericyi) '
             ', and then gives him a hint ff ( which is some node on the path '
             'from aa to bb) . Then, Little Ericyi is able to ask the '
             'following question repeatedly: If I rooted the tree at node rr ( '
             'Ericyi gets to choose rr) , what would be the Lowest Common '
             "Ancestor of aa and bb? Little Ericyi' s goal is to find the "
             'nodes aa and bb, and report them to Little Yvonne. However, '
             'Little Yvonne thought this game was too easy, so before he gives '
             'the hint ff to Little Ericyi, he also wants him to first find '
             'the maximum number of queries required to determine aa and bb '
             'over all possibilities of aa, bb, and ff assuming Little Ericyi '
             'plays optimally. Little Ericyi defines an optimal strategy as '
             'one that makes the minimum number of queries. Of course, once '
             'Little Ericyi replies with the maximum number of queries, Little '
             'Yvonne will only let him use that many queries in the game. The '
             'tree, aa, bb, and ff are all fixed before the start of the game '
             'and do not change as queries are made. InteractionFirst read a '
             'line containing the integer nn ( 1≤n≤1051≤n≤105) , the number of '
             "nodes in the tree. The next n−1n−1 lines describe Little Ericyi' "
             's tree. These lines contain two integers uu and vv ( 1≤u, '
             'v≤n1≤u, v≤n) denoting an edge between uu and vv ( u= ̸vu= ̸v) . '
             'It is guaranteed that these edges form a tree. After that you '
             'should output kk, the maximum number of queries needed to '
             'determine aa and bb over all possibilities of aa, bb, and ff '
             'assuming Little Ericyi plays optimally. You should output end of '
             'line and flush the output after printing kk. After that read a '
             'line containing the integer ff ( 1≤f≤n1≤f≤n) — the hint: a node '
             'on the path from aa to bb, inclusive. After that, you can start '
             'making queries. You will be limited to making at most kk '
             'queries, where kk is the number you printed. Each query is made '
             'in the format " ? r" , where rr is an integer 1≤r≤n1≤r≤n '
             'denoting the root node you want for the query. You will then '
             'receive an integer xx ( 1≤x≤n1≤x≤n) , the Lowest Common Ancestor '
             'of aa and bb if the tree was rooted at rr. When your program has '
             'found the nodes aa, bb, report the answer in the following '
             'format: " ! a b" , where aa and bb are the two hidden nodes and '
             'terminate your program normally immediately after flushing the '
             'output stream. You may output aa and bb in any order. After '
             'printing a query do not forget to output end of line and flush '
             'the output. Otherwise, you will get Idleness limit exceeded. To '
             'do this, use: fflush( stdout) or cout. flush( ) in C+ + ; '
             'System. out. flush( ) in Java; flush( output) in Pascal; stdout. '
             'flush( ) in Python; see documentation for other languages. If at '
             'any point you make an invalid output or make more than kk '
             'queries, the interaction will terminate and you will receive a '
             'Wrong Answer verdict. An invalid output is defined as either an '
             'invalid query or a value of kk less than 00 or greater than nn. '
             'HacksTo hack a solution, use the following format: The first '
             'line contains the integer nn ( 1≤n≤1051≤n≤105) . The next n−1n−1 '
             'lines contain two integers uu and vv ( 1≤u, v≤n1≤u, v≤n) '
             'denoting an edge between uu and vv ( u= ̸vu= ̸v) . These n−1n−1 '
             'edges must form a tree. The next line of input contains the '
             'nodes aa and bb ( 1≤a, b≤n1≤a, b≤n) , separated by a space. The '
             'final line of input contains the integer ff ( 1≤f≤n1≤f≤n) . Node '
             'ff should be on the simple path from aa to bb ( inclusive) .',
  'input': ' ',
  'note': 'Here is the the tree from the first sample interaction. Nodes aa '
          'and bb are highlighted. Notice that aa and bb can be output in any '
          'order. Additionally, here are the answers to querying every single '
          'node 1, 2, . . . , n1, 2, . . . , n for your convenience: 11: 11 '
          '22: 22 33: 22 44: 44_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '
          '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ Here is the the tree from the '
          'second sample interaction. Again, nodes aa and bb are highlighted. '
          'Lastly, here are the answers to querying every single node 1, 2, . '
          '. . , n1, 2, . . . , n ( in example 22) for your convenience: 11: '
          '11 22: 44 33: 11 44: 44 55: 44',
  'output': ' ',
  'title': 'Lost Nodes',
  'topics': ['constructive algorithms',
             'dp',
             'graphs',
             'interactive',
             'sortings',
             'trees'],
  'url': 'https://codeforces.com/problemset/problem/1534/H'},
 {'history': "You are given an array a consisting of n integers. Let' s call a "
             'pair of indices i, j good if 1≤i< j≤n and gcd( ai, 2aj) > 1 ( '
             'where gcd( x, y) is the greatest common divisor of x and y) . '
             'Find the maximum number of good index pairs if you can reorder '
             'the array a in an arbitrary way.',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of test cases. The first line of the test case contains a '
           'single integer n ( 2≤n≤2000) — the number of elements in the '
           'array. The second line of the test case contains n integers a1, '
           'a2, . . . , an ( 1≤ai≤105) . It is guaranteed that the sum of n '
           'over all test cases does not exceed 2000.',
  'note': 'In the first example, the array elements can be rearranged as '
          'follows: [ 6, 3, 5, 3] . In the third example, the array elements '
          'can be rearranged as follows: [ 4, 4, 2, 1, 1] .',
  'output': 'For each test case, output a single integer — the maximum number '
            'of good index pairs if you can reorder the array a in an '
            'arbitrary way.',
  'title': 'Array Reodering',
  'topics': ['brute force', 'greedy', 'math', 'number theory', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1535/B'},
 {'history': 'You are given a string s consisting of the characters 0, 1, and '
             "? . Let' s call a string unstable if it consists of the "
             'characters 0 and 1 and any two adjacent characters are different '
             "( i. e. it has the form 010101. . . or 101010. . . ) . Let' s "
             'call a string beautiful if it consists of the characters 0, 1, '
             'and ? , and you can replace the characters ? to 0 or 1 ( for '
             'each character, the choice is independent) , so that the string '
             'becomes unstable. For example, the strings 0? ? 10, 0, and ? ? ? '
             'are beautiful, and the strings 00 and ? 1? ? 1 are not. '
             'Calculate the number of beautiful contiguous substrings of the '
             'string s.',
  'input': 'The first line contains a single integer t ( 1≤t≤104) — number of '
           'test cases. The first and only line of each test case contains the '
           'string s ( 1≤| s| ≤2⋅105) consisting of characters 0, 1, and ? . '
           'It is guaranteed that the sum of the string lengths over all test '
           'cases does not exceed 2⋅105.',
  'note': ' ',
  'output': 'For each test case, output a single integer — the number of '
            'beautiful substrings of the string s.',
  'title': 'Unstable String',
  'topics': ['binary search',
             'dp',
             'greedy',
             'implementation',
             'strings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1535/C'},
 {'history': '2k2k teams participate in a playoff tournament. The tournament '
             'consists of 2k−12k−1 games. They are held as follows: first of '
             'all, the teams are split into pairs: team 11 plays against team '
             '22, team 33 plays against team 44 ( exactly in this order) , and '
             'so on ( so, 2k−12k−1 games are played in that phase) . When a '
             'team loses a game, it is eliminated, and each game results in '
             'elimination of one team ( there are no ties) . After that, only '
             '2k−12k−1 teams remain. If only one team remains, it is declared '
             'the champion; otherwise, 2k−22k−2 games are played: in the first '
             'one of them, the winner of the game " 11 vs 22" plays against '
             'the winner of the game " 33 vs 44" , then the winner of the game '
             '" 55 vs 66" plays against the winner of the game " 77 vs 88" , '
             'and so on. This process repeats until only one team remains. For '
             'example, this picture describes the chronological order of games '
             'with k= 3k= 3: Let the string ss consisting of 2k−12k−1 '
             'characters describe the results of the games in chronological '
             'order as follows: if sisi is 0, then the team with lower index '
             'wins the ii- th game; if sisi is 1, then the team with greater '
             'index wins the ii- th game; if sisi is ? , then the result of '
             'the ii- th game is unknown ( any team could win this game) . Let '
             'f( s) f( s) be the number of possible winners of the tournament '
             'described by the string ss. A team ii is a possible winner of '
             'the tournament if it is possible to replace every ? with either '
             '1 or 0 in such a way that team ii is the champion. You are given '
             'the initial state of the string ss. You have to process qq '
             'queries of the following form: pp cc — replace spsp with '
             'character cc, and print f( s) f( s) as the result of the query.',
  'input': 'The first line contains one integer kk ( 1≤k≤181≤k≤18) . The '
           'second line contains a string consisting of 2k−12k−1 characters — '
           'the initial state of the string ss. Each character is either ? , '
           '0, or 1. The third line contains one integer qq ( '
           '1≤q≤2⋅1051≤q≤2⋅105) — the number of queries. Then qq lines follow, '
           'the ii- th line contains an integer pp and a character cc ( '
           '1≤p≤2k−11≤p≤2k−1; cc is either ? , 0, or 1) , describing the ii- '
           'th query.',
  'note': ' ',
  'output': 'For each query, print one integer — f( s) f( s) .',
  'title': 'Playoff Tournament',
  'topics': ['data structures',
             'dfs and similar',
             'dp',
             'implementation',
             'trees'],
  'url': 'https://codeforces.com/problemset/problem/1535/D'},
 {'history': 'Suppose you are given two strings a and b. You can apply the '
             'following operation any number of times: choose any contiguous '
             'substring of a or b, and sort the characters in it in non- '
             'descending order. Let f( a, b) the minimum number of operations '
             'you have to apply in order to make them equal ( or f( a, b) = '
             '1337 if it is impossible to make a and b equal using these '
             'operations) . For example: f( ab, ab) = 0; f( ba, ab) = 1 ( in '
             'one operation, we can sort the whole first string) ; f( ebcda, '
             'ecdba) = 1 ( in one operation, we can sort the substring of the '
             'second string starting from the 2- nd character and ending with '
             'the 4- th character) ; f( a, b) = 1337. You are given n strings '
             's1, s2, . . . , sk having equal length. Calculate n∑i= 1n∑j= i+ '
             '1f( si, sj) .',
  'input': 'The first line contains one integer n ( 1≤n≤2⋅105) — the number of '
           'strings. Then n lines follow, each line contains one of the '
           'strings si, consisting of lowercase Latin letters. | s1| = | s2| = '
           '. . . = | sn| , and n⋅| s1| ≤2⋅105. All these strings are pairwise '
           'distinct.',
  'note': ' ',
  'output': 'Print one integer: n∑i= 1n∑j= i+ 1f( si, sj) .',
  'title': 'String Distance',
  'topics': ['binary search',
             'brute force',
             'data structures',
             'hashing',
             'implementation',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1535/F'},
 {'history': 'I, Fischl, Prinzessin der Verurteilung, descend upon this land '
             'by the call of fate an — Oh, you are also a traveler from '
             'another world? Very well, I grant you permission to travel with '
             'me. It is no surprise Fischl speaks with a strange choice of '
             'words. However, this time, not even Oz, her raven friend, can '
             'interpret her expressions! Maybe you can help us understand what '
             'this young princess is saying? You are given a string of n '
             'lowercase Latin letters, the word that Fischl just spoke. You '
             'think that the MEX of this string may help you find the meaning '
             'behind this message. The MEX of the string is defined as the '
             "shortest string that doesn' t appear as a contiguous substring "
             'in the input. If multiple strings exist, the lexicographically '
             'smallest one is considered the MEX. Note that the empty '
             'substring does NOT count as a valid MEX. A string a is '
             'lexicographically smaller than a string b if and only if one of '
             'the following holds: a is a prefix of b, but a= ̸b; in the first '
             'position where a and b differ, the string a has a letter that '
             'appears earlier in the alphabet than the corresponding letter in '
             'b. A string a is a substring of a string b if a can be obtained '
             'from b by deletion of several ( possibly, zero or all) '
             'characters from the beginning and several ( possibly, zero or '
             'all) characters from the end. Find out what the MEX of the '
             'string is!',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤1000) . Description of the test '
           'cases follows. The first line of each test case contains an '
           'integer n ( 1≤n≤1000) — the length of the word. The second line '
           'for each test case contains a single string of n lowercase Latin '
           'letters. The sum of n over all test cases will not exceed 1000.',
  'note': ' ',
  'output': 'For each test case, output the MEX of the string on a new line.',
  'title': 'Prinzessin der Verurteilung',
  'topics': ['brute force', 'constructive algorithms', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1536/B'},
 {'history': 'Uh oh! Ray lost his array yet again! However, Omkar might be '
             "able to help because he thinks he has found the OmkArray of Ray' "
             's array. The OmkArray of an array a with elements a1, a2, . . . '
             ', a2k−1, is the array b with elements b1, b2, . . . , bk such '
             'that bi is equal to the median of a1, a2, . . . , a2i−1 for all '
             'i. Omkar has found an array b of size n ( 1≤n≤2⋅105, '
             "−109≤bi≤109) . Given this array b, Ray wants to test Omkar' s "
             'claim and see if b actually is an OmkArray of some array a. Can '
             'you help Ray? The median of a set of numbers a1, a2, . . . , '
             'a2i−1 is the number ci where c1, c2, . . . , c2i−1 represents '
             'a1, a2, . . . , a2i−1 sorted in nondecreasing order.',
  'input': 'Each test contains multiple test cases. The first line contains a '
           'single integer t ( 1≤t≤104) — the number of test cases. '
           'Description of the test cases follows. The first line of each test '
           'case contains an integer n ( 1≤n≤2⋅105) — the length of the array '
           'b. The second line contains n integers b1, b2, . . . , bn ( '
           '−109≤bi≤109) — the elements of b. It is guaranteed the sum of n '
           'across all test cases does not exceed 2⋅105.',
  'note': 'In the second case of the first sample, the array [ 4] will '
          'generate an OmkArray of [ 4] , as the median of the first element '
          'is 4. In the fourth case of the first sample, the array [ 3, 2, 5] '
          'will generate an OmkArray of [ 3, 3] , as the median of 3 is 3 and '
          'the median of 2, 3, 5 is 3. In the fifth case of the first sample, '
          'the array [ 2, 1, 0, 3, 4, 4, 3] will generate an OmkArray of [ 2, '
          '1, 2, 3] as the median of 2 is 2 the median of 0, 1, 2 is 1 the '
          'median of 0, 1, 2, 3, 4 is 2 and the median of 0, 1, 2, 3, 3, 4, 4 '
          'is 3. In the second case of the second sample, the array [ 1, 0, 4, '
          '3, 5, −2, −2, −2, −4, −3, −4, −1, 5] will generate an OmkArray of [ '
          '1, 1, 3, 1, 0, −2, −1] , as the median of 1 is 1 the median of 0, '
          '1, 4 is 1 the median of 0, 1, 3, 4, 5 is 3 the median of −2, −2, 0, '
          '1, 3, 4, 5 is 1 the median of −4, −2, −2, −2, 0, 1, 3, 4, 5 is 0 '
          'the median of −4, −4, −3, −2, −2, −2, 0, 1, 3, 4, 5 is −2 and the '
          'median of −4, −4, −3, −2, −2, −2, −1, 0, 1, 3, 4, 5, 5 is −1 For '
          'all cases where the answer is NO, it can be proven that it is '
          'impossible to find an array a such that b is the OmkArray of a.',
  'output': 'For each test case, output one line containing YES if there '
            'exists an array a such that bi is the median of a1, a2, . . . , '
            'a2i−1 for all i, and NO otherwise. The case of letters in YES and '
            'NO do not matter ( so yEs and No will also be accepted) .',
  'title': 'Omkar and Medians',
  'topics': ['data structures', 'greedy', 'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1536/D'},
 {'history': 'You are a game designer and want to make an obstacle course. The '
             'player will walk from left to right. You have n heights of '
             'mountains already selected and want to arrange them so that the '
             'absolute difference of the heights of the first and last '
             'mountains is as small as possible. In addition, you want to make '
             'the game difficult, and since walking uphill or flat is harder '
             'than walking downhill, the difficulty of the level will be the '
             'number of mountains i ( 1≤i< n) such that hi≤hi+ 1 where hi is '
             "the height of the i- th mountain. You don' t want to waste any "
             'of the mountains you modelled, so you have to use all of them. '
             'From all the arrangements that minimize | h1−hn| , find one that '
             'is the most difficult. If there are multiple orders that satisfy '
             'these requirements, you may find any.',
  'input': 'The first line will contain a single integer t ( 1≤t≤100) — the '
           'number of test cases. Then t test cases follow. The first line of '
           'each test case contains a single integer n ( 2≤n≤2⋅105) — the '
           'number of mountains. The second line of each test case contains n '
           'integers h1, . . . , hn ( 1≤hi≤109) , where hi is the height of '
           'the i- th mountain. It is guaranteed that the sum of n over all '
           'test cases does not exceed 2⋅105.',
  'note': 'In the first test case: The player begins at height 2, next going '
          'up to height 4 increasing the difficulty by 1. After that he will '
          "go down to height 1 and the difficulty doesn' t change because he "
          'is going downhill. Finally the player will go up to height 2 and '
          'the difficulty will increase by 1. The absolute difference between '
          "the starting height and the end height is equal to 0 and it' s "
          'minimal. The difficulty is maximal. In the second test case: The '
          'player begins at height 1, next going up to height 3 increasing the '
          'difficulty by 1. The absolute difference between the starting '
          "height and the end height is equal to 2 and it' s minimal as they "
          'are the only heights. The difficulty is maximal.',
  'output': 'For each test case, output n integers — the given heights in an '
            'order that maximizes the difficulty score among all orders that '
            'minimize | h1−hn| . If there are multiple orders that satisfy '
            'these requirements, you may output any.',
  'title': 'Challenging Cliffs',
  'topics': ['constructive algorithms', 'greedy', 'implementation', 'math'],
  'url': 'https://codeforces.com/problemset/problem/1537/C'},
 {'history': 'This is the easy version of the problem. The only difference is '
             'the constraints on n and k. You can make hacks only if all '
             'versions of the problem are solved. You have a string s, and you '
             'can do two types of operations on it: Delete the last character '
             'of the string. Duplicate the string: s: = s+ s, where + denotes '
             'concatenation. You can use each operation any number of times ( '
             'possibly none) . Your task is to find the lexicographically '
             'smallest string of length exactly k that can be obtained by '
             'doing these operations on string s. A string a is '
             'lexicographically smaller than a string b if and only if one of '
             'the following holds: a is a prefix of b, but a= ̸b; In the first '
             'position where a and b differ, the string a has a letter that '
             'appears earlier in the alphabet than the corresponding letter in '
             'b.',
  'input': 'The first line contains two integers n, k ( 1≤n, k≤5000) — the '
           'length of the original string s and the length of the desired '
           'string. The second line contains the string s, consisting of n '
           'lowercase English letters.',
  'note': 'In the first test, it is optimal to make one duplication: " '
          'dbcadabc" → " dbcadabcdbcadabc" . In the second test it is optimal '
          'to delete the last 3 characters, then duplicate the string 3 times, '
          'then delete the last 3 characters to make the string have length k. '
          '" abcd" → " abc" → " ab" → " a" → " aa" → " aaaa" → " aaaaaaaa" → " '
          'aaaaaaa" → " aaaaaa" → " aaaaa" .',
  'output': 'Print the lexicographically smallest string of length k that can '
            'be obtained by doing the operations on string s.',
  'title': 'Erase and Extend (Easy Version)',
  'topics': ['binary search',
             'brute force',
             'dp',
             'greedy',
             'hashing',
             'implementation',
             'string suffix structures',
             'strings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1537/E1'},
 {'history': 'This is the hard version of the problem. The only difference is '
             'the constraints on n and k. You can make hacks only if all '
             'versions of the problem are solved. You have a string s, and you '
             'can do two types of operations on it: Delete the last character '
             'of the string. Duplicate the string: s: = s+ s, where + denotes '
             'concatenation. You can use each operation any number of times ( '
             'possibly none) . Your task is to find the lexicographically '
             'smallest string of length exactly k that can be obtained by '
             'doing these operations on string s. A string a is '
             'lexicographically smaller than a string b if and only if one of '
             'the following holds: a is a prefix of b, but a= ̸b; In the first '
             'position where a and b differ, the string a has a letter that '
             'appears earlier in the alphabet than the corresponding letter in '
             'b.',
  'input': 'The first line contains two integers n, k ( 1≤n, k≤5⋅105) — the '
           'length of the original string s and the length of the desired '
           'string. The second line contains the string s, consisting of n '
           'lowercase English letters.',
  'note': 'In the first test, it is optimal to make one duplication: " '
          'dbcadabc" → " dbcadabcdbcadabc" . In the second test it is optimal '
          'to delete the last 3 characters, then duplicate the string 3 times, '
          'then delete the last 3 characters to make the string have length k. '
          '" abcd" → " abc" → " ab" → " a" → " aa" → " aaaa" → " aaaaaaaa" → " '
          'aaaaaaa" → " aaaaaa" → " aaaaa" .',
  'output': 'Print the lexicographically smallest string of length k that can '
            'be obtained by doing the operations on string s.',
  'title': 'Erase and Extend (Hard Version)',
  'topics': ['binary search',
             'data structures',
             'greedy',
             'hashing',
             'string suffix structures',
             'strings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1537/E2'},
 {'history': 'Polycarp came up with a new programming language. There are only '
             'two types of statements in it: " x : = s" : assign the variable '
             'named x the value s ( where s is a string) . For example, the '
             'statement var : = hello assigns the variable named var the value '
             'hello. Note that s is the value of a string, not the name of a '
             'variable. Between the variable name, the : = operator and the '
             'string contains exactly one space each. " x = a + b" : assign '
             'the variable named x the concatenation of values of two '
             'variables a and b. For example, if the program consists of three '
             'statements a : = hello, b : = world, c = a + b, then the '
             'variable c will contain the string helloworld. It is guaranteed '
             'that the program is correct and the variables a and b were '
             'previously defined. There is exactly one space between the '
             'variable names and the = and + operators. All variable names and '
             'strings only consist of lowercase letters of the English '
             'alphabet and do not exceed 5 characters. The result of the '
             'program is the number of occurrences of string haha in the '
             'string that was written to the variable in the last statement. '
             'Polycarp was very tired while inventing that language. He asks '
             'you to implement it. Your task is — for given program statements '
             'calculate the number of occurrences of string haha in the last '
             'assigned variable.',
  'input': 'The first line contains an integer t ( 1≤t≤103) . Then t test '
           'cases follow. The first line of each test case contains a single '
           'integer n ( 1≤n≤50) — the number of statements in the program. All '
           'variable names and strings are guaranteed to consist only of '
           'lowercase letters of the English alphabet and do not exceed 5 '
           'characters. This is followed by n lines describing the statements '
           'in the format described above. It is guaranteed that the program '
           'is correct.',
  'note': 'In the first test case the resulting value of d is hhahahaha.',
  'output': 'For each set of input data, output the number of occurrences of '
            'the haha substring in the string that was written to the variable '
            'in the last statement.',
  'title': 'Funny Substrings',
  'topics': ['data structures',
             'hashing',
             'implementation',
             'matrices',
             'strings'],
  'url': 'https://codeforces.com/problemset/problem/1538/E'},
 {'history': 'Petya once wrote a sad love song and shared it to Vasya. The '
             'song is a string consisting of lowercase English letters. Vasya '
             'made up q questions about this song. Each question is about a '
             'subsegment of the song starting from the l- th letter to the r- '
             'th letter. Vasya considers a substring made up from characters '
             'on this segment and repeats each letter in the subsegment k '
             'times, where k is the index of the corresponding letter in the '
             'alphabet. For example, if the question is about the substring " '
             'abbcb" , then Vasya repeats letter \' a\' once, each of the '
             'letters \' b\' twice, letter \' c" three times, so that the '
             'resulting string is " abbbbcccbb" , its length is 10. Vasya is '
             'interested about the length of the resulting string. Help Petya '
             'find the length of each string obtained by Vasya.',
  'input': 'The first line contains two integers n and q ( 1≤n≤100000, '
           '1≤q≤100000) — the length of the song and the number of questions. '
           'The second line contains one string s — the song, consisting of n '
           "lowercase letters of English letters. Vasya' s questions are "
           'contained in the next q lines. Each line contains two integers l '
           'and r ( 1≤l≤r≤n) — the bounds of the question.',
  'note': 'In the first example Vasya is interested in three questions. In the '
          'first question Vasya considers the substring " aba" , that '
          'transforms to " abba" , so the answer is equal to 4. In the second '
          'question Vasya considers " baca" , that transforms to " bbaccca" , '
          'so the answer is 7. In the third question Vasya considers the '
          'string " abacaba" , that transforms to " abbacccabba" of length 11.',
  'output': 'Print q lines: for each question print the length of the string '
            'obtained by Vasya.',
  'title': 'Love Song',
  'topics': ['dp', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1539/B'},
 {'history': 'There are n students numerated from 1 to n. The level of the i- '
             'th student is ai. You need to split the students into stable '
             'groups. A group of students is called stable, if in the sorted '
             'array of their levels no two neighboring elements differ by more '
             'than x. For example, if x= 4, then the group with levels [ 1, '
             '10, 8, 4, 4] is stable ( because 4−1≤x, 4−4≤x, 8−4≤x, 10−8≤x) , '
             'while the group with levels [ 2, 10, 10, 7] is not stable ( 7−2= '
             '5> x) . Apart from the n given students, teachers can invite at '
             "most k additional students with arbitrary levels ( at teachers' "
             'choice) . Find the minimum number of stable groups teachers can '
             'form from all students ( including the newly invited) . For '
             'example, if there are two students with levels 1 and 5; x= 2; '
             'and k≥1, then you can invite a new student with level 3 and put '
             'all the students in one stable group.',
  'input': 'The first line contains three integers n, k, x ( 1≤n≤200000, '
           '0≤k≤1018, 1≤x≤1018) — the initial number of students, the number '
           'of students you can additionally invite, and the maximum allowed '
           'level difference. The second line contains n integers a1, a2, . . '
           '. , an ( 1≤ai≤1018) — the students levels.',
  'note': 'In the first example you can invite two students with levels 2 and '
          '11. Then you can split the students into two stable groups: [ 1, 1, '
          '2, 5, 8, 11, 12, 13] , [ 20, 22] . In the second example you are '
          'not allowed to invite new students, so you need 3 groups: [ 1, 1, '
          '5, 5, 20, 20] [ 60, 70, 70, 70, 80, 90] [ 420]',
  'output': 'In the only line print a single integer: the minimum number of '
            'stable groups you can split the students into.',
  'title': 'Stable Groups',
  'topics': ['greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1539/C'},
 {'history': 'Lena is the most economical girl in Moscow. So, when her dad '
             'asks her to buy some food for a trip to the country, she goes to '
             'the best store — " PriceFixed" . Here are some rules of that '
             'store: The store has an infinite number of items of every '
             'product. All products have the same price: 2 rubles per item. '
             'For every product i there is a discount for experienced buyers: '
             'if you buy bi items of products ( of any type, not necessarily '
             'type i) , then for all future purchases of the i- th product '
             'there is a 50',
  'input': 'The first line contains a single integer n ( 1≤n≤100000) — the '
           'number of products. Each of next n lines contains a product '
           'description. Each description consists of two integers ai and bi ( '
           '1≤ai≤1014, 1≤bi≤1014) — the required number of the i- th product '
           'and how many products you need to buy to get the discount on the '
           'i- th product. The sum of all ai does not exceed 1014.',
  'note': 'In the first example, Lena can purchase the products in the '
          'following way: one item of product 3 for 2 rubles, one item of '
          'product 1 for 2 rubles, one item of product 1 for 2 rubles, one '
          'item of product 2 for 1 ruble ( she can use the discount because 3 '
          'items are already purchased) , one item of product 1 for 1 ruble ( '
          'she can use the discount because 4 items are already purchased) . '
          'In total, she spends 8 rubles. It can be proved that it is '
          'impossible to spend less. In the second example Lena can purchase '
          'the products in the following way: one item of product 1 for 2 '
          'rubles, two items of product 2 for 2 rubles for each, one item of '
          'product 5 for 2 rubles, one item of product 3 for 1 ruble, two '
          'items of product 4 for 1 ruble for each, one item of product 1 for '
          '1 ruble. In total, she spends 12 rubles.',
  'output': 'Output the minimum sum that Lena needs to make all purchases.',
  'title': 'PriceFixed',
  'topics': ['binary search',
             'greedy',
             'implementation',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1539/D'},
 {'history': "The Alice' s computer is broken, so she can' t play her favorite "
             'card game now. To help Alice, Bob wants to answer n her '
             'questions. Initially, Bob holds one card with number 0 in the '
             'left hand and one in the right hand. In the i- th question, '
             'Alice asks Bob to replace a card in the left or right hand with '
             'a card with number ki ( Bob chooses which of two cards he '
             'changes, Bob must replace exactly one card) . After this action, '
             'Alice wants the numbers on the left and right cards to belong to '
             'given segments ( segments for left and right cards can be '
             'different) . Formally, let the number on the left card be x, and '
             'on the right card be y. Then after the i- th swap the following '
             'conditions must be satisfied: al, i≤x≤bl, i, and ar, i≤y≤br, i. '
             'Please determine if Bob can answer all requests. If it is '
             'possible, find a way to do it.',
  'input': 'The first line contains two integers n and m ( 2≤n≤100000, '
           '2≤m≤109) — the number of questions and the maximum possible value '
           'on the card. Then n queries are described. Every description '
           'contains 3 lines. The first line of the description of the i- th '
           'query contains a single integer ki ( 0≤ki≤m) — the number on a new '
           'card. The second line of the description of the i- th query '
           'contains two integers al, i and bl, i ( 0≤al, i≤bl, i≤m) — the '
           'minimum and maximum values of the card at the left hand after the '
           'replacement. The third line of the description of the i- th query '
           'contains two integers ar, i and br, i ( 0≤ar, i≤br, i≤m) — the '
           'minimum and maximum values of the card at the right hand after the '
           'replacement.',
  'note': ' ',
  'output': 'At the first line, print " Yes" , if Bob can answer all queries, '
            'and " No" otherwise. If Bob can answer all n queries, then at the '
            'second line print n numbers: a way to satisfy all requirements. '
            'If in i- th query Bob needs to replace the card in the left hand, '
            'print 0, otherwise print 1. If there are multiple answers, print '
            'any.',
  'title': 'Game with Cards',
  'topics': ['binary search',
             'constructive algorithms',
             'data structures',
             'dp',
             'greedy',
             'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1539/E'},
 {'history': 'Vasya has an array of n integers a1, a2, . . . , an. Vasya '
             'thinks that all numbers in his array are strange for some '
             'reason. To calculate how strange the i- th number is, Vasya '
             'created the following algorithm. He chooses a subsegment al, al+ '
             '1, . . . , ar, such that 1≤l≤i≤r≤n, sort its elements in '
             'increasing order in his head ( he can arrange equal elements '
             'arbitrary) . After that he finds the center of the segment. The '
             'center of a segment is the element at position ( l+ r) / 2, if '
             'the length of the segment is odd, and at position ( l+ r+ 1) / 2 '
             'otherwise. Now Vasya finds the element that was at position i '
             'before the sorting, and calculates the distance between its '
             'current position and the center of the subsegment ( the distance '
             'between the elements with indices j and k is | j−k| ) . The '
             'strangeness of the number at position i is the maximum distance '
             'among all suitable choices of l and r. Vasya wants to calculate '
             'the strangeness of each number in his array. Help him to do it.',
  'input': 'The first line contains a single integer n ( 1≤n≤200000) — the '
           'size of the array. The second line contains n integers a1, a2, . . '
           ". , an ( 1≤ai≤n) — Vasya' s array.",
  'note': 'In the first example: For the first position we choose the segment '
          'from 1 to 5. After sorting, it looks like [ 1, 2, 3, 4, 5] , the '
          'center is 3. The distance from the center to 5 is 2. For the second '
          'position we choose the segment from 2 to 4. For the third position '
          'we choose the segment from 3 to 5. For the fourth position we '
          'choose the segment from 1 to 4. After sorting, it looks like [ 2, '
          '3, 4, 5] , the center is 4. The distance from the center to 2 is 2. '
          'For the fifth position we choose the segment from 1 to 5.',
  'output': 'Print a single line with n numbers. The i- th of them must be '
            'equal to the strangeness of the i- th element of the array.',
  'title': 'Strange Array',
  'topics': ['data structures', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1539/F'},
 {'history': 'Farmer John has a farm that consists of n pastures connected by '
             'one- directional roads. Each road has a weight, representing the '
             'time it takes to go from the start to the end of the road. The '
             'roads could have negative weight, where the cows go so fast that '
             'they go back in time! However, Farmer John guarantees that it is '
             'impossible for the cows to get stuck in a time loop, where they '
             'can infinitely go back in time by traveling across a sequence of '
             'roads. Also, each pair of pastures is connected by at most one '
             'road in each direction. Unfortunately, Farmer John lost the map '
             'of the farm. All he remembers is an array d, where di is the '
             'smallest amount of time it took the cows to reach the i- th '
             'pasture from pasture 1 using a sequence of roads. The cost of '
             'his farm is the sum of the weights of each of the roads, and '
             'Farmer John needs to know the minimal cost of a farm that is '
             'consistent with his memory.',
  'input': 'The first line contains one integer t ( 1≤t≤104) — the number of '
           'test cases. Then t cases follow. The first line of each test case '
           'contains a single integer n ( 1≤n≤105) — the number of pastures. '
           'The second line of each test case contains n space separated '
           'integers d1, d2, . . . , dn ( 0≤di≤109) — the array d. It is '
           'guaranteed that d1= 0. It is guaranteed that the sum of n over all '
           'test cases does not exceed 105.',
  'note': 'In the first test case, you can add roads from pasture 1 to pasture '
          '2 with a time of 2, from pasture 2 to pasture 3 with a time of 1, '
          'from pasture 3 to pasture 1 with a time of −3, from pasture 3 to '
          'pasture 2 with a time of −1, from pasture 2 to pasture 1 with a '
          'time of −2. The total cost is 2+ 1+ −3+ −1+ −2= −3. In the second '
          'test case, you can add a road from pasture 1 to pasture 2 with cost '
          '1000000000 and a road from pasture 2 to pasture 1 with cost '
          '−1000000000. The total cost is 1000000000+ −1000000000= 0. In the '
          "third test case, you can' t add any roads. The total cost is 0.",
  'output': 'For each test case, output the minimum possible cost of a farm '
            "that is consistent with Farmer John' s memory.",
  'title': 'Great Graphs',
  'topics': ['constructive algorithms',
             'graphs',
             'greedy',
             'shortest paths',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1540/A'},
 {'history': 'There are n cats in a line, labeled from 1 to n, with the i- th '
             'cat at position i. They are bored of gyrating in the same spot '
             'all day, so they want to reorder themselves such that no cat is '
             'in the same place as before. They are also lazy, so they want to '
             'minimize the total distance they move. Help them decide what cat '
             'should be at each location after the reordering. For example, if '
             'there are 3 cats, this is a valid reordering: [ 3, 1, 2] . No '
             'cat is in its original position. The total distance the cats '
             'move is 1+ 1+ 2= 4 as cat 1 moves one place to the right, cat 2 '
             'moves one place to the right, and cat 3 moves two places to the '
             'left.',
  'input': 'The first line contains a single integer t ( 1≤t≤100) — the number '
           'of test cases. Then t test cases follow. The first and only line '
           'of each test case contains one integer n ( 2≤n≤100) — the number '
           'of cats. It can be proven that under the constraints of the '
           'problem, an answer always exist.',
  'note': 'For the first test case, there is only one possible permutation '
          'that satisfies the conditions: [ 2, 1] . The second test case was '
          'described in the statement. Another possible answer is [ 2, 3, 1] .',
  'output': 'Output t answers, one for each test case. Each answer consists of '
            'n integers — a permutation with the minimum total distance. If '
            'there are multiple answers, print any.',
  'title': 'Pretty Permutations',
  'topics': ['constructive algorithms', 'greedy', 'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1541/A'},
 {'history': 'You are given an array a1, a2, . . . , an consisting of n '
             'distinct integers. Count the number of pairs of indices ( i, j) '
             'such that i< j and ai⋅aj= i+ j.',
  'input': 'The first line contains one integer t ( 1≤t≤104) — the number of '
           'test cases. Then t cases follow. The first line of each test case '
           'contains one integer n ( 2≤n≤105) — the length of array a. The '
           'second line of each test case contains n space separated integers '
           'a1, a2, . . . , an ( 1≤ai≤2⋅n) — the array a. It is guaranteed '
           'that all elements are distinct. It is guaranteed that the sum of n '
           'over all test cases does not exceed 2⋅105.',
  'note': 'For the first test case, the only pair that satisfies the '
          'constraints is ( 1, 2) , as a1⋅a2= 1+ 2= 3For the second test case, '
          'the only pair that satisfies the constraints is ( 2, 3) . For the '
          'third test case, the pairs that satisfy the constraints are ( 1, 2) '
          ', ( 1, 5) , and ( 2, 3) .',
  'output': 'For each test case, output the number of pairs of indices ( i, j) '
            'such that i< j and ai⋅aj= i+ j.',
  'title': 'Pleasant Pairs',
  'topics': ['brute force', 'implementation', 'math', 'number theory'],
  'url': 'https://codeforces.com/problemset/problem/1541/B'},
 {'history': 'You are given a sequence A, where its elements are either in the '
             'form + x or - , where x is an integer. For such a sequence S '
             'where its elements are either in the form + x or - , define f( '
             "S) as follows: iterate through S' s elements from the first one "
             'to the last one, and maintain a multiset T as you iterate '
             "through it. for each element, if it' s in the form + x, add x to "
             'T; otherwise, erase the smallest element from T ( if T is empty, '
             "do nothing) . after iterating through all S' s elements, compute "
             'the sum of all elements in T. f( S) is defined as the sum. The '
             'sequence b is a subsequence of the sequence a if b can be '
             'derived from a by removing zero or more elements without '
             "changing the order of the remaining elements. For all A' s "
             'subsequences B, compute the sum of f( B) , modulo 998244353.',
  'input': 'The first line contains an integer n ( 1≤n≤500) — the length of A. '
           'Each of the next n lines begins with an operator + or - . If the '
           "operator is + , then it' s followed by an integer x ( 1≤x< "
           '998244353) . The i- th line of those n lines describes the i- th '
           'element in A.',
  'note': 'In the first example, the following are all possible pairs of B and '
          'f( B) : B= , f( B) = 0. B= - , f( B) = 0. B= + 1, - , f( B) = 0. B= '
          '- , + 1, - , f( B) = 0. B= + 2, - , f( B) = 0. B= - , + 2, - , f( '
          'B) = 0. B= - , f( B) = 0. B= - , - , f( B) = 0. B= + 1, + 2, f( B) '
          '= 3. B= + 1, + 2, - , f( B) = 2. B= - , + 1, + 2, f( B) = 3. B= - , '
          '+ 1, + 2, - , f( B) = 2. B= - , + 1, f( B) = 1. B= + 1, f( B) = 1. '
          'B= - , + 2, f( B) = 2. B= + 2, f( B) = 2. The sum of these values '
          'is 16.',
  'output': 'Print one integer, which is the answer to the problem, modulo '
            '998244353.',
  'title': 'Priority Queue',
  'topics': ['combinatorics', 'dp', 'implementation', 'math', 'ternary search'],
  'url': 'https://codeforces.com/problemset/problem/1542/D'},
 {'history': 'After defeating a Blacklist Rival, you get a chance to draw 1 '
             'reward slip out of x hidden valid slips. Initially, x= 3 and '
             'these hidden valid slips are Cash Slip, Impound Strike Release '
             "Marker and Pink Slip of Rival' s Car. Initially, the probability "
             'of drawing these in a random guess are c, m, and p, '
             'respectively. There is also a volatility factor v. You can play '
             "any number of Rival Races as long as you don' t draw a Pink "
             'Slip. Assume that you win each race and get a chance to draw a '
             'reward slip. In each draw, you draw one of the x valid items '
             'with their respective probabilities. Suppose you draw a '
             'particular item and its probability of drawing before the draw '
             'was a. Then, If the item was a Pink Slip, the quest is over, and '
             'you will not play any more races. Otherwise, If a≤v, the '
             'probability of the item drawn becomes 0 and the item is no '
             'longer a valid item for all the further draws, reducing x by 1. '
             'Moreover, the reduced probability a is distributed equally among '
             'the other remaining valid items. If a> v, the probability of the '
             'item drawn reduces by v and the reduced probability is '
             'distributed equally among the other valid items. For example, If '
             '( c, m, p) = ( 0. 2, 0. 1, 0. 7) and v= 0. 1, after drawing '
             'Cash, the new probabilities will be ( 0. 1, 0. 15, 0. 75) . If ( '
             'c, m, p) = ( 0. 1, 0. 2, 0. 7) and v= 0. 2, after drawing Cash, '
             'the new probabilities will be ( Invalid, 0. 25, 0. 75) . If ( c, '
             'm, p) = ( 0. 2, Invalid, 0. 8) and v= 0. 1, after drawing Cash, '
             'the new probabilities will be ( 0. 1, Invalid, 0. 9) . If ( c, '
             'm, p) = ( 0. 1, Invalid, 0. 9) and v= 0. 2, after drawing Cash, '
             'the new probabilities will be ( Invalid, Invalid, 1. 0) . You '
             'need the cars of Rivals. So, you need to find the expected '
             'number of races that you must play in order to draw a pink slip.',
  'input': 'The first line of input contains a single integer t ( 1≤t≤10) — '
           'the number of test cases. The first and the only line of each test '
           'case contains four real numbers c, m, p and v ( 0< c, m, p< 1, c+ '
           'm+ p= 1, 0. 1≤v≤0. 9) . Additionally, it is guaranteed that each '
           'of c, m, p and v have at most 4 decimal places.',
  'note': 'For the first test case, the possible drawing sequences are: P with '
          'a probability of 0. 6; CP with a probability of 0. 2⋅0. 7= 0. 14; '
          'CMP with a probability of 0. 2⋅0. 3⋅0. 9= 0. 054; CMMP with a '
          'probability of 0. 2⋅0. 3⋅0. 1⋅1= 0. 006; MP with a probability of '
          '0. 2⋅0. 7= 0. 14; MCP with a probability of 0. 2⋅0. 3⋅0. 9= 0. 054; '
          'MCCP with a probability of 0. 2⋅0. 3⋅0. 1⋅1= 0. 006. So, the '
          'expected number of races is equal to 1⋅0. 6+ 2⋅0. 14+ 3⋅0. 054+ '
          '4⋅0. 006+ 2⋅0. 14+ 3⋅0. 054+ 4⋅0. 006= 1. 532. For the second test '
          'case, the possible drawing sequences are: P with a probability of '
          '0. 4; CP with a probability of 0. 4⋅0. 6= 0. 24; CMP with a '
          'probability of 0. 4⋅0. 4⋅1= 0. 16; MP with a probability of 0. 2⋅0. '
          '5= 0. 1; MCP with a probability of 0. 2⋅0. 5⋅1= 0. 1. So, the '
          'expected number of races is equal to 1⋅0. 4+ 2⋅0. 24+ 3⋅0. 16+ 2⋅0. '
          '1+ 3⋅0. 1= 1. 86.',
  'output': 'For each test case, output a single line containing a single real '
            'number — the expected number of races that you must play in order '
            'to draw a Pink Slip. Your answer is considered correct if its '
            'absolute or relative error does not exceed 10−6. Formally, let '
            "your answer be a, and the jury' s answer be b. Your answer is "
            'accepted if and only if | a−b| max( 1, | b| ) ≤10−6.',
  'title': 'Need for Pink Slips',
  'topics': ['bitmasks',
             'brute force',
             'dfs and similar',
             'implementation',
             'math',
             'probabilities'],
  'url': 'https://codeforces.com/problemset/problem/1543/C'},
 {'history': 'AquaMoon has n friends. They stand in a row from left to right, '
             'and the i- th friend from the left wears a T- shirt with a '
             'number ai written on it. Each friend has a direction ( left or '
             'right) . In the beginning, the direction of each friend is '
             'right. AquaMoon can make some operations on friends. On each '
             'operation, AquaMoon can choose two adjacent friends and swap '
             'their positions. After each operation, the direction of both '
             'chosen friends will also be flipped: left to right and vice '
             'versa. AquaMoon hopes that after some operations, the numbers '
             'written on the T- shirt of n friends in the row, read from left '
             'to right, become non- decreasing. Also she wants, that all '
             'friends will have a direction of right at the end. Please find '
             'if it is possible.',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤50) — the number of test cases. The first '
           'line of each test case contains a single integer n ( 1≤n≤105) — '
           "the number of Aquamoon' s friends. The second line contains n "
           'integers a1, a2, . . . , an ( 1≤ai≤105) — the numbers, written on '
           'the T- shirts. It is guaranteed that the sum of n for all test '
           'cases does not exceed 105.',
  'note': 'The possible list of operations in the first test case: Swap a1 and '
          'a2. The resulting sequence is 3, 4, 2, 5. The directions are: left, '
          'left, right, right. Swap a2 and a3. The resulting sequence is 3, 2, '
          '4, 5. The directions are: left, left, right, right. Swap a1 and a2. '
          'The resulting sequence is 2, 3, 4, 5. The directions are: right, '
          'right, right, right.',
  'output': 'For each test case, if there exists a possible sequence of '
            'operations, print " YES" ( without quotes) ; otherwise, print " '
            'NO" ( without quotes) . You can print each letter in any case ( '
            'upper or lower) .',
  'title': 'AquaMoon and Strange Sort',
  'topics': ['sortings'],
  'url': 'https://codeforces.com/problemset/problem/1545/A'},
 {'history': 'There are three cells on an infinite 2- dimensional grid, '
             'labeled A, B, and F. Find the length of the shortest path from A '
             'to B if: in one move you can go to any of the four adjacent '
             'cells sharing a side; visiting the cell F is forbidden ( it is '
             'an obstacle) .',
  'input': 'The first line contains an integer t ( 1≤t≤104) — the number of '
           'test cases in the input. Then t test cases follow. Before each '
           'test case, there is an empty line. Each test case contains three '
           'lines. The first one contains two integers xA, yA ( 1≤xA, yA≤1000) '
           '— coordinates of the start cell A. The second one contains two '
           'integers xB, yB ( 1≤xB, yB≤1000) — coordinates of the finish cell '
           'B. The third one contains two integers xF, yF ( 1≤xF, yF≤1000) — '
           'coordinates of the forbidden cell F. All cells are distinct. '
           'Coordinate x corresponds to the column number and coordinate y '
           'corresponds to the row number ( see the pictures below) .',
  'note': 'An example of a possible shortest path for the first test case. An '
          'example of a possible shortest path for the second test case.',
  'output': 'Output t lines. The i- th line should contain the answer for the '
            'i- th test case: the length of the shortest path from the cell A '
            'to the cell B if the cell F is not allowed to be visited.',
  'title': 'Shortest Path with Obstacle',
  'topics': ['implementation', 'math'],
  'url': 'https://codeforces.com/problemset/problem/1547/A'},
 {'history': 'A string s of length n ( 1≤n≤26) is called alphabetical if it '
             'can be obtained using the following algorithm: first, write an '
             'empty string to s ( i. e. perform the assignment s : = " " ) ; '
             'then perform the next step n times; at the i- th step take i- th '
             'lowercase letter of the Latin alphabet and write it either to '
             'the left of the string s or to the right of the string s ( i. e. '
             'perform the assignment s : = c+ s or s : = s+ c, where c is the '
             'i- th letter of the Latin alphabet) . In other words, iterate '
             "over the n first letters of the Latin alphabet starting from ' "
             "a' and etc. Each time we prepend a letter to the left of the "
             'string s or append a letter to the right of the string s. '
             'Strings that can be obtained in that way are alphabetical. For '
             'example, the following strings are alphabetical: " a" , " ba" , '
             '" ab" , " bac" and " ihfcbadeg" . The following strings are not '
             'alphabetical: " z" , " aa" , " ca" , " acb" , " xyz" and " '
             'ddcba" . From the given string, determine if it is alphabetical.',
  'input': 'The first line contains one integer t ( 1≤t≤104) — the number of '
           'test cases. Then t test cases follow. Each test case is written on '
           'a separate line that contains one string s. String s consists of '
           'lowercase letters of the Latin alphabet and has a length between 1 '
           'and 26, inclusive.',
  'note': 'The example contains test cases from the main part of the '
          'condition.',
  'output': 'Output t lines, each of them must contain the answer to the '
            'corresponding test case. Output YES if the given string s is '
            'alphabetical and NO otherwise. You can output YES and NO in any '
            'case ( for example, strings yEs, yes, Yes and YES will be '
            'recognized as a positive answer) .',
  'title': 'Alphabetical Strings',
  'topics': ['greedy', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1547/B'},
 {'history': 'On a strip of land of length n there are k air conditioners: the '
             'i- th air conditioner is placed in cell ai ( 1≤ai≤n) . Two or '
             'more air conditioners cannot be placed in the same cell ( i. e. '
             'all ai are distinct) . Each air conditioner is characterized by '
             'one parameter: temperature. The i- th air conditioner is set to '
             'the temperature ti. Example of strip of length n= 6, where k= 2, '
             "a= [ 2, 5] and t= [ 14, 16] . For each cell i ( 1≤i≤n) find it' "
             's temperature, that can be calculated by the formula min1≤j≤k( '
             'tj+ | aj−i| ) , where | aj−i| denotes absolute value of the '
             'difference aj−i. In other words, the temperature in cell i is '
             'equal to the minimum among the temperatures of air conditioners, '
             "increased by the distance from it to the cell i. Let' s look at "
             'an example. Consider that n= 6, k= 2, the first air conditioner '
             'is placed in cell a1= 2 and is set to the temperature t1= 14 and '
             'the second air conditioner is placed in cell a2= 5 and is set to '
             'the temperature t2= 16. In that case temperatures in cells are: '
             'temperature in cell 1 is: min( 14+ | 2−1| , 16+ | 5−1| ) = min( '
             '14+ 1, 16+ 4) = min( 15, 20) = 15; temperature in cell 2 is: '
             'min( 14+ | 2−2| , 16+ | 5−2| ) = min( 14+ 0, 16+ 3) = min( 14, '
             '19) = 14; temperature in cell 3 is: min( 14+ | 2−3| , 16+ | 5−3| '
             ') = min( 14+ 1, 16+ 2) = min( 15, 18) = 15; temperature in cell '
             '4 is: min( 14+ | 2−4| , 16+ | 5−4| ) = min( 14+ 2, 16+ 1) = min( '
             '16, 17) = 16; temperature in cell 5 is: min( 14+ | 2−5| , 16+ | '
             '5−5| ) = min( 14+ 3, 16+ 0) = min( 17, 16) = 16; temperature in '
             'cell 6 is: min( 14+ | 2−6| , 16+ | 5−6| ) = min( 14+ 4, 16+ 1) = '
             'min( 18, 17) = 17. For each cell from 1 to n find the '
             'temperature in it.',
  'input': 'The first line contains one integer q ( 1≤q≤104) — the number of '
           'test cases in the input. Then test cases follow. Before each test '
           'case, there is an empty line. Each test case contains three lines. '
           'The first line contains two integers n ( 1≤n≤3⋅105) and k ( 1≤k≤n) '
           '— the length of the strip of land and the number of air '
           'conditioners respectively. The second line contains k integers a1, '
           'a2, . . . , ak ( 1≤ai≤n) — positions of air conditioners on the '
           'strip of land. The third line contains k integers t1, t2, . . . , '
           'tk ( 1≤ti≤109) — temperatures of air conditioners. It is '
           'guaranteed that the sum of n over all test cases does not exceed '
           '3⋅105.',
  'note': ' ',
  'output': 'For each test case output n integers separated by space: '
            'temperatures of air in cells.',
  'title': 'Air Conditioners',
  'topics': ['data structures',
             'dp',
             'implementation',
             'shortest paths',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1547/E'},
 {'history': 'There is a chessboard of size n by n. The square in the i- th '
             'row from top and j- th column from the left is labelled ( i, j) '
             '. Currently, Gregor has some pawns in the n- th row. There are '
             'also enemy pawns in the 1- st row. On one turn, Gregor moves one '
             'of his pawns. A pawn can move one square up ( from ( i, j) to ( '
             'i−1, j) ) if there is no pawn in the destination square. '
             'Additionally, a pawn can move one square diagonally up ( from ( '
             'i, j) to either ( i−1, j−1) or ( i−1, j+ 1) ) if and only if '
             'there is an enemy pawn in that square. The enemy pawn is also '
             'removed. Gregor wants to know what is the maximum number of his '
             'pawns that can reach row 1? Note that only Gregor takes turns in '
             "this game, and the enemy pawns never move. Also, when Gregor' s "
             'pawn reaches row 1, it is stuck and cannot make any further '
             'moves.',
  'input': 'The first line of the input contains one integer t ( 1≤t≤2⋅104) — '
           'the number of test cases. Then t test cases follow. Each test case '
           'consists of three lines. The first line contains a single integer '
           'n ( 2≤n≤2⋅105) — the size of the chessboard. The second line '
           'consists of a string of binary digits of length n, where a 1 in '
           'the i- th position corresponds to an enemy pawn in the i- th cell '
           'from the left, and 0 corresponds to an empty cell. The third line '
           'consists of a string of binary digits of length n, where a 1 in '
           "the i- th position corresponds to a Gregor' s pawn in the i- th "
           'cell from the left, and 0 corresponds to an empty cell. It is '
           'guaranteed that the sum of n across all test cases is less than '
           '2⋅105.',
  'note': 'In the first example, Gregor can simply advance all 3 of his pawns '
          'forward. Thus, the answer is 3. In the second example, Gregor can '
          'guarantee that all 4 of his pawns reach the enemy row, by following '
          'the colored paths as demonstrated in the diagram below. Remember, '
          'only Gregor takes turns in this " game" ! In the third example, '
          "Gregor' s only pawn is stuck behind the enemy pawn, and cannot "
          'reach the end. In the fourth example, Gregor has no pawns, so the '
          'answer is clearly 0.',
  'output': 'For each test case, print one integer: the maximum number of '
            "Gregor' s pawns which can reach the 1- st row.",
  'title': 'Gregor and the Pawn Game',
  'topics': ['dfs and similar',
             'dp',
             'flows',
             'graph matchings',
             'graphs',
             'greedy',
             'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1549/B'},
 {'history': "Suppose you have two points p= ( xp, yp) and q= ( xq, yq) . Let' "
             's denote the Manhattan distance between them as d( p, q) = | '
             "xp−xq| + | yp−yq| . Let' s say that three points p, q, r form a "
             "bad triple if d( p, r) = d( p, q) + d( q, r) . Let' s say that "
             'an array b1, b2, . . . , bm is good if it is impossible to '
             'choose three distinct indices i, j, k such that the points ( bi, '
             'i) , ( bj, j) and ( bk, k) form a bad triple. You are given an '
             'array a1, a2, . . . , an. Calculate the number of good subarrays '
             'of a. A subarray of the array a is the array al, al+ 1, . . . , '
             'ar for some 1≤l≤r≤n. Note that, according to the definition, '
             'subarrays of length 1 and 2 are good.',
  'input': 'The first line contains one integer t ( 1≤t≤5000) — the number of '
           'test cases. The first line of each test case contains one integer '
           'n ( 1≤n≤2⋅105) — the length of array a. The second line of each '
           "test case contains n integers a1, a2, . . . , an ( 1≤ai≤109) . It' "
           "s guaranteed that the sum of n doesn' t exceed 2⋅105.",
  'note': 'In the first test case, it can be proven that any subarray of a is '
          'good. For example, subarray [ a2, a3, a4] is good since it contains '
          'only three elements and: d( ( a2, 2) , ( a4, 4) ) = | 4−3| + | 2−4| '
          '= 3 < d( ( a2, 2) , ( a3, 3) ) + d( ( a3, 3) , ( a4, 4) ) = 3+ 1+ '
          '2+ 1= 7; d( ( a2, 2) , ( a3, 3) ) < d( ( a2, 2) , ( a4, 4) ) + d( ( '
          'a4, 4) , ( a3, 3) ) ; d( ( a3, 3) , ( a4, 4) ) < d( ( a3, 3) , ( '
          'a2, 2) ) + d( ( a2, 2) , ( a4, 4) ) ; In the second test case, for '
          'example, subarray [ a1, a2, a3, a4] is not good, since it contains '
          'a bad triple ( a1, 1) , ( a2, 2) , ( a4, 4) : d( ( a1, 1) , ( a4, '
          '4) ) = | 6−9| + | 1−4| = 6; d( ( a1, 1) , ( a2, 2) ) = | 6−9| + | '
          '1−2| = 4; d( ( a2, 2) , ( a4, 4) ) = | 9−9| + | 2−4| = 2; So, d( ( '
          'a1, 1) , ( a4, 4) ) = d( ( a1, 1) , ( a2, 2) ) + d( ( a2, 2) , ( '
          'a4, 4) ) .',
  'output': 'For each test case, print the number of good subarrays of array '
            'a.',
  'title': 'Manhattan Subarrays',
  'topics': ['brute force', 'geometry', 'greedy', 'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1550/C'},
 {'history': "Let' s call an integer array a1, a2, . . . , an good if ai= ̸i "
             'for each i. Let F( a) be the number of pairs ( i, j) ( 1≤i< j≤n) '
             "such that ai+ aj= i+ j. Let' s say that an array a1, a2, . . . , "
             'an is excellent if: a is good; l≤ai≤r for each i; F( a) is the '
             'maximum possible among all good arrays of size n. Given n, l and '
             'r, calculate the number of excellent arrays modulo 109+ 7.',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of test cases. The first and only line of each test case '
           'contains three integers n, l, and r ( 2≤n≤2⋅105; −109≤l≤1; '
           "n≤r≤109) . It' s guaranteed that the sum of n doesn' t exceed "
           '2⋅105.',
  'note': 'In the first test case, it can be proven that the maximum F( a) '
          'among all good arrays a is equal to 2. The excellent arrays are: [ '
          '2, 1, 2] ; [ 0, 3, 2] ; [ 2, 3, 2] ; [ 3, 0, 1] .',
  'output': 'For each test case, print the number of excellent arrays modulo '
            '109+ 7.',
  'title': 'Excellent Arrays',
  'topics': ['binary search',
             'combinatorics',
             'constructive algorithms',
             'implementation',
             'math',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1550/D'},
 {'history': 'You are given a string s of length n. Each character is either '
             'one of the first k lowercase Latin letters or a question mark. '
             'You are asked to replace every question mark with one of the '
             'first k lowercase Latin letters in such a way that the following '
             'value is maximized. Let fi be the maximum length substring of '
             'string s, which consists entirely of the i- th Latin letter. A '
             'substring of a string is a contiguous subsequence of that '
             "string. If the i- th letter doesn' t appear in a string, then fi "
             'is equal to 0. The value of a string s is the minimum value '
             'among fi for all i from 1 to k. What is the maximum value the '
             'string can have?',
  'input': 'The first line contains two integers n and k ( 1≤n≤2⋅105; 1≤k≤17) '
           '— the length of the string and the number of first Latin letters '
           'used. The second line contains a string s, consisting of n '
           'characters. Each character is either one of the first k lowercase '
           'Latin letters or a question mark.',
  'note': 'In the first example the question marks can be replaced in the '
          'following way: " aaaababbbb" . f1= 4, f2= 4, thus the answer is 4. '
          'Replacing it like this is also possible: " aaaabbbbbb" . That way '
          'f1= 4, f2= 6, however, the minimum of them is still 4. In the '
          'second example one of the possible strings is " aabbccdda" . In the '
          "third example at least one letter won' t appear in the string, "
          'thus, the minimum of values fi is always 0.',
  'output': 'Print a single integer — the maximum value of the string after '
            'every question mark is replaced with one of the first k lowercase '
            'Latin letters.',
  'title': 'Stringforces',
  'topics': ['binary search',
             'bitmasks',
             'brute force',
             'dp',
             'strings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1550/E'},
 {'history': 'This is a simplified version of the problem B2. Perhaps you '
             'should read the problem B2 before you start solving B1. Paul and '
             'Mary have a favorite string ss which consists of lowercase '
             'letters of the Latin alphabet. They want to paint it using '
             "pieces of chalk of two colors: red and green. Let' s call a "
             'coloring of a string wonderful if the following conditions are '
             'met: each letter of the string is either painted in exactly one '
             "color ( red or green) or isn' t painted; each two letters which "
             'are painted in the same color are different; the number of '
             'letters painted in red is equal to the number of letters painted '
             'in green; the number of painted letters of this coloring is '
             'maximum among all colorings of the string which meet the first '
             'three conditions. E. g. consider a string s equal to " kzaaa" . '
             'One of the wonderful colorings of the string is shown in the '
             'figure. The example of a wonderful coloring of the string " '
             'kzaaa" . Paul and Mary want to learn by themselves how to find a '
             'wonderful coloring of the string. But they are very young, so '
             'they need a hint. Help them find k — the number of red ( or '
             'green, these numbers are equal) letters in a wonderful coloring.',
  'input': 'The first line contains one integer t ( 1≤t≤1000) — the number of '
           'test cases. Then t test cases follow. Each test case consists of '
           'one non- empty string s which consists of lowercase letters of the '
           "Latin alphabet. The number of characters in the string doesn' t "
           'exceed 50.',
  'note': 'The first test case contains the string from the statement. One of '
          "the wonderful colorings is shown in the figure. There' s no "
          'wonderful coloring containing 3 or more red letters because the '
          "total number of painted symbols will exceed the string' s length. "
          'The string from the second test case can be painted as follows. '
          'Let\' s paint the first occurrence of each of the letters " c" , " '
          'o" , " e" in red and the second ones in green. Let\' s paint the '
          'letters " d" , " f" in red and " r" , " s" in green. So every '
          'letter will be painted in red or green, hence the answer better '
          "than 5 doesn' t exist. The third test case contains the string of "
          'distinct letters, so you can paint any set of characters in red, as '
          "long as the size of this set doesn' t exceed half of the size of "
          'the string and is the maximum possible. The fourth test case '
          'contains a single letter which cannot be painted in red because '
          'there will be no letter able to be painted in green. The fifth test '
          "case contains a string of identical letters, so there' s no way to "
          'paint more than one letter in red.',
  'output': 'For each test case, output a separate line containing one non- '
            'negative integer k — the number of letters which will be painted '
            'in red in a wonderful coloring.',
  'title': 'Wonderful Coloring - 1',
  'topics': ['greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1551/B1'},
 {'history': 'Stephen Queen wants to write a story. He is a very unusual '
             "writer, he uses only letters ' a' , ' b' , ' c' , ' d' and ' e' "
             '! To compose a story, Stephen wrote out n words consisting of '
             'the first 5 lowercase letters of the Latin alphabet. He wants to '
             'select the maximum number of words to make an interesting story. '
             'Let a story be a sequence of words that are not necessarily '
             'different. A story is called interesting if there exists a '
             'letter which occurs among all words of the story more times than '
             'all other letters together. For example, the story consisting of '
             'three words " bac" , " aaada" , " e" is interesting ( the letter '
             "' a' occurs 5 times, all other letters occur 4 times in total) . "
             'But the story consisting of two words " aba" , " abcde" is not ( '
             'no such letter that it occurs more than all other letters in '
             'total) . You are given a sequence of n words consisting of '
             "letters ' a' , ' b' , ' c' , ' d' and ' e' . Your task is to "
             'choose the maximum number of them to make an interesting story. '
             "If there' s no way to make a non- empty story, output 0.",
  'input': 'The first line contains one integer t ( 1≤t≤5000) — the number of '
           'test cases. Then t test cases follow. The first line of each test '
           'case contains one integer n ( 1≤n≤2⋅105) — the number of the words '
           'in the sequence. Then n lines follow, each of them contains a word '
           '— a non- empty string consisting of lowercase letters of the Latin '
           'alphabet. The words in the sequence may be non- distinct ( i. e. '
           "duplicates are allowed) . Only the letters ' a' , ' b' , ' c' , ' "
           "d' and ' e' may occur in the words. It is guaranteed that the sum "
           "of n over all test cases doesn' t exceed 2⋅105; the sum of the "
           "lengths of all words over all test cases doesn' t exceed 4⋅105.",
  'note': 'In the first test case of the example, all 3 words can be used to '
          'make an interesting story. The interesting story is " bac aaada e" '
          '. In the second test case of the example, the 1- st and the 3- rd '
          'words can be used to make an interesting story. The interesting '
          'story is " aba aba" . Stephen can\' t use all three words at the '
          "same time. In the third test case of the example, Stephen can' t "
          'make a non- empty interesting story. So the answer is 0. In the '
          'fourth test case of the example, Stephen can use the 3- rd and the '
          '4- th words to make an interesting story. The interesting story is '
          '" c bc" .',
  'output': 'For each test case, output the maximum number of words that '
            "compose an interesting story. Print 0 if there' s no way to make "
            'a non- empty interesting story.',
  'title': 'Interesting Story',
  'topics': ['greedy', 'sortings', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1551/C'},
 {'history': "The only difference between this problem and D1 is that you don' "
             't have to provide the way to construct the answer in D1, but you '
             "have to do it in this problem. There' s a table of n×m cells ( n "
             'rows and m columns) . The value of n⋅m is even. A domino is a '
             'figure that consists of two cells having a common side. It may '
             'be horizontal ( one of the cells is to the right of the other) '
             'or vertical ( one of the cells is above the other) . You need to '
             'place nm2 dominoes on the table so that exactly k of them are '
             'horizontal and all the other dominoes are vertical. The dominoes '
             'cannot overlap and must fill the whole table.',
  'input': 'The first line contains one integer t ( 1≤t≤10) — the number of '
           'test cases. Then t test cases follow. Each test case consists of a '
           'single line. The line contains three integers n, m, k ( 1≤n, '
           'm≤100, 0≤k≤nm2, n⋅m is even) — the count of rows, columns and '
           'horizontal dominoes, respectively.',
  'note': ' ',
  'output': 'For each test case: print " NO" if it\' s not possible to place '
            'the dominoes on the table in the described way; otherwise, print '
            '" YES" on a separate line, then print n lines so that each of '
            'them contains m lowercase letters of the Latin alphabet — the '
            'layout of the dominoes on the table. Each cell of the table must '
            'be marked by the letter so that for every two cells having a '
            'common side, they are marked by the same letters if and only if '
            'they are occupied by the same domino. I. e. both cells of the '
            'same domino must be marked with the same letter, but two dominoes '
            'that share a side must be marked with different letters. If there '
            'are multiple solutions, print any of them.',
  'title': 'Domino (hard version)',
  'topics': ['constructive algorithms', 'implementation', 'math'],
  'url': 'https://codeforces.com/problemset/problem/1551/D2'},
 {'history': 'A string s of length n, consisting of lowercase letters of the '
             'English alphabet, is given. You must choose some number k '
             'between 0 and n. Then, you select k characters of s and permute '
             'them however you want. In this process, the positions of the '
             'other n−k characters remain unchanged. You have to perform this '
             'operation exactly once. For example, if s= " andrea" , you can '
             'choose the k= 4 characters " a_ d_ ea" and permute them into " '
             'd_ e_ aa" so that after the operation the string becomes " '
             'dneraa" . Determine the minimum k so that it is possible to sort '
             's alphabetically ( that is, after the operation its characters '
             'appear in alphabetical order) .',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of test cases. Then t test cases follow. The first line of '
           'each test case contains one integer n ( 1≤n≤40) — the length of '
           'the string. The second line of each test case contains the string '
           's. It is guaranteed that s contains only lowercase letters of the '
           'English alphabet.',
  'note': 'In the first test case, we can choose the k= 2 characters " _ ol" '
          'and rearrange them as " _ lo" ( so the resulting string is " llo" ) '
          '. It is not possible to sort the string choosing strictly less than '
          '2 characters. In the second test case, one possible way to sort s '
          'is to consider the k= 6 characters " _ o_ _ force_ " and rearrange '
          'them as " _ c_ _ efoor_ " ( so the resulting string is " '
          'ccdeefoors" ) . One can show that it is not possible to sort the '
          'string choosing strictly less than 6 characters. In the third test '
          'case, string s is already sorted ( so we can choose k= 0 '
          'characters) . In the fourth test case, we can choose all k= 4 '
          'characters " dcba" and reverse the whole string ( so the resulting '
          'string is " abcd" ) .',
  'output': 'For each test case, output the minimum k that allows you to '
            'obtain a string sorted alphabetically, through the operation '
            'described above.',
  'title': 'Subsequence Permutation',
  'topics': ['sortings', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1552/A'},
 {'history': 'The Olympic Games have just started and Federico is eager to '
             'watch the marathon race. There will be n athletes, numbered from '
             '1 to n, competing in the marathon, and all of them have taken '
             'part in 5 important marathons, numbered from 1 to 5, in the '
             'past. For each 1≤i≤n and 1≤j≤5, Federico remembers that athlete '
             'i ranked ri, j- th in marathon j ( e. g. , r2, 4= 3 means that '
             'athlete 2 was third in marathon 4) . Federico considers athlete '
             'x superior to athlete y if athlete x ranked better than athlete '
             'y in at least 3 past marathons, i. e. , rx, j< ry, j for at '
             'least 3 distinct values of j. Federico believes that an athlete '
             'is likely to get the gold medal at the Olympics if he is '
             'superior to all other athletes. Find any athlete who is likely '
             'to get the gold medal ( that is, an athlete who is superior to '
             'all other athletes) , or determine that there is no such '
             'athlete.',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of test cases. Then t test cases follow. The first line of '
           'each test case contains a single integer n ( 1≤n≤50000) — the '
           'number of athletes. Then n lines follow, each describing the '
           'ranking positions of one athlete. The i- th of these lines '
           'contains the 5 integers ri, 1, ri, 2, ri, 3, ri, 4, ri, 5 ( 1≤ri, '
           'j≤50000) — the ranking positions of athlete i in the past 5 '
           'marathons. It is guaranteed that, in each of the 5 past marathons, '
           'the n athletes have distinct ranking positions, i. e. , for each '
           '1≤j≤5, the n values r1, j, r2, j, . . . , rn, j are distinct. It '
           'is guaranteed that the sum of n over all test cases does not '
           'exceed 50000.',
  'note': 'Explanation of the first test case: There is only one athlete, '
          'therefore he is superior to everyone else ( since there is no one '
          'else) , and thus he is likely to get the gold medal. Explanation of '
          'the second test case: There are n= 3 athletes. Athlete 1 is '
          'superior to athlete 2. Indeed athlete 1 ranks better than athlete 2 '
          'in the marathons 1, 2 and 3. Athlete 2 is superior to athlete 3. '
          'Indeed athlete 2 ranks better than athlete 3 in the marathons 1, 2, '
          '4 and 5. Athlete 3 is superior to athlete 1. Indeed athlete 3 ranks '
          'better than athlete 1 in the marathons 3, 4 and 5. Explanation of '
          'the third test case: There are n= 3 athletes. Athlete 1 is superior '
          'to athletes 2 and 3. Since he is superior to all other athletes, he '
          'is likely to get the gold medal. Athlete 2 is superior to athlete '
          '3. Athlete 3 is not superior to any other athlete. Explanation of '
          'the fourth test case: There are n= 6 athletes. Athlete 1 is '
          'superior to athletes 3, 4, 6. Athlete 2 is superior to athletes 1, '
          '4, 6. Athlete 3 is superior to athletes 2, 4, 6. Athlete 4 is not '
          'superior to any other athlete. Athlete 5 is superior to athletes 1, '
          '2, 3, 4, 6. Since he is superior to all other athletes, he is '
          'likely to get the gold medal. Athlete 6 is only superior to athlete '
          '4.',
  'output': 'For each test case, print a single integer — the number of an '
            'athlete who is likely to get the gold medal ( that is, an athlete '
            'who is superior to all other athletes) . If there are no such '
            'athletes, print −1. If there is more than such one athlete, print '
            'any of them.',
  'title': 'Running for Gold',
  'topics': ['combinatorics', 'graphs', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1552/B'},
 {'history': 'On a circle lie 2n2n distinct points, with the following '
             'property: however you choose 33 chords that connect 33 disjoint '
             'pairs of points, no point strictly inside the circle belongs to '
             'all 33 chords. The points are numbered 1, 2, . . . , 2n1, 2, . . '
             '. , 2n in clockwise order. Initially, kk chords connect kk pairs '
             'of points, in such a way that all the 2k2k endpoints of these '
             'chords are distinct. You want to draw n−kn−k additional chords '
             'that connect the remaining 2( n−k) 2( n−k) points ( each point '
             'must be an endpoint of exactly one chord) . In the end, let xx '
             'be the total number of intersections among all nn chords. '
             'Compute the maximum value that xx can attain if you choose the '
             'n−kn−k chords optimally. Note that the exact position of the '
             '2n2n points is not relevant, as long as the property stated in '
             'the first paragraph holds.',
  'input': 'The first line contains a single integer tt ( 1≤t≤1001≤t≤100) — '
           'the number of test cases. Then tt test cases follow. The first '
           'line of each test case contains two integers nn and kk ( '
           '1≤n≤1001≤n≤100, 0≤k≤n0≤k≤n) — half the number of points and the '
           'number of chords initially drawn. Then kk lines follow. The ii- th '
           'of them contains two integers xixi and yiyi ( 1≤xi, yi≤2n1≤xi, '
           'yi≤2n, xi= ̸yixi= ̸yi) — the endpoints of the ii- th chord. It is '
           'guaranteed that the 2k2k numbers x1, y1, x2, y2, . . . , xk, ykx1, '
           'y1, x2, y2, . . . , xk, yk are all distinct.',
  'note': 'In the first test case, there are three ways to draw the 22 '
          'additional chords, shown below ( black chords are the ones '
          'initially drawn, while red chords are the new ones) : We see that '
          'the third way gives the maximum number of intersections, namely 44. '
          'In the second test case, there are no more chords to draw. Of '
          'course, with only one chord present there are no intersections. In '
          'the third test case, we can make at most one intersection by '
          'drawing chords 1−31−3 and 2−42−4, as shown below:',
  'output': 'For each test case, output the maximum number of intersections '
            'that can be obtained by drawing n−kn−k additional chords.',
  'title': 'Maximize the Intersections',
  'topics': ['combinatorics',
             'constructive algorithms',
             'geometry',
             'greedy',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1552/C'},
 {'history': 'The numbers 1, 2, . . . , n⋅k1, 2, . . . , n⋅k are colored with '
             'nn colors. These colors are indexed by 1, 2, . . . , n1, 2, . . '
             '. , n. For each 1≤i≤n1≤i≤n, there are exactly kk numbers colored '
             'with color ii. Let [ a, b] [ a, b] denote the interval of '
             'integers between aa and bb inclusive, that is, the set a, a+ 1, '
             '. . . , ba, a+ 1, . . . , b. You must choose nn intervals [ a1, '
             'b1] , [ a2, b2] , . . . , [ an, bn] [ a1, b1] , [ a2, b2] , . . '
             '. , [ an, bn] such that: for each 1≤i≤n1≤i≤n, it holds 1≤ai< '
             'bi≤n⋅k1≤ai< bi≤n⋅k; for each 1≤i≤n1≤i≤n, the numbers aiai and '
             'bibi are colored with color ii; each number 1≤x≤n⋅k1≤x≤n⋅k '
             'belongs to at most ⌈nk−1⌉⌈nk−1⌉ intervals. One can show that '
             'such a family of intervals always exists under the given '
             'constraints.',
  'input': 'The first line contains two integers nn and kk ( 1≤n≤1001≤n≤100, '
           '2≤k≤1002≤k≤100) — the number of colors and the number of '
           'occurrences of each color. The second line contains n⋅kn⋅k '
           'integers c1, c2, . . . , cnkc1, c2, . . . , cnk ( 1≤cj≤n1≤cj≤n) , '
           'where cjcj is the color of number jj. It is guaranteed that, for '
           'each 1≤i≤n1≤i≤n, it holds cj= icj= i for exactly kk distinct '
           'indices jj.',
  'note': 'In the first sample, each number can be contained in at most '
          '⌈43−1⌉= 2⌈43−1⌉= 2 intervals. The output is described by the '
          'following picture: In the second sample, the only interval to be '
          'chosen is forced to be [ 1, 2] [ 1, 2] , and each number is indeed '
          'contained in at most ⌈12−1⌉= 1⌈12−1⌉= 1 interval. In the third '
          'sample, each number can be contained in at most ⌈33−1⌉= 2⌈33−1⌉= 2 '
          'intervals. The output is described by the following picture:',
  'output': 'Output nn lines. The ii- th line should contain the two integers '
            'aiai and bibi. If there are multiple valid choices of the '
            'intervals, output any.',
  'title': 'Colors and Intervals',
  'topics': ['constructive algorithms',
             'data structures',
             'greedy',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1552/E'},
 {'history': 'An ant moves on the real line with constant speed of 1 unit per '
             'second. It starts at 0 and always moves to the right ( so its '
             'position increases by 1 each second) . There are n portals, the '
             'i- th of which is located at position xi and teleports to '
             'position yi< xi. Each portal can be either active or inactive. '
             'The initial state of the i- th portal is determined by si: if '
             'si= 0 then the i- th portal is initially inactive, if si= 1 then '
             'the i- th portal is initially active. When the ant travels '
             'through a portal ( i. e. , when its position coincides with the '
             'position of a portal) : if the portal is inactive, it becomes '
             'active ( in this case the path of the ant is not affected) ; if '
             'the portal is active, it becomes inactive and the ant is '
             'instantly teleported to the position yi, where it keeps on '
             'moving as normal. How long ( from the instant it starts moving) '
             'does it take for the ant to reach the position xn+ 1? It can be '
             'shown that this happens in a finite amount of time. Since the '
             'answer may be very large, compute it modulo 998244353.',
  'input': 'The first line contains the integer n ( 1≤n≤2⋅105) — the number of '
           'portals. The i- th of the next n lines contains three integers xi, '
           'yi and si ( 1≤yi< xi≤109, si∈0, 1) — the position of the i- th '
           'portal, the position where the ant is teleported when it travels '
           'through the i- th portal ( if it is active) , and the initial '
           'state of the i- th portal. The positions of the portals are '
           'strictly increasing, that is x1< x2< ⋯< xn. It is guaranteed that '
           'the 2n integers x1, x2, . . . , xn, y1, y2, . . . , yn are all '
           'distinct.',
  'note': 'Explanation of the first sample: The ant moves as follows ( a curvy '
          'arrow denotes a teleporting, a straight arrow denotes normal '
          'movement with speed 1 and the time spent during the movement is '
          'written above the arrow) . 06⟶6⇝53⟶8⇝12⟶3⇝24⟶6⇝52⟶7⇝42⟶6⇝54⟶9 '
          'Notice that the total time is 6+ 3+ 2+ 4+ 2+ 2+ 4= 23. Explanation '
          'of the second sample: The ant moves as follows ( a curvy arrow '
          'denotes a teleporting, a straight arrow denotes normal movement '
          'with speed 1 and the time spent during the movement is written '
          'above the arrow) . 0454971987⟶454971987⇝40687490248097086⟶454971988 '
          'Notice that the total time is 454971987+ 48097086= 503069073. '
          'Explanation of the third sample: Since all portals are initially '
          'off, the ant will not be teleported and will go straight from 0 to '
          'xn+ 1= 899754846+ 1= 899754847.',
  'output': 'Output the amount of time elapsed, in seconds, from the instant '
            'the ant starts moving to the instant it reaches the position xn+ '
            '1. Since the answer may be very large, output it modulo '
            '998244353.',
  'title': 'Telepanting',
  'topics': ['binary search', 'data structures', 'dp', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1552/F'},
 {'history': 'Andrea has come up with what he believes to be a novel sorting '
             'algorithm for arrays of length n. The algorithm works as '
             'follows. Initially there is an array of n integers a1, a2, . . . '
             ', an. Then, k steps are executed. For each 1≤i≤k, during the i- '
             'th step the subsequence of the array a with indexes ji, 1< ji, '
             '2< ⋯< ji, qi is sorted, without changing the values with the '
             'remaining indexes. So, the subsequence aji, 1, aji, 2, . . . , '
             'aji, qi is sorted and all other elements of a are left '
             'untouched. Andrea, being eager to share his discovery with the '
             'academic community, sent a short paper describing his algorithm '
             'to the journal " Annals of Sorting Algorithms" and you are the '
             'referee of the paper ( that is, the person who must judge the '
             "correctness of the paper) . You must decide whether Andrea' s "
             'algorithm is correct, that is, if it sorts any array a of n '
             'integers.',
  'input': 'The first line contains two integers n and k ( 1≤n≤40, 0≤k≤10) — '
           "the length of the arrays handled by Andrea' s algorithm and the "
           "number of steps of Andrea' s algorithm. Then k lines follow, each "
           "describing the subsequence considered in a step of Andrea' s "
           'algorithm. The i- th of these lines contains the integer qi ( '
           '1≤qi≤n) followed by qi integers ji, 1, ji, 2, . . . , ji, qi ( '
           '1≤ji, 1< ji, 2< ⋯< ji, qi≤n) — the length of the subsequence '
           'considered in the i- th step and the indexes of the subsequence.',
  'note': 'Explanation of the first sample: The algorithm consists of 3 steps. '
          'The first one sorts the subsequence [ a1, a2, a3] , the second one '
          'sorts the subsequence [ a2, a3, a4] , the third one sorts the '
          'subsequence [ a1, a2] . For example, if initially a= [ 6, 5, 6, 3] '
          ', the algorithm transforms the array as follows ( the subsequence '
          'that gets sorted is highlighted in red) [ 6, 5, 6, 3] →[ 5, 6, 6, '
          '3] →[ 5, 3, 6, 6] →[ 3, 5, 6, 6] . One can prove that, for any '
          'initial array a, at the end of the algorithm the array a will be '
          'sorted. Explanation of the second sample: The algorithm consists of '
          '3 steps. The first one sorts the subsequence [ a1, a2, a3] , the '
          'second one sorts the subsequence [ a2, a3, a4] , the third one '
          'sorts the subsequence [ a1, a3, a4] . For example, if initially a= '
          '[ 6, 5, 6, 3] , the algorithm transforms the array as follows ( the '
          'subsequence that gets sorted is highlighted in red) [ 6, 5, 6, 3] '
          '→[ 5, 6, 6, 3] →[ 5, 3, 6, 6] →[ 5, 3, 6, 6] . Notice that a= [ 6, '
          '5, 6, 3] is an example of an array that is not sorted by the '
          'algorithm. Explanation of the third sample: The algorithm consists '
          'of 4 steps. The first 3 steps do nothing because they sort '
          'subsequences of length 1, whereas the fourth step sorts the '
          'subsequence [ a1, a3] . For example, if initially a= [ 5, 6, 4] , '
          'the algorithm transforms the array as follows ( the subsequence '
          'that gets sorted is highlighted in red) [ 5, 6, 4] →[ 5, 6, 4] →[ '
          '5, 6, 4] →[ 5, 6, 4] →[ 4, 6, 5] . Notice that a= [ 5, 6, 4] is an '
          'example of an array that is not sorted by the algorithm. '
          'Explanation of the fourth sample: The algorithm consists of 2 '
          'steps. The first step sorts the subsequences [ a2, a3, a4] , the '
          'second step sorts the whole array [ a1, a2, a3, a4, a5] . For '
          'example, if initially a= [ 9, 8, 1, 1, 1] , the algorithm '
          'transforms the array as follows ( the subsequence that gets sorted '
          'is highlighted in red) [ 9, 8, 1, 1, 1] →[ 9, 1, 1, 8, 1] →[ 1, 1, '
          '1, 8, 9] . Since in the last step the whole array is sorted, it is '
          'clear that, for any initial array a, at the end of the algorithm '
          'the array a will be sorted.',
  'output': "If Andrea' s algorithm is correct print ACCEPTED, otherwise print "
            'REJECTED.',
  'title': 'A Serious Referee',
  'topics': ['bitmasks', 'brute force', 'dfs and similar', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1552/G'},
 {'history': 'You have a string s and a chip, which you can place onto any '
             'character of this string. After placing the chip, you move it to '
             'the right several ( maybe zero) times, i. e. you perform the '
             'following operation several times: if the current position of '
             'the chip is i, you move it to the position i+ 1. Of course, '
             'moving the chip to the right is impossible if it is already in '
             'the last position. After moving the chip to the right, you move '
             'it to the left several ( maybe zero) times, i. e. you perform '
             'the following operation several times: if the current position '
             'of the chip is i, you move it to the position i−1. Of course, '
             'moving the chip to the left is impossible if it is already in '
             'the first position. When you place a chip or move it, you write '
             'down the character where the chip ends up after your action. For '
             'example, if s is abcdef, you place the chip onto the 3- rd '
             'character, move it to the right 2 times and then move it to the '
             'left 3 times, you write down the string cdedcb. You are given '
             "two strings s and t. Your task is to determine whether it' s "
             'possible to perform the described operations with s so that you '
             'write down the string t as a result.',
  'input': 'The first line contains one integer q ( 1≤q≤500) — the number of '
           'test cases. Each test case consists of two lines. The first line '
           'contains the string s ( 1≤| s| ≤500) , the second line contains '
           'the string t ( 1≤| t| ≤2⋅| s| −1) . Both strings consist of '
           'lowercase English characters. It is guaranteed that the sum of | '
           's| over all test cases does not exceed 500.',
  'note': 'Consider the examples. The first test case is described in the '
          'statement. In the second test case, you can place the chip on the '
          '1- st position, move it twice to the right, and then move it twice '
          'to the left. In the fourth test case, you can place the chip on the '
          "2- nd position, and then don' t move it at all. In the fifth test "
          'case, you can place the chip on the 1- st position, move it 5 times '
          'to the right, and then finish the process.',
  'output': 'For each test case, print " YES" if you can obtain the string t '
            'by performing the process mentioned in the statement with the '
            'string s, or " NO" if you cannot. You may print each letter in '
            'any case ( YES, yes, Yes will all be recognized as positive '
            'answer, NO, no and nO will all be recognized as negative answer) '
            '.',
  'title': 'Reverse String',
  'topics': ['brute force', 'dp', 'hashing', 'implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1553/B'},
 {'history': 'You are given two strings s and t, both consisting of lowercase '
             'English letters. You are going to type the string s character by '
             'character, from the first character to the last one. When typing '
             'a character, instead of pressing the button corresponding to it, '
             'you can press the " Backspace" button. It deletes the last '
             "character you have typed among those that aren' t deleted yet ( "
             'or does nothing if there are no characters in the current '
             'string) . For example, if s is " abcbd" and you press Backspace '
             'instead of typing the first and the fourth characters, you will '
             'get the string " bd" ( the first press of Backspace deletes no '
             "character, and the second press deletes the character ' c' ) . "
             'Another example, if s is " abcaa" and you press Backspace '
             'instead of the last two letters, then the resulting text is " a" '
             '. Your task is to determine whether you can obtain the string t, '
             'if you type the string s and press " Backspace" instead of '
             'typing several ( maybe zero) characters of s.',
  'input': 'The first line contains a single integer q ( 1≤q≤105) — the number '
           'of test cases. The first line of each test case contains the '
           'string s ( 1≤| s| ≤105) . Each character of s is a lowercase '
           'English letter. The second line of each test case contains the '
           'string t ( 1≤| t| ≤105) . Each character of t is a lowercase '
           'English letter. It is guaranteed that the total number of '
           'characters in the strings over all test cases does not exceed '
           '2⋅105.',
  'note': 'Consider the example test from the statement. In order to obtain " '
          'ba" from " ababa" , you may press Backspace instead of typing the '
          'first and the fourth characters. There\' s no way to obtain " bb" '
          'while typing " ababa" . There\' s no way to obtain " aaaa" while '
          'typing " aaa" . In order to obtain " ababa" while typing " aababa" '
          ', you have to press Backspace instead of typing the first '
          'character, then type all the remaining characters.',
  'output': 'For each test case, print " YES" if you can obtain the string t '
            'by typing the string s and replacing some characters with presses '
            'of " Backspace" button, or " NO" if you cannot. You may print '
            'each letter in any case ( YES, yes, Yes will all be recognized as '
            'positive answer, NO, no and nO will all be recognized as negative '
            'answer) .',
  'title': 'Backspace',
  'topics': ['dp', 'greedy', 'strings', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1553/D'},
 {'history': 'You are given two integers n and m. Find the MEX of the sequence '
             'n⊕0, n⊕1, . . . , n⊕m. Here, ⊕ is the bitwise XOR operator. MEX '
             'of the sequence of non- negative integers is the smallest non- '
             "negative integer that doesn' t appear in this sequence. For "
             'example, MEX( 0, 1, 2, 4) = 3, and MEX( 1, 2021) = 0.',
  'input': 'The first line contains a single integer t ( 1≤t≤30000) — the '
           'number of test cases. The first and only line of each test case '
           'contains two integers n and m ( 0≤n, m≤109) .',
  'note': 'In the first test case, the sequence is 3⊕0, 3⊕1, 3⊕2, 3⊕3, 3⊕4, '
          '3⊕5, or 3, 2, 1, 0, 7, 6. The smallest non- negative integer which '
          "isn' t present in the sequence i. e. the MEX of the sequence is 4. "
          'In the second test case, the sequence is 4⊕0, 4⊕1, 4⊕2, 4⊕3, 4⊕4, '
          '4⊕5, 4⊕6, or 4, 5, 6, 7, 0, 1, 2. The smallest non- negative '
          "integer which isn' t present in the sequence i. e. the MEX of the "
          'sequence is 3. In the third test case, the sequence is 3⊕0, 3⊕1, '
          "3⊕2, or 3, 2, 1. The smallest non- negative integer which isn' t "
          'present in the sequence i. e. the MEX of the sequence is 0.',
  'output': 'For each test case, print a single integer — the answer to the '
            'problem.',
  'title': 'Mikasa',
  'topics': ['binary search', 'bitmasks', 'greedy', 'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1554/C'},
 {'history': 'You are given an integer n. Find any string s of length n '
             'consisting only of English lowercase letters such that each non- '
             'empty substring of s occurs in s an odd number of times. If '
             'there are multiple such strings, output any. It can be shown '
             'that such string always exists under the given constraints. A '
             'string a is a substring of a string b if a can be obtained from '
             'b by deletion of several ( possibly, zero or all) characters '
             'from the beginning and several ( possibly, zero or all) '
             'characters from the end.',
  'input': 'The first line contains a single integer t ( 1≤t≤500) — the number '
           'of test cases. The first line of each test case contains a single '
           'integer n ( 1≤n≤105) . It is guaranteed that the sum of n over all '
           "test cases doesn' t exceed 3⋅105.",
  'note': 'In the first test case, each substring of " abc" occurs exactly '
          'once. In the third test case, each substring of " bbcaabbba" occurs '
          'an odd number of times. In particular, " b" occurs 5 times, " a" '
          'and " bb" occur 3 times each, and each of the remaining substrings '
          'occurs exactly once.',
  'output': 'For each test case, print a single line containing the string s. '
            'If there are multiple such strings, output any. It can be shown '
            'that such string always exists under the given constraints.',
  'title': 'Diane',
  'topics': ['constructive algorithms', 'greedy', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1554/D'},
 {'history': 'Alice and Bob are playing a game on a matrix, consisting of 22 '
             'rows and mm columns. The cell in the ii- th row in the jj- th '
             'column contains ai, jai, j coins in it. Initially, both Alice '
             'and Bob are standing in a cell ( 1, 1) ( 1, 1) . They are going '
             'to perform a sequence of moves to reach a cell ( 2, m) ( 2, m) . '
             'The possible moves are: Move right — from some cell ( x, y) ( x, '
             'y) to ( x, y+ 1) ( x, y+ 1) ; Move down — from some cell ( x, y) '
             '( x, y) to ( x+ 1, y) ( x+ 1, y) . First, Alice makes all her '
             'moves until she reaches ( 2, m) ( 2, m) . She collects the coins '
             'in all cells she visit ( including the starting cell) . When '
             'Alice finishes, Bob starts his journey. He also performs the '
             'moves to reach ( 2, m) ( 2, m) and collects the coins in all '
             "cells that he visited, but Alice didn' t. The score of the game "
             'is the total number of coins Bob collects. Alice wants to '
             'minimize the score. Bob wants to maximize the score. What will '
             'the score of the game be if both players play optimally?',
  'input': 'The first line contains a single integer tt ( 1≤t≤1041≤t≤104) — '
           'the number of testcases. Then the descriptions of tt testcases '
           'follow. The first line of the testcase contains a single integer '
           'mm ( 1≤m≤1051≤m≤105) — the number of columns of the matrix. The '
           'ii- th of the next 22 lines contain mm integers ai, 1, ai, 2, . . '
           '. , ai, mai, 1, ai, 2, . . . , ai, m ( 1≤ai, j≤1041≤ai, j≤104) — '
           'the number of coins in the cell in the ii- th row in the jj- th '
           "column of the matrix. The sum of mm over all testcases doesn' t "
           'exceed 105105.',
  'note': 'The paths for the testcases are shown on the following pictures. '
          "Alice' s path is depicted in red and Bob' s path is depicted in "
          'blue.',
  'output': 'For each testcase print a single integer — the score of the game '
            'if both players play optimally.',
  'title': 'Coin Rows',
  'topics': ['brute force', 'constructive algorithms', 'dp', 'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1555/C'},
 {'history': "Let' s call the string beautiful if it does not contain a "
             'substring of length at least 2, which is a palindrome. Recall '
             'that a palindrome is a string that reads the same way from the '
             'first character to the last and from the last character to the '
             'first. For example, the strings a, bab, acca, bcabcbacb are '
             "palindromes, but the strings ab, abbbaa, cccb are not. Let' s "
             'define cost of a string as the minimum number of operations so '
             'that the string becomes beautiful, if in one operation it is '
             'allowed to change any character of the string to one of the '
             'first 3 letters of the Latin alphabet ( in lowercase) . You are '
             'given a string s of length n, each character of the string is '
             'one of the first 3 letters of the Latin alphabet ( in lowercase) '
             '. You have to answer m queries — calculate the cost of the '
             'substring of the string s from li- th to ri- th position, '
             'inclusive.',
  'input': 'The first line contains two integers n and m ( 1≤n, m≤2⋅105) — the '
           'length of the string s and the number of queries. The second line '
           'contains the string s, it consists of n characters, each character '
           'one of the first 3 Latin letters. The following m lines contain '
           'two integers li and ri ( 1≤li≤ri≤n) — parameters of the i- th '
           'query.',
  'note': 'Consider the queries of the example test. in the first query, the '
          'substring is baa, which can be changed to bac in one operation; in '
          'the second query, the substring is baacb, which can be changed to '
          'cbacb in two operations; in the third query, the substring is cb, '
          'which can be left unchanged; in the fourth query, the substring is '
          'aa, which can be changed to ba in one operation.',
  'output': 'For each query, print a single integer — the cost of the '
            'substring of the string s from li- th to ri- th position, '
            'inclusive.',
  'title': 'Say No to Palindromes',
  'topics': ['brute force', 'constructive algorithms', 'dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1555/D'},
 {'history': 'You are given n segments on a number line, numbered from 1 to n. '
             'The i- th segments covers all integer points from li to ri and '
             'has a value wi. You are asked to select a subset of these '
             'segments ( possibly, all of them) . Once the subset is selected, '
             "it' s possible to travel between two integer points if there "
             'exists a selected segment that covers both of them. A subset is '
             "good if it' s possible to reach point m starting from point 1 in "
             'arbitrary number of moves. The cost of the subset is the '
             'difference between the maximum and the minimum values of '
             'segments in it. Find the minimum cost of a good subset. In every '
             'test there exists at least one good subset.',
  'input': 'The first line contains two integers n and m ( 1≤n≤3⋅105; 2≤m≤106) '
           '— the number of segments and the number of integer points. Each of '
           'the next n lines contains three integers li, ri and wi ( 1≤li< '
           'ri≤m; 1≤wi≤106) — the description of the i- th segment. In every '
           'test there exists at least one good subset.',
  'note': ' ',
  'output': 'Print a single integer — the minimum cost of a good subset.',
  'title': 'Boring Segments',
  'topics': ['data structures', 'sortings', 'trees', 'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1555/E'},
 {'history': 'William has an array of nn integers a1, a2, . . . , ana1, a2, . '
             '. . , an. In one move he can swap two neighboring items. Two '
             'items aiai and ajaj are considered neighboring if the condition '
             '| i−j| = 1| i−j| = 1 is satisfied. William wants you to '
             'calculate the minimal number of swaps he would need to perform '
             'to make it so that the array does not contain two neighboring '
             'items with the same parity.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases tt ( 1≤t≤1041≤t≤104) . Description of the '
           'test cases follows. The first line of each test case contains an '
           'integer nn ( 1≤n≤105) ( 1≤n≤105) which is the total number of '
           "items in William' s array. The second line contains nn integers "
           'a1, a2, . . . , ana1, a2, . . . , an ( 1≤ai≤109) ( 1≤ai≤109) which '
           "are William' s array. It is guaranteed that the sum of nn over all "
           'test cases does not exceed 105105.',
  'note': 'In the first test case the following sequence of operations would '
          'satisfy the requirements: swap( 2, 3) . Array after performing the '
          'operation: [ 6, 1, 6] [ 6, 1, 6] In the second test case the array '
          'initially does not contain two neighboring items of the same '
          'parity. In the third test case the following sequence of operations '
          'would satisfy the requirements: swap( 3, 4) . Array after '
          'performing the operation: [ 1, 1, 2, 1, 2, 2] [ 1, 1, 2, 1, 2, 2] '
          'swap( 2, 3) . Array after performing the operation: [ 1, 2, 1, 1, '
          '2, 2] [ 1, 2, 1, 1, 2, 2] swap( 4, 5) . Array after performing the '
          'operation: [ 1, 2, 1, 2, 1, 2] [ 1, 2, 1, 2, 1, 2] In the fourth '
          'test case it is impossible to satisfy the requirements. In the '
          'fifth test case the following sequence of operations would satisfy '
          'the requirements: swap( 2, 3) . Array after performing the '
          'operation: [ 6, 3, 2, 4, 5, 1] [ 6, 3, 2, 4, 5, 1] swap( 4, 5) . '
          'Array after performing the operation: [ 6, 3, 2, 5, 4, 1] [ 6, 3, '
          '2, 5, 4, 1]',
  'output': 'For each test case output the minimal number of operations needed '
            'or −1−1 if it is impossible to get the array to a state when no '
            'neighboring numbers have the same parity.',
  'title': 'Take Your Places!',
  'topics': ['implementation'],
  'url': 'https://codeforces.com/problemset/problem/1556/B'},
 {'history': 'William has a favorite bracket sequence. Since his favorite '
             'sequence is quite big he provided it to you as a sequence of '
             'positive integers c1, c2, . . . , cnc1, c2, . . . , cn where '
             'cici is the number of consecutive brackets " ( " if ii is an odd '
             'number or the number of consecutive brackets " ) " if ii is an '
             'even number. For example for a bracket sequence " ( ( ( ) ) ( ) '
             ') ) " a corresponding sequence of numbers is [ 3, 2, 1, 3] [ 3, '
             '2, 1, 3] . You need to find the total number of continuous '
             'subsequences ( subsegments) [ l, r] [ l, r] ( l≤rl≤r) of the '
             'original bracket sequence, which are regular bracket sequences. '
             'A bracket sequence is called regular if it is possible to obtain '
             'correct arithmetic expression by inserting characters " + " and '
             '" 1" into this sequence. For example, sequences " ( ( ) ) ( ) " '
             ', " ( ) " and " ( ( ) ( ( ) ) ) " are regular, while " ) ( " , " '
             '( ( ) " and " ( ( ) ) ) ( " are not.',
  'input': 'The first line contains a single integer nn ( 1≤n≤1000) ( '
           '1≤n≤1000) , the size of the compressed sequence. The second line '
           'contains a sequence of integers c1, c2, . . . , cnc1, c2, . . . , '
           'cn ( 1≤ci≤109) ( 1≤ci≤109) , the compressed sequence.',
  'note': 'In the first example a sequence ( ( ( ( ) ( ( ) ) ) ( is described. '
          'This bracket sequence contains 55 subsegments which form regular '
          'bracket sequences: Subsequence from the 33rd to 1010th character: ( '
          '( ) ( ( ) ) ) Subsequence from the 44th to 55th character: ( ) '
          'Subsequence from the 44th to 99th character: ( ) ( ( ) ) '
          'Subsequence from the 66th to 99th character: ( ( ) ) Subsequence '
          'from the 77th to 88th character: ( ) In the second example a '
          'sequence ( ) ) ) ( ( ) ( ( ) ) ) ) is described. In the third '
          'example a sequence ( ) ( ) ( ( ) ) is described.',
  'output': 'Output a single integer — the total number of subsegments of the '
            'original bracket sequence, which are regular bracket sequences. '
            'It can be proved that the answer fits in the signed 64- bit '
            'integer data type.',
  'title': 'Compressed Bracket Sequence',
  'topics': ['brute force', 'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1556/C'},
 {'history': 'Ezzat has an array of n integers ( maybe negative) . He wants to '
             'split it into two non- empty subsequences a and b, such that '
             'every element from the array belongs to exactly one subsequence, '
             'and the value of f( a) + f( b) is the maximum possible value, '
             'where f( x) is the average of the subsequence x. A sequence x is '
             'a subsequence of a sequence y if x can be obtained from y by '
             'deletion of several ( possibly, zero or all) elements. The '
             'average of a subsequence is the sum of the numbers of this '
             'subsequence divided by the size of the subsequence. For example, '
             'the average of [ 1, 5, 6] is ( 1+ 5+ 6) / 3= 12/ 3= 4, so f( [ '
             '1, 5, 6] ) = 4.',
  'input': 'The first line contains a single integer t ( 1≤t≤103) — the number '
           'of test cases. Each test case consists of two lines. The first '
           'line contains a single integer n ( 2≤n≤105) . The second line '
           'contains n integers a1, a2, . . . , an ( −109≤ai≤109) . It is '
           'guaranteed that the sum of n over all test cases does not exceed '
           '3⋅105.',
  'note': 'In the first test case, the array is [ 3, 1, 2] . These are all the '
          'possible ways to split this array: a= [ 3] , b= [ 1, 2] , so the '
          'value of f( a) + f( b) = 3+ 1. 5= 4. 5. a= [ 3, 1] , b= [ 2] , so '
          'the value of f( a) + f( b) = 2+ 2= 4. a= [ 3, 2] , b= [ 1] , so the '
          'value of f( a) + f( b) = 2. 5+ 1= 3. 5. Therefore, the maximum '
          'possible value 4. 5. In the second test case, the array is [ −7, '
          '−6, −6] . These are all the possible ways to split this array: a= [ '
          '−7] , b= [ −6, −6] , so the value of f( a) + f( b) = ( −7) + ( −6) '
          '= −13. a= [ −7, −6] , b= [ −6] , so the value of f( a) + f( b) = ( '
          '−6. 5) + ( −6) = −12. 5. Therefore, the maximum possible value −12. '
          '5.',
  'output': 'For each test case, print a single value — the maximum value that '
            'Ezzat can achieve. Your answer is considered correct if its '
            'absolute or relative error does not exceed 10−6. Formally, let '
            "your answer be a, and the jury' s answer be b. Your answer is "
            'accepted if and only if | a−b| max( 1, | b| ) ≤10−6.',
  'title': 'Ezzat and Two Subsequences',
  'topics': ['brute force', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1557/A'},
 {'history': 'Moamen has an array of n distinct integers. He wants to sort '
             'that array in non- decreasing order by doing the following '
             'operations in order exactly once: Split the array into exactly k '
             'non- empty subarrays such that each element belongs to exactly '
             'one subarray. Reorder these subarrays arbitrary. Merge the '
             'subarrays in their new order. A sequence a is a subarray of a '
             'sequence b if a can be obtained from b by deletion of several ( '
             'possibly, zero or all) elements from the beginning and several ( '
             'possibly, zero or all) elements from the end. Can you tell '
             'Moamen if there is a way to sort the array in non- decreasing '
             'order using the operations written above?',
  'input': 'The first line contains a single integer t ( 1≤t≤103) — the number '
           'of test cases. The description of the test cases follows. The '
           'first line of each test case contains two integers n and k ( '
           '1≤k≤n≤105) . The second line contains n integers a1, a2, . . . , '
           'an ( 0≤| ai| ≤109) . It is guaranteed that all numbers are '
           'distinct. It is guaranteed that the sum of n over all test cases '
           'does not exceed 3⋅105.',
  'note': 'In the first test case, a= [ 6, 3, 4, 2, 1] , and k= 4, so we can '
          'do the operations as follows: Split a into [ 6] , [ 3, 4] , [ 2] , '
          '[ 1] . Reorder them: [ 1] , [ 2] , [ 3, 4] , [ 6] . Merge them: [ '
          '1, 2, 3, 4, 6] , so now the array is sorted. In the second test '
          'case, there is no way to sort the array by splitting it into only 2 '
          'subarrays. As an example, if we split it into [ 1, −4] , [ 0, −2] , '
          'we can reorder them into [ 1, −4] , [ 0, −2] or [ 0, −2] , [ 1, −4] '
          '. However, after merging the subarrays, it is impossible to get a '
          'sorted array.',
  'output': 'For each test case, you should output a single string. If Moamen '
            'can sort the array in non- decreasing order, output " YES" ( '
            'without quotes) . Otherwise, output " NO" ( without quotes) . You '
            'can print each letter of " YES" and " NO" in any case ( upper or '
            'lower) .',
  'title': 'Moamen and k-subarrays',
  'topics': ['greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1557/B'},
 {'history': 'You have a permutation: an array a= [ a1, a2, . . . , an] of '
             'distinct integers from 1 to n. The length of the permutation n '
             'is odd. Consider the following algorithm of sorting the '
             'permutation in increasing order. A helper procedure of the '
             'algorithm, f( i) , takes a single argument i ( 1≤i≤n−1) and does '
             'the following. If ai> ai+ 1, the values of ai and ai+ 1 are '
             "exchanged. Otherwise, the permutation doesn' t change. The "
             'algorithm consists of iterations, numbered with consecutive '
             'integers starting with 1. On the i- th iteration, the algorithm '
             'does the following: if i is odd, call f( 1) , f( 3) , . . . , f( '
             'n−2) ; if i is even, call f( 2) , f( 4) , . . . , f( n−1) . It '
             'can be proven that after a finite number of iterations the '
             'permutation will be sorted in increasing order. After how many '
             'iterations will this happen for the first time?',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤104) . Description of the test '
           'cases follows. The first line of each test case contains a single '
           'integer n ( 3≤n≤2⋅105−1; n is odd) — the length of the '
           'permutation. The second line contains n distinct integers a1, a2, '
           '. . . , an ( 1≤ai≤n) — the permutation itself. It is guaranteed '
           'that the sum of n over all test cases does not exceed 2⋅105−1.',
  'note': 'In the first test case, the permutation will be changing as '
          'follows: after the 1- st iteration: [ 2, 3, 1] ; after the 2- nd '
          'iteration: [ 2, 1, 3] ; after the 3- rd iteration: [ 1, 2, 3] . In '
          'the second test case, the permutation will be changing as follows: '
          'after the 1- st iteration: [ 4, 5, 1, 7, 2, 3, 6] ; after the 2- nd '
          'iteration: [ 4, 1, 5, 2, 7, 3, 6] ; after the 3- rd iteration: [ 1, '
          '4, 2, 5, 3, 7, 6] ; after the 4- th iteration: [ 1, 2, 4, 3, 5, 6, '
          '7] ; after the 5- th iteration: [ 1, 2, 3, 4, 5, 6, 7] . In the '
          'third test case, the permutation is already sorted and the answer '
          'is 0.',
  'output': 'For each test case print the number of iterations after which the '
            'permutation will become sorted in increasing order for the first '
            'time. If the given permutation is already sorted, print 0.',
  'title': 'Strange Sort',
  'topics': ['data structures', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1558/F'},
 {'history': "Polycarp doesn' t like integers that are divisible by 3 or end "
             'with the digit 3 in their decimal representation. Integers that '
             'meet both conditions are disliked by Polycarp, too. Polycarp '
             'starts to write out the positive ( greater than 0) integers '
             'which he likes: 1, 2, 4, 5, 7, 8, 10, 11, 14, 16, . . . . Output '
             'the k- th element of this sequence ( the elements are numbered '
             'from 1) .',
  'input': 'The first line contains one integer t ( 1≤t≤100) — the number of '
           'test cases. Then t test cases follow. Each test case consists of '
           'one line containing one integer k ( 1≤k≤1000) .',
  'note': ' ',
  'output': 'For each test case, output in a separate line one integer x — the '
            'k- th element of the sequence that was written out by Polycarp.',
  'title': 'Dislike of Threes',
  'topics': ['implementation'],
  'url': 'https://codeforces.com/problemset/problem/1560/A'},
 {'history': 'Polycarp has found a table having an infinite number of rows and '
             'columns. The rows are numbered from 11, starting from the '
             'topmost one. The columns are numbered from 11, starting from the '
             "leftmost one. Initially, the table hasn' t been filled and "
             'Polycarp wants to fix it. He writes integers from 11 and so on '
             'to the table as follows. The figure shows the placement of the '
             'numbers from 11 to 1010. The following actions are denoted by '
             'the arrows. The leftmost topmost cell of the table is filled '
             'with the number 11. Then he writes in the table all positive '
             'integers beginning from 22 sequentially using the following '
             'algorithm. First, Polycarp selects the leftmost non- filled cell '
             'in the first row and fills it. Then, while the left neighbor of '
             'the last filled cell is filled, he goes down and fills the next '
             'cell. So he goes down until the last filled cell has a non- '
             'filled neighbor to the left ( look at the vertical arrow going '
             'down in the figure above) . After that, he fills the cells from '
             'the right to the left until he stops at the first column ( look '
             'at the horizontal row in the figure above) . Then Polycarp '
             'selects the leftmost non- filled cell in the first row, goes '
             'down, and so on. A friend of Polycarp has a favorite number kk. '
             'He wants to know which cell will contain the number. Help him to '
             'find the indices of the row and the column, such that the '
             'intersection of the row and the column is the cell containing '
             'the number kk.',
  'input': 'The first line contains one integer tt ( 1≤t≤1001≤t≤100) — the '
           'number of test cases. Then tt test cases follow. Each test case '
           'consists of one line containing one integer kk ( 1≤k≤1091≤k≤109) '
           'which location must be found.',
  'note': ' ',
  'output': 'For each test case, output in a separate line two integers rr and '
            'cc ( r, c≥1r, c≥1) separated by spaces — the indices of the row '
            'and the column containing the cell filled by the number kk, '
            'respectively.',
  'title': 'Infinity Table',
  'topics': ['implementation', 'math'],
  'url': 'https://codeforces.com/problemset/problem/1560/C'},
 {'history': 'You are given an integer n. In 1 move, you can do one of the '
             "following actions: erase any digit of the number ( it' s "
             'acceptable that the number before the operation has exactly one '
             'digit and after the operation, it is " empty" ) ; add one digit '
             'to the right. The actions may be performed in any order any '
             'number of times. Note that if, after deleting some digit from a '
             'number, it will contain leading zeroes, they will not be '
             'deleted. E. g. if you delete from the number 301 the digit 3, '
             'the result is the number 01 ( not 1) . You need to perform the '
             'minimum number of actions to make the number any power of 2 ( i. '
             "e. there' s an integer k ( k≥0) such that the resulting number "
             'is equal to 2k) . The resulting number must not have leading '
             'zeroes. E. g. consider n= 1052. The answer is equal to 2. First, '
             "let' s add to the right one digit 4 ( the result will be 10524) "
             ". Then let' s erase the digit 5, so the result will be 1024 "
             'which is a power of 2. E. g. consider n= 8888. The answer is '
             "equal to 3. Let' s erase any of the digits 8 three times. The "
             'result will be 8 which is a power of 2.',
  'input': 'The first line contains one integer t ( 1≤t≤104) — the number of '
           'test cases. Then t test cases follow. Each test case consists of '
           'one line containing one integer n ( 1≤n≤109) .',
  'note': 'The answer for the first test case was considered above. The answer '
          'for the second test case was considered above. In the third test '
          "case, it' s enough to add to the right the digit 4 — the number 6 "
          "will turn into 64. In the fourth test case, let' s add to the right "
          'the digit 8 and then erase 7 and 5 — the taken number will turn '
          'into 8. The numbers of the fifth and the sixth test cases are '
          "already powers of two so there' s no need to make any move. In the "
          'seventh test case, you can delete first of all the digit 3 ( the '
          'result is 01) and then the digit 0 ( the result is 1) .',
  'output': 'For each test case, output in a separate line one integer m — the '
            'minimum number of moves to transform the number into any power of '
            '2.',
  'title': 'Make a Power of Two',
  'topics': ['greedy', 'math', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1560/D'},
 {'history': 'Polycarp has a string s. Polycarp performs the following actions '
             'until the string s is empty ( t is initially an empty string) : '
             'he adds to the right to the string t the string s, i. e. he does '
             't= t+ s, where t+ s is a concatenation of the strings t and s; '
             'he selects an arbitrary letter of s and removes from s all its '
             'occurrences ( the selected letter must occur in the string s at '
             'the moment of performing this action) . Polycarp performs this '
             'sequence of actions strictly in this order. Note that after '
             'Polycarp finishes the actions, the string s will be empty and '
             'the string t will be equal to some value ( that is undefined and '
             'depends on the order of removing) . E. g. consider s= " abacaba" '
             'so the actions may be performed as follows: t= " abacaba" , the '
             'letter \' b\' is selected, then s= " aacaa" ; t= " abacabaaacaa" '
             ', the letter \' a\' is selected, then s= " c" ; t= " '
             'abacabaaacaac" , the letter \' c\' is selected, then s= " " ( '
             'the empty string) . You need to restore the initial value of the '
             'string s using only the final value of t and find the order of '
             'removing letters from s.',
  'input': 'The first line contains one integer T ( 1≤T≤104) — the number of '
           'test cases. Then T test cases follow. Each test case contains one '
           'string t consisting of lowercase letters of the Latin alphabet. '
           "The length of t doesn' t exceed 5⋅105. The sum of lengths of all "
           "strings t in the test cases doesn' t exceed 5⋅105.",
  'note': 'The first test case is considered in the statement.',
  'output': 'For each test case output in a separate line: −1, if the answer '
            "doesn' t exist; two strings separated by spaces. The first one "
            'must contain a possible initial value of s. The second one must '
            "contain a sequence of letters — it' s in what order one needs to "
            'remove letters from s to make the string t. E. g. if the string " '
            'bac" is outputted, then, first, all occurrences of the letter \' '
            "b' were deleted, then all occurrences of ' a' , and then, "
            "finally, all occurrences of ' c' . If there are multiple "
            'solutions, print any one.',
  'title': 'Polycarp and String Transformation',
  'topics': ['binary search', 'implementation', 'sortings', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1560/E'},
 {'history': 'You have a permutation: an array a= [ a1, a2, . . . , an] of '
             'distinct integers from 1 to n. The length of the permutation n '
             'is odd. Consider the following algorithm of sorting the '
             'permutation in increasing order. A helper procedure of the '
             'algorithm, f( i) , takes a single argument i ( 1≤i≤n−1) and does '
             'the following. If ai> ai+ 1, the values of ai and ai+ 1 are '
             "exchanged. Otherwise, the permutation doesn' t change. The "
             'algorithm consists of iterations, numbered with consecutive '
             'integers starting with 1. On the i- th iteration, the algorithm '
             'does the following: if i is odd, call f( 1) , f( 3) , . . . , f( '
             'n−2) ; if i is even, call f( 2) , f( 4) , . . . , f( n−1) . It '
             'can be proven that after a finite number of iterations the '
             'permutation will be sorted in increasing order. After how many '
             'iterations will this happen for the first time?',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤100) . Description of the test '
           'cases follows. The first line of each test case contains a single '
           'integer n ( 3≤n≤999; n is odd) — the length of the permutation. '
           'The second line contains n distinct integers a1, a2, . . . , an ( '
           '1≤ai≤n) — the permutation itself. It is guaranteed that the sum of '
           'n over all test cases does not exceed 999.',
  'note': 'In the first test case, the permutation will be changing as '
          'follows: after the 1- st iteration: [ 2, 3, 1] ; after the 2- nd '
          'iteration: [ 2, 1, 3] ; after the 3- rd iteration: [ 1, 2, 3] . In '
          'the second test case, the permutation will be changing as follows: '
          'after the 1- st iteration: [ 4, 5, 1, 7, 2, 3, 6] ; after the 2- nd '
          'iteration: [ 4, 1, 5, 2, 7, 3, 6] ; after the 3- rd iteration: [ 1, '
          '4, 2, 5, 3, 7, 6] ; after the 4- th iteration: [ 1, 2, 4, 3, 5, 6, '
          '7] ; after the 5- th iteration: [ 1, 2, 3, 4, 5, 6, 7] . In the '
          'third test case, the permutation is already sorted and the answer '
          'is 0.',
  'output': 'For each test case print the number of iterations after which the '
            'permutation will become sorted in increasing order for the first '
            'time. If the given permutation is already sorted, print 0.',
  'title': 'Simply Strange Sort',
  'topics': ['brute force', 'implementation', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1561/A'},
 {'history': 'In a certain video game, the player controls a hero '
             'characterized by a single integer value: power. The hero will '
             'have to beat monsters that are also characterized by a single '
             'integer value: armor. On the current level, the hero is facing n '
             'caves. To pass the level, the hero must enter all the caves in '
             'some order, each cave exactly once, and exit every cave safe and '
             'sound. When the hero enters cave i, he will have to fight ki '
             'monsters in a row: first a monster with armor ai, 1, then a '
             'monster with armor ai, 2 and so on, finally, a monster with '
             'armor ai, ki. The hero can beat a monster if and only if the '
             "hero' s power is strictly greater than the monster' s armor. If "
             "the hero can' t beat the monster he' s fighting, the game ends "
             'and the player loses. Note that once the hero enters a cave, he '
             "can' t exit it before he fights all the monsters in it, strictly "
             'in the given order. Each time the hero beats a monster, the '
             "hero' s power increases by 1. Find the smallest possible power "
             'the hero must start the level with to be able to enter all the '
             'caves in some order and beat all the monsters.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤105) . Description of the test '
           'cases follows. The first line of each test case contains a single '
           'integer n ( 1≤n≤105) — the number of caves. The i- th of the next '
           'n lines contains an integer ki ( 1≤ki≤105) — the number of '
           'monsters in the i- th cave, followed by ki integers ai, 1, ai, 2, '
           '. . . , ai, ki ( 1≤ai, j≤109) — armor levels of the monsters in '
           'cave i in order the hero has to fight them. It is guaranteed that '
           'the sum of ki over all test cases does not exceed 105.',
  'note': 'In the first test case, the hero has to beat a single monster with '
          "armor 42, it' s enough to have power 43 to achieve that. In the "
          'second test case, the hero can pass the level with initial power 13 '
          'as follows: enter cave 2: beat a monster with armor 12, power '
          'increases to 14; beat a monster with armor 11, power increases to '
          '15; enter cave 1: beat a monster with armor 10, power increases to '
          '16; beat a monster with armor 15, power increases to 17; beat a '
          'monster with armor 8, power increases to 18.',
  'output': 'For each test case print a single integer — the smallest possible '
            'power the hero must start the level with to be able to enter all '
            'the caves in some order and beat all the monsters.',
  'title': 'Deep Down Below',
  'topics': ['binary search', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1561/C'},
 {'history': 'During the hypnosis session, Nicholas suddenly remembered a '
             "positive integer n, which doesn' t contain zeros in decimal "
             'notation. Soon, when he returned home, he got curious: what is '
             'the maximum number of digits that can be removed from the number '
             'so that the number becomes not prime, that is, either composite '
             'or equal to one? For some numbers doing so is impossible: for '
             "example, for number 53 it' s impossible to delete some of its "
             'digits to obtain a not prime integer. However, for all n in the '
             "test cases of this problem, it' s guaranteed that it' s possible "
             'to delete some of their digits to obtain a not prime number. '
             'Note that you cannot remove all the digits from the number. A '
             'prime number is a number that has no divisors except one and '
             'itself. A composite is a number that has more than two divisors. '
             '1 is neither a prime nor a composite number.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'one positive integer t ( 1≤t≤103) , denoting the number of test '
           'cases. Description of the test cases follows. The first line of '
           'each test case contains one positive integer k ( 1≤k≤50) — the '
           'number of digits in the number. The second line of each test case '
           "contains a positive integer n, which doesn' t contain zeros in "
           'decimal notation ( 10k−1≤n< 10k) . It is guaranteed that it is '
           'always possible to remove less than k digits to make the number '
           'not prime. It is guaranteed that the sum of k over all test cases '
           'does not exceed 104.',
  'note': "In the first test case, you can' t delete 2 digits from the number "
          '237, as all the numbers 2, 3, and 7 are prime. However, you can '
          'delete 1 digit, obtaining a number 27= 33. In the second test case, '
          'you can delete all digits except one, as 4= 22 is a composite '
          'number.',
  'output': 'For every test case, print two numbers in two lines. In the first '
            'line print the number of digits, that you have left in the '
            'number. In the second line print the digits left after all '
            'delitions. If there are multiple solutions, print any.',
  'title': 'Scenes From a Memory',
  'topics': ['brute force',
             'constructive algorithms',
             'implementation',
             'math',
             'number theory'],
  'url': 'https://codeforces.com/problemset/problem/1562/B'},
 {'history': 'Morning desert sun horizonRise above the sands of time. . . '
             'Fates Warning, " Exodus" After crossing the Windswept Wastes, '
             'Ori has finally reached the Windtorn Ruins to find the Heart of '
             'the Forest! However, the ancient repository containing this '
             'priceless Willow light did not want to open! Ori was taken '
             'aback, but the Voice of the Forest explained to him that the '
             'cunning Gorleks had decided to add protection to the repository. '
             'The Gorleks were very fond of the " string expansion" operation. '
             'They were also very fond of increasing subsequences. Suppose a '
             'string s1s2s3. . . sn is given. Then its " expansion" is defined '
             'as the sequence of strings s1, s1s2, . . . , s1s2. . . sn, s2, '
             's2s3, . . . , s2s3. . . sn, s3, s3s4, . . . , sn−1sn, sn. For '
             'example, the " expansion" the string \' abcd\' will be the '
             "following sequence of strings: ' a' , ' ab' , ' abc' , ' abcd' , "
             "' b' , ' bc' , ' bcd' , ' c' , ' cd' , ' d' . To open the "
             'ancient repository, Ori must find the size of the largest '
             'increasing subsequence of the " expansion" of the string s. '
             'Here, strings are compared lexicographically. Help Ori with this '
             'task! A string a is lexicographically smaller than a string b if '
             'and only if one of the following holds: a is a prefix of b, but '
             'a= ̸b; in the first position where a and b differ, the string a '
             'has a letter that appears earlier in the alphabet than the '
             'corresponding letter in b.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'one positive integer t ( 1≤t≤103) , denoting the number of test '
           'cases. Description of the test cases follows. The first line of '
           'each test case contains one positive integer n ( 1≤n≤5000) — '
           'length of the string. The second line of each test case contains a '
           'non- empty string of length n, which consists of lowercase latin '
           'letters. It is guaranteed that the sum of n over all test cases '
           'does not exceed 104.',
  'note': 'In first test case the " expansion" of the string is: \' a\' , \' '
          "ac' , ' acb' , ' acba' , ' acbac' , ' c' , ' cb' , ' cba' , ' cbac' "
          ", ' b' , ' ba' , ' bac' , ' a' , ' ac' , ' c' . The answer can be, "
          "for example, ' a' , ' ac' , ' acb' , ' acba' , ' acbac' , ' b' , ' "
          "ba' , ' bac' , ' c' .",
  'output': 'For every test case print one non- negative integer — the answer '
            'to the problem.',
  'title': 'Rescue Niwen!',
  'topics': ['dp', 'greedy', 'string suffix structures', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1562/E'},
 {'history': 'It is the easy version of the problem. The only difference is '
             'that in this version n= 1. In the cinema seats can be '
             'represented as the table with n rows and m columns. The rows are '
             'numbered with integers from 1 to n. The seats in each row are '
             'numbered with consecutive integers from left to right: in the k- '
             'th row from m( k−1) + 1 to mk for all rows 1≤k≤n. 12⋯m−1mm+ 1m+ '
             '2⋯2m−12m2m+ 12m+ 2⋯3m−13m⋮⋮⋱⋮⋮m( n−1) + 1m( n−1) + 2⋯nm−1nm The '
             'table with seats indices There are nm people who want to go to '
             'the cinema to watch a new film. They are numbered with integers '
             'from 1 to nm. You should give exactly one seat to each person. '
             'It is known, that in this cinema as lower seat index you have as '
             'better you can see everything happening on the screen. i- th '
             "person has the level of sight ai. Let' s define si as the seat "
             'index, that will be given to i- th person. You want to give '
             'better places for people with lower sight levels, so for any two '
             'people i, j such that ai< aj it should be satisfied that si< sj. '
             'After you will give seats to all people they will start coming '
             'to their seats. In the order from 1 to nm, each person will '
             'enter the hall and sit in their seat. To get to their place, the '
             "person will go to their seat' s row and start moving from the "
             'first seat in this row to theirs from left to right. While '
             'moving some places will be free, some will be occupied with '
             'people already seated. The inconvenience of the person is equal '
             "to the number of occupied seats he or she will go through. Let' "
             's consider an example: m= 5, the person has the seat 4 in the '
             'first row, the seats 1, 3, 5 in the first row are already '
             'occupied, the seats 2 and 4 are free. The inconvenience of this '
             'person will be 2, because he will go through occupied seats 1 '
             'and 3. Find the minimal total inconvenience ( the sum of '
             'inconveniences of all people) , that is possible to have by '
             'giving places for all people ( all conditions should be '
             'satisfied) .',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤100) — the number of test cases. '
           'Description of the test cases follows. The first line of each test '
           'case contains two integers n and m ( n= 1, 1≤m≤300) — the number '
           'of rows and places in each row respectively. The second line of '
           'each test case contains n⋅m integers a1, a2, . . . , an⋅m ( '
           "1≤ai≤109) , where ai is the sight level of i- th person. It' s "
           'guaranteed that the sum of n⋅m over all test cases does not exceed '
           '105.',
  'note': 'In the first test case, there is a single way to arrange people, '
          'because all sight levels are distinct. The first person will sit on '
          'the first seat, the second person will sit on the second place, the '
          'third person will sit on the third place. So inconvenience of the '
          'first person will be 0, inconvenience of the second person will be '
          '1 and inconvenience of the third person will be 2. The total '
          'inconvenience is 0+ 1+ 2= 3. In the second test case, people should '
          'sit as follows: s1= 2, s2= 1, s3= 5, s4= 4, s5= 3. The total '
          'inconvenience will be 6.',
  'output': 'For each test case print a single integer — the minimal total '
            'inconvenience that can be achieved.',
  'title': 'Seating Arrangements (easy version) ',
  'topics': ['data structures', 'greedy', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1566/D1'},
 {'history': 'It is the hard version of the problem. The only difference is '
             'that in this version 1≤n≤300. In the cinema seats can be '
             'represented as the table with n rows and m columns. The rows are '
             'numbered with integers from 1 to n. The seats in each row are '
             'numbered with consecutive integers from left to right: in the k- '
             'th row from m( k−1) + 1 to mk for all rows 1≤k≤n. 12⋯m−1mm+ 1m+ '
             '2⋯2m−12m2m+ 12m+ 2⋯3m−13m⋮⋮⋱⋮⋮m( n−1) + 1m( n−1) + 2⋯nm−1nm The '
             'table with seats indices There are nm people who want to go to '
             'the cinema to watch a new film. They are numbered with integers '
             'from 1 to nm. You should give exactly one seat to each person. '
             'It is known, that in this cinema as lower seat index you have as '
             'better you can see everything happening on the screen. i- th '
             "person has the level of sight ai. Let' s define si as the seat "
             'index, that will be given to i- th person. You want to give '
             'better places for people with lower sight levels, so for any two '
             'people i, j such that ai< aj it should be satisfied that si< sj. '
             'After you will give seats to all people they will start coming '
             'to their seats. In the order from 1 to nm, each person will '
             'enter the hall and sit in their seat. To get to their place, the '
             "person will go to their seat' s row and start moving from the "
             'first seat in this row to theirs from left to right. While '
             'moving some places will be free, some will be occupied with '
             'people already seated. The inconvenience of the person is equal '
             "to the number of occupied seats he or she will go through. Let' "
             's consider an example: m= 5, the person has the seat 4 in the '
             'first row, the seats 1, 3, 5 in the first row are already '
             'occupied, the seats 2 and 4 are free. The inconvenience of this '
             'person will be 2, because he will go through occupied seats 1 '
             'and 3. Find the minimal total inconvenience ( the sum of '
             'inconveniences of all people) , that is possible to have by '
             'giving places for all people ( all conditions should be '
             'satisfied) .',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤100) — the number of test cases. '
           'Description of the test cases follows. The first line of each test '
           'case contains two integers n and m ( 1≤n, m≤300) — the number of '
           'rows and places in each row respectively. The second line of each '
           'test case contains n⋅m integers a1, a2, . . . , an⋅m ( 1≤ai≤109) , '
           "where ai is the sight level of i- th person. It' s guaranteed that "
           'the sum of n⋅m over all test cases does not exceed 105.',
  'note': 'In the first test case, there is a single way to give seats: the '
          'first person sits in the first place and the second person — in the '
          'second. The total inconvenience is 1. In the second test case the '
          'optimal seating looks like this: In the third test case the optimal '
          "seating looks like this: The number in a cell is the person' s "
          'index that sits on this place.',
  'output': 'For each test case print a single integer — the minimal total '
            'inconvenience that can be achieved.',
  'title': 'Seating Arrangements (hard version) ',
  'topics': ['data structures',
             'greedy',
             'implementation',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1566/D2'},
 {'history': 'There are n points and m segments on the coordinate line. The '
             'initial coordinate of the i- th point is ai. The endpoints of '
             'the j- th segment are lj and rj — left and right endpoints, '
             'respectively. You can move the points. In one move you can move '
             'any point from its current coordinate x to the coordinate x−1 or '
             'the coordinate x+ 1. The cost of this move is 1. You should move '
             'the points in such a way that each segment is visited by at '
             'least one point. A point visits the segment [ l, r] if there is '
             'a moment when its coordinate was on the segment [ l, r] ( '
             'including endpoints) . You should find the minimal possible '
             'total cost of all moves such that all segments are visited.',
  'input': 'The input consists of multiple test cases. The first line contains '
           'a single integer t ( 1≤t≤104) — the number of test cases. '
           'Description of the test cases follows. The first line of each test '
           'case contains two integers n and m ( 1≤n, m≤2⋅105) — the number of '
           'points and segments respectively. The next line contains n '
           'distinct integers a1, a2, . . . , an ( −109≤ai≤109) — the initial '
           'coordinates of the points. Each of the next m lines contains two '
           'integers lj, rj ( −109≤lj≤rj≤109) — the left and the right '
           "endpoints of the j- th segment. It' s guaranteed that the sum of n "
           'and the sum of m over all test cases does not exceed 2⋅105.',
  'note': 'In the first test case the points can be moved as follows: Move the '
          'second point from the coordinate 6 to the coordinate 5. Move the '
          'third point from the coordinate 14 to the coordinate 13. Move the '
          'fourth point from the coordinate 18 to the coordinate 17. Move the '
          'third point from the coordinate 13 to the coordinate 12. Move the '
          'fourth point from the coordinate 17 to the coordinate 16. The total '
          'cost of moves is 5. It is easy to see, that all segments are '
          'visited by these movements. For example, the tenth segment ( [ 7, '
          '13] ) is visited after the second move by the third point. Here is '
          'the image that describes the first test case:',
  'output': 'For each test case print a single integer — the minimal total '
            'cost of all moves such that all segments are visited.',
  'title': 'Points Movement',
  'topics': ['data structures', 'dp', 'greedy', 'implementation', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1566/F'},
 {'history': 'You are given an undirected weighted graph, consisting of n '
             'vertices and m edges. Some queries happen with this graph: '
             'Delete an existing edge from the graph. Add a non- existing edge '
             'to the graph. At the beginning and after each query, you should '
             'find four different vertices a, b, c, d such that there exists a '
             'path between a and b, there exists a path between c and d, and '
             'the sum of lengths of two shortest paths from a to b and from c '
             'to d is minimal. The answer to the query is the sum of the '
             'lengths of these two shortest paths. The length of the path is '
             'equal to the sum of weights of edges in this path.',
  'input': 'The first line contains two integers n and m ( 4≤n, m≤105) — the '
           'number of vertices and edges in the graph respectively. Each of '
           'the next m lines contain three integers v, u, w ( 1≤v, u≤n, v= ̸u, '
           '1≤w≤109) — this triple means that there is an edge between '
           'vertices v and u with weight w. The next line contains a single '
           'integer q ( 0≤q≤105) — the number of queries. The next q lines '
           'contain the queries of two types: 0 v u — this query means '
           'deleting an edge between v and u ( 1≤v, u≤n, v= ̸u) . It is '
           'guaranteed that such edge exists in the graph. 1 v u w — this '
           'query means adding an edge between vertices v and u with weight w '
           '( 1≤v, u≤n, v= ̸u, 1≤w≤109) . It is guaranteed that there was no '
           'such edge in the graph. It is guaranteed that the initial graph '
           'does not contain multiple edges. At the beginning and after each '
           "query, the graph doesn' t need to be connected. It is guaranteed "
           'that at each moment the number of edges will be at least 4. It can '
           'be proven, that at each moment there exist some four vertices a, '
           'b, c, d such that there exists a path between vertices a and b, '
           'and there exists a path between vertices c and d.',
  'note': 'Before the queries you can choose vertices ( a, b) = ( 3, 2) and ( '
          'c, d) = ( 1, 4) . The sum of lengths of two shortest paths is 3+ 1= '
          '4. After the first query you can choose vertices ( a, b) = ( 2, 5) '
          'and ( c, d) = ( 1, 4) . The sum of lengths of two shortest paths is '
          '2+ 1= 3. After the second query you can choose vertices ( a, b) = ( '
          '3, 4) and ( c, d) = ( 2, 5) . The sum of lengths of two shortest '
          'paths is 1+ 2= 3. After the third query, you can choose vertices ( '
          'a, b) = ( 2, 6) and ( c, d) = ( 4, 5) . The sum of lengths of two '
          'shortest paths is 4+ 3= 7. After the last query you can choose '
          'vertices ( a, b) = ( 1, 6) and ( c, d) = ( 2, 5) . The sum of '
          'lengths of two shortest paths is 3+ 2= 5.',
  'output': 'Print q+ 1 integers — the minimal sum of lengths of shortest '
            'paths between chosen pairs of vertices before the queries and '
            'after each of them.',
  'title': 'Four Vertices',
  'topics': ['constructive algorithms',
             'data structures',
             'graphs',
             'greedy',
             'implementation',
             'shortest paths'],
  'url': 'https://codeforces.com/problemset/problem/1566/G'},
 {'history': 'Alice has a grid with 2 rows and n columns. She fully covers the '
             'grid using n dominoes of size 1×2 — Alice may place them '
             'vertically or horizontally, and each cell should be covered by '
             'exactly one domino. Now, she decided to show one row of the grid '
             'to Bob. Help Bob and figure out what the other row of the grid '
             'looks like!',
  'input': 'The input consists of multiple test cases. The first line contains '
           'an integer t ( 1≤t≤5000) — the number of test cases. The '
           'description of the test cases follows. The first line of each test '
           'case contains an integer n ( 1≤n≤100) — the width of the grid. The '
           'second line of each test case contains a string s consisting of n '
           'characters, each of which is either L, R, U, or D, representing '
           'the left, right, top, or bottom half of a domino, respectively ( '
           'see notes for better understanding) . This string represents one '
           'of the rows of the grid. Additional constraint on the input: each '
           'input corresponds to at least one valid tiling.',
  'note': 'In the first test case, Alice shows Bob the top row, the whole grid '
          'may look like: In the second test case, Alice shows Bob the bottom '
          'row, the whole grid may look like: In the third test case, Alice '
          'shows Bob the bottom row, the whole grid may look like: In the '
          'fourth test case, Alice shows Bob the top row, the whole grid may '
          'look like:',
  'output': 'For each test case, output one string — the other row of the '
            'grid, using the same format as the input string. If there are '
            'multiple answers, print any.',
  'title': 'Domino Disaster',
  'topics': ['implementation', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1567/A'},
 {'history': 'On the board, Bob wrote n positive integers in base 10 with sum '
             's ( i. e. in decimal numeral system) . Alice sees the board, but '
             'accidentally interprets the numbers on the board as base- 11 '
             'integers and adds them up ( in base 11) . What numbers should '
             "Bob write on the board, so Alice' s sum is as large as possible?",
  'input': 'The input consists of multiple test cases. The first line contains '
           'an integer t ( 1≤t≤100) — the number of test cases. The '
           'description of the test cases follows. The only line of each test '
           'case contains two integers s and n ( 1≤s≤109; 1≤n≤min( 100, s) ) — '
           'the sum and amount of numbers on the board, respectively. Numbers '
           's and n are given in decimal notation ( base 10) .',
  'note': "In the first test case, 7010+ 2710= 9710, and Alice' s sum is 7011+ "
          '2711= 9711= 9⋅11+ 7= 10610. ( Here xb represents the number x in '
          'base b. ) It can be shown that it is impossible for Alice to get a '
          'larger sum than 10610. In the second test case, Bob can only write '
          'a single number on the board, so he must write 17. In the third '
          "test case, 310+ 410+ 10010+ 410= 11110, and Alice' s sum is 311+ "
          '411+ 10011+ 411= 11011= 1⋅112+ 1⋅11= 13210. It can be shown that it '
          'is impossible for Alice to get a larger sum than 13210.',
  'output': 'For each test case, output n positive integers — the numbers Bob '
            "should write on the board, so Alice' s sum is as large as "
            'possible. If there are multiple answers, print any of them.',
  'title': 'Expression Evaluation Error',
  'topics': ['constructive algorithms', 'greedy', 'implementation', 'math'],
  'url': 'https://codeforces.com/problemset/problem/1567/D'},
 {'history': 'Alice has an empty grid with n rows and m columns. Some of the '
             'cells are marked, and no marked cells are adjacent to the edge '
             'of the grid. ( Two squares are adjacent if they share a side. ) '
             'Alice wants to fill each cell with a number such that the '
             'following statements are true: every unmarked cell contains '
             'either the number 1 or 4; every marked cell contains the sum of '
             'the numbers in all unmarked cells adjacent to it ( if a marked '
             'cell is not adjacent to any unmarked cell, this sum is 0) ; '
             "every marked cell contains a multiple of 5. Alice couldn' t "
             'figure it out, so she asks Bob to help her. Help Bob find any '
             'such grid, or state that no such grid exists.',
  'input': 'The first line of input contains two integers n and m ( 1≤n, '
           'm≤500) — the number of rows and the number of columns in the grid, '
           'respectively. Then n lines follow, each containing m characters. '
           "Each of these characters is either ' . ' or ' X' — an unmarked and "
           'a marked cell, respectively. No marked cells are adjacent to the '
           'edge of the grid.',
  'note': 'It can be shown that no such grid exists for the second test.',
  'output': 'Output " \' NO" if no suitable grid exists. Otherwise, output " '
            '\' YES" \' . Then output n lines of m space- separated integers — '
            'the integers in the grid.',
  'title': 'One-Four Overload',
  'topics': ['2-sat',
             'constructive algorithms',
             'dfs and similar',
             'dsu',
             'graphs',
             'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1567/F'},
 {'history': 'You are given a string s, consisting of n letters, each letter '
             "is either ' a' or ' b' . The letters in the string are numbered "
             'from 1 to n. s[ l; r] is a continuous substring of letters from '
             'index l to r of the string inclusive. A string is called '
             "balanced if the number of letters ' a' in it is equal to the "
             'number of letters \' b\' . For example, strings " baba" and " '
             'aabbab" are balanced and strings " aaab" and " b" are not. Find '
             'any non- empty balanced substring s[ l; r] of string s. Print '
             'its l and r ( 1≤l≤r≤n) . If there is no such substring, then '
             'print −1 −1.',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of testcases. Then the descriptions of t testcases follow. '
           'The first line of the testcase contains a single integer n ( '
           '1≤n≤50) — the length of the string. The second line of the '
           'testcase contains a string s, consisting of n letters, each letter '
           "is either ' a' or ' b' .",
  'note': 'In the first testcase there are no non- empty balanced subtrings. '
          'In the second and third testcases there are multiple balanced '
          'substrings, including the entire string " abbaba" and substring " '
          'baba" .',
  'output': 'For each testcase print two integers. If there exists a non- '
            'empty balanced substring s[ l; r] , then print l r ( 1≤l≤r≤n) . '
            'Otherwise, print −1 −1.',
  'title': 'Balanced Substring',
  'topics': ['implementation'],
  'url': 'https://codeforces.com/problemset/problem/1569/A'},
 {'history': 'There is a city that can be represented as a square grid with '
             'corner points in ( 0, 0) and ( 106, 106) . The city has n '
             'vertical and m horizontal streets that goes across the whole '
             'city, i. e. the i- th vertical streets goes from ( xi, 0) to ( '
             'xi, 106) and the j- th horizontal street goes from ( 0, yj) to ( '
             '106, yj) . All streets are bidirectional. Borders of the city '
             'are streets as well. There are k persons staying on the streets: '
             'the p- th person at point ( xp, yp) ( so either xp equal to some '
             "xi or yp equal to some yj, or both) . Let' s say that a pair of "
             'persons form an inconvenient pair if the shortest path from one '
             'person to another going only by streets is strictly greater than '
             'the Manhattan distance between them. Calculate the number of '
             'inconvenient pairs of persons ( pairs ( x, y) and ( y, x) are '
             "the same pair) . Let' s recall that Manhattan distance between "
             'points ( x1, y1) and ( x2, y2) is | x1−x2| + | y1−y2| .',
  'input': 'The first line contains a single integer t ( 1≤t≤1000) — the '
           'number of test cases. The first line of each test case contains '
           'three integers n, m and k ( 2≤n, m≤2⋅105; 2≤k≤3⋅105) — the number '
           'of vertical and horizontal streets and the number of persons. The '
           'second line of each test case contains n integers x1, x2, . . . , '
           'xn ( 0= x1< x2< ⋯< xn−1< xn= 106) — the x- coordinates of vertical '
           'streets. The third line contains m integers y1, y2, . . . , ym ( '
           '0= y1< y2< ⋯< ym−1< ym= 106) — the y- coordinates of horizontal '
           'streets. Next k lines contains description of people. The p- th '
           'line contains two integers xp and yp ( 0≤xp, yp≤106; xp∈x1, . . . '
           ', xn or yp∈y1, . . . , ym) — the coordinates of the p- th person. '
           "All points are distinct. It guaranteed that sum of n doesn' t "
           "exceed 2⋅105, sum of m doesn' t exceed 2⋅105 and sum of k doesn' t "
           'exceed 3⋅105.',
  'note': 'The second test case is pictured below: For example, points 3 and 4 '
          'form an inconvenient pair, since the shortest path between them ( '
          'shown red and equal to 7) is greater than its Manhattan distance ( '
          'equal to 5) . Points 3 and 5 also form an inconvenient pair: the '
          'shortest path equal to 1000001 ( shown green) is greater than the '
          "Manhattan distance equal to 999999. But points 5 and 9 don' t form "
          'an inconvenient pair, since the shortest path ( shown purple) is '
          'equal to its Manhattan distance.',
  'output': 'For each test case, print the number of inconvenient pairs.',
  'title': 'Inconvenient Pairs',
  'topics': ['binary search',
             'data structures',
             'implementation',
             'sortings',
             'two pointers'],
  'url': 'https://codeforces.com/problemset/problem/1569/D'},
 {'history': '2k2k teams participate in a playoff tournament. The tournament '
             'consists of 2k−12k−1 games. They are held as follows: first of '
             'all, the teams are split into pairs: team 11 plays against team '
             '22, team 33 plays against team 44 ( exactly in this order) , and '
             'so on ( so, 2k−12k−1 games are played in that phase) . When a '
             'team loses a game, it is eliminated, and each game results in '
             'elimination of one team ( there are no ties) . After that, only '
             '2k−12k−1 teams remain. If only one team remains, it is declared '
             'the champion; otherwise, 2k−22k−2 games are played: in the first '
             'one of them, the winner of the game " 11 vs 22" plays against '
             'the winner of the game " 33 vs 44" , then the winner of the game '
             '" 55 vs 66" plays against the winner of the game " 77 vs 88" , '
             'and so on. This process repeats until only one team remains. '
             'After the tournament ends, the teams are assigned places '
             'according to the tournament phase when they were eliminated. In '
             'particular: the winner of the tournament gets place 11; the team '
             'eliminated in the finals gets place 22; both teams eliminated in '
             'the semifinals get place 33; all teams eliminated in the '
             'quarterfinals get place 55; all teams eliminated in the 1/ 8 '
             'finals get place 99, and so on. For example, this picture '
             'describes one of the possible ways the tournament can go with k= '
             '3k= 3, and the resulting places of the teams: After a tournament '
             'which was conducted by the aforementioned rules ended, its '
             'results were encoded in the following way. Let pipi be the place '
             'of the ii- th team in the tournament. The hash value of the '
             'tournament hh is calculated as h= ( ∑i= 12ki⋅Api) mod998244353h= '
             '( ∑i= 12ki⋅Api) mod998244353, where AA is some given integer. '
             'Unfortunately, due to a system crash, almost all tournament- '
             'related data was lost. The only pieces of data that remain are '
             'the values of kk, AA and hh. You are asked to restore the '
             'resulting placing of the teams in the tournament, if it is '
             'possible at all.',
  'input': 'The only line contains three integers kk, AA and hh ( 1≤k≤51≤k≤5; '
           '100≤A≤108100≤A≤108; 0≤h≤9982443520≤h≤998244352) .',
  'note': 'The tournament for the first example is described in the statement. '
          'For the third example, the placing [ 1, 2, 3, 3] [ 1, 2, 3, 3] ( '
          'team 11 gets place 11, team 22 gets place 22, teams 33 and 44 get '
          'place 33) could result in a hash value of 70201007020100 with A= '
          '100A= 100, but no tournament can result in such placing since teams '
          '11 and 22 play against each other in the semifinals, so they cannot '
          'get two first places.',
  'output': 'If it is impossible to find any placing of the teams that is '
            'consistent with the data you have, print one integer −1−1. '
            'Otherwise, print 2k2k integers, where ii- th integer should be '
            'equal to pipi ( the place of the ii- th team) . Note that your '
            'answer should be consistent with one of the possible ways the '
            'tournament could go, and note that the initial structure of the '
            'tournament is fixed ( for example, teams 11 and 22 always play in '
            'the first phase of the tournament against each other) . If there '
            'are multiple ways to restore the places of the teams which are '
            'consistent with the data you have, print any of them.',
  'title': 'Playoff Restoration',
  'topics': ['bitmasks',
             'brute force',
             'hashing',
             'implementation',
             'meet-in-the-middle'],
  'url': 'https://codeforces.com/problemset/problem/1569/E'},
 {'history': "Let' s say that two strings s and t rhyme if both strings have "
             'length at least k, and their last k characters are equal. For '
             'example, if k= 3, the strings abcd and cebcd rhyme, the strings '
             "ab and ab don' t rhyme, the strings aaaa and aaaaa rhyme, the "
             "strings abcd and abce don' t rhyme. You have n pairs of strings "
             '( si, ti) , and for each pair of strings you know, should they '
             'rhyme or should not. Find all possible non- negative integer '
             'values for k such that pairs that have to rhyme, rhyme and pairs '
             "that must not rhyme, don' t rhyme.",
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤1000) . Description of the test '
           'cases follows. The first line of each test case contains a single '
           'integer n ( 1≤n≤105) — the number of string pairs. Next n lines '
           'contains descriptions of pairs — one per line. The i- th line '
           'contains space- separated strings si and ti and marker ri. Strings '
           'are non- empty, consist of lowercase Latin letters and each have '
           'length at most 2⋅105. The marker ri equals to 1 if strings have to '
           "rhyme, or 0 if they must not rhyme. It' s guaranteed that for each "
           'test case there is at least one pair with ri equal to 1 and that '
           "the total length of all strings over all test cases doesn' t "
           'exceed 4⋅105.',
  'note': 'In the first test case, if k is at least 1 then kotlin and heroes '
          "don' t rhyme. In the second test case, for k= 2 join and kotlin "
          "rhyme, and episode and eight don' t rhyme.",
  'output': 'For each test case, firstly print integer m — the number of '
            'possible non- negative integer values of k such that pairs that '
            "have to rhyme, rhyme and pairs that must not rhyme, don' t rhyme. "
            'Next, print all these values of k ( without repetitions) . You '
            'can print them in any order.',
  'title': 'Rhyme',
  'topics': ['*special', 'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1571/C'},
 {'history': 'Kotlin Heroes competition is nearing completion. This time nn '
             'programmers took part in the competition. Now organizers are '
             'thinking how to entertain spectators as well. One of the '
             'possibilities is holding sweepstakes. So for now they decided to '
             'conduct a survey among spectators. In total, organizers asked mm '
             'viewers two questions: Who will take the first place? Who will '
             'take the last place? After receiving answers, organizers ranked '
             'all spectators based on the number of programmers they guessed '
             'right. Suppose, there are c2c2 viewers who guessed right both '
             'first and last place, c1c1 viewers who guessed either first or '
             "last place right and c0c0 viewers who didn' t guess at all. All "
             'c2c2 viewers will get rank 11, all viewers with one right answer '
             'will get rank c2+ 1c2+ 1 and all remaining viewers — rank c2+ '
             'c1+ 1c2+ c1+ 1. You were one of the interviewed spectators. '
             'Also, as one of the organizers, you have access to survey '
             'results, but not to competition results. Calculate, what is the '
             "worst rank you can possibly get according to organizers' ranking "
             'system?',
  'input': 'The first line contains two integers nn and mm ( 2≤n≤10002≤n≤1000; '
           '1≤m≤2⋅1051≤m≤2⋅105) — the number of programmers participating in '
           'the competition and the number of surveyed spectators. Next mm '
           'lines contain answers of spectators. The ii- th line contains two '
           'integers fifi and lili ( 1≤fi, li≤n1≤fi, li≤n; fi= ̸lifi= ̸li) — '
           'the indices of programmers who will take the first and last places '
           'in opinion of the ii- th viewer. For simplicity, you are the first '
           'among spectators, so your answers are f1f1 and l1l1.',
  'note': 'In the first example, if the second programmer takes first place, '
          "while the first programmer takes last place, you' ll have 00 right "
          "answers while the other two spectators — 22 right answers. That' s "
          'why your rank ( in the worst case) will be c2+ c1+ 1c2+ c1+ 1 = = '
          '2+ 0+ 1= 32+ 0+ 1= 3. In the second example, for example, if the '
          'third programmer takes the first place and the second programmer '
          "takes the last place, then you' ll have 11 right answer. The "
          'spectators 22, 44 and 55 will have 22 right answers, spectator 66 — '
          '11 right answer and spectator 33 — 00 right answers. As a result, '
          'your rank will be equal to c2+ 1c2+ 1 = = 3+ 1= 43+ 1= 4. ( Note '
          'that spectator 66 will have the same rank 44) .',
  'output': 'Print the single integer — the worst rank among spectators you '
            "can possibly get according to organizers' ranking system ( bigger "
            'rank — worse, of course) .',
  'title': 'Sweepstake',
  'topics': ['*special',
             'brute force',
             'constructive algorithms',
             'implementation',
             'math'],
  'url': 'https://codeforces.com/problemset/problem/1571/D'},
 {'history': 'You are given a book with n chapters. Each chapter has a '
             'specified list of other chapters that need to be understood in '
             'order to understand this chapter. To understand a chapter, you '
             'must read it after you understand every chapter on its required '
             "list. Currently you don' t understand any of the chapters. You "
             'are going to read the book from the beginning till the end '
             'repeatedly until you understand the whole book. Note that if you '
             "read a chapter at a moment when you don' t understand some of "
             "the required chapters, you don' t understand this chapter. "
             'Determine how many times you will read the book to understand '
             'every chapter, or determine that you will never understand every '
             'chapter no matter how many times you read the book.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤2⋅104) . The first line of each '
           'test case contains a single integer n ( 1≤n≤2⋅105) — number of '
           'chapters. Then n lines follow. The i- th line begins with an '
           'integer ki ( 0≤ki≤n−1) — number of chapters required to understand '
           'the i- th chapter. Then ki integers ai, 1, ai, 2, . . . , ai, ki ( '
           '1≤ai, j≤n, ai, j= ̸i, ai, j= ̸ai, l for j= ̸l) follow — the '
           'chapters required to understand the i- th chapter. It is '
           'guaranteed that the sum of n and sum of ki over all testcases do '
           'not exceed 2⋅105.',
  'note': 'In the first example, we will understand chapters 2, 4 in the first '
          'reading and chapters 1, 3 in the second reading of the book. In the '
          'second example, every chapter requires the understanding of some '
          'other chapter, so it is impossible to understand the book. In the '
          'third example, every chapter requires only chapters that appear '
          'earlier in the book, so we can understand everything in one go. In '
          'the fourth example, we will understand chapters 2, 3, 4 in the '
          'first reading and chapter 1 in the second reading of the book. In '
          'the fifth example, we will understand one chapter in every reading '
          'from 5 to 1.',
  'output': 'For each test case, if the entire book can be understood, print '
            'how many times you will read it, otherwise print −1.',
  'title': 'Book',
  'topics': ['binary search',
             'brute force',
             'data structures',
             'dp',
             'graphs',
             'implementation',
             'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1572/A'},
 {'history': 'You are given two arrays a and b of length n. Array a contains '
             'each odd integer from 1 to 2n in an arbitrary order, and array b '
             'contains each even integer from 1 to 2n in an arbitrary order. '
             'You can perform the following operation on those arrays: choose '
             'one of the two arrays pick an index i from 1 to n−1 swap the i- '
             'th and the ( i+ 1) - th elements of the chosen array Compute the '
             'minimum number of operations needed to make array a '
             'lexicographically smaller than array b. For two different arrays '
             'x and y of the same length n, we say that x is lexicographically '
             'smaller than y if in the first position where x and y differ, '
             'the array x has a smaller element than the corresponding element '
             'in y.',
  'input': 'Each test contains multiple test cases. The first line contains '
           'the number of test cases t ( 1≤t≤104) . The first line of each '
           'test case contains a single integer n ( 1≤n≤105) — the length of '
           'the arrays. The second line of each test case contains n integers '
           'a1, a2, . . . , an ( 1≤ai≤2n, all ai are odd and pairwise '
           'distinct) — array a. The third line of each test case contains n '
           'integers b1, b2, . . . , bn ( 1≤bi≤2n, all bi are even and '
           'pairwise distinct) — array b. It is guaranteed that the sum of n '
           'over all test cases does not exceed 105.',
  'note': 'In the first example, the array a is already lexicographically '
          'smaller than array b, so no operations are required. In the second '
          'example, we can swap 5 and 3 and then swap 2 and 4, which results '
          'in [ 3, 5, 1] and [ 4, 2, 6] . Another correct way is to swap 3 and '
          '1 and then swap 5 and 1, which results in [ 1, 5, 3] and [ 2, 4, 6] '
          '. Yet another correct way is to swap 4 and 6 and then swap 2 and 6, '
          'which results in [ 5, 3, 1] and [ 6, 2, 4] .',
  'output': 'For each test case, print one integer: the minimum number of '
            'operations needed to make array a lexicographically smaller than '
            'array b. We can show that an answer always exists.',
  'title': 'Swaps',
  'topics': ['greedy', 'math', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1573/B'},
 {'history': 'Recently, Petya learned about a new game " Slay the Dragon" . As '
             'the name suggests, the player will have to fight with dragons. '
             'To defeat a dragon, you have to kill it and defend your castle. '
             'To do this, the player has a squad of n heroes, the strength of '
             'the i- th hero is equal to ai. According to the rules of the '
             'game, exactly one hero should go kill the dragon, all the others '
             "will defend the castle. If the dragon' s defense is equal to x, "
             'then you have to send a hero with a strength of at least x to '
             "kill it. If the dragon' s attack power is y, then the total "
             'strength of the heroes defending the castle should be at least '
             'y. The player can increase the strength of any hero by 1 for one '
             'gold coin. This operation can be done any number of times. There '
             'are m dragons in the game, the i- th of them has defense equal '
             'to xi and attack power equal to yi. Petya was wondering what is '
             'the minimum number of coins he needs to spend to defeat the i- '
             'th dragon. Note that the task is solved independently for each '
             'dragon ( improvements are not saved) .',
  'input': 'The first line contains a single integer n ( 2≤n≤2⋅105) — number '
           'of heroes. The second line contains n integers a1, a2, . . . , an '
           '( 1≤ai≤1012) , where ai is the strength of the i- th hero. The '
           'third line contains a single integer m ( 1≤m≤2⋅105) — the number '
           'of dragons. The next m lines contain two integers each, xi and yi '
           '( 1≤xi≤1012; 1≤yi≤1018) — defense and attack power of the i- th '
           'dragon.',
  'note': 'To defeat the first dragon, you can increase the strength of the '
          'third hero by 1, then the strength of the heroes will be equal to [ '
          '3, 6, 3, 3] . To kill the dragon, you can choose the first hero. To '
          'defeat the second dragon, you can increase the forces of the second '
          'and third heroes by 1, then the strength of the heroes will be '
          'equal to [ 3, 7, 3, 3] . To kill the dragon, you can choose a '
          'second hero. To defeat the third dragon, you can increase the '
          'strength of all the heroes by 1, then the strength of the heroes '
          'will be equal to [ 4, 7, 3, 4] . To kill the dragon, you can choose '
          "a fourth hero. To defeat the fourth dragon, you don' t need to "
          'improve the heroes and choose a third hero to kill the dragon. To '
          'defeat the fifth dragon, you can increase the strength of the '
          'second hero by 2, then the strength of the heroes will be equal to '
          '[ 3, 8, 2, 3] . To kill the dragon, you can choose a second hero.',
  'output': 'Print m lines, i- th of which contains a single integer — the '
            'minimum number of coins that should be spent to defeat the i- th '
            'dragon.',
  'title': 'Slay the Dragon',
  'topics': ['binary search', 'greedy', 'sortings', 'ternary search'],
  'url': 'https://codeforces.com/problemset/problem/1574/C'},
 {'history': 'Ivan is playing yet another roguelike computer game. He controls '
             'a single hero in the game. The hero has n equipment slots. There '
             'is a list of ci items for the i- th slot, the j- th of them '
             'increases the hero strength by ai, j. The items for each slot '
             'are pairwise distinct and are listed in the increasing order of '
             'their strength increase. So, ai, 1< ai, 2< ⋯< ai, ci. For each '
             'slot Ivan chooses exactly one item. Let the chosen item for the '
             'i- th slot be the bi- th item in the corresponding list. The '
             'sequence of choices [ b1, b2, . . . , bn] is called a build. The '
             'strength of a build is the sum of the strength increases of the '
             'items in it. Some builds are banned from the game. There is a '
             "list of m pairwise distinct banned builds. It' s guaranteed that "
             "there' s at least one build that' s not banned. What is the "
             'build with the maximum strength that is not banned from the '
             'game? If there are multiple builds with maximum strength, print '
             'any of them.',
  'input': 'The first line contains a single integer n ( 1≤n≤10) — the number '
           'of equipment slots. The i- th of the next n lines contains the '
           'description of the items for the i- th slot. First, one integer ci '
           '( 1≤ci≤2⋅105) — the number of items for the i- th slot. Then ci '
           'integers ai, 1, ai, 2, . . . , ai, ci ( 1≤ai, 1< ai, 2< ⋯< ai, '
           "ci≤108) . The sum of ci doesn' t exceed 2⋅105. The next line "
           'contains a single integer m ( 0≤m≤105) — the number of banned '
           'builds. Each of the next m lines contains a description of a '
           'banned build — a sequence of n integers b1, b2, . . . , bn ( '
           "1≤bi≤ci) . The builds are pairwise distinct, and there' s at least "
           "one build that' s not banned.",
  'note': ' ',
  'output': 'Print the build with the maximum strength that is not banned from '
            'the game. If there are multiple builds with maximum strength, '
            'print any of them.',
  'title': 'The Strongest Build',
  'topics': ['binary search',
             'brute force',
             'data structures',
             'dfs and similar',
             'graphs',
             'greedy',
             'hashing',
             'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1574/D'},
 {'history': 'A matrix of size n×m, such that each cell of it contains either '
             '0 or 1, is considered beautiful if the sum in every contiguous '
             'submatrix of size 2×2 is exactly 2, i. e. every " square" of '
             "size 2×2 contains exactly two 1' s and exactly two 0' s. You are "
             'given a matrix of size n×m. Initially each cell of this matrix '
             "is empty. Let' s denote the cell on the intersection of the x- "
             'th row and the y- th column as ( x, y) . You have to process the '
             'queries of three types: x y −1 — clear the cell ( x, y) , if '
             'there was a number in it; x y 0 — write the number 0 in the cell '
             '( x, y) , overwriting the number that was there previously ( if '
             'any) ; x y 1 — write the number 1 in the cell ( x, y) , '
             'overwriting the number that was there previously ( if any) . '
             'After each query, print the number of ways to fill the empty '
             'cells of the matrix so that the resulting matrix is beautiful. '
             'Since the answers can be large, print them modulo 998244353.',
  'input': 'The first line contains three integers n, m and k ( 2≤n, m≤106; '
           '1≤k≤3⋅105) — the number of rows in the matrix, the number of '
           'columns, and the number of queries, respectively. Then k lines '
           'follow, the i- th of them contains three integers xi, yi, ti ( '
           '1≤xi≤n; 1≤yi≤m; −1≤ti≤1) — the parameters for the i- th query.',
  'note': ' ',
  'output': 'For each query, print one integer — the number of ways to fill '
            'the empty cells of the matrix after the respective query, taken '
            'modulo 998244353.',
  'title': 'Coloring',
  'topics': ['combinatorics',
             'constructive algorithms',
             'implementation',
             'math'],
  'url': 'https://codeforces.com/problemset/problem/1574/E'},
 {'history': 'Andi and Budi were given an assignment to tidy up their '
             'bookshelf of n books. Each book is represented by the book title '
             '— a string si numbered from 1 to n, each with length m. Andi '
             'really wants to sort the book lexicographically ascending, while '
             'Budi wants to sort it lexicographically descending. Settling '
             'their fight, they decided to combine their idea and sort it asc- '
             'desc- endingly, where the odd- indexed characters will be '
             'compared ascendingly, and the even- indexed characters will be '
             'compared descendingly. A string a occurs before a string b in '
             'asc- desc- ending order if and only if in the first position '
             'where a and b differ, the following holds: if it is an odd '
             'position, the string a has a letter that appears earlier in the '
             'alphabet than the corresponding letter in b; if it is an even '
             'position, the string a has a letter that appears later in the '
             'alphabet than the corresponding letter in b.',
  'input': 'The first line contains two integers n and m ( 1≤n⋅m≤106) . The i- '
           'th of the next n lines contains a string si consisting of m '
           'uppercase Latin letters — the book title. The strings are pairwise '
           'distinct.',
  'note': 'The following illustrates the first example.',
  'output': 'Output n integers — the indices of the strings after they are '
            'sorted asc- desc- endingly.',
  'title': 'Another Sorting Problem',
  'topics': ['data structures', 'sortings', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1575/A'},
 {'history': 'The Winter holiday will be here soon. Mr. Chanek wants to '
             "decorate his house' s wall with ornaments. The wall can be "
             'represented as a binary string a of length n. His favorite '
             'nephew has another binary string b of length m ( m≤n) . Mr. '
             "Chanek' s nephew loves the non- negative integer k. His nephew "
             'wants exactly k occurrences of b as substrings in a. However, '
             'Mr. Chanek does not know the value of k. So, for each k ( '
             '0≤k≤n−m+ 1) , find the minimum number of elements in a that have '
             'to be changed such that there are exactly k occurrences of b in '
             'a. A string s occurs exactly k times in t if there are exactly k '
             'different pairs ( p, q) such that we can obtain s by deleting p '
             'characters from the beginning and q characters from the end of '
             't.',
  'input': 'The first line contains two integers n and m ( 1≤m≤n≤500) — size '
           'of the binary string a and b respectively. The second line '
           'contains a binary string a of length n. The third line contains a '
           'binary string b of length m.',
  'note': 'For k= 0, to make the string a have no occurrence of 101, you can '
          'do one character change as follows. 100101011 → 100100011For k= 1, '
          'you can also change a single character. 100101011 → 100001011For k= '
          '2, no changes are needed.',
  'output': 'Output n−m+ 2 integers — the ( k+ 1) - th integer denotes the '
            'minimal number of elements in a that have to be changed so there '
            'are exactly k occurrences of b as a substring in a.',
  'title': 'Holiday Wall Ornaments',
  'topics': ['dp', 'strings'],
  'url': 'https://codeforces.com/problemset/problem/1575/H'},
 {'history': 'Mr. Chanek has a new game called Dropping Balls. Initially, Mr. '
             'Chanek has a grid a of size n×mEach cell ( x, y) contains an '
             'integer ax, y denoting the direction of how the ball will move. '
             'ax, y= 1 — the ball will move to the right ( the next cell is ( '
             'x, y+ 1) ) ; ax, y= 2 — the ball will move to the bottom ( the '
             'next cell is ( x+ 1, y) ) ; ax, y= 3 — the ball will move to the '
             'left ( the next cell is ( x, y−1) ) . Every time a ball leaves a '
             'cell ( x, y) , the integer ax, y will change to 2. Mr. Chanek '
             'will drop k balls sequentially, each starting from the first '
             'row, and on the c1, c2, . . . , ck- th ( 1≤ci≤m) columns. '
             'Determine in which column each ball will end up in ( position of '
             'the ball after leaving the grid) .',
  'input': 'The first line contains three integers n, m, and k ( 1≤n, m≤1000, '
           '1≤k≤105) — the size of the grid and the number of balls dropped by '
           'Mr. Chanek. The i- th of the next n lines contains m integers ai, '
           '1, ai, 2, . . . , ai, m ( 1≤ai, j≤3) . It will satisfy ai, 1= ̸3 '
           'and ai, m= ̸1. The next line contains k integers c1, c2, . . . , '
           "ck ( 1≤ci≤m) — the balls' column positions dropped by Mr. Chanek "
           'sequentially.',
  'note': 'In the first example, the first ball will drop as follows. Note '
          'that the cell ( 1, 1) will change direction to the bottom '
          'direction. The second and third balls will drop as follows. All '
          'balls will be dropped from the first row and on the c1, c2, . . . , '
          'ck- th columns respectively. A ball will stop dropping once it '
          'leaves the grid.',
  'output': 'Output k integers — the i- th integer denoting the column where '
            'the i- th ball will end.',
  'title': 'Jeopardy of Dropped Balls',
  'topics': ['binary search', 'brute force', 'dsu', 'implementation'],
  'url': 'https://codeforces.com/problemset/problem/1575/J'},
 {'history': 'Mr. Chanek wants to knit a batik, a traditional cloth from '
             'Indonesia. The cloth forms a grid aa with size n×mn×m. There are '
             'kk colors, and each cell in the grid can be one of the kk '
             'colors. Define a sub- rectangle as an ordered pair of two cells '
             '( ( x1, y1) , ( x2, y2) ) ( ( x1, y1) , ( x2, y2) ) , denoting '
             'the top- left cell and bottom- right cell ( inclusively) of a '
             'sub- rectangle in aa. Two sub- rectangles ( ( x1, y1) , ( x2, '
             'y2) ) ( ( x1, y1) , ( x2, y2) ) and ( ( x3, y3) , ( x4, y4) ) ( '
             '( x3, y3) , ( x4, y4) ) have the same pattern if and only if the '
             'following holds: they have the same width ( x2−x1= x4−x3x2−x1= '
             'x4−x3) ; they have the same height ( y2−y1= y4−y3y2−y1= y4−y3) ; '
             'for every pair ( i, j) ( i, j) where 0≤i≤x2−x10≤i≤x2−x1 and '
             '0≤j≤y2−y10≤j≤y2−y1, the color of cells ( x1+ i, y1+ j) ( x1+ i, '
             'y1+ j) and ( x3+ i, y3+ j) ( x3+ i, y3+ j) are equal. Count the '
             'number of possible batik color combinations, such that the '
             'subrectangles ( ( ax, ay) , ( ax+ r−1, ay+ c−1) ) ( ( ax, ay) , '
             '( ax+ r−1, ay+ c−1) ) and ( ( bx, by) , ( bx+ r−1, by+ c−1) ) ( '
             '( bx, by) , ( bx+ r−1, by+ c−1) ) have the same pattern. Output '
             'the answer modulo 109+ 7109+ 7.',
  'input': 'The first line contains five integers nn, mm, kk, rr, and cc ( '
           '1≤n, m≤1091≤n, m≤109, 1≤k≤1091≤k≤109, 1≤r≤min( 106, n) 1≤r≤min( '
           '106, n) , 1≤c≤min( 106, m) 1≤c≤min( 106, m) ) — the size of the '
           'batik, the number of colors, and size of the sub- rectangle. The '
           'second line contains four integers axax, ayay, bxbx, and byby ( '
           '1≤ax, bx≤n1≤ax, bx≤n, 1≤ay, by≤m1≤ay, by≤m) — the top- left '
           'corners of the first and second sub- rectangle. Both of the sub- '
           'rectangles given are inside the grid ( 1≤ax+ r−11≤ax+ r−1, bx+ '
           'r−1≤nbx+ r−1≤n, 1≤ay+ c−11≤ay+ c−1, by+ c−1≤mby+ c−1≤m) .',
  'note': 'The following are all 3232 possible color combinations in the first '
          'example.',
  'output': 'Output an integer denoting the number of possible batik color '
            'combinations modulo 109+ 7109+ 7.',
  'title': 'Knitting Batik',
  'topics': ['implementation', 'math'],
  'url': 'https://codeforces.com/problemset/problem/1575/K'},
 {'history': 'Mr. Chanek gives you a sequence a indexed from 1 to n. Define f( '
             'a) as the number of indices where ai= i. You can pick an element '
             'from the current sequence and remove it, then concatenate the '
             'remaining elements together. For example, if you remove the 3- '
             'rd element from the sequence [ 4, 2, 3, 1] , the resulting '
             'sequence will be [ 4, 2, 1] . You want to remove some elements '
             'from a in order to maximize f( a) , using zero or more '
             'operations. Find the largest possible f( a) .',
  'input': 'The first line contains one integer n ( 1≤n≤2⋅105) — the initial '
           'length of the sequence. The second line contains n integers a1, '
           'a2, . . . , an ( 1≤ai≤2⋅105) — the initial sequence a.',
  'note': 'In the first example, f( A) = 3 by doing the following operations. '
          '[ 2, 1, 4, 2, 5, 3, 7] →[ 2, 1, 2, 5, 3, 7] →[ 1, 2, 5, 3, 7] →[ 1, '
          '2, 5, 3] →[ 1, 2, 3] In the second example, f( A) = 2 and no '
          'additional operation is needed.',
  'output': 'Output an integer denoting the largest f( a) that can be obtained '
            'by doing zero or more operations.',
  'title': 'Longest Array Deconstruction',
  'topics': ['data structures', 'divide and conquer', 'dp', 'sortings'],
  'url': 'https://codeforces.com/problemset/problem/1575/L'},
 {'history': 'Eonathan Eostar decided to learn the magic of multiprocessor '
             'systems. He has a full binary tree of tasks with height hh. In '
             'the beginning, there is only one ready task in the tree — the '
             'task in the root. At each moment of time, pp processes choose at '
             'most pp ready tasks and perform them. After that, tasks whose '
             'parents were performed become ready for the next moment of time. '
             'Once the task becomes ready, it stays ready until it is '
             'performed. You shall calculate the smallest number of time '
             'moments the system needs to perform all the tasks.',
  'input': 'The first line of the input contains the number of tests tt ( '
           '1≤t≤5⋅1051≤t≤5⋅105) . Each of the next tt lines contains the '
           'description of a test. A test is described by two integers hh ( '
           '1≤h≤501≤h≤50) and pp ( 1≤p≤1041≤p≤104) — the height of the full '
           'binary tree and the number of processes. It is guaranteed that all '
           'the tests are different.',
  'note': 'Let us consider the second test from the sample input. There is a '
          'full binary tree of height 33 and there are two processes. At the '
          'first moment of time, there is only one ready task, 11, and p1p1 '
          'performs it. At the second moment of time, there are two ready '
          'tasks, 22 and 33, and the processes perform them. At the third '
          'moment of time, there are four ready tasks, 44, 55, 66, and 77, and '
          'p1p1 performs 66 and p2p2 performs 55. At the fourth moment of '
          'time, there are two ready tasks, 44 and 77, and the processes '
          'perform them. Thus, the system spends 44 moments of time to perform '
          'all the tasks.',
  'output': 'For each test output one integer on a separate line — the '
            'smallest number of time moments the system needs to perform all '
            'the tasks.',
  'title': 'Easy Scheduling',
  'topics': ['implementation', 'math'],
  'url': 'https://codeforces.com/problemset/problem/1578/E'}]

def getAllProblems(onlyThisTopics = []):
  """
  Dummy client, given certain topics returns data only with those topics
  """
  if len(onlyThisTopics):
    for problem in staticProblems:
      problem['topics'] = [topic for topic in problem['topics'] if topic in onlyThisTopics]

  return staticProblems


# pprint(getAllProblems()[:5])
# pprint(getAllProblems(['implementation', 'sortings', 'strings'])[:5])