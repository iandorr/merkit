function count_checkboxes(){
    var checkboxes = document.querySelectorAll('div.service_checkbox_count > input[type="checkbox"]:checked');
    var unchecked = document.querySelectorAll('div.service_checkbox_count > input[type="checkbox"]:not(:checked)');
    var button = document.getElementById('service_checkbox_button');
    if (checkboxes.length >= 3){
        var value = true
        if (checkboxes.length == 3){
            button.disabled = false;
        }
    } else{
        var value = false
        button.disabled = true;
    }
    for (let i = 0;i<unchecked.length;i++){
        unchecked[i].disabled = value;
    }
}