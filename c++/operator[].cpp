#include<iostream>
#include<stdexcept>
#include<string>

class User{
	private:
		std::string name, email;
	public:
		User(const std::string&_name, const std::string&_email) : name(_name), email(_email){}
		void setName(const std::string&);
		void setEmail(const std::string&);
		std::string getName() const;
		std::string getEmail() const;
		bool operator == (const User&) const;
		User operator + (const User&) const;
		std::string& operator[](int);
		const std::string&operator[](int) const;
		friend std::ostream& operator << (std::ostream&,const User&);
		static User createFromInput();
};

void User::setName(const std::string&_name){
	name = _name; 
}
void User::setEmail(const std::string&_email){
	email = _email;
}
std::string User::getName() const{
	return name;
}
std::string User::getEmail() const{
	return email;
}
bool User::operator == (const User&u) const{
	return email == u.email;
} 
User User::operator + (const User&other) const{
	return User(name + " & " +other.name, "combined");
} 
std::string& User::operator[](int index){
	if(index == 0) return name;
	if(index == 1) return email;
	throw std::out_of_range("User index out of range");
} 
const std::string&User::operator[](int index) const{
	if(index == 0) return name;
	if(index == 1) return email;
	throw std::out_of_range("User index out of range");
}
std::ostream& operator << (std::ostream&os, const User&u){
	os<<"Name: "<<u.name<<" | Email: "<<u.email;
	return os;
}
User User::createFromInput(){
	std::string name,email;
	
	std::cout<<"Enter name: "; 
	std::getline(std::cin, name);
	std::cout<<"Enter email: ";
	std::getline(std::cin, email);
	
	return User(name, email);
}


int main(){
	User user1("Jose", "Programador@gmail.com");
	User user2("Mario", "MarioBro@gmail.com");
	
	std::cout<<user1<<std::endl;
	std::cout<<user2<<std::endl;
	
	if(user1 == user2){
		std::cout<<"The names and emils are same"<<std::endl;
	}else{
		std::cout<<"The names and emails are not same"<<std::endl;
	}
	
	User user3 = user1 + user2;
	
	std::cout<<user3<<std::endl;
	
	User user4 = User::createFromInput();
	std::cout<<user4<<std::endl;
	
	return 0;
}