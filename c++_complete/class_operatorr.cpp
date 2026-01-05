#include<iostream>

class Vector2D{
	private:
		int x,y;
	public:
		Vector2D(int _x,int _y) : x(_x), y(_y){}
		~Vector2D();
		void setX(int);
		void setY(int);
		int getX() const;
		int getY() const;
		Vector2D operator+(const Vector2D&) const;
		friend void mostrar(const Vector2D&);
};
Vector2D::~Vector2D(){}

void Vector2D::setX(int _x){
	x = _x;
}
void Vector2D::setY(int _y){
	y = _y;
}
int Vector2D::getX() const{
	return x;
}
int Vector2D::getY() const{
	return y;
}

Vector2D Vector2D::operator+(const Vector2D&other) const {
	return Vector2D(x + other.x, y + other.y);
}
void mostrar(const Vector2D&v){
	std::cout<<"("<<v.x<<", "<<v.y<<")"<<std::endl;
}


int main(){
	Vector2D v1(2, 3);
	Vector2D v2(3, 5);
	
	mostrar(v1);
	mostrar(v2);
	
	Vector2D v3 = v1 + v2;
	
	mostrar(v3);
	
	
	
	return 0;
}