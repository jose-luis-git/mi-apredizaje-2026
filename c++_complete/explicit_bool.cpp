#include<iostream>

class Socket{
	private:
		bool connected;
	public:
		explicit Socket(bool c) : connected(c){}
		explicit operator bool() const;	
		friend std::ostream& operator << (std::ostream&, const Socket&);
};
Socket::operator bool() const{
	return connected;
}

std::ostream& operator << (std::ostream&os, const Socket&s){
	if(s.connected){
		os<<"Connected";
	}else{
		os<<"Unplugged";
	}
	
	return os;
}

int main(){
	// no funciona = Sockect s = true;
	//tampoco int a = s;
	Socket s1(false);
	Socket s2(true);
	
	std::cout<<s1<<std::endl;
	std::cout<<s2<<std::endl;
	
	if(s1){
		std::cout<<"Socked OK"<<std::endl;
	}
	if(s2){
		std::cout<<"Socked OK"<<std::endl;
	}
	
	return 0;
}