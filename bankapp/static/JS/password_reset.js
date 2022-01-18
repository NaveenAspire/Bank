function passwordValidation() {
    const psw = document.getElementById('new_password').value;
    if (/^((?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#@$&*-]).{8,})+$/.test(psw)){
        document.getElementById('pswerr').innerHTML = ""
        document.getElementById('new_password').style.border = ""
        return true
    }
    else{
        document.getElementById('pswerr').innerHTML = "* Password combine Uppercase,lowercase,special characters(#@$&*-) and numeric of minimum 8 characters"
        document.getElementById('new_password').style.border = "1px solid red"
        return false
    }
}

function validateForm(){
    if(!passwordValidation()){
        return false
    }
}