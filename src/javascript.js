
function now(){
return Date.now()
}

function timelapse(function_to_test){
    let initialTime = now()
    function_to_test
    let final_time = now()
    let timelapse = final_time - initialTime
    console.log(`L'éxécution a duré ${timelapse} millisecondes`);
    
}

function calculate(number1, number2){
    return(number1 + number2)
}

timelapse(calculate(6, 5));
