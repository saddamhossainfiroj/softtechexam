$(document).ready(function(){
    $(".select2").select2();
});

function image_view(input, img_id) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        reader.onload = function (e) {
            $('#'+img_id).attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}