    Assumptions: Probability of having a boy or girl is same. Also, the probability of next kid being a girl doesn’t depend on history.
    
    The problem can be solved by counting expected number of boys before a girl is born.
    
    Let NB be the expected no. of boys before a girl is born
    
    Let p be the probability that a child is boy and (1-p)
    be probability that a child is girl.
    
    NB can be written as sum of following infinite series.
    
    NB = 0*(1-p) + 1*p*(1-p) + 2*p*p*(1-p) + 3*p*p*p*(1-p) + 4*p*p*p*p*(1-p) +.....
    
    Putting p = 1/2 and (1-p) = 1/2 in above formula.
    
    NB    = 0*(1/2) + 1*(1/2)2 + 2*(1/2)3 + 3*(1/2)4  +  4*(1/2)5 + ...
    1/2*NB = 0*(1/2)2 + 1*(1/2)3 + 2*(1/2)4 + 3*(1/2)5  +  4*(1/2)6 + ...
    
    NB - NB/2 =  1*(1/2)2 + 1*(1/2)3 + 1*(1/2)4 + 1*(1/2)5  +  1*(1/2)6 + ...
    
    Using sum formula of infinite geometrical progression with
    ratio less than 1
    NB/2 = (1/4)/(1-1/2) = 1/2
    
    NB = 1
    So Expected Number of number of boys = 1
    
    Since the expected number of boys is 1 and there is always a girl, the expected ratio of boys and girls is 50:50