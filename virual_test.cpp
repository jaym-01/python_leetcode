#include<iostream>

// this code shows that removing the virtual keyword
// causes the base class function to be class -> when publicaly inherited

class base {
    public:
        virtual void tmp_func(){
            std::cout << "this is in the base class" << std::endl;
        }
};

class child: public base{
    public:
        void tmp_func(){
            std::cout << "this is in the child class" << std::endl;
        }
};

int main(){
    base *b1 = new base();

    base *c1 = new child();

    b1->tmp_func();
    c1->tmp_func();

    delete b1;
    delete c1;

    return 0;
}