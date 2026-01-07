#include<iostream>

class Temperature{
	private:
		double celcius;
	public:
		explicit Temperature(double c) : celcius(c){}
		friend std::ostream& operator << (std::ostream&, const Temperature&);
};

std::ostream& operator << (std::ostream&os, const Temperature&t){
	os<<"Temperature: "<<t.celcius<<" celcius";
	return os;
}

int main(){
	Temperature t(2);
	
	std::cout<<t<<std::endl;
	
	return 0;
}