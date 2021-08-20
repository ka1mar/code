// Разминка-3.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
using namespace std;

class Complex
{
public:
    Complex(double realPart = 0, double imaginaryPart = 0)
     {
         this->realPart = realPart;
         this->imaginaryPart = imaginaryPart;
     };
    void enterComplex()
     {
        double x = 0;
        double y = 0;
        cout << "Enter Complex: ";
        cin >> x >> y;
        this->realPart = x;
        this->imaginaryPart = y;
       
     };
    void printComplex()
    {
        cout << this->realPart << " + " << this->imaginaryPart << "i ";
    };
    Complex& operator=(Complex const& a)
    {
        if (this != &a)
        {
            realPart = a.realPart;
            imaginaryPart = a.imaginaryPart;
        };
        return *this;
    };
    double getReal() const {
        return realPart;
    };
    double getImaginary() const {
        return imaginaryPart;
    };
private:
     double realPart;
     double imaginaryPart;
};

Complex operator+(Complex const& a, Complex const& b)
{
    return Complex(a.getReal() + b.getReal(), a.getImaginary() + b.getImaginary());
};
Complex operator-(Complex const& a, Complex const& b)
{
    return Complex(a.getReal() - b.getReal(), a.getImaginary() - b.getImaginary());
};
Complex operator*(Complex const& a, Complex const& b)
{
    return Complex(a.getReal() * b.getReal() - a.getImaginary() * b.getImaginary(), a.getImaginary() * b.getReal() + b.getImaginary() * a.getReal());
};
Complex operator/(Complex const& a, Complex const& b)
{
    return Complex((a.getReal() * b.getReal() + a.getImaginary() * b.getImaginary()) / (b.getReal() * b.getReal() + b.getImaginary() * b.getImaginary()), (b.getReal() * a.getImaginary() - b.getImaginary() * a.getReal()) / (b.getReal() * b.getReal() + b.getImaginary() * b.getImaginary()));
};

int main()
{
    Complex * A = new Complex;
   // A->enterComplex();
    //A.printComplex();
    Complex * B = new Complex;
    //B->enterComplex();
    *A = *A + *B;
    Complex C = 20;
    C.printComplex();
    Complex D(5);
    //A->printComplex();
    //D.printComplex();

}


