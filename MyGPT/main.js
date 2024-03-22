
document.getElementById("inputForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var text = document.getElementById("textInput").value;
    fetch('https://jai14.pythonanywhere.com/response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("response").style.display = 'flex';
        document.getElementById("output").innerHTML = data.output;
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        // Display an error message to the user
        document.getElementById("output").innerHTML = "Error: Failed to fetch data from the server";
    });
});