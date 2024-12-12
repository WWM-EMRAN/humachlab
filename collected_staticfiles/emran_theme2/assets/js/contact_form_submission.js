fetch(actionUrl, {
    method: 'POST',
    body: formData,
    headers: {
        'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
    },
})
    .then((response) => response.json())
    .then((data) => {
        loadingDiv.style.display = 'none';
        if (data.status === 'success') {
            // Show success message
            successDiv.style.display = 'block';
            successDiv.textContent = data.message;
            errorDiv.style.display = 'none'; // Hide any error messages
            form.reset(); // Clear the form on success
        } else {
            // Show error message
            errorDiv.style.display = 'block';
            errorDiv.textContent = data.message || 'An error occurred. Please try again.';
            successDiv.style.display = 'none'; // Hide any success messages
        }
    })
    .catch(() => {
        loadingDiv.style.display = 'none';
        errorDiv.style.display = 'block';
        errorDiv.textContent = 'An unexpected error occurred.';
        successDiv.style.display = 'none'; // Hide any success messages
    });








// document.addEventListener('DOMContentLoaded', function () {
//     const form = document.getElementById('contact-form');
//
//     if (form) {
//         form.addEventListener('submit', function (e) {
//             e.preventDefault(); // Prevent the default form submission
//
//             // Use the form's action attribute or a default URL
//             const actionUrl = form.getAttribute('action') || '/emran/contacts';
//             const formData = new FormData(form);
//             const loadingDiv = document.querySelector('.loading');
//             const errorDiv = document.querySelector('.error-message');
//             const successDiv = document.querySelector('.sent-message');
//
//             loadingDiv.style.display = 'block';
//             errorDiv.style.display = 'none';
//             successDiv.style.display = 'none';
//
//             fetch(actionUrl, {
//                 method: 'POST',
//                 body: formData,
//                 headers: {
//                     'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
//                 },
//             })
//                 .then((response) => response.json())
//                 .then((data) => {
//                     loadingDiv.style.display = 'none';
//                     if (data.status === 'success') {
//                         successDiv.style.display = 'block';
//                         successDiv.textContent = data.message;
//                         form.reset();
//                     } else {
//                         errorDiv.style.display = 'block';
//                         errorDiv.textContent = data.message || 'An error occurred. Please try again.';
//                     }
//                 })
//                 .catch(() => {
//                     loadingDiv.style.display = 'none';
//                     errorDiv.style.display = 'block';
//                     errorDiv.textContent = 'An unexpected error occurred.';
//                 });
//         });
//     }
// });
