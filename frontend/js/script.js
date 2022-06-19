
function generate(){

    url = 'http://127.0.0.1:8000/nepsultsapi/'
    requestOptions = {
        method:'GET',
        headers:{'Content-Type':'application/json',},
    }
    fetch(url, requestOptions).then((response)=>{
        return response.json();
    }).then((data)=>{
        insult = data.detail
        insultstr = JSON.stringify(insult)
        insultfinal = insultstr.replace(/['"]+/g, '')
       

        console.log(insultfinal)
        document.getElementById('insultarea').innerHTML = insultfinal;

    })

    
}

