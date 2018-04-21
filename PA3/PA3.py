# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:23:35 2017

@author: jkinya1
"""

#   This code is a DFA machine which tests different words in an alphabet 
#   {a,b}* and only accepts words that are in the language L by returning 
#   true andrejects words that are not in the language by returning false


#begin by defining the DFA object in as a class

class DFA:
    #a variable for present state in the DFA machine
    Qpresent = None;
    
#    DFA constructor _INIT_ builds the DFA object by: Initialing the 
#    elements of the DFA machine according to the variables
#    passed by the caller(self). It also introcudes a 6th element
#    :Qpresent which will help track a word being tested from  
#    initial state Q0 to final state Qf or to a state Qx where
#    the word is exhausted




    def __init__(self, Qstates, alphabet, transFunc, Qstart, Qfinal):
        self.Qstates = Qstates;
        self.alphabet = alphabet;
        self.transFunc = transFunc;
        self.Qstart = Qstart;
        self.Qfinal = Qfinal;
        self.Qpresent = Qstart;
        return;
#  ****************************METHODS IN CLASS DFA**************************
    

#    This method accepts the DFA object(self)-as caller and the word to be tested
#    Self refers to the object that called the method in this case DFA machine
#    It initiates the test using mobile status Qpresent from Q0
#    It loops through the word jumping to the new state  
#    and updating Qpresent to the state if valid or none if invalid
#    When the word is exhausted, it tests Qpresent againsts the 
#    pre-defined final state(s)    
    
    
    def TESTWORD(self,word):
        #set present state to initial Q0
        self.Qpresent = self.Qstart;
        
#    loop through the word
#    This code performs the operation Delta(Qx,char)=Qy where input (char)
#    is introduced to Qx causing it to transition to Qy according to the predefined
#    transition path of the DFA. QX, the current state and is tupled together  
#    with the input character. (Qpresent,input) tuple is compared to the  
#    transition state tuples of the machine(keys. 
#    Qpresent is assigned Qy, if a match is found. 
#    otherwise it is assigned value none.             
        
        
        for ch in word:
            if((self.Qpresent, ch) not in self.transFunc.keys()):
                self.Qpresent = None;
                continue;
            self.Qpresent = self.transFunc[(self.Qpresent, ch)];
        #return;             
                         
        
#    at the end of the word, compare present state with final states
#    This code compares the Qpresent (a numeric value)to 
#    the final QF of the DFA machine given as an array and returs true or false
#      
       
        return self.Qpresent in self.Qfinal                       
            
def L1():

#   ************************NITIALIZE ELEMENTS******************************

#   Build the 5 elements required for a DFA 
#   (transition statesQ, alphabet, transFunc(delta), initial state, final states)

#   set your alphabet

    alphabet={'a','b'};


#   Build the DFA machine by using a set of transition functions delta(Qx,input)=Qy
#   the data structure is a dictionary where Qx,input) is the key and Qy is the 
#   value in the dictionar's (key,value) pair
                                                                    
    transFunc=dict();
#   populate the dictionary object with the various states of the machine
#   Q states represented by numerical values and input character by char variables

   
    transFunc[(0, 'a')] = 3;
    transFunc[(0, 'b')] = 1;
    transFunc[(1, 'a')] = 2;
    transFunc[(1, 'b')] = 1;
    transFunc[(2, 'a')] = 2;
    transFunc[(2, 'b')] = 2;
    transFunc[(3, 'a')] = 3;
    transFunc[(3, 'b')] = 3;          
                                                                    
                                                                    
#   declare the initial state as an integer since we only have one 
#   and final states as an array coz we can have many
#   and all the states in the machine as an array
    Qinitial = 0;
    Qfinal = {2};                                                                
    Qstates = {0,1,2,3};                                                                   
#    inputword={'a','d','a','a','a','a','a','a','a'}; 
#   inputword as a list 
    inputword = [list('abaaaaaa'),list('bbbbbbbbb'),list('aab'),list('babbaabb'),list('bbbbbbbbbbbbabb')];                                                  
    #word =  list('babbaabb')                                                              
#   call constructor for DFA

    dfamachine= DFA(Qstates, alphabet, transFunc, Qinitial, Qfinal) 

#   now test the word though the machine and see if it is acceptesd
    print ('Test DFA for L1');
    for word in inputword:
        print word;
        print dfamachine.TESTWORD(word);                                                                  
                                                                    
##################################################################################                                                                   
    
def L2():

#   ************************NITIALIZE ELEMENTS******************************

#   Build the 5 elements required for a DFA 
#   (transition statesQ, alphabet, transFunc(delta), initial state, final states)

#   set your alphabet

    alphabet={'a','b'};


#   Build the DFA machine by using a set of transition functions delta(Qx,input)=Qy
#   the data structure is a dictionary where Qx,input) is the key and Qy is the 
#   value in the dictionar's (key,value) pair
                                                                    
    transFunc=dict();
#   populate the dictionary object with the various states of the machine
#   Q states represented by numerical values and input character by char variables

    transFunc[(0, 'a')] =1;
    transFunc[(0, 'b')] =1;
    transFunc[(1, 'a')] =0;
    transFunc[(1, 'b')] =0;
   
              
                                                                    
                                                                    
#   declare the initial state as an integer since we only have one 
#   and final states as an array coz we can have many
#   and all the states in the machine as an array
    Qinitial = 0;
    Qfinal = {1};                                                                
    Qstates = {0,1};                                                                   
#    inputword={'a','d','a','a','a','a','a','a','a'}; 
#   inputwords as an array of lists 
    inputword = [list(''),list('bbbbbbbbb'),list('aab'),list('babbaabb'),list('bbbbbbbbbbbbabb')];                                                
                                                                    
#   call constructor for DFA

    dfamachine= DFA(Qstates, alphabet, transFunc, Qinitial, Qfinal) 

#   now test the word though the machine and see if it is acceptesd
    print ('Test DFA for L2');
    for word in inputword:
        print word;
        print dfamachine.TESTWORD(word);

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def L3():
#   ************************NITIALIZE ELEMENTS******************************

#   Build the 5 elements required for a DFA 
#   (transition statesQ, alphabet, transFunc(delta), initial state, final states)

#   set your alphabet

    alphabet={'a','b'};


#   Build the DFA machine by using a set of transition functions delta(Qx,input)=Qy
#   the data structure is a dictionary where Qx,input) is the key and Qy is the 
#   value in the dictionar's (key,value) pair
                                                                    
    transFunc=dict();
#   populate the dictionary object with the various states of the machine
#   Q states represented by numerical values and input character by char variables

    
    transFunc[(0, 'a')] = 1;
    transFunc[(0, 'b')] = 1;
    transFunc[(1, 'a')] = 2;
    transFunc[(1, 'b')] = 2;
    transFunc[(2, 'a')] = 0;
    transFunc[(2, 'b')] = 0;

              
                                                                    
                                                                    
#   declare the initial state as an integer since we only have one 
#   and final states as an array coz we can have many
#   and all the states in the machine as an array
    Qinitial = 0;
    Qfinal = {0,1};                                                                
    Qstates = {0,1,2};                                                                   
#   inputword={'a','d','a','a','a','a','a','a','a'}; 
#   inputwords as an array of lists 
    inputword = [list(''),list('bbbbbbbbb'),list('aab'),list('babbaabb'),list('bbbbbbbbbbbbab')];                                                  
                                                                    
#   call constructor for DFA

    dfamachine= DFA(Qstates, alphabet, transFunc, Qinitial, Qfinal) 

#   now test the word though the machine and see if it is acceptesd
    print ('Test DFA for L3');
    for word in inputword:
        print word;
        print dfamachine.TESTWORD(word); 
#********************************************************************************
def L4():
    #   ************************NITIALIZE DFA ELEMENTS******************************

#   Build the 5 elements required for a DFA 
#   (transition statesQ, alphabet, transFunc(delta), initial state, final states)

#   set your alphabet

    alphabet={'a','b'};


#   Build the DFA machine by using a set of transition functions delta(Qx,input)=Qy
#   the data structure is a dictionary where Qx,input) is the key and Qy is the 
#   value in the dictionar's (key,value) pair
                                                                    
    transFunc=dict();
#   populate the dictionary object with the various states of the machine
#   Q states represented by numerical values and input character by char variables

    
    
    transFunc[(0, 'a')] = 1;
    transFunc[(0, 'b')] = 3;
    transFunc[(1, 'a')] = 2;
    transFunc[(1, 'b')] = 4;
    transFunc[(2, 'a')] = 2;
    transFunc[(2, 'b')] = 6;
    transFunc[(3, 'a')] = 5;
    transFunc[(3, 'b')] = 6;
    transFunc[(4, 'a')] = 7;
    transFunc[(4, 'b')] = 6;
    transFunc[(5, 'a')] = 7;
    transFunc[(5, 'b')] = 7;
    transFunc[(6, 'a')] = 7;
    transFunc[(6, 'b')] = 6;
    transFunc[(7, 'a')] = 7;
    transFunc[(7, 'b')] = 7;     
                                                                    
                                                                    
#   declare the initial state as an integer since we only have one 
#   and final states as an array coz we can have many
#   and all the states in the machine as an array
    Qinitial = 0;
    Qfinal = {0, 1, 2, 5, 6};                                                               
    Qstates = {0, 1, 2, 3, 4, 5, 6, 7 };                                                                   
#   inputword={'a','d','a','a','a','a','a','a','a'}; 
#   inputword as an array of lists 
    inputword = [list(''),list('bbbbbbbbb'),list('aab'),list('aaa'),list('bbbbbbbbbbbbab'),list('baa'),list('ba')];                                                        
                                                                    
#   call constructor for DFA

    dfamachine= DFA(Qstates, alphabet, transFunc, Qinitial, Qfinal) 

#   now test the word though the machine and see if it is acceptesd
    print ('Test DFA for L4');
    for word in inputword:
        print word;
        print dfamachine.TESTWORD(word); 
                                                                
L1(); 
L2();                                                             
L3();
L4();


   

