const urlName = document.getElementById('url-name')
const form = document.getElementById('form');

form.addEventListener('submit', handleSubmit)

async function handleSubmit(e) {
    e.preventDefault()
    const urlNameValue = urlName.value

    const jsonObj = {
        "url": urlNameValue,
    }

    const options = {
        method: 'POST',
        body: JSON.stringify(jsonObj),
        headers: {
            'Content-Type': 'application/json'
        }
    }
    const response = await fetch('http://localhost:5000/urls', options)
    const json = await response.json()
    console.log(json)
}

const fetchData = async () => {
    fetch('http://localhost:5000/urls')
    .then(resp => resp.json())
    .then(resp => {
    postChoc(resp)
    })
}

const displayUrl = document.getElementById('display-urls');

function postUrl(resp) {
    resp.forEach(c => {
        const div = document.createElement('div');
        div.setAttribute('class', 'url-div')
        div.innerHTML = `<p>${urls}</p>`
    displayUrl.appendChild(div)
    })
}

fetchData()