$('#slider1, #slider2, #slider3 ,#slider4').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})



$('.plus-cart').click(function()
{
    var id=$(this).attr("pid").toString();
    var elm=this.parentNode.children[2]
    console.log(id);
    console.log("hiii");
    $.ajax({
          type:"GET",
          url:"/pluscart",
          data:{
              prod_id:id
          },
          success:function(data){
            elm.innerText=data.quantity
            console.log(data);
            document.getElementById("amount").innerText=data.am
            document.getElementById("total").innerText=data.tt
 
    
             
          }

    })
})


$('.minus-cart').click(function()
{
    var id=$(this).attr("pid").toString();
    var elm=this.parentNode.children[2]
    console.log(id);
    console.log("hiii");
    $.ajax({
          type:"GET",
          url:"/minuscart",
          data:{
              prod_id:id
          },
          success:function(data){
            elm.innerText=data.quantity
            console.log(data);
            document.getElementById("amount").innerText=data.am
            document.getElementById("total").innerText=data.tt
 
    
             
          }

    })
})


$('.remove-cart').click(function()
{
    var id=$(this).attr("pid").toString();
    var eml=this
    console.log(id);
    console.log("hiii");
    $.ajax({
          type:"GET",
          url:"/removecart",
          data:{
              prod_id:id
          },
          success:function(data){
            console.log("delete");
            document.getElementById("amount").innerText=data.am
            document.getElementById("total").innerText=data.tt

            eml.parentNode.parentNode.parentNode.parentNode.remove()
             
          }

    })
})


