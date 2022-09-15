
function AddComment(articleid){
    var text = $("#textarea").val();
    var parent_id = $("#parent").val();
    if (text !== "" && text != null){
        $.get("/articles/article-comment" , {text ,article_id:articleid , parent_id }).then(response => {
        $("#comments_area").html(response);
        $("#textarea").val(" ");
        $("#parent").val(" ");
        if (parent_id !== "" && parent_id !== null){
            document.getElementById("reply_comment_scroll_" + parent_id).scrollIntoView({behavior:"smooth"})
        }else {
            document.getElementById("comments_area").scrollIntoView({behavior:"smooth"})
        }
        } );
    }
}


function AddReplyComment(commentid){
    console.log("ok")
    $("#parent").val(commentid)
    document.getElementById("box-scroll").scrollIntoView({behavior:"smooth"})
}



function Filter(){

    const price = $("#sl2").val();
    const start_price = price.split(',')[0]
    const end_price = price.split(',')[1]
    $("#start_price").val(start_price)
    $("#end_price").val(end_price)
    $("#send_price").submit()

}


function Show(image){

    $("#img-show").attr('src' , image)
}



function AddCommentProduct(product_id){
    let message = $("#text-aria-product").val()
    if (message !== "" && message != null){
        $.get("/products/product-comment" , {product_id , message}).then(response=>{
        $("#text-aria-product").val("");
        $("#comments_area_product").html(response);
        document.getElementById("scroll").scrollIntoView({behavior:"smooth"});

        });
    }

}

function AddProductToCart(product_id){
    const count = $("#count").val()

    $.get("/cart/add-product-to-cart" , {count , product_id}).then(response => {
        if(response.status === "successful"){

            Swal.fire({
              position: 'top-start',
              icon: 'success',
              title: response.title,
              showConfirmButton: false,
              timer: 1300
            })

        }else{
            Swal.fire({
                  title: response.title,
                  text: response.message,
                  icon: response.icon,
                  confirmButtonColor: '#3085d6',
                  confirmButtonText: response.confirmButtonText
                }).then((result) => {
                  if (result.isConfirmed) {
                    Swal.fire(
                      window.location.href = '/account/login'
                    )
                  }
                })
        }

    })

}

// function RemoveProduct(product_id){
//     $.get('/cart/remove-from-cart' , {product_id}).then(response => {
//         $("#product-cart").html(response);
//     });
// }

function RemoveProduct(detail_id){
    $.get("/cart/remove-from-cart" , {detail_id}).then(response => {
        $("#main-section").html(response);
        Swal.fire({
              position: 'top-start',
              icon: 'success',
              title: "کالای مورد نظر باموفقیت از سبد خرید حذف شد",
              showConfirmButton: false,
              timer: 1400
            })
        } );

}

function Change_cart_detail_count(detail_id , state) {
    $.get("/cart/change-product-count", {detail_id, state}).then(response => {
        console.log(response)
        $("#main-section").html(response);

    })
}


function Search(){
    let text = $("#search_box").val()
    let div_search_box = $("#search-box-full")
    if (text ===''){
        res = document.getElementById('result')
        res.style.display='none'
        div_search_box.css('height' , '33px')
        div_search_box.css('box-shadow' , 'none')
        return
    }

    $.get('/search_momentary' , {text}).then(response => {
        res = document.getElementById('result')
        res.innerHTML = ''
        let list = '';
        let results = response.result_search
        let text = $("#search_box").val()
        if (text === '' || results.length === 0){
            res.style.display='none'
            div_search_box.css('height' , '33px')
            div_search_box.css('box-shadow' , 'none')
            return
        }

        for(i=0; i<results.length; i++){
            list += '<li>'+results[i].a +'</li>';
        }
        div_search_box.css('box-shadow' , '0px 0px 4px black')
        div_search_box.css('height' , '280px')

        res.style.display='block'

        res.innerHTML = '<ul>' + list + '</ul>';

    })
}

$(document).mouseup(function(e)
{
    if ($("#search_box").is(":focus")) {
        $("#icon-search").css('border' , 'none')
        $("#icon-search").css('border-bottom' , '1px solid #d3d3d2')



    }else {
        $("#icon-search").css('border' , 'none')
        $("#icon-search").css('border-right' , '1px solid #d3d3d2')
    }

    var container = $("#result");

    // if the target of the click isn't the container nor a descendant of the container
    if (!container.is(e.target) && container.has(e.target).length === 0)
    {
        container.hide()
    }
    var containers = $("#search-box-full");

    // if the target of the click isn't the container nor a descendant of the container
    if (!containers.is(e.target) && containers.has(e.target).length === 0)

    {
        containers.css('height' , '33px')
        containers.css('box-shadow' , 'none')
    }
});

// function Search_Full(){
//     let text = $("#search_box").val()
//     console.log(text)
//     search_full = 'FULL'
//     $.get('/search' , {text})
// }

function product_order_list() {
    let text = $("#search_box").val()
    if (text === ''){
        return Swal.fire({
              title: 'خطا!',
              text: "متنی در قسمت جستجو برای سرچ وجود ندارد!",
              icon: 'warning',
              confirmButtonColor: '#3085d6',
              confirmButtonText: 'باشه!'
            })
        }
    const url = '/search/'+ text
    $("#search-form").attr('action' , url)
    $("#search-form").submit()

}

