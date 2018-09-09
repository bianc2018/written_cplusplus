#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector<string> ch;
int main()
{
    string word="";
    while(cin>>word)
    {
		cout<<word<<endl;
        int s = ch.size();
        bool flag = true;
        for(int i=0;i<s;i++)
		{
            if (word==ch[i])
			{	
				flag = false;
                break;
			}
		}
        if (flag)
        ch.push_back(word);
    }
    cout<<ch.size();
    return 0;
}