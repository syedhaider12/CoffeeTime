console.log('working')
if (localStorage.getItem('cart') == null)
{
    var cart = {};
}
else
{
    cart = JSON.parse(localStorage.getItem('cart'));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;

}
$(".cart").click(function(){
    var idstr = this.id.toString();
    
    if (cart[idstr] != undefined){
        cart[idstr] = cart[idstr] + 1
    }
    else{
        cart[idstr] =  1
    }
    console.log(cart);
    
    var total = 0;
    for(var i=0; i<Object.values(cart).length; i++){
        total += Object.values(cart)[i];
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = total;
    
    
});