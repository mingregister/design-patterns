package main 
                        
import ( 
    "./singleton"
) 
                        
func main() { 
    mSingleton, nSingleton := singleton.NewSingleton("hello"), singleton.NewSingleton("hi") 
    mSingleton.SaySomething() 
    nSingleton.SaySomething() 
}