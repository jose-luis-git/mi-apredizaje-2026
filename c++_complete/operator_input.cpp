#include<iostream>
#include<stdexcept>
#include<string>
#include<vector>

class User{
	private:
		std::string name, email;
	public:
		User(const std::string&n,const std::string&e) : name(n), email(e){}
		explicit User(const std::string&e) : name(""), email(e){}
		void setName(const std::string&);
		void setEmail(const std::string&);
		std::string getName() const;
		std::string getEmail() const;
		User operator + (const User&) const;
		bool operator == (const User&) const;
		std::string& operator[](int);
		const std::string& operator[](int) const;
		friend std::ostream& operator << (std::ostream&, const User&);
		friend std::istream& operator >> (std::istream&, User&);
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
User User::operator + (const User&other) const{
	return User(name + " & " + other.name, "combined");
}
bool User::operator == (const User&u) const{
	return email == u.email;
}
std::string&User::operator[](int index){
	if(index == 0) return name;
	if(index == 1) return email;
	throw std::out_of_range("User index out of range");
}
const std::string&User::operator[](int index) const{
	if(index == 0) return name;
	if(index == 1) return email;
	throw std::out_of_range("User index out of range");
}
std::ostream&operator << (std::ostream&os, const User&u){
	os<<"Nombre: "<<u.name<<" | email: "<<u.email;
	return os;
}
std::istream&operator >> (std::istream&is, User&u){
	std::cout<<"Enter name: ";
	std::getline(is, u.name);
	std::cout<<"Enter email: ";
	std::getline(is, u.email);
	
	return is;
}

User User::createFromInput(){
	User u("", "");
	std::cin>>u;
	return u;
}

int main(){
	std::vector<User> users;
	
	users.push_back(User::createFromInput());
	users.push_back(User::createFromInput());
	users.push_back(User::createFromInput());
	
	for(const auto&u : users){
		std::cout<<u<<std::endl;
	}
	
	User combined = users[0] + users[1];
	std::cout<<"Combined: "<<combined<<std::endl;
	
	std::cout<<"First user name: "<<users[0][0]<<std::endl;
	
	if(users[0][1] == users[1][1]){
		std::cout<<"Same email"<<std::endl;
	}else if(users[0][1] == users[2][1]){
		std::cout<<"Same email"<<std::endl;
	}else{
		std::cout<<"Diferrents emails"<<std::endl;
	}
	
	//User u = "nuevoemail@gmail.com" == error
	User u("NewEmail@gmail.com");
	std::cout<<u<<std::endl;
	
	return 0;
}