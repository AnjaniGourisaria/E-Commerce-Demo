// 
$('.plus-cart').click(function () {
    var id = $(this).attr('pid').toString();
    var eml = this.parentNode.childNodes[2]
    //  console.log(id)
    $.ajax({
        type: 'GET',
        url: '/plus_cart',
        data: {
            prod_id:id
        },
        success: function(data) { // <!-- By views.py -->
    //      console.log(data)  
            eml.innerText = data.quantity
            document.getElementById("amount").innerHTML = data.amount
            document.getElementById("totalamount").innerHTML = data.totalamount

        }
    })
})

// Minus Code 
$('.minus-cart').click(function () {
    var id = $(this).attr('pid').toString();
    var eml = this.parentNode.childNodes[2]
    //  console.log(id)
    $.ajax({
        type: 'GET',
        url: '/minus_cart',
        data: {
            prod_id:id
        },
        success: function(data) { // <!-- By views.py -->
    //      console.log(data)  
            eml.innerText = data.quantity
            document.getElementById("amount").innerHTML = data.amount
            document.getElementById("totalamount").innerHTML = data.totalamount

        }
    })
})