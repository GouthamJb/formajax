$(document).ready(function(){
    $('#post-form').on("submit", function (e) {
        e.preventDefault();
            var name= $("#name").val();
            var email= $("#email").val();
             var phone=$("#phone").val();
            var description=$("#description").val();
         $.ajax({
           type: "POST",
           url: "",
           data: {
               name : name,
               email : email,
                phone : phone,
                description  : description,
               csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val(),
               action : 'post'
            
           },
           
           success: function (json) {
             document.getElementById("post-form").reset();
             document.getElementById("successfield").innerHTML="Form submitted successfully (AJAX Worked) ";
             
           },
           error: function (xhr, errmsg, err) {
            document.getElementById("errorfield").innerHTML="Form submission failure (Error in AJAX)";
             console.log(xhr.status + ": " + xhr.resposeText);
    
           },
         });
        });
         
       });
       
       
       
       
     
       