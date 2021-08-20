#include <iostream>
#include <fstream>
#include <stdexcept>
#include <vector>

using namespace std;

class Matrix{
public:
	Matrix(){
		rows=0;
		cols=0;
	}
	Matrix(int r, int c){
		if(r<0||c<0) throw out_of_range("out of range");
	
	else{
		rows=r;
		cols=c;
		vector <int> v;
		v.assign(c, 0);
		for(int i=0; i<r; i++)
			matrix.push_back(v);
	}
	}
	void Reset(int r, int c){
		if(r<0||c<0) throw out_of_range("out of range");
		matrix.clear();
		rows=r;
		cols=c;
		vector <int> v;
		v.assign(c, 0);
		for(int i=0; i<r; i++)
			matrix.push_back(v);
	
	}
	int At(int r, int c) const{
	//	if(r>=rows||c>=cols || r<0||c<0) throw out_of_range("out of range");
		return matrix.at(r).at(c);
	}
	int&  At(int r, int c) {
		if(r>=rows||c>=cols|| r<0||c<0) throw out_of_range("out of range");
		return matrix[r][c];
	}
	int GetNumRows() const {
		return rows;
	}
	
	int GetNumColumns() const {
		return cols;
	} 
private:
		vector<vector<int>> matrix;
		int rows;
		int cols;
};

bool operator==(const Matrix& l, const Matrix &r){
	if((l.GetNumRows()==0 || l.GetNumColumns()==0) && (r.GetNumRows()==0 || r.GetNumColumns()==0))return true;
	if(l.GetNumRows()!=r.GetNumRows() 
		|| l.GetNumColumns()!=r.GetNumColumns()) return false;
	for (int i=0; i<l.GetNumRows(); i++)
		for (int j=0; j<l.GetNumColumns();j++)
			if(l.At(i, j)!=r.At(i,j)) return false;
	return true;
}


ostream& operator<<(ostream& stream, const Matrix & m) {
	if(m.GetNumRows()==0 || m.GetNumColumns()==0) return stream;
	stream<<m.GetNumRows()<<' '<<m.GetNumColumns()<<endl;
for (int i=0; i<m.GetNumRows(); i++){
		for (int j=0; j<m.GetNumColumns();j++)
			stream<<m.At(i,j)<<' ';
			
			if( i!=m.GetNumRows()-1)stream<<endl;
		}
return stream;
}

istream& operator >> (istream& stream, Matrix & m) {
	
    int r, c;
    stream>>r>>c;
     m.Reset(r ,c);
    if(r==0 || c==0)
    //	cout<<m.GetNumRows()<<' '<<m.GetNumColumns()<<endl;
	return stream;
    
   for (int i=0; i<r; i++)
		for (int j=0; j<c;j++)
			stream>>m.At(i,j);
    return stream;
}

Matrix operator+(const Matrix& l, const Matrix &r){
		if((l.GetNumRows()==0 || l.GetNumColumns()==0) && (r.GetNumRows()==0 || r.GetNumColumns()==0))return Matrix();

	if(l.GetNumRows()!=r.GetNumRows() 
		|| l.GetNumColumns()!=r.GetNumColumns())throw  invalid_argument("zises're not equal'");
	Matrix sum(l.GetNumRows(),r.GetNumColumns());
	for (int i=0; i<l.GetNumRows(); i++)
		for (int j=0; j<l.GetNumColumns();j++)
			sum.At(i,j)=l.At(i,j)+r.At(i,j);	
	return sum;
}

/* int main(){
	//std::cout << std::boolalpha << (Matrix(0, 1) == Matrix(2, 0)) << '\n';
	Matrix a;
	cin>>a;
	cout<<endl;
	cout<<a<<endl;
	a.Reset(1,2);
	//	cout<<a.GetNumRows()<<' '<<a.GetNumColumns()<<endl;
	cout<<a;
	return 0;
}
*/ 
