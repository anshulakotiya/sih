//var a = document.getElementById('age');
function personage(){
var b = document.getElementById('age').value;
var a = Number(b)
if ( a <= 17 || a > 100 )
{
 document.getElementById("hello").innerHTML='age is wrong';
}
else
{
document.getElementById("hello").innerHTML='';
}
}

function checkDate(){
let selectedtext = document.getElementById('dob').value;
let selecteddate = new Date(selectedtext);
let todaysdate = new Date();
    if (selecteddate >= todaysdate)
    {
    alert("date must not be greater than todays date");
    document.getElementById("dob") = todaysdate;
    }
//    else if (selecteddate == todaysdate)
//    {
//    alert("date must not be greater than todays date");
//
//    console.log("1");
//    }
}