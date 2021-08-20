#include<map>
#include<iomanip>
#include<set>
#include<string>
#include<exception>
#include<iostream>
#include<sstream>
#include <locale>
#include <cctype> 

using namespace std;


class Date {
public:
  int GetYear() const{
  return year;
  };
  int GetMonth() const{
  return month;
  };
  int GetDay() const{
  return day;
  };
  
  Date(int y, int m, int d){
  	year=y;
  	month=m;
  	day=d;
  }
  Date()
  {
  	year=0; month=0; day=0;
  }
  private:
  	int year;
  	int month;
  	int day;
};

bool operator<(const Date& lhs, const Date& rhs){
	if (lhs.GetYear()<rhs.GetYear()) return true;
	if(lhs.GetYear()>rhs.GetYear()) return false;
	if(lhs.GetMonth()<rhs.GetMonth()) return true;
	if(lhs.GetMonth()>rhs.GetMonth()) return false;
	if(lhs.GetDay()<rhs.GetDay()) return true;
	if(lhs.GetDay()>rhs.GetDay()) return false;
};

istream& operator >> (istream& stream, Date & date) {
    int y, m, d;
    char c1, c2;
    string str;
    stream.ignore(1);
    getline(stream, str, ' ');
    //cout<<str;
    istringstream inp (str);
    //cout<<str;
    try{
    if (inp >> y && inp >> c1 && inp >> m && inp>>c2 && inp>> d) {
    	if(m>12 ||m<1) throw("month_ex");
    	if(d>31 || d<1) throw("day_ex");
    	if(c1!='-' || c2 !='-' ) throw("wrong_date");
    	if(ispunct(inp.peek()) ||  isalpha(inp.peek())) throw ("wrong_date");
        date = Date(y, m, d);
       // cout<<str<<endl;
       // c//out<<d<<endl;
        //cout<<end<<endl;
    }
    else throw("wrong_date");
	}
	catch(const char* exception){
	
		if(exception == "month_ex")
		cout<<"Month value is invalid: "<<m<<endl;
		if(exception == "day_ex")
		cout<<"Day value is invalid: "<<d<<endl;
		if(exception=="wrong_date")
		cout<<"Wrong date format: "<< str<<endl;
	
	}
	
    return stream;
}


class Database {
public:
  void AddEvent(const Date& date, const string& event){
  	data[date].insert(event);
  	
  };
  bool DeleteEvent(const Date& date, const string& event){
  	if(data.count(date)==0)return false;
  	if(data.at(date).count(event)==1){
  		data.at(date).erase(event);
  		return true;
	  }
	  return false;
  };
  int  DeleteDate(const Date& date){
  	int N=0;
  	if (!data.count(date)==0){
	N = data.at(date).size();
  	data.erase(date);
     }
  	return N;
  };

  bool Find(const Date& date) const{
  if(data.count(date)==0) return false;
  for (const string & s :data.at(date))
  cout<<s<<endl;
  return true;
  };
  
  void Print() const{
  for(const auto & p:data){
  	for (const string & s:data.at(p.first))
  	{
  	cout<<setw(4)<<setfill('0')<<p.first.GetYear()<<'-';
  	cout<<setw(2)<<setfill('0')<<p.first.GetMonth()<<'-';
  	cout<<setw(2)<<setfill('0')<<p.first.GetDay()<<' ';
  	cout<<s<<endl;
 	 }
  }
}
  private:
  map<Date,set<string>> data;
};

int main() {
  Database db;
  string command;
  while (getline(cin, command)) {
  	istringstream input (command);
  	string id;
  	input>>id;
    if(id=="Add"){
    
    try{
	Date cur_date={-1,-1,-1};
		input>>cur_date;
		if(cur_date.GetDay()==-1) break;
    	string event;
    	input>>event;
    	db.AddEvent(cur_date, event);
	}
	catch(exception){}
    
	}
	else if(id=="Print") db.Print();
	else if(id=="Find"){
	try{
		Date cur_date={-1,-1,-1};
		input>>cur_date;
		if(cur_date.GetDay()==-1) break;
		
    	db.Find(cur_date);
     }
    catch(exception){}
	}
	else if(id=="Del"){
		try{
	    Date cur_date={-1,-1,-1};
		input>>cur_date;
		if(cur_date.GetDay()==-1) break;
	//	input.ignore(1);
		if(input.eof()) {
		int N = db.DeleteDate(cur_date);
		cout<<"Deleted "<<N<<" events"<<endl;
		}
		else {
			string event;
			input>>event;
			if(db.DeleteEvent(cur_date, event)) cout<<"Deleted successfully"<<endl;
			else cout<<"Event not found"<<endl;
		}
	}
	catch(exception){}
	}
	
	else if(command.length()==0);
	else cout<<"Unknown command: "<<id<<endl;
	
  }
  
  //db.Print();

  return 0;
}
