window.onbeforeunload = ()=>{
    window.location.reload(true);
}
var a=0;
function formVisible(){
    
    if(a==1){
        document.getElementById("benificiary_form_container").style.display="";
        return a=0;
    }
    else{
        document.getElementById("benificiary_form_container").style.display="none";
        return a=1;
    }
}
    
function benificiaryValidate(){
    var accountNumber = document.getElementById("benificiary_acc").value;
    var name = document.getElementById('name').value;
    var nick_name = document.getElementById('nick').value
    if (name.length<=2){
        document.getElementById('name').style.border="2px solid red"
        alert("Name Should have more than 2 characters!")
        return
    }
    if (nick_name.length<=2){
        document.getElementById('nick').style.border="2px solid red"
        alert("Name Should have more than 2 characters!")
    }
    if(accountNumber.length != 9){
        document.getElementById("benificiary_acc").style.border="2px solid red"
        alert("Account number should be 9 digit only!");
        return false
    }
    
}   
// function benificiaryName(){
//     var name = document.getElementById('name').value;
//     console.log(name)
//     if (name.length<=2){
//         document.getElementById('name').style.border="1px solid red"
//     }
//     else{
//         document.getElementById('name').style.border="1px solid black"
//     }
// }

function setAccountNumber(){
    var e = document.getElementById("select");
    document.getElementById("accountnumber").innerHTML = e.value;
}
function removeBenificiary(){
    let accepted = confirm("Are you sure you want to delete this?");
    if (accepted) {
        document.getElementById('myForm').submit();
    }
}
