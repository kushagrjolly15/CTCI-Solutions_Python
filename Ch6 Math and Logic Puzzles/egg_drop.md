    When we drop an egg from a floor x, there can be two cases (1) The egg breaks (2) The egg doesn’t break.
    
    If the egg breaks after dropping from ‘xth’ floor, then we only need to check for floors lower than ‘x’ with remaining eggs as some floor should exist lower than ‘x’ in which egg would not break; so the problem reduces to x-1 floors and n-1 eggs.
    If the egg doesn’t break after dropping from the ‘xth’ floor, then we only need to check for floors higher than ‘x’; so the problem reduces to ‘k-x’ floors and n eggs.
    Since we need to minimize the number of trials in worst case, we take the maximum of two cases. We consider the max of above two cases for every floor and choose the floor which yields minimum number of trials.
    
    k ==> Number of floors
    n ==> Number of Eggs
    eggDrop(n, k) ==> Minimum number of trials needed to find the critical
    floor in worst case.
    
    eggDrop(n, k) = 1 + min{max(eggDrop(n – 1, x – 1), eggDrop(n, k – x)), where x is in {1, 2, …, k}}
    
    Concept of worst case: 
    For example :
    Let there be ‘2’ eggs and ‘2’ floors then-:
    
    
    
    
    If we try throwing from ‘1st’ floor:
    Number of tries in worst case= 1+max(0, 1)
    0=>If the egg breaks from first floor then it is threshold floor (best case possibility).
    1=>If the egg does not break from first floor we will now have ‘2’ eggs and 1 floor to test which will give answer as
    ‘1’.(worst case possibility)
    We take the worst case possibility in account, so 1+max(0, 1)=2
    
    If we try throwing from ‘2nd’ floor:
    Number of tries in worst case= 1+max(1, 0)
    1=>If the egg breaks from second floor then we will have 1 egg and 1 floor to find threshold floor.(Worst Case)
    0=>If egg does not break from second floor then it is threshold floor.(Best Case)
    We take worst case possibility for surety, so 1+max(1, 0)=2.
    
    The final answer is min(1st, 2nd, 3rd….., kth floor)
    So answer here is ‘2’.