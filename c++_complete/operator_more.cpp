#include<iostream>
#include<vector>
#include<string>
#include<exception>
#include<stdexcept>
#include<cmath>

class BanckAccount{
	private:
		std::string owner;
		double balance;
	public:
		BanckAccount(const std::string&o, double b): owner(o), balance(b){}
		explicit BanckAccount(const std::string&o): owner(o), balance(0){}
		~BanckAccount() = default;
		void setOwner(const std::string&);
		void setBalance(double);
		std::string getOwner() const;
		double getBalance() const;
		BanckAccount(const BanckAccount&) = delete;
		BanckAccount&operator = (const BanckAccount&) = delete;
		BanckAccount(BanckAccount&&) = default;
		BanckAccount&operator = (BanckAccount&&) = default;
		BanckAccount operator + (const BanckAccount&) const;
		BanckAccount operator - (const BanckAccount&) const;
		BanckAccount operator * (const BanckAccount&) const;
		BanckAccount operator / (const BanckAccount&) const;
		bool operator == (const BanckAccount&) const;
		bool operator < (const BanckAccount&) const;
		bool operator > (const BanckAccount&) const;
		bool operator != (const BanckAccount&) const;
		std::string operator[] (int);
		const std::string operator[](int) const;
		friend std::ostream&operator << (std::ostream&,const BanckAccount&);
		friend std::istream&operator >> (std::istream&, BanckAccount&);
		static BanckAccount createFromInput();
};
void BanckAccount::setOwner(const std::string&_owner){
	owner = _owner;
}
void BanckAccount::setBalance(double _balance){
	balance = _balance;
}
std::string BanckAccount::getOwner() const{
	return owner;
}
double BanckAccount::getBalance() const{
	return balance;
}
BanckAccount BanckAccount::operator + (const BanckAccount&other) const{
	return BanckAccount("Combined owner", balance + other.balance);
}
BanckAccount BanckAccount::operator - (const BanckAccount&other) const{
	return BanckAccount("Combined owner", balance - other.balance);
}
BanckAccount BanckAccount::operator * (const BanckAccount&other) const{
	return BanckAccount("Combined owner", balance * other.balance);
}
BanckAccount BanckAccount::operator / (const BanckAccount&other) const{
	if(other.balance == 0) throw std::runtime_error("Division by zero!");
	return BanckAccount("Combined owner", balance / other.balance);
}
std::string BanckAccount::operator[](int index){
	if(index == 0) return owner;
	
	throw std::out_of_range("The index exceeds the limit");
}
const std::string BanckAccount::operator[](int index) const{
	if(index == 0) return owner;
	
	throw std::out_of_range("The index exceeds the limit");
}
bool BanckAccount::operator == (const BanckAccount&ba) const{
	return std::fabs(balance - ba.balance) < 0.0001f;
}
bool BanckAccount::operator < (const BanckAccount&ba) const{
	return balance < ba.balance;
}
bool BanckAccount::operator > (const BanckAccount&ba) const{
	return balance > ba.balance;
}
bool BanckAccount::operator != (const BanckAccount&ba) const{
	return balance != ba.balance;
}
std::ostream& operator << (std::ostream&os, const BanckAccount&ba){
	os<<"Owner: "<<ba.owner<<"\nBalance: "<<ba.balance;
	return os;
}
std::istream& operator >> (std::istream&is,BanckAccount&ba){
	std::string owner;
	double balance;
	
	std::cout<<"Enter a owner: "; is>>owner;
	std::cout<<"Enter a balance: "; is>>balance;
	
	ba.owner = owner;
	ba.balance = balance;
	
	return is;
}
BanckAccount BanckAccount::createFromInput(){
	BanckAccount ba("", 0.0);
	std::cin>>ba;
	
	return ba;
}

int main(){
	//operator >>
	BanckAccount ba1 = BanckAccount::createFromInput();
	std::cout<<std::endl;
	BanckAccount ba2 = BanckAccount::createFromInput();
	std::cout<<std::endl;
	BanckAccount ba3 = BanckAccount::createFromInput();
	std::cout<<std::endl;
	
	//operator ==
	if(ba1 == ba2){
		std::cout<<"Account 1 and 2 have the same amout money"<<std::endl;
	}else{
		std::cout<<"Account 1 and 2 do not have the same amount money"<<std::endl;
	}
	std::cout<<std::endl;
	//operator < and >
	if((ba1 > ba2) && (ba1 > ba2)){
		std::cout<<"The balance of account 1 is higher"<<std::endl;
	}else if((ba2 > ba1) && (ba2 > ba3)){
		std::cout<<"The balance of account 2 is higher"<<std::endl;
	}else{
		std::cout<<"The balance of account 3 is higher"<<std::endl;
	}
	std::cout<<std::endl;
	//operator !=
	if(ba3 != ba1){
		std::cout<<"Account 3 and 1 do not have the same amount money"<<std::endl;
	}else{
		std::cout<<"Accoutn 3 and 1 have the same amount money"<<std::endl;
	}
	
	//operator +
	BanckAccount ba4 = ba1 + ba2;
	//operator -
	BanckAccount ba5 = ba1 - ba2;
	//operator *
	BanckAccount ba6 = ba1 * ba2;
	//operator /
	BanckAccount ba7 = ba1 / ba2;
	
	//operator <<
	
	std::cout<<"The sum account1 and account2: "<<ba4<<std::endl;
	std::cout<<"The rest accoutn1 and account2: "<<ba5<<std::endl;
	std::cout<<"The multiplication accoutn1 and account2: "<<ba6<<std::endl;
	std::cout<<"The division account1 and account2: "<<ba7<<std::endl;
	BanckAccount ban("j", 1);
	BanckAccount ban1("jo", 1);
	BanckAccount ban2("jos", 1);
	
// 	this works
//	BanckAccount ban3 = ban+ ban1 + ban2;
//	
//	std::cout<<ban3<<std::endl;
//
//	
//	std::cout<<b<<std::endl;
	
	
	std::cout<<std::endl;
	std::cout<<"Testing operator[]"<<std::endl;
	std::cout<<"Owner BanckAccoutn1: "<<ba1[0]<<std::endl;
	std::cout<<"Balance BanckAccount1: "<<ba1[1]<<std::endl;
	
	return 0;
}