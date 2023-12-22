function insertOne(data) {
    const table = document.querySelector('table')
    const row = table.insertRow();
    const interableData = Object.entries(data)
    interableData.forEach(x => {
        const [key, value] = x
        const elem = document.createElement('td')
        const elemValue = document.createTextNode(value)
        elem.appendChild(elemValue)
        row.appendChild(elem)
    })
}

function removeAll() {
    const elemtsList = document.querySelectorAll('tr:not(:first-child)')
    elemtsList.forEach(x => {
        x.remove()
    })
    return true
}

async function callGenerationData() {
    try {
        const result = await fetch("http://localhost:8000/population/generate", {
            method: 'POST',
            redirect: 'follow',
            headers: {
                "Access-Control-Allow-Origin": "*"
            }
        })
        const data = await result.json()

        if (removeAll()) {
            data.map(x => insertOne(x))
        }

    } catch (e) {
        alert("Tente novamente em alguns minutos...")
    }
}
