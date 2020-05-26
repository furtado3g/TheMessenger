setTimeout(() => {
    $("#search").select2();
},500)


let timer 
async function searchFriend(event){
    clearTimeout(timer)
    const data = {
        url  : '/friend/find',
        options : {
            method : "post",
            body : JSON.stringify({
                fieldValue : event.target.value,
                csrftoken : getCookie('csrftoken')
            }),
            headers: new Headers({
                'Content-Type' : 'application/json'
            })
        }
    }
    timer = setTimeout(async()=>{
        const response = await makeRequest(data)
        if(response != 404){
            el =document.querySelector("#new-friend");
            while(el.firstChild){
                el.removeChild(el.firstChild);
            }
            el.innerHTML = response
        }
    },500)
}

async function makeRequest(data) {
    const request = await fetch(data.url,data.options)
    let retornable
    request.status != 200 ? retornable = 404 : retornable = request.text()
    return retornable
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}