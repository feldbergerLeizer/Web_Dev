(function() {
    'use strict';
  
    function createAccount(bal) {
        return {
          balance: bal,
          processTransaction: function (amount) {
              this.balance += amount;
            console.log(this.balance);
          }
        };
      }

      const processTransaction2 = function (amount) {
        this.balance += amount;
      console.log(this.balance);
    };
      
      const act1 = createAccount(5000);
      act1.processTransaction(5000);


      processTransaction2.call(act1, 100);
      processTransaction2.apply(act1,[ 100]);
  }());