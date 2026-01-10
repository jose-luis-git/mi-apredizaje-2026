#include<iostream>
#include<string>
#include<memory>

class FileSimulator{
	private:
		std::string phrase;
	public:
		FileSimulator(const std::string&_phrase="File opened") : phrase(_phrase){
			std::cout<<phrase<<std::endl;
		}	
		~FileSimulator(){
			std::cout<<"File closed"<<std::endl;
		}
};

int main(){
	{
		std::unique_ptr<FileSimulator> fileSimulator = std::make_unique<FileSimulator>();
		std::cout<<"Doing work...."<<std::endl;
	}
	
	std::cout<<"Program ended"<<std::endl;
	
	
	return 0;
}