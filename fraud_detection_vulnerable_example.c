
#include <stdio.h>

int main() {
    int transaction_amount = 1000000000;  
    int fraud_threshold = 2000000000;     
    int risk_score = 100;                 
    int risk_multiplier = 50;             
    int final_risk_score;
    
    if (transaction_amount + fraud_threshold > 10000000000) {  
    
        
        final_risk_score = risk_score * risk_multiplier;  
        
  
        short small_risk_score = (short)final_risk_score;  
        
       
        final_risk_score = final_risk_score + risk_score;  
    }
    
    return 0;
}
