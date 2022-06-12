function extractText() {
    let elements = Array.from(document.getElementsByTagName('li'));
    let result = elements.map(el => el.textContent).join('\n');

    document.getElementById('result').value = result;
}