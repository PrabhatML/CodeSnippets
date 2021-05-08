<script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>

$.ajax({
    type: "method",
    url: "url",
    data: "data",
    dataType: "dataType",
    success: function (response) {
        
    },
    beforeSend: function(data){

    },
    complete: function(data){

    },
    error: function(data){

    }
});

fetch('url').then(response => response.json()).then(data => console.log(data))

async function myFetch(){
    response = await fetch('url')
    data = response.json()
    console.log(data)
}

myFetch()