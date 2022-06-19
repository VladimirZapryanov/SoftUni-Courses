function validate() {
    const email = document.getElementById('email');
    email.addEventListener('change', check);
    let pattern = /[a-z]*@[a-z]*.[a-z]*/g;

    function check(event) {
        let match = pattern.exec(event.target.value);

        if (!match) {
            email.classList.add('error');
        } else {
            email.classList.remove('error');
        }
    }
}