 document.addEventListener('DOMContentLoaded', function () {
            // AJAX handling for query buttons
            document.querySelectorAll('.ajax-button').forEach(button => {
                button.addEventListener('click', function (e) {
                    e.preventDefault();

                    const query = this.getAttribute('data-query');
                    const type = this.getAttribute('data-type');

                    fetch('/button/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'X-CSRFToken': '{{ csrf_token }}' // Include CSRF token
                        },
                        body: new URLSearchParams({
                            query: query,
                            type: type
                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                        // After query button is clicked, update button text with the response
                        this.innerText = `${this.innerText}: ${data.data || 'Success'}`;
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        this.innerText = 'Error occurred!';
                    });
                });
            });

            // Handle command buttons without page refresh
            document.querySelectorAll('.command-button').forEach(form => {
                form.addEventListener('submit', function (e) {
                    e.preventDefault();

                    const query = this.querySelector('input[name="query"]').value;
                    const button = this.querySelector('button');
                    const resultSpan = this.querySelector('.response');

                    fetch('/button/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'X-CSRFToken': '{{ csrf_token }}' // Include CSRF token
                        },
                        body: new URLSearchParams({
                            query: query,
                            type: 'command'
                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                        // After command button is clicked, update button text and show response
                        button.innerText = `${button.innerText}: Completed`;
                        resultSpan.innerText = `Command Result: ${data.data || 'Success'}`;
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        resultSpan.innerText = 'Error occurred!';
                    });
                });
            });
        });