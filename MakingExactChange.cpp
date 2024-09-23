/*********************************************************************
* Name: Calvin Valdez
* Lab 2: Making Exact Change
* Editor(s) used: Visual Studio Code
* Compiler(s) used: Visual Studio Code
* Description:
*     This program allows the user to enter the amount needed and
      tendered when a purchase is made. The program uses loops and
      conditional statements to accurately output the change needed
      to give back to the customer.
**********************************************************************/




#include <iostream>
using namespace std;

#include <ctime>

// User-defined functions
void welcome();
void time();


/*********************************************************************
* Function: Main
**********************************************************************/

int main()
{

    welcome();
    time();

    // Variables declared

    double amount = 0;
    double amount_tendered = 0;
    int fifty_dollars = 0;
    int twenty_dollars = 0;
    int ten_dollars = 0;
    int five_dollars = 0;
    int one_dollar = 0;
    int fifty_cent = 0;
    int twenty_five_cent = 0;
    int ten_cent = 0;
    int five_cent = 0;
    int one_cent = 0;
    

    cin >> amount;
    cin >> amount_tendered;

    double change = amount_tendered - amount;
    cout.setf(ios::fixed);
    cout.precision(2);
    cout << "$" << change << endl;



    // Calculates the change
    do{
        if(change > 49.99){
            change -= 50;
            fifty_dollars ++;
            continue;

        }

        else if (49.99 >= change && change > 19.99){
            change -= 20;
            twenty_dollars ++;
            continue;
        }

        else if (19.99 >= change && change > 9.99){
            change -= 10;
            ten_dollars ++;
            continue;
        }

        else if (9.99 >= change && change > 4.99){
            change -= 5;
            five_dollars ++;
            continue;
        }

        else if (4.99 >= change && change > 0.99){
            change -= 1;
            one_dollar ++;
            continue;
        }

        else if (0.99 >= change && change > 0.49){
            change -= 0.50;
            fifty_cent ++;
            continue;
        }

        else if (0.49 >= change && change > 0.24){
            change -= 0.25;
            twenty_five_cent ++;
            continue;
        }



        else if (0.24 >= change && change > 0.0999999){
            change -= 0.10;
            ten_cent ++;
            continue;
        }


        else if (0.099 > change && change > 0.04){
                change -= 0.05;
                five_cent++;
                continue;
        }

        else if (0.04 >= change && change > 0.009){
            change -= 0.01 ;
            one_cent ++;
            continue;
        }

        else{
            break;
        }
    }while(change > 0);


    // Outputs the necessary change needed to be returned
    switch(fifty_dollars)
    {
        case 0:
            break;

        case 1:
            cout << fifty_dollars << " $50 bill" << endl;
            break;

        default:
            cout << fifty_dollars << " $50 bills" << endl;

    }


    switch(twenty_dollars)
    {
    case 0:
        break;

    case 1:
        cout << twenty_dollars << " $20 bill" << endl;
        break;

    default:
        cout << twenty_dollars << " $20 bills" << endl;

    }

    switch(ten_dollars)
    {
    case 0:
        break;

    case 1:
        cout << ten_dollars << " $10 bill" << endl;
        break;

    default:
        cout << ten_dollars << " $10 bills" << endl;

    }

    switch(five_dollars)
    {
    case 0:
        break;

    case 1:
        cout << five_dollars << " $5 bill" << endl;
        break;

    default:
        cout << ten_dollars << " $5 bills" << endl;

    }

    switch(one_dollar)
    {
    case 0:
        break;

    case 1:
        cout << one_dollar << " $1 bill" << endl;
        break;

    default:
        cout <<  one_dollar << " $1 bills" << endl;

    }

    switch(fifty_cent)
    {
    case 0:
        break;

    case 1:
        cout << fifty_cent << " 50-cent coin" << endl;
        break;

    default:
        cout << fifty_cent << " 50-cent coins" << endl;

    }

   switch(twenty_five_cent)
   {
   case 0:
       break;

   case 1:
       cout << twenty_five_cent << " 25-cent coin" << endl;
       break;

   default:
       cout << twenty_five_cent << " 25-cent coins" << endl;

   }

    switch(ten_cent)
    {
    case 0:
        break;

    case 1:
        cout << ten_cent << " 10-cent coin" << endl;
        break;

    default:
        cout << ten_cent << " 10-cent coins" << endl;

    }

    switch(five_cent)
    {
    case 0:
        break;

    case 1:
        cout << five_cent << " 5-cent coin" << endl;
        break;

    default:
        cout << five_cent << " 5-cent coins" << endl;

    }

   switch(one_cent)
   {
    case 0:
        break;

    case 1:
        cout << one_cent << " 1-cent coin" << endl;
        break;

    default:
        cout << one_cent << " 1-cent coins" << endl;

   }






    return 0;
}



/*********************************************************************
* Function: Outputs a message greeting the user and 
*           welcoming them to the machine/program
**********************************************************************/

void welcome()
{
    cout << "Welcome To My Change Machine" << endl;
}


/*********************************************************************
* Function: Outputs the current date and time to the user
**********************************************************************/

void time()
{
    time_t currTime = time(NULL);
    cout << "Current date and time is : " << ctime(&currTime);
}
