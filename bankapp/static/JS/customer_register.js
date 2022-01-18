var submit = document.getElementById('submit')
function nameValidation(){
    const name = document.getElementById('name').value;
    if (/^([a-zA-Z]{3,30}\s*)+$/.test(name)){
        document.getElementById('nameerr').innerHTML = ""
        document.getElementById('name').style.border = ""
        return true
    }
    else{
        document.getElementById('nameerr').innerHTML = "* Name Should contain more than two characters and alphabets only"
        document.getElementById('name').style.border = "1px solid red"
        return false
    }
}

function fatherNameValidation(){
    const name = document.getElementById('father_name').value;
    if (/^([a-zA-Z]{3,30}\s*)+$/.test(name)){
        document.getElementById('father_nameerr').innerHTML = ""
        document.getElementById('father_name').style.border = ""
        return true
    }
    else{
        document.getElementById('father_nameerr').innerHTML = "* Father Name Should contain more than 2 characters and alphabets only"
        document.getElementById('father_name').style.border = "1px solid red"
        return false
    }
}

function emailValidation() {
    const email = document.getElementById('email').value;
    if (/^[a-z]+\w+([\.-]?\w+)*@[a-z]+([\.-]?\+)*(\.\w{2,3})+$/.test(email)){
        document.getElementById('emailerr').innerHTML = ""
        document.getElementById('email').style.border = ""
        return true
    }
    else{
        document.getElementById('emailerr').innerHTML = "* Not a valid Email"
        document.getElementById('email').style.border = "1px solid red"
        return false
    }
}

function mobileValidation() {
    const mobile = document.getElementById('mobile').value;
    if (/^([6-9]\d{9})+$/.test(mobile)){
        document.getElementById('mobileerr').innerHTML = ""
        document.getElementById('mobile').style.border = ""
        return true
    }
    else{
        document.getElementById('mobileerr').innerHTML = "* Mobile Number Should contains 10 digits"
        document.getElementById('mobile').style.border = "1px solid red"
        return false
    }
}

function dobValidation() {
    const dob = document.getElementById('date_of_birth').value;
    if (/^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])+$/.test(dob)){
        document.getElementById('doberr').innerHTML = ""
        document.getElementById('date_of_birth').style.border = ""
        return true
    }
    else{
        document.getElementById('doberr').innerHTML = "* Date Of Birth should be as YYYY-MM-DD"
        document.getElementById('date_of_birth').style.border = "1px solid red"
        return false
    }
}

function passwordValidation() {
    const psw = document.getElementById('psw').value;
    if (/^((?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#@$&*-]).{8,})+$/.test(psw)){
        document.getElementById('pswerr').innerHTML = ""
        document.getElementById('psw').style.border = ""
        return true
    }
    else{
        document.getElementById('pswerr').innerHTML = "* Password combine Uppercase,lowercase,special characters(#@$&*-) and numeric of minimum 8 characters"
        document.getElementById('psw').style.border = "1px solid red"
        return false
    }
}

function validateForm(){
    if(!(nameValidation()&&fatherNameValidation()&&emailValidation()&&mobileValidation()
    &&dobValidation()&&passwordValidation())){
        return false;
    }
}



