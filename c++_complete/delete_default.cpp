#include<iostream>
#include<vector>

class SafeVector{
	private:
		std::vector<int> data;
	public:
		explicit SafeVector(size_t n) : data(n, 0){}
		SafeVector(const SafeVector&) = delete;
		SafeVector& operator =  (const SafeVector&) = delete;
		SafeVector(SafeVector&&) = default;
		SafeVector& operator = (SafeVector&&) = default;
		size_t size() const;
};
size_t SafeVector::size() const{
	return data.size();
}

int main(){
	SafeVector sv(5);
	
	std::cout<<"Size vector: "<<sv.size()<<std::endl;
	
	return 0;
}