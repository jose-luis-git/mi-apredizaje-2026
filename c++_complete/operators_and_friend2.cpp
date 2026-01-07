#include<iostream>
#include<cmath>
#include<stdexcept>

class Rectangle{
	private:
		float broad, high;
	public:
		Rectangle(float _broad,float _high) : broad(_broad), high(_high){}
		~Rectangle();
		void setBroad(float);
		void setHigh(float);
		float getBroad() const;
		float getHigh() const;
		bool operator == (const Rectangle&) const;
		Rectangle operator * (float) const;
		Rectangle operator + (const Rectangle&) const;
		float& operator[](int);
		const float& operator[](int) const;
		friend std::ostream& operator << (std::ostream&,const Rectangle&);
};

void Rectangle::setBroad(float _broad){
	broad = _broad;
}
void Rectangle::setHigh(float _high){
	high = _high;
}
float Rectangle::getBroad() const{
	return broad;
}
float Rectangle::getHigh() const{
	return high;
}
bool Rectangle::operator == (const Rectangle&r) const{
	return std::fabs(broad - r.broad) < 0.0001f &&
		   std::fabs(high - r.high) < 0.0001f;
}
Rectangle Rectangle::operator * (float scale) const{
	return Rectangle(broad*scale, high*scale);
}
Rectangle Rectangle::operator + (const Rectangle&other) const{
	return Rectangle(broad + other.broad, high + other.high);
} 
std::ostream& operator << (std::ostream&os, const Rectangle&r){
	os<<"Broad: "<<r.broad<<" | High: "<<r.high;
	return os;
}
float&Rectangle::operator[](int index){
	if(index == 0) return broad;
	if(index == 1) return high;
	throw std::out_of_range("Rectangle index out of range");
}
const float&Rectangle::operator[](int index) const{
	if(index == 0) return broad;
	if(index == 1) return high;
	throw std::out_of_range("Rectangle index out of range");
}

int main(){
	Rectangle r1(12, 45);
	Rectangle r2(12, 45);
	Rectangle r3 = r1 + r2;
	
	if(r1 == r2){
		std::cout<<"The rectangles one and two are the same"<<std::endl;
	}else{
		std::cout<<"The rectangles are not the same"<<std::endl;
	}
	
	std::cout<<r3<<std::endl;
	
	
	//with operator[]
	std::cout<<"\n\n\n\n\n\n\n"<<std::endl;
	
	Rectangle r4(23, 56);
	std::cout<<r4[0]<<std::endl;
	std::cout<<r4[1]<<std::endl;
	
	r4[0] = 45;
	
	std::cout<<r4[0]<<std::endl;
	
	return 0;
}