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
    var nick_name = document.getElementById('nick').value;
    var alert_array = [];
    len = alert_array.length;
    if (name.length<=2){
        document.getElementById('name').style.border="2px solid red"
        alert_array.push((++len)+" : Name Should have more than 2 characters!")
    }
    else{
        document.getElementById('name').style.border="1px solid black"
    }
    if (nick_name.length<=2){
        document.getElementById('nick').style.border="2px solid red"
        alert_array.push((++len)+" : Nick name Should have more than 2 characters!")
    }
    else{
        document.getElementById('nick').style.border="1px solid black"
    }
    if(accountNumber.length != 9){
        document.getElementById("benificiary_acc").style.border="2px solid red"
        alert_array.push((++len)+" : Account number should be 9 digit only!");
        
    }
    else{
        document.getElementById('benificiary_acc').style.border="1px solid black"
    }
    if(len != 0){
        alert(alert_array.join("\n"));
        return false
    }
    else{
        return true
    }
}   

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
