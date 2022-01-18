function validateAccountNumber(){
    var accountNumber = document.getElementById('account_number')
    if(accountNumber.length != 9){
        document.getElementById("benificiary_acc").style.border="2px solid red"
        alert("Account number should be 9 digit only!");
    }
}