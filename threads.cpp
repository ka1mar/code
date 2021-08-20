#include <iostream>
#include <vector>
#include <thread>
#include <iomanip>
#include <chrono>
using namespace std;



ostream& operator <<(ostream &out, const vector<vector<int>> & v){
	for (const auto & a : v) {
		for (const auto & b : a)
			out<<setw(3)<<b<<' ';
	out<<endl;	
	}
	return out;
}

 class Sign{
 public:	
 int upd(){
 		if (sign == 1) sign = -1;
 		else sign = 1;
 		return sign;
	 }
 	int sign = 1;
};


    
vector<vector<int>> getMinor(const vector<vector<int>> & m, int index){
   		int size = m.size();
   		vector<vector<int>> minor;
   		for (int j = 0; j < size; j++) {
   			vector<int> v (m[j].begin()+1, m[j].end());
   	    	if (j != index) 
				minor.push_back(v);
			}
	return minor;
}
    
    
int determinant(const vector<vector<int>> & m, int size){
   	int return_value=0;
   	Sign sign;
   	if (size==2) return m[0][0]*m[1][1]-m[0][1]*m[1][0];
   	for (int i = 0; i<size; i++) {
   		vector<vector<int>> minor = getMinor(m, i);	
		return_value += sign.upd()*m[i][0]*determinant(minor, size-1);
		}
	
	return return_value;    	
}



int main(){

	int size = 4;
	vector<int> det_minor(size);
	vector<vector<int>> b = {{ 1, 2, 3, 4},
							{5,6, 7, 8 },
							{2, 3, 2, 3},
							{4, 4, 4, 7}};
 vector<thread> threads;
 
auto start = chrono::system_clock::now();
 
for(int i = 0; i<size; i++) {
auto minor = getMinor(b, i);
threads.push_back(thread([ &det_minor, i, minor, size](){
	det_minor[i] = determinant(minor, size-1);}));
	}


for(auto& t : threads) {
t.join();
}

int result = 0;
for(int i =0; i<size; i++) {
int r= (det_minor[i])*(b[i][0]);
if(i % 2 == 0)result = result+ r;
else result=result - r;
}

//int result = determinant(b, size);

auto end = chrono::system_clock::now();
chrono::duration<double> worktime = end - start;


     cout<< "det= "<<result<<endl;
	 cout<<"time: "<<worktime.count();
    
	return 0;
}
