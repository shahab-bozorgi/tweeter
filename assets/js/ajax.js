function like(id){
    var element =document.getElementById('like')
    var count =document.getElementById('count')
    $.get(`/tweeter`).then(response =>{
        if(response['response'] === 'liked'){
            element.className = 'fa fa-heart'
            count.innerText = Number(count.innerText ) -1
        }else{
            element.className = 'fa fa-heart-o'
            count.innerText = Number(count.innerText ) +1


        }
    })
}