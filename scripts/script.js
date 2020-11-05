$(document).ready(function(){
  
  $("#name").on("blur", function() {
    if ( $(this).val().match('^[a-zA-Z  ]{3,16}$') ) {
      document.getElementById('valname').innerHTML=" ";
   } else {
    document.getElementById('valname').innerHTML="*invalid name 3-16 characters required";
    }
   });
   $("#email").on("blur", function() {
    if ( $(this).val().match('^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$') ) {
      document.getElementById('valemail').innerHTML=" ";
   } else {
    document.getElementById('valemail').innerHTML="*please provide a valid email(abc@example.com)";
    }
   });
   $("#phone").on("blur", function() {
    if ( $(this).val().match('^[0-9]{10}$') ) {
      document.getElementById('valphone').innerHTML=" ";
   } else {
    document.getElementById('valphone').innerHTML="*please provide a valid 10-digit phone number";
    }
   });

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
           
           success: function (textStatus) {
             document.getElementById("post-form").reset();
             document.getElementById("successfield").innerHTML="Form submitted successfully (AJAX Worked) ";
             console.log(textStatus);
           },
           error: function (xhr, errmsg, err) {
            document.getElementById("errorfield").innerHTML="Form submission failure (Error in AJAX)";
             console.log(xhr.status + ": " + xhr.resposeText);
    
           },
         });
        });
         
       });
  
       
       
       
     
       